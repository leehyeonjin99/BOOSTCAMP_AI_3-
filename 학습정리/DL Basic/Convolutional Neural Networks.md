# Convolutional Neural Networks
## Convolution
<img src="https://user-images.githubusercontent.com/57162812/153021290-4d5e56f9-0006-4115-bef7-3ffb22c2bde9.png" width=400>

- 2D Convolution의 의미는?<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153022190-f569d81c-96cc-496b-bb1a-8bb2b1fbadbc.png" width=400></p>
  - 해당 convolution filter의 모양을 input image에 찍는다. 적용하고자 하는 filter의 모양에 따라서 같은 이미지에 대해서 convolution output이 다음과 같은 효과를 나타낸다.  
    - Blur : 블러 효과  
    - Emboss : 강조 효과  
    - Outline : 외곽선  
  - 예를 들어, 3x3 filter의 모든 칸의 값이 1/9라면 3x3 이미지에 있는 값의 평균이 다음번 convolution filter output이 된다. 따라서 평균을 내기 때문에 블러 효과를 낼 수 있다.

## RGB Image Convolution

- kernel의 channel 숫자는 input의 channel의 수에 결정된다. Convolution operation이 진행되고 난 Feature Map의 channel은 1이 된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153023104-64965a0c-ca05-4803-9842-edb565bacd76.png" width=400></p>

- 그렇다면, feature map의 channel의 수는 어떻게 변경할까?
  - kernel의 개수를 원하는 feature map의 channel의 수만큼 늘리면 된다. 만약 input의 channel이 3이고 feature map의 channel이 4이기를 원한다면, 5x5x3 kernel 4개가 필요하다.
  - 즉, input channel과 convolution feature map의 channel을 알면 적용되는 convolution의 channel의 수와 개수를 알 수 있다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153023859-a758ed0e-3c54-4d3b-86fd-fd6cb9c1e13f.png" width=400></p>

## Stack of Convolutions

여러번의 Convolution 연산을 적용시키면 Stack of Convolution이 된다. 단, 여러번의 Convolution 연산은 하나의 선형적인 연산으로 가능므로 Convolution 연산이 끝난 후 ReLU, Sigmoid, Tanh와 같은 nonlinear 연산을 적용한다. 

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153024271-fed1b2a5-30e8-46a9-9bfa-bbb74907a962.png" width=400></p>

그렇다면 Convolution 연산에 필요한 parameter의 개수는 어떻게 계산할까?
- #parameter = kernel size(= kernel width X kernel height) X #input channel X #output channel
- 위 그림에서 첫번째 Convoluiton 연산에 필요한 parameter의 개수는 5x5x3x4=300 이 된다.

## Convoluitonal Neural Networks
CNN은 다음의 구성요소를 갖는다.
1. Convolution Layer
2. Pooling Layer
3. Fully Connected Layer

Convoluiton Layer와 Pooling Layer는 feature extraction의 역할을 한다.

Fully Connected Layer는 decision making 역할을 한다. 하지만, 모델의 parameter의 수가 늘어날수록 generalization performance가 떨어져 학습이 어려워져 Fully Connected Layer를 없애거나 줄이는 추세에 있다.

## Stride

- 커널로 입력값을 옮기는 단위

## Padding
- Convolution feature map의 size는 input size보다 작다. 즉, bound(외곽)의 정보가 흐릿해진다.
- Padding을 통해 입력의 가장자리에 0을 채워넣어 feature map의 size를 키워줄 수 있다. 따라서 입력값의 가장자리를 잘 관찰할 수 있다. 
- 1 Stride와 적절한 Padding(=Kernel width//2)으로 input과 convoperation의 출력인 feature map의 spatial dimension을 같게 할 수 있다. 

## 1x1 Convolution

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153027327-998b9ddc-a847-4fc3-b109-c27d7dc31ce2.png" width=400></p>

1x1 Convolution을 사용하는 이유는?
1. Channel 방향의 차원 축소
2. Model의 깊이를 증가시킴과 동시에 parameter의 수를 줄인다.  
  Channel의 수를 감소시킴으로써 다음 Convolution 연산의 파라미터를 줄여준다.
3. Bottleneck Architecture





