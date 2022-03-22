# Efficient in Object Detection
## Model Scaling
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159458296-f388e533-3242-4f9c-9f39-ce239fdb5904.png" width="80%"></p>

- 효율적으로 모델을 쌓는 방법은?
  - width scaling : channel을 늘리는 방향
  - depth scaling : layer의 수를 늘리는 방법
  - resolution scaling : image size를 늘리는 방법

**Width Scaling**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159458615-a9362ff9-38c4-4d8c-994c-d0478fdb3075.png" width="60%"></p>

**Depth Scaling**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159458651-d9e0d934-4187-4d9c-8fad-d91be0eeadd0.png" width="90%"></p>

## 등장배경

더 높은 **정확도**와 **효율성**을 가지면서 ConvNet의 크기를 키우는 방법은 없을까?
> EfficientNet 팀의 연구는 네트워크의 폭, 깊이, 해상도 모든 차원에서의 균형을 맞추는 것이 중요하다는 것을 보여주었다. 그리고 이러한 균형은 각각의 크기를 일정한 비율로 확장하는 것으로 달성할 수 있었다.

# EfficientNet
## 등장배경
- parameter 수가 점점 많아지고 있는 모델들
- ConvNet은 점점 더 커짐에 따라 점점 더 정확해지고 있다.

**But**
- 점점 빠르고 작은 모델에 대한 요구 증가
- 효율성과 정확도의 trade-off를 통해 모델 사이즈를 줄이는 것이 일반적
- 하지만, 큰 모델에 대해서는 어떻게 압축시킬지가 불분명
- 따라서 이 논문은 아주 큰 SOTA ConvNet의 efficiency를 확보하는 것을 목표로 한다.
- 그리고 모델 스케일링을 통해 이 목표를 달성

## Scale up
**Width Scaling**
- 네트워크의 width를 스케일링 하는 방법은 작은 모델에서 주로 사용
- 더 wide한 네트워크는 미세한 특징을 잘 잡아내는 경향이 있으며 학습이 쉽다.
- 하지만, 더 극단적으로 넓지만 얕은 모델은 high-level 특징을 잘 잡지 못하는 경향이 있다.

**Depth Scaling**
- 네트워크의 깊이를 스케일링 하는 방법은 많은 ConvNet에서 쓰이는 방법
- 깉은 ConvNet은 더 풍부하고 복잡한 특징들을 잡아낼 수 있고, 새로운 테스크에도 잘 일반화됨
- 하지만, 깊은 네트워크는 gradient vanishing 문제가 있어 학습이 어려움

**Resolution Scaling**
- 고화질의 input 이미지를 이용하면 ConvNet은 미세한 패턴을 잘 잡아낼 수 있음
- Gpipe는 480x480 이미지를 이용하여, ImageNet에서 SOTA를 달성

**Compund Scaling**
- 세가지를 모두 늘린다.

## Accuracy & Efficiency
모델의 Accuracy를 max하는 d,w,r을 찾는다. 
s.t. 
- 모델의 메모리는 target memory보다 작다
- 모델의 FLOPS는 target_flop보다 작다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159466873-0918369d-f417-44ba-ae7a-1285a68f0fda.png" width="40%"> <img src="https://user-images.githubusercontent.com/57162812/159466990-e04ca739-36d0-4d9d-8edb-4b673fa50d74.png" width="55%"></p>

**Observation1**
> 네트워크의 폭, 깊이, 혹은 해상도를 키우면 정확도가 향상된다. 하지만, 더 큰 모델에 대해서는 정확도 향상 정도가 감소한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159467667-2d9e94c4-a161-450c-8714-279e60a3b5d8.png" width="70%"></p>

**Observation2**
> 더 나은 정확도와 효율성을 위해서는, ConvNet 스케일링 과정에서 네트워크의 폭, 깊이, 해상도의 균형을 잘 맞춰주는 것이 중요하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159467877-6be0621c-646c-4eab-9cf5-4365b30723f5.png" width="40%"></p>

**Compound Scaling Method**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159468070-97523c46-1cee-498b-b924-260845dd2073.png" width="30%"></p>

## EfficientNet
- EfficientNet-B0
  - MnasNet에 영감을 받음
- Acc와 FLOPs를 모두 고려한 Neural Net 

**Step1**
- ∅=1로 고정
- α, β, γ를 samll grid search를 통해 찾음
- α=1.2, β=1.1, γ=1.15 under constraint of  αβ²γ²≈2
**Step2**
- α, β, γ를 상수로 고정
- 다른 ∅를 사용해 scale up
- EfficientNet - B1~B7

## EfficientDet

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159470796-0756661c-45bf-4460-b5b0-04c4ed124699.png" width="80%"></p>

**Object Detection은 특히나 속도가 중요**
- 모델이 실생활에서 사용되기 위해서는 모델의 사이즈와 대기 시간에 제약이 있기 때문에, 모델의 사이즈와 연산량을 고려해 활용여부가 결정된다.
- 이러한 제약으로 인해 Object Detection에서 Efficiency가 중요해지게 됨

**그동안의 시도들**
- 1 Stage Model
  - YOLO, SSD
- ANchor free model
  - CornerNet
- 하지만, Accuracy가 낮다.

**Motivation**
- 자원의 제약이 있는 상태에서 더 높은 정확도 및 효율성을 가진 detection 구조를 만드는 것이 가능할까?
  - Backbone, Neck, Head 세 가지를 적당히 scale up 해서 정확도 및 효율성을 올릴 수 있을까?

## Challenge
1. Efficient multi-sclae feature fusion
  - high level feature map과 low level feature map을 단순히 더했다.
  - 서로 다른 resolution의 feature map을 단순 합이 맞을까?
  - 따라서, 가중합!! BiFPN  
  ➡ 하나의 간선을 가진 노드 제거, Output 노드에 input 노드 간선 추가
2. Model scaling
  - EfficientNet B0~B6을 backbone으로 사용
  - width와 depth를 compound 계수에 따라 증가시킴
