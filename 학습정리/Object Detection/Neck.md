# Neck
## Overview
**History**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159402189-8555c5d4-6ab4-40fc-be66-76a23fc7c621.png" width="50%"></p>

- FPN은 `Neck`이다.
- 하지만, FPN 이전의 YOLOv1부터 Neck의 개념이 등장하기 시작한다.

**Neck은 무엇인가?**

- 일반적 2 way object detection은 backbone의 마지막 feature map을 RPN에 활용한다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159403959-ff54f7f6-86a0-415c-ba9f-edaeb242b699.png" width="70%"></p>

- Neck : 중간의 feature map도 함께 응용해 ROI를 추출해보자
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159404000-fff24159-3e34-41b3-a00f-59e732ce277e.png" width="70%"></p>
  
**Neck은 왜 필요한가?**
- image에는 다양한 크기의 object가 존재한다.
- 여러 크기의 feature map을 사용하게 된다면 (각각의 feature map에서 다양한 크기의 object를 대응할 수 았다면) ROI head에서 보는 feature map이 풍부해진다.
  - 일반적으로, 작은 (high level의) feature map일수록 큰 범위를 보며 큰 (low level의) feature map일수록 작은 범위를 본다.
- `다양한 크기의 객체를 더 잘 탐지하기 위해서 Neck이 반드시 필요하다.`
- 하위 level의 feature는 semantic이 약하므로 상대적으로 semantic이 강한 상위 feature와의 교환이 필요하다. : Neck의 역할

## Feature Pytamid Network(FPN)

**작은 객체를 탐지하기 위한 시도들**
- image pyramid를 쌓아 feature를 추출
  - 다양한 크기의 이미지로부터 feature 추출한다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159405032-2bcb1bf9-40d8-4799-983c-c77b79ad8537.png" width="20%"></p>

- 한 이미지의 마지막 feature map으로부터 prediction
- 중간의 feature map을 그대로 활용 : **SSD**
  - 한계 : semantic이 골고루 섞이지 않는다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159405168-c2b9f973-6599-4e22-8e60-6b729b3ef4f2.png" width="20%"></p>

**FPN**
- high level에서 low level로 semantic 정보 전달이 필요하다.
- 따라서 `top-down path way` 추가
  - Pyramid 구조 
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159405483-fedccf92-6667-41bb-be5a-871fb741684b.png" width="30%"></p>

**Lateral connection**
- high level의 정보를 low level로 전달하는 방법
  - bottom-up 과정에서의 feature map은 1x1 Conv를 통해 channel을 맞춰준다.
  - top-down 과정에서의 feature map은 Upsampling을 통해 image size를 맞춰준다.
    > **Upsampling** : Nearest Neighbor Upsampling
    > <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159406094-4533f401-bca5-4fa5-8c30-7beb05b9eced.png" width="50%"></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159406401-20bdd2a5-3d5f-47c8-8fc7-9c7fbf7d4db2.png" width="40%"></p>

**Pipeline**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159406565-5f224b9c-6138-489f-a998-97ab2245fcf6.png" width="80%"></p>

- Backbone : ResNet
- lateral connection을 통한 각 feature map이 RPN을 통과해 나온 ROI를 NMS에 적용해 Top N ROI를 Select하게 된다.
- ROI projection을 위해서는 대상이 되는 feature map이 필요하게 된다. 이때 input feature map이 다양하므로 mapping이 필요하다. 공식 활용!! ROI의 w, h가 작을수록 low level의 feature와 mapping된다.

**Contribution**
- 여러 scale의 물체를 탐지하기 위해 설계
- 이를 달성하기 위해서는 여러 크기의 feature를 사용해야할 필요가 있다.

**Summary**
- Bottom up에서 다양한 크기의 feature map 추출
- 다양한 크기의 feature map의 sematic을 교환하기 위해 top-down 방식 사용

**Code**
- Build laterals : 각 feature map 마다 다른 채널을 맞춰주는 단계
  ```python
  laterals = [lateral_conv(inputs[i]) for i, lateral_conv in enuerate(self.lateral_convs)]
  ```
- Build Top-down : channel을 맞춘 후 top-down 형식으로 feature map 교환
  ```python
  for i in range(3, 0, -1):
      prev_shape = laterals[i-1].shape[2:]
      laterals += F.interpolate(laterals[i], size = prev_shape)
  ```
- Build outputs : 최종 3x3 convolution을 통과하여 RPN으로 들어갈 feature 완성
  ```python
  outs = [self.fpn_convs[i](laterals[i]) for i in range(4)]
  ```
  
## Path Aggregation Network(PANet)
**Problem in FPN**
- bottom-up 과정에서 path가 짧아보이지만, 실제 resnet의 backbone을 보면 각 stage 마다의 path가 굉장히 길다. 그렇다면 low=level의 feature가 hight level의 feature로 제대로 전달이 될 수 잇을까?

**Bottom-up Path Augmentation**
- bottom up을 추가해준다.
- low level의 feature를 다시 한번 high level의 feature에 전달해준다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159408539-6bb0ea63-0334-4c6a-a0d6-2df09b3d0356.png" width="80%"></p>

**Adaptive Feature Pooling**
- FPN에서는 ROI의 stage를 하나만 정해서 사용하지만, PANet은 모든 stage의 feature map을 chanel-wise하게 concatenation하여 사용한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159409009-279b09cc-6d08-4d22-83c9-2153b27d15e8.png" width="50%"></p>

**Code**
- FPN : Top-dwon에 3x3 convoltuion layer 통과하는 것 까지 동일
  ```python
  inter_outs = [self.fpn_convs[i](laterals[i]) for i in range(4)]
  ```
- Add bottom-up : FPN을 통과한 후, bottom-up path를 더해준다.
  ```python
  for i in range(3):
      inter_outs[i+1] += self.downsample_convs[i](inter_outs[i])
  ```
- Build outputs : 이후 FPN과 마찬가지로 학습을 위해 3x3 convoltuion layer 통과
  ```python
  outs = []
  outs.append(inter_outs[0])
  outs.exend([self.pafpn_convs[i-1](inter_outs[i]) for i in range(1, 4)])
  ```
 
# After FPN
## DetectoRS
**Motivation**
- Looking and thinking twice
  - Region Proposal Network(RPN)
  - Cascade R-CNN

**주요 구성**
- Recursive Fearue Pyramid(RPF)
- Switchable Atrous Convolution(SAC)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159409968-cab23471-acb0-43e7-b4b3-bbe57b3fef0d.png" width="70%"></p>

**Recursive Feature Pyramid(RFP)**

- FPN을 recursive하게 진행한다.
- backbone도 neck 정보를 활용해서 학습한다.
  - backbone 연산을 반복하기 때문에 FLOP가 증가한다는 단점이 있다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159410548-7b3bafc6-2820-4ee4-a78a-e9b0269cac91.png" width="40%"></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159410698-d88a1c3a-a517-4027-aebb-a1f6f6ef1850.png" width="70%"></p>

- top-down의 feature map을 backbone에 넘겨줄 때, ASPP 과정을 실행한다.

**ASPP**

- 하나의 feature map에서 pooling 진행시, atrous convolution을 다양하게 주어 receptive field를 증가시킨다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159411140-1d7df71b-0c91-438e-8e12-db4a958c6c23.png" width="70%"></p>

**Standard Convolution vs. Atrous Convolution(a.k.a dilated convoltuion)**
<p align='center'><img src="https://gaussian37.github.io/assets/img/dl/concept/dilated_residual_network/1.gif" width='60%'></p>

- 3x3 kernel size로 receptive field는 5x5로 커진다.

## Bi-direction Feature Pyramid(BiFPN)
**Pipeline**

-효율성을 위해 PANet을 수정하였다.
  - feature map이 한 곳에서 오는 node들을 제거한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159412221-1c8b3b2b-5983-446a-b661-ee66ec35d687.png" width='60%'></p>

**Weighted Feature Fusion**

- 정보가 다른 두 feature map의 lateral connection시 단순한 합으로 연산하지 말자!!
- FPN과 같이 단순 summation이 아닌 각 feature 별로 가중치를 부여한 뒤 summation

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159412622-f9ab8ddf-35b3-4668-bc69-b495a038b6d6.png" width='70%'></p>

## NASFPN
- 단순 일방향 (top-down 또는 bottom-up) summation보다 좋은 방법은?
- RPN 아키텍처를 NAS를 통해서 찾자!

**Architecture**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159413012-a0e1bfcc-245a-41b0-97af-9fb0d697fd47.png" width='70%'></p>

**단점**
- COCO dataset, ResNet 기준으로 찾은 architecture로 범용적이지 못하다.
- High search cost

## AugFPN
**Overview**
- Problem in FPN
  - 서로 다른 level의 feature 간의 semantic 차이
  - Hightest feature map의 정보 손실 : 채널을 줄이는 Conv
  - 1개의 feature map에서 ROI 생성
- 주요 구성
  - Consistent Supervision
  - Residual Feature Augmentation
    - information 손실이 발생할 수 있는 마지막 node에 residual feature augmentation을 해준다.
  - Soft RoI Selection
