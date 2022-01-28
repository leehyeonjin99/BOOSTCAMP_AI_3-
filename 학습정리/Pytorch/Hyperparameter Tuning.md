# Hyperparameter Tuning

## 모델의 성능 올리는 방법

1️⃣ 모델 바뀌보기  
  - 이미지:RestNet, CNN / NLP:Transformer 과 같이 각 데이터 별 모델은 거의 고정되어 있으므로 처음에 잘 선택하자

2️⃣ 데이터 추가하기 및 학습 데이터 오류 찾아보기
  - 가장 효과적인 방법이다.

3️⃣ HyperParameter 튜닝하기
  - HyperParameter : 모델이 스스로 학습하지 않으며 사람이 지정해준다.
  - ex) learning rate, 모델의 크기, optimizer
  - 하지만 요즘은 데이터의 크기로 극복해 hyperparmeter 튜닝의 중요성은 낮아졌다.

### HyperParameter Tuning
1️⃣ GridSearch
  
  - 일정한 범위를 정해 값을 자른다.
  
  <img src="https://user-images.githubusercontent.com/57162812/151369079-1c5c6dad-42c7-4dec-b83e-c42621372283.png" width=200>

2️⃣ RandomizedSearch

  - 랜덤하게 파라미터를 지정한다.
  
  <img src="https://user-images.githubusercontent.com/57162812/151369312-c98a30e8-116f-420e-8295-eb35ecfdc3e2.png">

3️⃣ 베이지안 기반 기법 : BOHB

### Ray : 하이퍼파라미터 튜님을 위한 도구
- multi-node multi processing 지원 모듈
- ML/DL의 병렬 처리를 위해 개발된 모듈
- 분산 응용 프로그램을 빌드하고 실행하기 위한 간단한 기본 요소 제공
- HyperParameter Search를 위한 다양한 모듈 제공
