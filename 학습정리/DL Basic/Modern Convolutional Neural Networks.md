# Modern Convolutional Neural Networks
## AlexNet
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153027845-7a537129-8f88-47cd-8327-a5c87e4490aa.png" width=400></p>

- input에 대해 2개의 network 존재한다. 즉, 2개의 output이 존재한다. 하나의 GPU의 용량 문제로 2개의 GPU로 나누어 진행한 것으로 보인다.
- 11x11 filter를 사용하였다.
  - 이는 receptive field(하나의 convolutional kernel이 볼 수 있는 이미지 영역)은 커지지만 상대적으로 더 많은 파라미터가 필요하다.
- 5 Convolutional Layers + 3 Dense Layer
- KEY IDEA
  - ReLU activation
  - 2개의 GPU 사용
  - Local response normalization(입력공간에서 response가 많이 나오는 몇개를 죽여버린다.), Overlapping pooling
  - Data Augmentation
  - Dropout  
  ➡ 요즘 흔히 사용하는 방법들을 제시
  
### ReLU activation

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153028844-ec177966-c24a-4d7a-9254-b075b22aa70e.png" width=250></p>

- Linear model의 성질을 보존한다. : 0보다 값이 많이 커져도 기울기가 1로 일정하다.
- 경사하강법으로 최적화하기에 용이하다.
- Generalization에 좋다.
- 기울기 소실 문제를 극복하였다.
  - Sigmoid, Tanh activation은 0을 기준으로 멀어지면 기울기가 0에 수렴한다. 따라서 모델의 깊이가 깊어질수록 기울기가 소실되어 학습이 불가능해진다.

## VGGNet

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153029450-0532cb0c-e600-4a5e-96ce-57856815a3b5.png" width=400></p>

- Stride 1인 3x3 Convolution filter를 사용하여 Model의 depth를 증가시켰다.
- Fully Connected Layer에서 1x1 Convolution이 사용되었다.
- Dropout with p=0.5
- Layer의 개수에 따라 VGG16, VGG19

### Why 3x3 Convolution?

결론적으로, 3x3 convolution은 이보다 더 큰 filter의 convolution의 연산과 같은 결과 값을 가지는 동시에 parameter를 줄일 수 있다. 

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153030057-24e0bf80-a3d9-47f7-b557-5e27b70352f4.png" width=400></p>

- 3x3 Convolution 2번 : #params = 3x3x128x128x2=**294,912**
- 5x5 Convoluiton 1번 : #params = 5x5x128x128=**409,600**

3x3 Convolution을 2번 연산한 결과와 5x5 Convoluiton을 1번 연산한 결과는 같지만 parameter의 수는 3x3 Convolution 연산을 2번 진행한 것이 15% 적다. 즉, parameter의 수에 의존하는 학습 성능이 더 좋다 말할 수 있다. 

## GoogleNet

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153030845-5e5bad3c-da4f-4865-85c2-c3d442ae611f.png" width=500></p>

- 비슷한 Network 구조가 반복되는 NIN(network-in-network) 구조이다.
- Inception block : 하나의 입력이 들어왔을 때, 여러개로 퍼졌다가 하나로 합쳐진다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153031255-facd1cb0-6b50-496d-9cb4-433213c6d02b.png" width=400></p>

### Inception Block의 효과
**parameter의 개수를 줄인다.**

어떻게?  
1x1 Conv가 중간에 들어가있으므로, channel 방향의 dimension이 감소되어 전체적인 parameter의 수를 줄인다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153031810-67d11bbf-c65a-4135-a45e-1c78b902d131.png" width=450></p>

1x1 Convolution을 추가함으로써 parameter의 수를 30% 감소시킬 수 있다.

## ResNet

Overfitting은 주로 paramter의 개수로 인해 발생한다. 하지만 아래 그래프를 보면 알 수 있듯이 깊은 Layer의 모델은 Overfitting으로 인한 성능 감소가 아니다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153032518-63d184fd-8174-4d66-8541-c930667f449b.png" width=400></p>

ResNet은 Layer를 쌓더라도 성능이 잘 나오게 하는 데에 집중하였다.

따라서, Identity map(Skip Connection)을 추가하였다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153032767-88549fa3-d950-4341-a701-993ad86ae40a.png" width=400></p>

이는 예측값에 x(input)을 더해줌으로써 차이를 학습하기를 원하며 그 결과 Network가 Deep하게 학습 가능하도록 하였다.

### Bottleneck Architecture

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153033941-89acdfad-c57d-414e-8594-a3f700989733.png" width=400></p>

- Convolution 연산 전에 1x1 Convolution 연산을 통해 channel dimension을 줄여주고, Convoluiton 연산 후 1x1 Convolution 연산을 통해 원래 channel dimension으로 증가시켜준다.
- 이로써 #parameter를 줄여준다.

## DenseNet

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153034503-55c6c032-f974-43a9-b93d-b4aee3571b8f.png" width=320></p>

- input과 output을 더해주는 ResNet의 구조 대신 concatenate를 해준다.
- Dense Block : 각 layer는 모든 이전 layer의 feature map을 conatenation한다. 따라서 channel의 수가 기하급수적으로 증가한다.
- Transition Block : BatchNorm → 1x1 Conv → 2x2 AvgPooling 을 통해 channel dimension을 줄인다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153035363-8ec8e50b-84a6-4902-9fd3-f1c465ebbc18.png" width=530></p>

## Further Question

1. 수업에서 다룬 modern CNN network의 일부는, Pytorch 라이브러리 내에서 pre-trained 모델로 지원합니다. pytorch를 통해 어떻게 불러올 수 있을까요?

```python
import torchvision.models as models

resnet18=models.resnet18(pretrained=True)
alexnet=models.alexnet(pretrained=True)
squeezenet=models.squeezenet1_0(pretrained=True)
vgg16=models.vgg16(pretrained=True)
densenet=models.densenet161(pretrained=True)
```

