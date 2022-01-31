# Abstract
- deep neural network

  ▶ (+) powerful

  ▶ (-) memorization : 학습시 정답만 기억

  ▶ (-) sensitivity to adversarial examples(대조 샘플)

→ 대안책 : mixup : example의 convex combination을 통한 data augmentaion

- mixup

  ▶ (+) Generalization of SOTA(현재 최고 수준의 결과) neural network architecture 개선
  
  ▶ (+) corrupt label의 memorization 감소
  
  ▶ (+) adversarial example에 대한 견고함
  
  ▶ (+) GAN의 training에 안정적
  
# Introduction
- 신경망의 특징

  1. training data의 평균 error를 최소화함으로써 신경망을 최적화 한다. : **ERM** 
  2. SOTA 신경망 사이즈 ∝ training example의 수

- ERM의 단점
  
  ▶ (-) learning machine의 크기가 training data의 수에 비례하게 증가하지 않아야 ERM의 수련 보장 : 신경망의 특징2에 위배
  
  ▶ (-) 강한 규제에도 training data를 memorize : 과적합 → OOD 데이터에 취약
  
  ∴ 대안책 : VRM : 훈련 데이터와 훈련데이터셋의 근방 분포로 학습하여 데이터 증강 : generalization 개선
  
## Contribution
- method of constructing virtual training examples

  ▶ linear combination  
      <p align="center"><img src="https://user-images.githubusercontent.com/57162812/151776846-603324db-372e-4903-b2c0-be6fd34d6975.png" width=400></p>
  
  ▶ (+) CIFAR-10, CIFAR-100, ImageNet-2012 데이터셋에서 SOTA 성능
  
  ▶ (+) corrupt labels 혹은 adversarial example에 있어서 견고함
  
  ▶ (+) speech(음성), tabular(표) 데이터에 대한 일반화 개선
  
  ▶ (+) GAN에서 견고함
  
# From Empirical Risk Minimization To Mixup
## ERM 기반 학습
- f∈F : relationship between a random feature vector X and random target vector Y
- l : loss function that penalizes the diffences betwwen prediction f(x) and actual target y

  ▶ **minimize the average of the loss function** over the data distrubution P : **expected risk**
  
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151779120-a7c0a73f-8ec8-466d-98c1-96d151ad47c0.png" width=200></p>
  
  ▶ 하지만 보통 모집단의 분포는 모르기 때문에 training dataset을 통해 근사한다. : **empirical distribution**(경험적 분포)
  
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151779512-cfe9faf1-618c-4735-b4ad-489b36f0d0fb.png" width=200></p>

  ▶ expected risk + empirical distribution = empirical risk
  
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151779767-da544769-acc4-4dcb-a904-c7964b85b37c.png" width=300></p>

  → empirical risk를 최소화 : ERM 기반 학습

  ▶ (-) parameter의 수가 많은 모델에서 학습시, empirical distribution을 전부 외워버린다.
  
  → 대안책 : VRM
  
## VRM 기반 학습
  
  ▶ **vicinity distribution**(근방 분포)
  
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151780462-988a20ae-c95f-4a50-a009-75408bf749bf.png" width=200></p>

  ▶ empirical risk + vicinity distribution = empirical vicinal risk
  
  <p align="center"><img src="https://user-images.githubusercontent.com/57162812/151780729-46317697-c00c-4b4d-bd3d-a9d46af096c0.png" width=200></p>

  → empirical vicinal risk 최소화 : VRM 기반 학습
  
### VRM 기반 학습 : Mixup

- λ~Beta(α,α) with α∈[0,1]

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151781521-82bc006c-a94a-4fab-a09b-c70ad3e61fff.png" width=500></p>

  ▶ α는 mixup의 hyper-parameter로 feature-target 쌍의 imterpolation의 strength를 조절한다. 또한 ERM의 α→0 현상은 일어나지 않게 한다.
  
## What is mixup doing?

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151782747-e0997550-9314-4caa-ab86-f5300df3a6fd.png" width=300></p>


- Encourage the model f to behave linearly in-between traing ezamples

  ▶ (+) 훈련 데이터가 아닌 데이터에서 예상치 못한 결과를 내는 것을 줄여준다.
  
  ▶ (+) Occam's razor의 측면에서 좋은 inductive bias
  
- <img src="https://user-images.githubusercontent.com/57162812/151782875-ee517f43-0133-43f8-8224-40d85ace3fa1.png" width=300>

  ▶ mixup은 uncertainty의 측정을 부드럽게 나타내 decision boundary, 즉 class와 class 사이를 선형적으로 표현
  
  ▶ mixup이 ERM에 비해 과적합이 덜 발생하며 regularization 역할을 한다.
  
- <img src="https://user-images.githubusercontent.com/57162812/151783331-3c096c6a-98d5-4bc5-bda1-51877dcfac41.png" width=700>

  ▶ miss 측면과 norm of the gradients of the model 측면에서 모두 Mixup이 ERM보다 좋은 성능을 보인다.
