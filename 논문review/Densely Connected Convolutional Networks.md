# Densely Connected Convolutional Networks
## Intro
DenseNet 논문이 발표될 당시 resnet을 비롯한 여러 논문에서의 연구 결과에서 layer에 "skip connection"을 포함하고 있다면 network를 좀 더 깊게 쌓을 수 있고 학습을 용이하게 만든다는 점에서 착안하여 각 layer 간 feed-forward 형태로 연결한 "DenseNet"을 소개한다.

## Dense Connection
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154312978-b8953806-60a2-4fa3-8a91-eb2074d5d818.png" width=400></p>

DenseNet은 `ResNet`의 Shortcut 개념을 더 확장하여 CNN 구조를 바꾸는 시도를 하였다. 즉, 입력값의 `Summation`에서 `Concatenation`으로의 변화이다.

layer 간 정보 흐름을 최대화하기 위해서 **모든 layer들이 서로 연결되게끔 구성**하였다. 각각의 layer는 이전의 모든 layer들로부터 추가적인 정보를 얻고, 그들 고유의 feature map을 그 다음의 모든 layer로 전달한다. 따라서 Dense하게 연결되었다는 이유로 이 구조를 DenseNet이라 부른다.

수식으로 표현하자면 L layer에 대해서 ResNet의 경우 L번의 connection이 필요하다면, DenseNet의 경우 L(L+1)/2 connection이 필요하다.

## DenseNet의 장점

- DenseNet은 기존의 convolution network에 비해 장황한 feature map에 대한 불필요한 학습은 필요없다. 왜냐하면 이제는 이전의 모든 layer로부터 정보를 받기에, feature map 이 더 견고해지기 때문이다. 따라서 **더 적은 파라미터 수**를 요구한다.

- DenseNet은 네트워크에 더해지는 정보를 명확하게 구분하면서 정보를 보존한다. DenseNet은 매우 **narrow**한데, feature map을 그대로 보존하면서 feature map의 작은 집합을 네트워크 전역에서 관리하는 뭉쳐있는 정보 덩어리에 추가하기 때문이다.

- 정보와 기울기의 개선된 흐름 덕에 **학습하기 매우 쉽다**. 각각의 layer들은 loss function 및 input signal로부터의 기울기에 직접적을 접근할 수 있기 때문에 네트워크의 구조가 깊더라도 학습이 쉬워진다.

- dense connection은 **regularizing 효과**가 있어 overfitting을 줄여준다.

## DenseNet

- x_0 : conv network를 통과한 single image
- H_l() : l번째 layer의 비선형 변환 : BN, ReLU, Pooling, Conv로 구성된 `Composite Function`
- x_l : ㅣ번째 layer의 출력

`ResNet`의 경우 <img src="https://user-images.githubusercontent.com/57162812/154315582-55c12d62-86f3-4187-9988-a5d3f258444e.png" width=160> 과 같이 표현할 수 있다.

이때, ResNet의 장점은 identity function을 통해 gradient가 뒤쪽 layer에서 앞쪽 layer로 직접 흐를 수 있다는 점이다. 하지만, identity function과 H_l의 출력이 summation으로 합해지기 때문에 네트워크의 정보 흐름을 방해할 수 있다.

`DenseNet`의 경우 <img src="https://user-images.githubusercontent.com/57162812/154316066-837f29d4-f0f9-4a0d-a1d1-0491596a35ad.png" width=160> 과 같이 표현할 수 있다.

`Pooling layer의 필요성` : Concatenation 연산은 feature map의 크기가 다를 경우 연산이 불가능하다. 따라서 down-smapling layer를 이용하여 feature map의 크기를 바꾸는데, 이를 위해 네트워크를 여러개의 dense block으로 나누고, 그 사이에 transition layer를 둔다. transition layer는 convolution 연산 및 pooling을 수행하는데, 이는 BN layer → 1x1 Conv → 2x2 Average Pooling layer 로 구성된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154316708-3432e54f-113d-4421-8eb6-ce34f5423fb2.png" width=400></p>

`Growth Rate` l번째 layer는 k_0+k(l-1)개의 input channel을 가지는데, 여기서 k가 하이퍼파라미터로 네트워크의 growth rate를 의미한다. 첫번째 그림에서는 k=4 인 것이다. growth rate는 전역 상태에 각 layer가 기여하는 새로운 정보의 양을 조절한다.

ImageNet을 대상으로한 DenseNet의 구조는 다음과 같다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154317546-34c46aec-db79-4117-9f77-973b28ca1b56.png" width=600></p>

## Conclusion
결과적으로, DenseNet은 degradation이나 overfitting 없이 정확도를 꾸준히 개선할 수 있었으며, 상당히 적은 수의 파라미터 및 연산량으로도 최고의 수준을 낼 수 있었다.

이는 DenseNet이 identity mapping, dense supervision, diversed depth를 통합하여 네트워크 전역에서의 feature reuse를 가능하게 하였고, 그 덕에 더 작으면서도 정확한 모델을 학습할 수 있었기 때문이다.
