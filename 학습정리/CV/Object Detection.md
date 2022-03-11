# Object Detection
## What is object detection

**Fundamental Image Recogntion Task**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157362284-eed6abed-7e19-4bd7-872c-e90c341c1846.png" width='60%'></p>

Sementic segmentation vs. Instance Segmentation, Panoptic Segmentation

- 같은 class라도 개체가 다르면 구분 가능 여부 : Instance 구분 가능 여부
- Instance Segmentation가 Panoptic Segmentation은 개체들을 따로 segmentation이 가능한 기술로, 훨씬 유용한 정보 제공 가능
- Instance Segmentation ⊂ Panoptic Segmentation

**Classification + Box Localization**
- 특정 Object를 Bounding Box의 형태로 위치를 측정 후 해당 박스 내의 물체의 Category 또한 인식
- Classification뿐만 아니라 물체가 몇개 있으며 어디 있는지까지 결정하는 영상 인식보다도 고차원의 문제

## What are the application of object detection
- Autonomous driving

<img src="https://user-images.githubusercontent.com/57162812/157363141-966f470a-3469-4845-8d29-f3f6d8ed9bec.png" width='30%'></p>

- Optical Character Recognition (OCR)

<img src="https://user-images.githubusercontent.com/57162812/157363251-33efd36b-1f77-451e-bdb3-3083105b621a.png" width='40%'></p>

# Two-stage detector
## Traditional Method : Hand-crafted techniques

**Gradient-Based Detector**

- 경계선의 특징을 잘 모델링하기 위한 엔지니어링 :  사람의 직관을 통해서 알고리즘 설계
- 선형 classifier인 SVM을 통해서 관심 물체인지 아닌지를 판별하는 판별기를 학습
- 영상의 gradient를 기반으로한 Detector

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157363862-0c31443f-3748-4d54-8d2d-758c0d277f09.png" width='60%'></p>

**Selective Search**

- Bounding box를 제안

1. 영상을 비슷한 set끼리 잘게 분할  : `Over Segmentation`
2. 잘게 분할된 영역들을 비슷한 영역끼리 합친다 : 비슷하다 = 색이 비슷하다, 분포가 비슷하다 등등 정의 필요
3. 합치는 것을 반복
4. 큰 Segmentation을 포함하는 Bounding Box를 추출해 물체의 후보군으로 사용

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157364337-bd703fce-6a7a-435f-b89a-5bbd87d70d11.png" width='50%'></p>

## R-CNN

**Directly leverage image classification networks for object detection**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157464385-19cf9139-0ac6-47be-b672-e75934c7d550.png" width='50%'></p>

1. Input Image
2. 2000개 이하의 region proposal
3. 각 region porposal 모두 적절한 같은 크기로 warp
  > **warp** : 찌그러트리는 기술
4. 기존에 training 되어있던, fine-tuning이 된 CNN model에 넣어 CNN feature을 계산한다.
  > CNN은 미리 영상 인식에 학습된 network를 사용한 후, 뒤쪽에 fc layer에서 추출된 feature를 기반으로 SVM만을 학습시켜 사용
5. Category 예측
6. bounding box regression을 통해 더욱 정교한 위치를 교정해준다.
  > 어떻게?
  >
  > bbox의 ground truth와 비슷해지도록 학습
  > [갈아먹는 Object Detection [1] R-CNN](https://yeomko.tistory.com/13)

**단점**

- 각각의 region proposal를 모두 model에 넣어 processsing을 하기 때문에 속도가 느리다
- region proposal은 Selective Search와 같은 별도의 hand design된 알고리즘을 사용하여 학습을 통한 성능 향상에 한계가 있다.

## Fast R-CNN
**Recycle a pre-computed feature for multiple object detection**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157464881-a8656d5a-787c-4e1a-8349-766e21814a7f.png" width='50%'></p>

R-CNN의 한계를 극복하고자 설계

영상 전체에 대한 feature를 한 번에 추출 후, 재활용해 여러 object를 detection
1. CNN에서 Conv layer까지 feature map을 뽑는다.
  - Tensor 형태 (HxWxC)
  - input size에 상관 없이 feature map 추출 가능 → warping 미실행
2. ROI(Region of Interest) pooling을 통해 ROI feature 추출
  - ROI는 region proposal이 제시한 물체의 후보 위치로, bounding box가 주어지면 ROI에 해당하는 feature만을 추출 후 fixed dimension을 가질 수 있도록 일정 사이즈로 Resampling한다.
3. class와 더 정밀한 bounding box 위치를 추정하기 위해 bbox regression과 classification을 수행한다.

**단점**
- 여전히 Selective Search 사용하여 성능 향상에 한계가 있다.

## Faster R-CNN
**End-to-end object detection by neural region proposal**

> **IoU** : Intersection over Union
>
> 두 영역의 overlap을 측정하는 기준을 제공하는 `metric`
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/157470049-a18440ad-1a59-4315-a7dc-397dc9a11180.png" width='30%'></p>
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/157470305-0d9144e5-bd65-42b9-b155-5a8513148426.png" width='30%'></p>

>**새로운 Region Proposal 등장**
>
> Anchor Boxes : 각 위치에서 발생할 것 같은 서로 다른 Scale과 Ratio의 박스들을 미리 정의해둔 후보군
> - IoU with Ground Truth > 0.7 : **Positive Sample**
> - IoU with Ground Truth < 0.3 : **Negative Sample**
> 논문에서는 Scale:(128, 256, 512), Aspect Ratio(2:1, 1:1, 1:2)를 사용하여 총 9개의 Anchor Box 생성

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157471608-b01c6a69-01ca-411e-9cd2-bceb12830c56.png" width='40%'></p>

- Selective Search와 같은 region proposal algorithm 대신에 Region Proposal Network(RPN) 제시
- Fast R-CNN과 마찬가지로 영상 하나에서부터 공유되는 feature map을 추출해 RPN에서 region proposal을 제안하여 ROI pooling을 실시해 classifier과 bbox regression 수행

**RPN의 방식**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157472698-73f68e64-7fdf-481f-b36f-3095dc1a6f8c.png" width='40%'></p>

conv feature map을 sliding window 방식으로 매 위치마다 k개의 anchor box를 고려한다.

> **미리 정해 놓은 k개의 anchor box를 결정하는 방법은?**
>
> 1. 각 위치에서 256 dimension feature를 추출한다. 
> 2. Object vs. Non-object를 판별하는 2k개의 classification score 추출 : HxWx2xk
>   - **Loss** : Classification Loss : Cross Entropy Loss
> 3. k개의 bbox의 정교한 위치를 regression하는 4k개(x, y, w, h)의 regression output 출력 : HxWx4xk
>   - 왜 미리 정해놓은 anchor box를 regression하는가? 촘촘한 anchor box를 사용한다면 문제가 없겠지만 시간이 오래 걸린다. 따라서 적당한 양의 anchor box를 결정해두고 정교한 위치는 regression을 통해 변경해 나가자.
>   - **Loss** : Regression Loss
>
> 두 가지 Loss 모두 RPN을 위한 Loss이며, 전체 Target Task를 위한 ROI 별 Category Classificatoin에 대한 Classification Loss는 따로 설정되어 전체적인 end-to-end 학습

Test 시에는 RPN에서 일정 Objectness score 이상 나오는 경우가 많으며 엄밀한 threshold를 정의하기 어려워 중복되는 bbox가 생성된다. → 효과적으로 filtering과 screening의 방법으로 `Non-Maximum Suppression(NMS)` 알고리즘 사용

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157478764-65399752-f40f-41ae-a1b6-9f3e0ba7dbd4.png" width='60%'></p>

**Summary of the R-CNN family**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157479073-ff92922c-6a56-4fa7-a8d3-e07747845351.png" width='60%'></p>

# Single-Stage Detector
## Comparision with two-stage detectors
**One-Stage vs. Two-Stage**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157480106-52d0aa09-698b-4aff-8e9e-83d2f66fdc55.png" width='80%'></p>

- Single Stage Detector
  - 정확도를 조금 포기하더라도 속도를 확보해 Real Time Detection을 설계하는 데에 목적
  - Region Proposal을 기반으로한 ROI pooling을 사용하지 않고 곧바로 Box regression과 Classification 수행 : 구조가 간단하며 빠른 시간
- Two Stage Detector
  - RPN에서 sampling된 위치에 대해서만 Classifier 진행

## You only look once(YOLO)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157481493-03982a6d-a2be-4b53-a923-2c49f98f9a6d.png" width='60%'></p>

1. Input Image를 SxS grid로 분할
2. 각 grid에 대해서 중심을 grid 안쪽으로 하면서 크기가 일정하지 않은 bbox와 confidence score 예측 + 각 grid에 따른 class score 예측
3. NMS 알고리즘을 사용하여 정리된 bbox만을 출력

**YOLO structure**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157482432-849c5a4f-cc06-4205-b238-4485ae4ed311.png" width='80%'></p>

최종 출력 : 7x7x30
- 왜 30 Channel?
  - Bounding box anchor 2개 사용 + 20개의 Class
  - 2x(x, y, w, h, obj score) + 20 = 30

YOLO는 마지막 layer에서만 prediction을 진행하기 때문에 localization 정확도가 떨어지는 경향이 있다.

## Single Shot MultiBox Detector(SSD)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157483994-7027093f-cba9-4d95-8318-8e6e91e019c3.png" width='50%'></p>

Multi scale object를 잘 처리하기 위해서 중간 feature map을 각 해상도에 적절한 bbox를 출력할 수 있도록 multi scale 구조를 만들었다.

**SSD structure**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157485197-e22c78a5-f9cf-4255-bb2d-43bd2b5869c4.png" width='80%'></p>

- backbone : VGG
- Conv4 block의 feature map 출력에서 부터 최종 결과들을 출력하게 Classifier가 구성되어있다. : 각 scale마다 Object Detection 결과를 출력하도록 Design해서 다양한 scale의 Object에 대해서 잘 대응할 수 있도록 설계
- 8732 : 각 layer에서 parsing된 detection bbox의 총합

# Two-stage detector vs. One-stage detector
## Focal Loss
**Class Imbalance Problem**

- Single stage detector는 ROI pooling이 없기 때문에 모든 영역에서의 loss를 계산하게 되고 일정 gradient가 발생된다.
- 일반적인 영상에서는 background 영역이 더 넓고 실제 물체는 일부분을 차지하고 있으며, 심지어 object detection 문제에서는 물체가 적당한 크기의 bbox 하나로 취급된다.
- Positive sample은 적은 반면 유용한 정보는 아닌 배경에서 오는 Negative sample로 인해 Class Imbalance 발생
- 이 문제를 해결하기 위해 **Focal Loss** 제안
  > **Focal Loss**
  > <p align='center'><img src="https://user-images.githubusercontent.com/57162812/157486253-4c1c5718-e8f1-400c-b001-aaaaaa03dc58.png" width='40%'></p>
  >
  > - Cross Entropy의 확장 : γ=0일 경우
  > - 잘 맞춘 경우 loss를 더 낮추며, 맞추지 못하는 경우 sharp한 loss를 준다.
  > - 오답일 경우, γ가 클수록 더 작은 loss를 갖는다.
  >   - 오답에서의 gradient가 더 커지기 때문에 γ가 클수록 sharp한 변화가 생긴다.
  >   - 반면에 정답에 가까울 경우, γ가 클수록 gradient가 0에 가까워저 고려되지 않아진다. 즉, 변화가 거의 없다.

## RetinaNet
**RetinaNet is a one-stage network**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157487987-21968be7-4d91-4182-8656-3382c8de6d3d.png" width='80%'></p>

- Feature Pyramid Network(FPN) + class/box prediction branches
- low level의 특징과 high level의 특징을 모두 활용하면서도 각 scale 별 물체를 잘 찾기 위한 multi scale 구조를 갖기 위해서 설계
- UNet과 달리 Concatenation이 아닌 Plus로 fusion
- Class head와 Box head가 따로 구성되어 classification과 regression을 각 위치마다 Dense하게 수행

# Detection with Transformer
## DETR
**Transformer**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157488965-949faef2-5bdd-4c9d-ac00-011a6f1f3f7d.png" width='70%'></p>

Transformer의 Object Detection에 적용한 사례

- CNN의 feature와 각 위치의 multi dimension으로 표현한 encoding을 통해 입력 token을 만들어준다.

## Further reading
bounding box를 regression 하지 말고 다른 형태의 data 구조로 탐지가 가능할까? 에 대한 연구 진행 중!!
- 최근에는 box 표현 대신에 물체의 중심점을 대신 찾는 방법 혹은 왼쪽 위와 오른쪽 아래의 양 끝 점을 찾아 box를 곧바로 regression하는 것을 피해 효율적인 계산을 취하는 방법들이 개발 되고 있다.

