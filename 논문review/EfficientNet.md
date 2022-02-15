# Abstract
기존 CNN은 정확도를 높일 때, arichitecture를 만들고 channel, depth, resolution 중 하나를 높이는 방식으로 계산량을 늘려 정확도를 올리는 방식을 사용하였다.
- 본 연구에서는 depth, width, 그리고 resolutiondㅢ balancing이 더 나은 성능으로 이끌 수 있음을 보여준다.
- How?
  - compound coefficient 파라미터를 사용해 scailing
 
 EfficientNet : NAS(Neural Architecture Search, 인공 신경망 설계를 자동화하는 기술)를 통해 설계한 새로운 Baseline
 
 EfficientNet-B7은 ImageNet 데이터에서 가장 성능이 좋은 정확도 84.3%을 달성하며, 기존의 CNN보다 파라미터 수가 훨씬 적다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154090342-77b6d412-be21-4061-be5b-3e06348e6511.png" width=500></p>
 
 # Introduction
 모델은 scaled up될수록 성능이 좋아지는 경우가 많다. 또한, 이전 연구들에서는 channel, depth, resolution 중 하나를 높이는 방식으로 scaled up 하였다.
 
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154087584-e2f56def-3536-4d45-937b-a217a37cc7a6.png" width=1000></p>

(a, b, c, d)는 기존 모델의 scale up 방식이고, (e)는 논문에서 발표한 방식이다.

본 연구에서 CNN의 정확도를 높이기 위해 사용한 방법
- Compound Scaling Method
  - 네트워크의 width/depth/resolution의 **balance를 맞추는 것이 중요**하다
  - 이 balance는 width, depth, resolution을 각각 일정한 비율로 증가하기만 하면 된다.
  - 간단하고 효율적인 **compund scaling method**를 제안한다.
  - 고정된 스케일링 계수 세트를 사용하여 **각 요인을 균등하게 스케일링**한다.
  - 예를 들어, 컴퓨팅 리소스를 2^N배 만큼 더 사용하고 싶으면, 다음과 같이 파라미터들을 N승으로 증가시킨다.
    - depth by α^N, width by β^N, image size by γ^N
    - α, β, γ는 constant coefficients이며, original small model에서 grid search를 통해 결정
- New Baseline : EfficientNet
  - 기존의 MobileNets와 ResNet에 scaling mehtod가 잘 작동된다는 것을 볼 수 있다.
  - model scaling의 효과는 baseline network(MobileNets, ResNet)에 크게 의존한다.
  - 본 연구에서는 NAS를 통해 새로운 baseline을 개발했으며, 이를 EfficientNet이라 부른다.

# Compund Model Scaling
## 각각의 Dimension scale up의 효과
- Depth
  - 효과
    - capture richer, complex feature
    - generalization performance 향상
  - 단점
    - vanishing gradinet : skip connection이나 BN에도 불구하고 존재하는 문제이다.

- Widht
  - 특징
    - width의 scale up은 보통 작은 network에서 사용된다.
  - 효과
    - fine-grained feature를 더 잘 뽑아내고 train이 쉽다
  - 단점
    - 너무 넓고 얕은 network는 higher level feature를 뽑아내기 어렵다.

- Resolution
  - 효과
    - potentially fine-grained pattern을 잘 뽑아낸다.

각각의 dimension을 늘리는 것은 accuracy 향상에 도움되지만, 일정 수준에 도달한 모델들에서는 accuracy gain이 사라진다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154093711-35183f68-2891-4131-86ad-51e628b7728c.png" width=800></p>

## Compound Scaling : 3 Dimension 변화
w를 증가시켰을 때, d와 r의 값에 따른 정확도를 표현한 그래프이다. 그래프를 보면, d와 r을 같이 증가시켰을 때 가장 좋은 성능을 보였다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154094139-8ed6dd9c-6ab5-4285-94af-8a507aec443d.png" width=500></p>

따라서, **w, d, r을 모두 balance 있게 증가시키는 것이 중요**하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154094862-da155e41-3c38-4475-9f13-2be44ceb7ea1.png" width=300></p>

α, β, γ는 small grid search로 결정할 수 있다. 또한, Φ는 사용자가 지정하는 coefficient로 컴퓨터 자원을 얼마나 더 사용할 수 있는지를 나타낸다.

# EfficientNet Architecture
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154095976-0cf2e7e3-f5ae-439a-8716-9a52716e04fb.png" width=500></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154096016-3e6245ce-3688-46f4-8923-bd0c22c393dc.png" width=500></p>

