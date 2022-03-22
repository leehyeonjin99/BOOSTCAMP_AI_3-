# 1 stage Detectors
## Background
**2 Stage Detectors**
- RCNN, FastRCNN, SPPNnet, ...
  - Localization : 후보 영역 찾기
  - Classification : 후보 영역에 대한 분류
- 한계 : 속도가 느려  Real World에서 응용 불가능하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159414658-9f2db7c6-823a-4a4e-b9b2-b3e5e8bd0e65.png" width="80%"></p>

- feature map으로 부터 RPN 과정 없이 class와 coordinate를 예측한다.

**1 Stage Detectors**
- Localization, Classification이 동시에 진행
- 전체 이미지에 대해 특징 추출, 객체 검출이 이루어짐 → 간단하고 쉬운 디자인
- 속도가 매우 빠름 : Real-time detection
- 영역을 추출하지 않고 전체 이미지를 보기 때문에 객체에 대한 맥락적 이해가 높음
  - Background error가 낮음
- YOLO, SSD, RetinaNet

## History
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159415066-b11fdaba-87c8-4c34-a051-65d2cb751262.png" width="60%"></p>

# YOLOv1
## Overview
**접근 전략**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159415815-3e328a00-b542-4b89-9dac-0c525c745307.png" width="80%"></p>

**YOLO 특징**
- Region proposal 단계가 없다.
- 전체 이미지에서 bbox 예측과 class를 예측하는 일을 동시에 진행
  - 이미지, 물체를 전체적으로 관찰하여 추론 : 맥락적 이해 높아짐

## Pipeline
**Network** 
- GoogLeNet 변형
  - 24개의 Conv layer(특징 추출) + 2개 FC layer(bbox 좌표 및 확률 계산)
- 입력 이미지를 SxS 그리드 영역으로 나누기(S=7)
- 각 그리드 영역마다 B개의 bounding box와 confidence score 계산(B=2)
  - 신뢰도 = Pr(Object) x IOU(ground_truth, pred)
- 각 그리드 영역마다 C개의 class에 대한 해당 클래스일 확률 계산(C=20)
  - conditional class probability = P(Class_i|Object)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159416624-94532235-3f1c-4c08-9bcc-e51a0852ef7e.png" width="60%"></p>

- GoogLeNet의 output이 7x7이기 때문에 7x7 grid 영역으로 나누었다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159416885-39eecb7c-c2e9-4dfe-aaf9-7c375a1b78bd.png" width="70%"></p>

- 30 channel  
  = 첫번째 박스 정보 5 (bbox_ctr_x, bbox_ctr_y, bbox_w, bbox_h, bbox_confidence_socre)  
  \+ 두번째 박스 정보 5 (bbox_ctr_x, bbox_ctr_y, bbox_w, bbox_h, bbox_confidence_socre)  
  \+ 20-class에 대한 확률

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159416971-0f40605b-5b5a-49b5-935a-1d955ee5ba8f.png" width="70%"></p>

- **inference**
  - 첫번쨰 bbox의 confidence score와 20개의 class 확률을 곱한다. : 첫번째 bbox에 대한 각 class의 확률
  - 두번째 bbox의 confidence score와 20개의 class 확률을 곱한다. : 두번째 bbox에 대한 각 class 확률
  - grid의 각 cell마다 모두 진행한다. : 2x(7x7)개의 (20, 1) 확률 matrix가 생긴다.
    <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159417715-666703bf-bb74-4b0d-b314-fa3d6120b962.png" width="60%"></p>
  
  - 각 class에 대한 score들에 대해서 threshold보다 작은 값들에 대해서 0으로 바꾼다.
  - 내림차순으로 정렬한다.
  - NMS 연산을 진행한다.
    <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159417972-8cfc6130-7904-4947-a60e-19cb4a41abc5.png" width="90%"></p>

  - 위의 과정에 따르면 bb3와 bb1을 종이상자 bbox로 그려준다.

**Loss**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159418163-f43d6516-aa2c-4aca-99cc-5eca298f7c3f.png" width="90%"></p>

- Localization
  - 각 grid의 각 box 별로 object를 포함하고 있을 때, 중심점의 위치를 loss로 준다.
  - 각 grid의 각 box 별로 object를 포함하고 있을 때, 높이와 너비에 대해 loss를 준다.
- Confidence
  - 각 grid의 각 box 별로 object를 포함하지 않을 때, confidence loss
  - 각 grid의 각 box 별로 object를 포함하고 있을 때, confidence loss
- Classification
  - 각 grid의 각 box 별로 object를 포함하고 있을 때, class 확률에 대한 loss

## Results

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159418613-09215f89-8218-4c34-a680-805fd10a7ae6.png" width="90%"></p>

YOLO를 토대로 background error를 걸러내고 Faster RCNN을 실행하면 궁합이 좋다.

**장점**
- Faster R-CNN에 비해 6배 빠른 속도
- 다른 real-time detector에 비해 2배 높은 정확도
- 이미지 전체를 보기 때문에 클래스와 사진에 대한 맥락적 정보를 가지고 있다.
- 물체의 일반화된 표현을 학습
  - 사용된 dataset의 새로운 도메인에 대한 이미지에 대한 좋은 성능을 보인다.

# SSD
## Overview
**YOLO 단점**
- 7x7 그리드 영역으로 나눠 Bounding box prediction 진행  
  ➡ 그리드보다 작은 크기의 물체 검출 불가능
- 신경망을 통과하여 마지막 feature만 사용  
  ➡ 정확도 하락

**YOLO vs. SSD**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159419574-4761b839-a169-4b0a-a59d-2c67b33aa8d6.png" width="90%"></p>

- 448x448 image vs. 300x300 image
- Fully Connected Layer  vs. Fully Conv Layer
- backbone 통과 후 detection 수행 vs. 추가로 만들어진 Conv layer의 feature map으로 detection 수행

**SSD 특징**
- Extra convolution layer에 나온 feature map들 모두 detection 수행
  - 6개의 서로 다른 scale의 feature map 사용
  - 큰 feature map(early stage feature map)에서는 작은 물체 탐지
  - 작은 feature map(late stage feature map)에서는 큰 물체 탐지
- Fully connected layer 대신 convolution layer 사용하여 속도 향상
- Default box 사용(anchor box)
  - 서로 다른 scale과 비율을 가진 미리 계산된 box 사용
## Pipeline
**Network**
- VGG16 backbone + Extra Conv layers
- input image : 300x300

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159420487-8a33e17d-ad32-4915-85f8-579313436734.png" width="90%"></p>

**Multi-scale feature maps**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159420785-defbbc79-7691-47d4-8ba7-6172d5c8afd3.png" width="60%"></p>

- 256 channel을 3x3 Conv를 통해 (box의 개수)x(각 박스별 offset + class개수)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159420926-616cc7b2-8532-40ad-aa64-2710ca566618.png" width="60%"></p>
  
- offset : anchor box의 중심점, w, h
- class : num classes(20) + background
- box 개수
  - a_r=1일 때에 한하여, 다음 단계의 길이와 현재의 길이 사이의 정사각형 box를 하나 더 생성한다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159421966-79325bf3-dab9-419d-a531-9f0503513119.png" width="70%"></p>
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159422262-b2150c3b-d29e-445e-b8bc-55d9be908789.png" width="70%"></p>
  
  - 6개의 default box 사용
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159422299-7cbb1381-a2e5-488c-8f97-4771bcda012f.png" width="70%"></p>


**Default Box**
- feature map의 각 cell마다 서로 다른 scale, 비율을 가진 미리 정해진 box 생성
- Faster R-CNN의 anchor box와 유사

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159422908-bd1a9ca8-5962-48e2-a1fb-8e1c709e732e.png" width="70%"></p>

모든 extra conv layer의 feature map에 대해서 각 cell마다 default box가 나온다. : 8732개의 bbox

**Training**
- Hard negative mining 수행
- Non maximum supression(NMS) 수행

**Loss**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159423349-fb90b3bb-bc5a-4fd3-834c-227b366bf119.png" width="70%"></p>

# YOLO Follow-up
## YOLOv2
- Better : 정확도가 높게
- Faster : 더 빠르게
- Stronger : 더 많은 calss 예측 80-> 9000

**Better**
- Batch Normalization
- High resolution classifier
  - YOLO v1 : 224x224 image로 사전 학습된 VGG를 448x448 detection task에 적용
  - YOLO v2 : 448x448 image로 새롭게 finetuning
- Convolution with anchor boxes
  - FC layer 제거
  - anchor box 도입
  - K means cluster on COCO datasets : 5개의 anchor box
  - 좌표 값 대신 offset 예측하는 문제가 단순하고 학습하기 쉽다.
- Fine-grained features
  - 크기가 작은 feature map은 low level 정보 부족
  - Early feature map을 late feature map에 합쳐주는 passthrough layer 도입
  <img src="https://user-images.githubusercontent.com/57162812/159424166-62ee860b-1b07-4eb3-b806-58c43db33dc3.png" width="30%">
  
**Faster**
- Backbone model
  - GoogLeNet -> Darknet-19
- Darknet-19 for detection
  - fc layer 제거
  - 대신, 3x3 conv layer로 대체
  - 1x1 conv layer 추가

## YOLO v3
- Skip connection
- Max Pooling x, conv stride=2 사용
- FPN 사용

# RetinaNet
## Overview
**1 Stage Detector Problem**
- Class imbalance
  - Positive sample(객체 영역) < Negative sample(배경 영역)
- Anchor box 대부분 Negative Samples
  - 2 Stage detector의 경우 region proposal에서 background sample 제거(sample search, RPN)
  - Positive/Negative sample 수 적절하게 유지(hard negative mining)
**Concept**
- 새로운 loss function : cross entropy loss + scaling factor : focal loss
  - 쉬운 예제에 작은 가중치, 어려운 예제에 큰 가중치
  - 결과적 어려운 예제에 집중
