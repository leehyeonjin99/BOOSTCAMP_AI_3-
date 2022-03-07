# Problems with deeper layers
## Going neural network is getting deeper and wider

- Deeper networks가 성능이 더 좋다
  - Larger receptive fields
  - More capacity and non-linearity
## Hard to optimizer
**Deeper networks are harder to optimize**

- Deeper networks의 부작용
  - Backpropagation에서의 Gradient vanishing/exploding
  - 계산 복잡도 증가
  - Degradation Problem : network의 depth가 커질수록 accuracy는 saturated (마치 뭔가 가득차서 현상태에서 더 진전이 없어져 버리는 상태)가 되고 degradation이 진행
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156992704-139e4d6d-1662-4ad7-87ba-39ba0c73cdeb.png" width='60%'></p>

# CNN architectures for image classification 2
## GoogLeNet
**Inception module**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156993838-ad49fc25-d34b-4ef1-858a-ee70da609194.png" width='70%'></p>

- 하나의 layer에서 다양한 크기의 conv filter를 사용하여 여러 측면으로 activation을 관찰 → 수평 확장
- 여러 측면의 activation을 channel 축으로 **concatenation**하여 다음 layer로 전달한다.
- 하지만, width 확장으로 계산 복잡도와 용량이 증가하게 된다. → **1x1 conv**을 통해서 channel dimension을 줄여준다. → **bottleneck layer**

**1x1 convolutions**
- 공간의 크기는 변하지 않는다.
- filter의 개수로 channel dimension을 변경시켜준다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156994167-e20d7bfe-6b29-4da1-b75b-a4be07562a76.png" width='70%'></p>

**Overall architecture**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156996495-806661ab-2cea-4c86-8413-77dc55f1cd64.png" width='100%'></p>

- Stem network : 일반적인 CNN 형태
- Stacked Inception modules
- 깊게 쌓으면 backpropagtion gradient vanishing 문제 발생 → Auxiliary classifier
  - 중간 결과로부터 task를 수행하기 위해 auxiliary classifier의 도움으로써 loss를 측정하게 되고 backpropagation이 가능해진다.

**Auxiliary classifier**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156996696-a3ebcea6-4d88-43a4-86b5-5b899b38cdd0.png" width='30%'></p>

- gradient vanishing problem을 해결해준다.
- AvgPool + Conv + FC + FC + Softmax Activation
- 학습 도중에만 사용하고 Test 시에는 사용하지 않는다.

## ResNet
**Degradation problem**
- network의 depth가 증가하면 accuracy는 staurated한다. → **degrade rapidly**
- training error 또한 증가하였으므로 overfitting이 원인이 아니다. 이 문제가 **optimization**

**Hypothesis**
- layer가 깊어질수록 target function인 H(x)를 바로 학습하기 어려워진다.
- 따라서, residual를 학습하자.
  - Target function : H(x)=F(x)+x
  - Residual function : F(x)=H(x)-x

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156998324-e34017d3-8f94-40a9-ba7b-5eff79a44ac1.png" width='50%'></p>

**A solution** : Shortcut connection, Skip connection

backpropagation의 진행 방향이 두가지가 생긴다. 그 중 shorcut connection을 통해 backpropagation이 진행될 경우에는 gradient vanishing problem을 걱정할 필요가 없다.

**Analysis of residual connection**
residual connection이 좋은 이유는?

- 2^n의 경우의 수로 gradient가 지나갈 수 있는 input, output path가 생성된다. → 다양한 경로를 통해서 복잡한 mapping을 학습해낼 수 있다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156999220-14552ea8-a3ba-4f87-a4aa-823d505b9412.png" width='70%'></p>

**Overall architecture**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/156999940-6a9177bb-6cd2-47fa-9b35-2ec01e774ecb.png" width='70%'></p>

- He initialization :  resnet에 적합한 initialization
  - skip connection에서 x값이 더해진다면 큰값이 계속해서 더해질 수 있기 때문이다.

## Beyond ResNets
**DenseNet**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157001191-b1ec14c2-9500-4993-a77e-0eed5c4c9c82.png" width='70%'></p>

- 직전의 block뿐 아니라 이전의 모든 layer의 정보들을 전달한다.
- 상위 layer에서도 하위 layer에서의 정보를 재참조할 수 있다.
- channel axis 방향으로 concatenation
  - channel이 늘어나 필요 memory 증가

**SENet**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157002428-a9b9e1dd-f937-47c0-81f0-4e661bb69ea0.png" width='70%'></p>

- Channel 간의 중요도를 파악한다.
- Squeeze : AvgPooling을 통해 각 channel의 공간정보를 없애고 각 채널의 분포를 구한다.
- excitation : FC layer를 통해 채널간의 연관성 고려해 channel을 gating

**EfficientNet**
deep, wide, 그리고 high resolution 네트워크를 적절한 비율로 모두 증가시킨다.
