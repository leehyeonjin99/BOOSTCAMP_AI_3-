# R-CNN
## Overview
![image](https://user-images.githubusercontent.com/57162812/159202000-e3f978b2-9d99-4eae-a34e-e33ba7e4607c.png)

- Sliding Window
  - scale과 ratio가 다른 sliding window를 통해 뽑힌 region을 통해 후보 영역을 사용한다.
  - 단점 : 무수히 많은 후보 영역, 후보 영역이 객체를 포함할 가능성이 낮다.

- Selective Search
  - 이미지의 색, 질감, shape의 특성을 통해 무수히 많은 작은 영역으로 나눠 영역을 점차 통합해 나간다.
  ![image](https://user-images.githubusercontent.com/57162812/159202241-0030c042-2b0b-4530-b236-e7b3560e6130.png)

## Pipeline
![image](https://user-images.githubusercontent.com/57162812/159202945-a9d32f0b-adaa-489f-8a53-a5c7b5e8c6cb.png)

1. 입력 이미지 받기
2. Selective Search를 통해 약 2000개의 ROI를 추출
3. ROI의 크기를 조절해 모두 동일한 사이즈로 변형
    - CNN의 마지막 FC layer의 입력 사이즈가 고정이므로 이 과정 수행
4. ROI를 CNN에 넣어 feature 추출
    - 각 region마다 4096 dim feature vector 추출
    - pretrained AlexNet 구조 활용
      - AlexNet 마지막에 FC layer 추가
      - 필요에 따라 Finetuning 실행
5. CNN을 통해 나온 feature를 SVM에 넣어 분류 진행
    - input : 2000 x 4096 features
    - output : Class(C+1) + Confidence scores
      - Class 개수(C) + 배경 여부(1)
6. CNN을 통해 나온 feature를 regression을 통해 bbox를 예측
    - bbox의 중심점과 실제 ground truth bbox의 중심점의 delta에 대해 학습
    - bbox의 width와 height의 변화에 대해서 학습한다.

## Training
- Alexnet
  - Dataset
    - IoU > 0.5 : positive samples
    - IoU < 0.5 : negative samples
    - 1 batch = 32 Positive samples + 96 Negative samples
- Linear SVM
  - Dataset
    - Ground truth : positive samples
    - IoU < 0.3 : negative samples
    - 1 batch = 32 Positive samples + 96 Negative samples
  - Hard negative mining
    - 배경으로 식별하기 어려운 sample들을 강제로 다음 배치의 negative sample로 mining하는 방법
    - Hard negative :  Fase Positive
    - 2000개의 ROI 중 대부분이 배경이기 때문에 negative region의 높은 퀄리티를 위해서

- Bbox regressor
  - Dataset 구성
    - IoU > 0.6 : positive samples
  - Loss function
    - MSE

## Shortcomings
1. 2000개의 Region을 각각 CNN 통과 : 계산 복잡도 증가
2. 강제 Warping, 성능 하락 가능성
3. CNN, SVM classifier, bounding box regressor 따로 학습
4. End-to-End X

# SPPNet
## Overview
**R-CNN 한계점**
- Conv Net의 입력 이미지가 고정되어있다.
  - 이미지를 고정된 크기로 Crop 또는 Warp 해야한다.
- ROI마다 CNN 통과
  - 2000번 CNN 통과로 시간 오래 걸린다.

![image](https://user-images.githubusercontent.com/57162812/159204480-8e599beb-640c-4b20-9b99-0f38b658fd2e.png)

## Spatial Pyramid Pooling

**R-CNN vs. SPPNet**

![image](https://user-images.githubusercontent.com/57162812/159204711-88681170-dd66-46b4-bc23-53786bbd7fba.png)

- 2000 ROI → CNN vs. CNN → 2000 ROI 
- warping vs. spatial pyramid pooling layer

**Spatial Pyramid Pooling**

![image](https://user-images.githubusercontent.com/57162812/159204947-bebb50cb-4d45-4f8d-8695-998fd298b6a6.png)

![image](https://user-images.githubusercontent.com/57162812/159204968-1fa7ed23-3305-4c3e-a04b-76f9f2720022.png)

image를 고정된 여러가지의 feature size에 맞게 binnig하여 pooling을 통해 feature vector를 추출해 concatenation한다.

## Shortcomings
1. ~~2000개의 Region을 각각 CNN 통과 : 계산 복잡도 증가~~
2. ~~강제 Warping, 성능 하락 가능성~~
3. CNN, SVM classifier, bounding box regressor 따로 학습
4. End-to-End X

# Fast R-CNN
## Pipeline

![image](https://user-images.githubusercontent.com/57162812/159205163-18202cd6-5811-4df1-b99c-cd2ea7d1ede6.png)

1. 이미지를 CNN에 넣어 feature 추출 
    - VGG16 사용
2. RoI Projection을 통해 feature map 상에서 RoI를 계산
  - 원본 이미지에서 2000개의 Selective Search를 통해 RoI를 뽑아 feature map에 그대로 수용시킨다. 
  ![image](https://user-images.githubusercontent.com/57162812/159205487-25b17330-3bc4-4e11-bbc1-f9d7d6696ed8.png)
3. RoI Pooling을 토앻 일정한 크기의 feature를 추출 ≓ spatial pyramid pooling
    - target grid size 7x7 하나만 사용
    ![image](https://user-images.githubusercontent.com/57162812/159205698-ebb6dde4-b13c-416a-b722-b29bcdfb9736.png)
4. Fully connected layer 이후, Softmax Classifier과 Bounding Box Regressor
    - class 개수 : C + 1

## Training
- multi task loss 사용
  - classification loss + bounding box regression
- Loss function
  - Classification : Cross Entropy
  - BB regressor : Smooth L1
    - L1, L2보다 outlier에 덜 민감하다.
- Dataset
  - IoU > 0.5 : positive samples
  - 0.1 < IoU < 0.5 : negative samples
  - 25% positive samples + 75% negative samples
- Hierarchical sampling
  - R-CNN의 경우 각 이미지의 RoI를 모두 저장해 사용
  - 한 batch에 서로 다른 이미지의 RoI가 포함
  - Fast R-CNN의 경우 한 배치에 한 이미지의 RoI만을 사용
  - 한 batch 안에 연산과 메모리를 공유할 수 있다.

## Shortcomings
1. ~~2000개의 Region을 각각 CNN 통과 : 계산 복잡도 증가~~
2. ~~강제 Warping, 성능 하락 가능성~~
3. ~~CNN, SVM classifier, bounding box regressor 따로 학습~~
4. End-to-End X : Selective Search는 CPU에서의 알고리즘

# Faster R-CNN

**Fast R-CNN vs. Faster R-CNN**

![image](https://user-images.githubusercontent.com/57162812/159206146-f056e5fd-4152-49b3-8fa1-a10add78e554.png)

- Selective Search vs. RPN(Region Proposal Network)

1. 이미지를 CNN에 넣어 feature maps 추출
2. feature map으로부터 RPN을 통과해 ROI 계산
  - Anchor box 개념 사용
  > **Anchor box**
  > 각 cell마다의 scale과 ratio를 다르게 설정해 미리 설정한 bbox
  > ![image](https://user-images.githubusercontent.com/57162812/159206471-8b88ff81-dcf9-4cb2-acdb-e18544b58459.png)

  > **Region Proposal Network(RPN)**
  > ![image](https://user-images.githubusercontent.com/57162812/159206671-f7d5557a-ae61-4344-bbf0-64f0c9642510.png)
  > ![image](https://user-images.githubusercontent.com/57162812/159207008-c839a508-af59-4cbd-af28-dd68c4da95a0.png)
  > - 이미지 마다 feature map이 존재하며, 각 feature map의 각 cell마다 n개의 anchor box에 대해서 객체를 포함하는지 아닌지 확인하고 포함한다면 변화량을 학습한다.
  > - 2k scores + 4k coordinates
  
  > **NMS**
  > - 유사한 RPN Proposal 제거하기 위해 사용
  > - Class score를 기준으로 proposal 분류
  > - IoU가 0.7 이상인 proposal 영역들은 중복된 영역으로 판단한 뒤 제거
  > ![image](https://user-images.githubusercontent.com/57162812/159207323-64aadd71-c5d9-40af-ada5-1b74009e68b3.png)
  > - bb1을 기준으로 RoI가 큰 값들에 대해서 제거한다.
  >   - IoU(bb1, bb2) = 0.8 > 0.7 : bb2를 제거하며, bb2에 대한 bb2의 class score를 0으로 한다.

## Training
- RPN
  - Dataset
    - IoU > 0.7 or highest IoU with GT : positive samples
    - IoU < 0.3 : negative samples
  - Loss
    ![image](https://user-images.githubusercontent.com/57162812/159207619-eedf1a9a-a44d-428a-97f8-dbd661209048.png)
    - regression loss는 객체가 있는 ROI에 대해서만 수행하기 위해 p_i를 곱해준다.
- RPN 이후
  - Dataset
    - IoU > 0.5 : positive smaples : 32개
    - IoU < 0.5 : negative samples : 96개
  - Loss
    - Fast R-CNN과 동일
    
- RPN과 Fast RCNN 학습을 위해 4 step alternative training 활용
  1. Imagenet pretrained backbone load + RPN 학습
  2. Imagenet pretrained backbone laod + RPN from step 1 + Fast RCNN 학습
  3. Step 2 finetuned backbone load & freeze + RPN 학습
  4. Step 2 finetuned backbone load & freeze + RPN from strp 3 + Fast RCNN 학습
- 학습 과정이 매우 복잡해서, loss를 합쳐 학습하는 approximate joint training을 활용한다.

## Shortcomings
1. ~~2000개의 Region을 각각 CNN 통과 : 계산 복잡도 증가~~
2. ~~강제 Warping, 성능 하락 가능성~~
3. ~~CNN, SVM classifier, bounding box regressor 따로 학습~~
4. ~~End-to-End X : Selective Search는 CPU에서의 알고리즘~~
5. 2 track의 속도적 측면의 한계
