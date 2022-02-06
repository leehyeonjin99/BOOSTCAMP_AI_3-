# VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION
## Abstruct
- 3x3 convolution filter를 사용한 architecture에서 epth를 증가시킨 network 평가
- depth를 16-19 weight layer로 증가시켜 이전 기술들보다 개선됨

→ ImageNet Challenge 2014의 classification 분야에서 2등 차지

**However** 깊이가 깊어짐에 따라 생기는 overfitting과 gradient vanishing 문제는 어떻게 해결하였을까?

## 1. Introduction
- Convolutional Networks(ConvNets) : 이미지, 비디오 인식 분야에서 큰 활약   
  → ImageNet과 같은 큰 이미지 저장소와 + GPU
- 본 논문에서는 ConvNets 구조에서 깊이의 측명에 집중  
  → 구조의 parameter 고정 및 (3x3 convolution filter를 통해) convolution layer를 증가
  
∴ **결과** : ILSVRC classification과 localisation 작업에서 좋은 accuracy 달성

## 2. Convnet Configurations
### 2-1. Architecture

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152679014-b56cd450-8089-4fb5-9456-6481aaa21a2a.png" width=400></p>

- ConvnNets 입력값 : 224x224 RGB 고정
- Unique Preprocessing : 각 pixel에서 Training set에서 계산된 mean RGB 값을 빼는 것
- 입력 이미지를 3x3 filter가 적용된 ConvNet에 전달 : 위, 아래, 왼쪽, 오른쪽, 중앙을 인식시키기 위한 가장 작은 크기
- Convolution Strid : 1 pixel 고정
- Convolution Padding : 3x3 conv layer에 1 pixel  
  → Padding을 적용하지 않으면 Stride로 인해 이미지의 외곽부분은 잘 반영되지 않고 점점 image의 vanishing이 잃어나기 때문에 Padding으로 이를 방지
- Max Pooling : 2x2 pixel window, stride=2  
  → Spatial Pooling은 5개의 max pooling layer에 의해 수행되며 모든 conv layer 뒤에 pooling layer가 오는 것은 아니다.
- Stack of Conv layer 뒤에 3개의 FC(Fully-Connected) layer 온다.  
  → 첫번째와 두번째는 각각 4096개의 채널  
  → 세번째(softmax layer)는 1000way ILSVRC classification 수행 : 각 class마다 한 개의 채널을 가져가서 1000개의 채널 가진다.
- 모든 hidden laayer에 활성화 함수로 rectification no-linear(ReLU) 이용

### 2-2. Configurations

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152679192-c0cc970a-55dd-4b72-bc68-71c95801acb7.png" width=400></p>

모든 configuration은 architecture에 제시된 일반적인 설계를 따르며, depth만 다르다.
- network A : weight layer 11(8 conv layer + 3 FC layer)
- network E : weight layer 19(16 conv layer + 3 FC layer)

Conv layer의 width(채널의 수)는 64로 시작하여 max-pooling층을 지날때마다 2배씩 증가하여 512까지 증가한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152679210-2166eb59-33a2-4b36-8a9b-29a1225905f0.png" width=400></p>

Conv layer parameter = Conv receptive field size - Number of channels


### 2-3. Discussion

**network 전체에 걸쳐 매우 작은 3x3 receptive field 사용 (with strid = 1)**

하나의 7x7 Conv layer를 사용하는 것보다 3x3 Conv layer를 사용함을로서 얻게 되는 점은?
- 1개의 non-linear rectification layer 대신 3개의 non-linear rectification layer를 사용해 결정함수의 비선형성 증가  
  → feature의 식별성 증가
- training parameter의 수 감소
  → 3개의 3x3 Conv layer stack이 C개의 channel을 가지고 있다고 가정하면 stack의 3\*(3^2)\*(C^2)=27C^2 가중치에 의해 파라미터화 되는 반면 단일 7x7 Conv layer는 (7^2)\*(C^2)=49C^2 파라미터 수가 필요해 거의 81%가 더 필요하다.
  
## 3. Classification Framework
### 3-1. Training
- Batch size = 256
- Momentum = 0.9
- Weight Decay(L2 penalty multiplier set)에 의해 정규화
- 첫 두 FC layer에서 Drop Out 정규화(p=0.5)
- Learning Rate : 초기에 0.01로 설정되었다가 validation set의 accuracy가 10번 안에 좋아지지 않으면 낮아진다.  
  → 총 3번 감소하고 370K(74 epochs)번의 반복 이후에는 학습 중단
- 가중치 초기화 매우 중요  
  → (why?) 잘못된 초기화가 deep net의 gradient의 불안정성으로 인해 학습을 지연시킬 수 있다.   
  → (Solution?) 무작위 초기화로 교육될 정도로 얕은 구성A 부터 
- 깊은 Architecture 훈련 시, 처음 4개의 Conv layer과 마지막 3개의 FC layer를 net A의 layer로 초기화
  → 중간 layer들은 무작위로 초기화
  → 무작위로 초기화하기 위해 mean=0, variance=0.01의 정규분포에서 가중치를 sampleing, 편향은 0으로 초기화
- 224x224 크기의 ConvNEt input image를 얻기 위해 rescaled training image를 무작위로 crop
  → 훈련 세트를 추가로 늘리기 위해 crop 시, random horizontal flipping과 random RGB colour shift
  
#### 학습 이미지 크기
모델 학습 시 입력 이미지의 크기는 모두 224x224로 고정하였다.  
학습 이미지는 각 이미지에 대해 256x256 ~ 512x512 내에서 임의의 크기로 변환하고, 크기가 변환된 이미지 Object의 일부가 포함된 224x224 이미지를 Crop 하여 사용하였다.

[Rescaled Training Image]

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152680076-102478e7-8077-4fa6-b70c-82185c5f2b09.png" width=400></p>

[Crop Image of 256x256 to 224x224]

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152680079-7fe0af26-62df-4746-9ad3-5258238a5702.png" width=400></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152680089-66befdc2-87e1-48da-bdb3-be6416997a87.png" width=400></p>

[Crop Image of 512x512 to 224x224]

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152680091-e8d9d0ae-64a8-4be6-8a45-a236f8e6cdfc.png" width=400></p>

이처럼 학습 데이터를 다양한 크기로 변환하고 그 중 일부분을 샘플링해 사용함으로써 몇 가지 효과를 얻을 수 있다.
1. Data Augmentation
2. 하나의 Object에 대한 다양한 측면을 학습 시 반영시킬 수 있다. 변환된 이미지가 작을수록 개체에 전체적인 측면을 학습할 수 있고, 변환된 이미지가 클수록 개체의 특정한 부분을 학습에 반영할 수 있다.

→ Overfitting을 방지하는 데 도음이 된다.

### 3-2. Testing
- Input image는 pre-define된 smallest image side로 isotropically rescale되며 test scale Q로 표시된다.  
  → Q가 training scale S와 같을 필요 없다. 각 S에 대해 몇 가지 Q를 쓰는 것이 성능 향상에 도움된다.
- FC layer가 Conv layer로 변환된다.  
  → 첫번째 FC layer는 7x7 Conv layer로, 마지막 두 FC layer은 1x1 Conv layer로 변환된다.  
  → Resulting Fully Convolutional Network가 전체 image에 적용  
  → 결과
  - class의 개수와 동일한 개수의 channel을 갖는 class score map
  - Input image size에 따라 변하는 spatial resolution = input image size의 제약이 없어짐
  - 하나의 image를 다양한 scale로 사용한 결과를 조합해 image classification accuracy 개선가능

### 3-3. Implementaion details

- Multi-GPU training은 각 GPU에서 병렬로 처리되는 여러 GPU batch들로 각 training image를 분할하여 사용한다. 
- GPU batch gradient를 계산 후 full batch의 gradient를 얻기 위해 평균을 계산한다.
- Gradient 계산은 GPU 전체에 걸쳐 동시에 진행  
  → 결과가 단일 GPU에서 train할 때와 정확히 일치
- 4-GPU 시스템에서 단일 GPU 시스템보다 속도가 3.75배 향상
