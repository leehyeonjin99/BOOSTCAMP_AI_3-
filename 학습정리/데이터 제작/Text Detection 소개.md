# 1. Basics
## 1.1 일반 객체 영역 검출 vs. 글자 영역 검출

- 예측하고자 하는 정보 : 클래스와 위치 vs. `Text`라는 단일 클래스로 위치만 예측
- 객체의 특징
  - 매우 높은 밀도
  - 극단적 종횡비
  - 특이 모양 : 구겨진 영역, 휘어진 영역, 세로 쓰기 영역
  - 모호한 객체 영역
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/163095308-c13677a6-c01e-4815-ab16-e9b6331a46e9.png" width="60%"></p>

## 1.2 글자 영역 표현법

- 사각형 종류들
  - 직사각형(RECT) : (*x_1, y_1, width, height*) or (*x_1, y_1, x_2, y_2*)
  - 직사각형 + 각도(RBOX): (*x_1, y_1, width, height, θ*) or (*x_1, y_1, x_2, y_2, θ*)
  - 사각형(QUAD) : (*x_1, y_1, x_2, y_2, ⋯, x_4, y_4*)
- 다각형(Polygon) : (*x_1, y_1, x_2, y_2, ⋯, x_N, y_N*)
  - 일반적으로 2N points를 이용하고, 상하 점들이 쌍을 이루도록 배치

# 2. Taxonomy
## 2.0 SW1.0 vs. SW2.0
- Human Detection  
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/163096153-c7ebd893-3aaa-4265-a0dc-2d336697221e.png" width="60%"></p>
- Text Detection
  - SW1.0에서의 Text Detection은 많은 파이프라인들이 결합되기 때문에 복잡도가 증가한다.
    <p align='center'><img src="https://user-images.githubusercontent.com/57162812/163096724-e49501f6-da8f-46d1-b22a-dcdb9019e191.png" width="60%"></p>
    <p align='center'><img src="https://user-images.githubusercontent.com/57162812/163096789-11084d00-45f1-471e-8711-04c047b9f0ae.png" width="60%"></p>
  - 반면, SW2.0은 Pipeline 복잡도와 사람의 개입을 줄였다. → 성능 향상
 
## 2.1 Regression - based vs. Segmentation-based

- `Regression-based` : 이미지를 입력 받아 글자 영역 표현값들을 바로 출력
  - **TextBoxes '18** : 객체 검출에 사용되는 SSD를 글자 검출 task에 맞게 수정 → 글자 객체의 특징에 맞게 anchor box의 밀도와 종횡비 수정
  - 단점
    - 사각형 형태의 글자 검출에 특화되어있어, 임의의 글자 모양에는 한계를 가진다. : `Arbitrary-shaped text` → 불필요한 영역의 포함
    - anchor box보다 큰 종횡비의 box의 경우 성능이 하락한다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/163097674-22c4fcd4-af3c-4fa3-88b3-886bccbbf02f.png"></p>
- `Segmentation-based` : 이미지를 입력 받아 글자 영역 표현값들에 사용되는 화소 단위 정보를 뽑고, 후처리를 통해서 최종 글자 영역 표현 값들을 확보
  - **PixelLink '18** : 각 화소 별로 글자 영역에 속할 확률 & 한 화소가 글자 영역에 속하면 그 주위의 8개의 인접한 화소에 대해서 글자 영역에 속할 확률 → 임계치를 적용하여 이진화 → 연결된 성분 분석 → OpenCV를 사용하여 RBOX 정합
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/163098013-2f28a001-36d7-4d44-a8a0-98664a63680e.png" width="60%"></p>
  - 단점
    - 복잡하고 시간이 오래걸리는 후처리가 필요할 수 있다.
    - 서로 간섭이 있거나 인접한 개체 간의 구분은 어렵다.
-  `Hybrid` = `Regression-based로 대략의 사각영역` + `Segmentation-based로 해당 여역에서 화소 정보 추출`

## 2.2 Character-based vs. Word-based
- Character-Based Methods
  - 글자 기반으로 검출
  - 이를 조합하여 단어 단위의 위치 예측
  - 단점 : 글자 단위 위치 정보를 labeling이 필요
  - **CRAFT '19** : character region과 연결성을 예측 → word로 조합
    -이때, 글자별 GT가 필요한 것을 `Weakly-Supervised Learning`으로 해결
    - Weakly-Supervised Learning : 단어 단위 라벨링을 통해 글자 단위 라벨링 추정
- Word-Based Methods
  - 단어 기반 검출
  - 글자 단위 GT 필요 없음

# 3. Baseline Model-EAST

## 1.1 Introduction

`Efficient` + `Accurate`

**IDEA**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/163098956-ef2edc36-9e92-4857-bd28-5a32784f8b2c.png" width="60%"></p>

- 화소 단위 정보
  - 글자 영역 **중심**에 해당하는지 : score map
  - 어떤 화소가 글자 영역이라면 해당 Bounding box의 위치는 어디인지 : geometry map

**Fully Convolutional Network**
- UNet 구조
  - Feature extractor stem : 큰 이미지 → 작은 이미지
  - Feature merging branch : 작은 이미지 → 큰 이미지
  - Output : 화소 단위 정보 출력
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/163099342-cfff7235-04a6-4afa-89ea-ac14c22af041.png" width="40%"></p>

**Score Map** : 글자 영역 중심에 해당하는지 
- H/4 x W/4 x 1 binary map

**Geometric Map** : 글자 영역이라면 해당 bbox의 위치는 어디인지
- RBOX 형식 = 회전 각도 예측(1 channel) + bbox의 4개 경계선까지의 거리 예측(4 channel)
- QUAD 형식 = bbox의 4개 점까지의 offset을 예측(8 channel)

**Post-processing** : RBOX 기준
1. Score map 이진화
2. 사각형 좌표값 복원
    1. p0~p3의 좌표를 쉽게 구할 수 있는 좌표축을 새로 설정
    2. 좌표축을 이미지 좌표축으로 변환하는 과정을 구하고,
    3. 이 변환의 역변환을 좌표값들에 적용
3. 중심 영역의 화소별로 bbox가 생기므로 하나의 글자에 여러개의 bbox가 생긴다.
    - 이를 하나로 합쳐주기 위해 `Locality-Aware NMS` → Standard NMS에 비해 월등한 시간 복잡도
    - 위치 순서로 탐색하면서 비슷한 것들을 하나로 통합한다. : IoU 기반
    - 통합 시 score map 값을 weighted merge
 

