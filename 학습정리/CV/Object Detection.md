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













