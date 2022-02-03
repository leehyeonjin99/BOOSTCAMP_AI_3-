# Data 이해하기

## 1. dataset의 종류

- 구조 관점 : 정형 vs 반정형 vs 비정형
- 시간 관점 : 실시간 vs 비실시간
- 저장 형태 관점 : 파일 vs 데이터 베이스 vs 콘텐츠 vs 스트림


- 수치형 데이터
  - 연속형 : 길이, 무게, 온도
  - 이산형 : 주사위 눈금, 사람 수
- 범주형 데이터
  - 명목형 : 혈액형, 종교
  - 순서형 : 학년, 별점, 등급


### 1-1. 정형 데이터

<img src="https://user-images.githubusercontent.com/57162812/152337574-0b7b6170-5e10-4718-af10-fd6b67abae88.png" width=300>

- 테이블 형태로 제공 → csv, tsv 등
- Row : 1개 item
- Column : feature(attribute)

✅ 가장 쉽게 시각화 가능 : 통계적 특성과 feature 사이 관계, 데이터 간 관계, 데이터 간 비교

### 1-2. 시계열 데이터

<img src="https://user-images.githubusercontent.com/57162812/152337657-1abc4b2b-f01b-4a0e-8a26-dfc3f51ad87e.png" width=500>

- 시간 흐름에 따른 데이터 : Time-Series
- ex) 정형 : 기온, 주가 / 비정형 : 음성, 비디오
- 구성 요소
  - 추세 요인 : 자료가 어떤 특정한 형태를 취함
  - 계절 요인 : 고정된 주기에 따라 자료가 변화할 경우
  - 순환 요인 : 알려지지 않은 주기를 가지고 자료가 변화
  - 불규칙 요인 : 추세, 계절, 순환 요인으로 설명할 수 없는 회귀 분석에서 오차에 해당하는 요인

### 1-3. 지리/지도 데이터

<img src="https://user-images.githubusercontent.com/57162812/152337828-7a34cd73-2fb4-4022-ad4b-2985e2d27378.png" width=400>

- 지도 정보와 보고자 하는 정보간의 조화 중요+지도 정보를 단순화 시키는 경우도 존재
- 다양한 실사용

### 1-4. 관계 데이터 

<img src="https://user-images.githubusercontent.com/57162812/152338136-f1b2e632-350a-4560-99c6-c8d83a53bd19.png" width=350>

- 객체 간의 관계 시각화 : Graph visualization / Network Visualization
- Node : 객체
- Link : 관계
- 크기, 색, 수 등으로 객체와 관계의 가중치 표현

### 1-5. 계층적 데이터

<img src="https://user-images.githubusercontent.com/57162812/152338493-716a97de-fc1a-422a-9342-0dc988f05fa5.png" width=300>

- 포함관계 분명 : 네트워크 시각화로도 표현 가능
- ex) Tree, Treemap, Sunburst

# 시각화 이해하기

- Mark : 이미지의 기초적인 graphical element
  - 점, 선, 면으로 이루어진 데이터 시각화

- Visual Channel : 각 마크들을 변경할 수 있는 요소
  - Position : Horizontal, Vertical, Both
  - Color : Black, Red, Green
  - Shape : star, triangle
  - Tilt
  - Size : Length, Area, Volume

## 전주의적 속성 : Pre-attentive Attribute

- 주의를 주지 않아도 인지하게 되는 요소
  - Orientation, Length, Width, Size 등등 다양한 전주의적 속성 존재
- 여러가지 전주의적 속성을 동시에 사용하면 인지하기 어렵다.
  - Visual Popout(시각적 분리)는 적절한 사용시 발생한다.
