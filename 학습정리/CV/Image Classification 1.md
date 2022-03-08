# Course Overview
## Why is visual perception important?
**Artificial Intelligence(AI)**
- 인간의 지능을 필요로 하는 기능을 컴퓨터가 가능하게 한다.
- Cognition&Perception, Memory&Inference, Decision Making, Reasoning

**Perception to system**
- Input, Output data
- multi-modal association을 통해 정보 신호를 받는다
  > **Multi Modal**
  >
  > - 여러 가지 형태와 의미로 컴퓨터와 대화하는 환경
  > - 텍스트 외에 음성, 제스처, 시선, 표정, 생체신호 등 여러 입력 방식을 융합하여 인간과 컴퓨터 사이에 자연스러운 의사소통이 가능한 사용자 친화형 기술
  > 
  > [멀티 모달(Multi Modal) 딥러닝](https://ohs-o.tistory.com/93)

## What is computer vision?

이 중 Sight, 대략 75%의 정보가 눈으로부터 오고 뇌의 50% 이상이 시각적 정보로 이루어져있다.

- 사람의 시각의 연관성
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156964247-f509ab43-e8bb-40d2-b064-207854419dfc.png" width="70%"></p>
- CV의 시각의 연관성
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156964732-67ab71ee-5510-47ea-84be-a47b9fee880d.png" width="70%"></p>

그렇다면, 분석해놓은 정보를 이용해 장면에 해당하는 이미지나 3D scene을 재구성하는 것을 **Rendering**을 통한 **Computer Graphics**라고 한다. 반대로, 이미지나 3D scene을 통해 정보를 분석하는 것을 **Inverse Rendering**을 통한 **Computer Visoin**이라 한다. 

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156965048-d9dfa91f-aaa1-4648-bc7d-ba8c7506ad92.png" width="70%"></p>

CV는 컴퓨터로 구현하는 것 뿐 아니라, 사람의 시각 능력에 대한 이해를 바탕으로 한 CV 알고리즘의 연구를 포함한다. 즉, 사람의 biologic을 이해하고 어떤 식의 컴퓨터 알고리즘으로 구현할지까지도 포한다. 따라서, 사람의 시각능력에 대해 잘 이해해야 한다.

하지만, 우리의 visual perceptron은 불완전하다.
- 눈과 시각을 담당하는 뇌 부분들이 학습될 때, 똑바로 서있는 사람들에 대한 얼굴 패턴은 많이 봐왔지만, 얼굴이 뒤집힌 상태로 볼 기회는 많지 않았다. 따라서, 시각 기능이 편향되어서 학습되어 있다고 볼 수 있다.
- 어떤 시각 능력을 컴퓨터로 처음 만들기 위해서 사람의 구조를 모방하는 것이 자연스러운 시작인데, 사람의 시각 능력의 장단점을 먼저 이해함으로써 불완전성을 보완할 수 있는 방법을 생각해보는 것이 중요한 step이 될 것이다.

feature extraction의 패러다임이 변화하였다. 사람이 feature를 직접 추출하는 방안에서 데이터와 학습 방법을 통해서 feature를 추출한다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156965618-66ffa77f-fbc4-4795-8d1b-ea843a921fd8.png" width="70%"></p>
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156965641-3073d11e-5f81-44a5-ac58-7e3fe1adf152.png" width="70%"></p>

# Image Classification
## What is classification
**Classifier(분류기)**
- Input : 영상
- Ouput : 영상에 해당하는 category, class
- 어떤 물체가 영상속에 있는지 분류하는 mapping을 Classifier이라 한다.

## An ideal approach for image recognition
만약 이 세상의 모든 데이터를 가지고 있다면? **K Nearest Neighbors(k-NN)**를 통한 검증 문제가 된다.

> **k-NN**    
> <img src="https://user-images.githubusercontent.com/57162812/156966289-e91ca355-cd29-401d-aff4-5b80b963f318.png" width="30%">  
> query data가 들어오면 근방의 k개의 이웃 data를 찾고, 그 data의 label 정보들을 기반으로 분류한다.

한계
- Time complexity : O(n), n=infinite
- Memory complexity : O(n), n=infinite
- 영상 간의 유사도를 정의해야한다. 이 정의는 쉬운 문제가 아니다.

## Convolutional Neural Networks(CNN)

**Nueral Network**는 방대한 데이터를 제한된 복잡도의 시스템에 압축해서 녹여 넣는다.  
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156966747-e281f1a4-9596-4a2e-b25d-6bfc20c19e79.png" width="70%"></p>

**Fully Connected Layer**  
모든 pixel들을 서로 다른 가중치를 weighted sum : 내적 → activation function을 통한 분류 score로 출력

**Single Layer를 영상 분류에 적용했을 때의 문제점**
- weight를 visualize를 해보면, 각 class의 평균 양상을 보인다.
  - layer가 single이라 단순하기 때문에, 평균 이미지 이외에는 표현되지 않는다.
- Training 시, 영상에 가득찬 하나의 물체에 대해서만 열심히 학습해서 그 class의 대표적인 pattern을 학습한다. 하지만 Crop된 영상을 넣어주면 training 시에 본 적이 없기 때문에 template의 위치나 scale이 맞지 않으면 다른 해석을 내놓는다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156967754-55a80888-6abf-4793-8d06-b99f1fb26b80.png" width="50%"></p>

**Convolution Neural Network의 등장**
- locally connected nueral network
- parameter sharing : the number of parameter is decreased

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156968336-6c7930ce-332d-493c-955e-0d5bc4d51a71.png" width="70%"></p>

# CNN architectures for image classification 1
## AlexNet
- 한 글자 단위 인식 및 우편물 인식 성공적
- Layer가 7개로 늘어나 Deep → Parameter의 증가
- 큰 데이터 셋인 Imagenet을 사용한 학습
- ReLU라는 개발된 activation function으로 알고리즘 강화

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156968783-31746c86-0026-4ffa-a2c7-507df6ad3323.png" width="70%"></p>

- Overall architecure : Conv-Pool-LRN-Conv-Pool-LRN-Conv-Conv-Conv-Pool-FC-FC-FC : LRN = Local Response Normalization
- Path가 2가지로 나뉜 이유는? GPU memory가 작아서 network를 나눠서 각각 두가지의 GPU에 올렸다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156969714-7d0231dd-e273-48c2-9993-25a15a87e4ba.png" width="80%"></p>

- MaxPooling된 2D activation map이 linear layer로 가기 위해서는 **벡터화**해야 한다. : AveragePooling, Flatten
  - Alexnet에서는 `torch.flatten(x,1)`이 사용되었다.
- LRN은 현재 사용하지 않는다.
  - normalization layer
  - activation map에서 명암을 normalization
  - **Batch Normalization**이 대체
- 11x11 convolution filter
  - receptive field의 문제
  - KxK conv, stride 1, pooling layer of size PxP
  - 하나의 단계에서 보면 (P+K-1)x(P+K-1)

## VGGNet

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156970832-881f4236-86df-4fda-a5d2-8b8d3184db73.png" width="80%"></p>

- 16 또는 19 layer의 깊은 구조
- 더 간단한 architecture
  - No LRN
  - 3x3 conv filter block, 2x2 max pooling
    - 더 적은 parameter
    - 작은 사이즈의 conv filter도 깊이 쌓으면 큰 receptive field size를 얻을 수 있다.
- 간단한 구조에 좋은 성능
- 일반화가 잘되는 특징 추출 : better generalization
