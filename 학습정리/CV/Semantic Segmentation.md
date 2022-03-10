# Semantic segmentation
## What is sementic segmentation

- Image classification을 영상 단위가 아닌 pixel 단위로 구분
- 단, 영상 속에 있는 같은 class의 물체들을 다른 물체로 구분하지 않는다.
  - 예를 들어, 같은 영상 속 사람이 두명 이상 있다면 모두 같은 색으로 분류한다.
  - 같은 class라도 다른 물체들을 구분하는 segmentation은 `instance segmentation`이라 한다.

## Where can semantic segmentation be applied to?

- Medical Images
<img src="https://user-images.githubusercontent.com/57162812/157228795-138d26ae-6431-423c-ab02-0eacbed81fbb.png" width='30%'>

- Autonomous driving
<img src="https://user-images.githubusercontent.com/57162812/157228912-cba5be3e-2fef-4f94-a333-bffd2f81bdeb.png" width='30%'>

- Computational photography

# Semantic segmentatino architecture
## Fully Convolutinoal Networks(FCN)

- 첫 end-to-end semantic segmentation
  > **end-to-end**
  >
  > - 입력에서 출력까지 모두 미분 가능한 Neural Network의 형태
  > - 입력과 출력의 pair만 있다면 중간에 있는 Nueral Network의 학습을 통해서 target task 해결 가능
- 이전에는 사람이 손으로 만든 알고리즘을 결합해서 semantic segmentation 수행
  - data가 많더라도 학습 가능한 부분 제한적
  - 성능을 높이기 위한 수학적인 모델을 사람의 손으로 시도하여 성능 향상이 어려움
- 임의의 해상도의 영상을 넣을 수 있고 입력 해상도에 맞춰진 출력이 되도록 구성 → 입력 해상도 호환 가능
- 중간의 Network가 학습 가능한 Nueral Network로 학습을 통해서 semantic segmentation 문제 해결 가능

**Fully Connected vs. Fully Convolutional**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157230746-96c19cee-dae2-4711-ba70-9cd445a40753.png" width='60%'></p>

- Fully `Connected` Layer : 공간 정보를 고려하지 않고 fixed dimensional vector가 주어지면 fixed dimensional vector가 나온다.
- Fully  `Convolutional` Layer : 입력과 출력 모두 activation map으로 spatial coordinate를 유지한 상태로 operation이 수행된다. By **1x1 Conv**

**Interperting fully connected layers as 1x1 convolutions**

- Fully Connected Layer : channel 상관 없이 flattening을 통해 벡터 형태로 변경하여 fully connected를 진행한다.
  - 영상의 공간 정보가 고려되지 않고 하나의 벡터로 섞이게 된다.
  - 각각의 공간 정보를 고려하기 위해서는?
    - Channle 축으로 flatterning한다. 따라서 각 위치마다 벡터가 하나씩 나오게 된며 각각에 대해서 Fully Connected를 진행한다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157232189-3b0ac3b3-89e1-423b-958d-4cffd4329f30.png" width='40%'></p>

- Fully Convoltional Layer : channel 축으로 1x1 convolution kernel이 fc kernel의 한 weight column으로 볼 수 있다.
  - filter 개수만큼 통과 시켜 각 위치마다 fc layer를 별도로 돌려 각각의 위치에 결과값을 채워넣는 것과 동일한 결과이다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157232287-2f7a4752-d03d-410e-8902-4126dd61a7a2.png" width='40%'></p>

FC layer를 1x1 Conv layer로 변경하여 어떤 입력 사이즈에도 대응 가능한 Fully Convolutional Layer!! 

**But** : 이렇게 Semantic segmentation model을 만들어 사용하게 되면 굉장히 작은 Score map을 얻게 된다.

**Why** : stride, pooling layer를 통해 최종 해상도가 굉장히 저해상도가 된다.

**Solution** : Upsampling

**Upsampling**

Stride와 Pooling을 제거하면 큰 activation map을 얻을 수 있지만, receptive field size가 작기 떄문에 영상의 전반적 context를 얻을 수 없다.

→ 일단은 작게 만들어서 receptive field를 키워 성능을 증가시키고 강제로 Upsampling을 하여 resolution을 증가시킨다.

방법
- Transposed Convolution
- Upsample and Convolution

**Transposed Convolution**
- kernel_size=2, stride=1
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157233488-f87ce8c7-55e3-48bd-a0ee-db94fa2ec23c.png" width='50%'></p>

의문점? kernel size가 중첩된다고 해서 결과를 일정 간격으로 더해도 되나? 중첩되는 부분은 일정 부분인데?

- kernel_size=2, stride=2
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157233243-4a7cf31e-7dec-453e-bb77-3d51b7822628.png" width='50%'></p>

위와 같이 convolutional kernel size와 stride parameter을 잘 조정하여 중첩되는 부분이 없이 tuning 해야한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157233917-3c540436-a30f-4098-b908-e8077d407fdc.png" width='20%'></p>

중첩되어 반복되는 block을 `checkerboarde artifact`라고 한다.

**Better approaches for upsampling**

- spatial upsampling{Nearest-neighbor(NN), Bilinear}+feature convolution
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157234294-a401caaa-f415-4c2f-aff7-52ee7e4ff598.png" width='50%'></p>

그렇지만 아무리 upsampling을 했을지라도 해상도가 이미 줄어든 상태에서 잃어버린 정보를 다시 살리는 일은 쉽지 않다.
- Low Layer : receptive field size가 작기 때문에 굉장히 `국지적`이고 작은 차이에도 `민감`하다.
- High Layer : 해상도는 낮아지지만 큰 receptive field size를 갖기 때문에 `전반적`이고 `의미론`적인 정보를 포함한다.

Semantic Segmentation에는 Lower Layer(pixel별 의미)과 High Layer(경계 부분 파악) 모두 필요하다.

**Adding skip connections for enlarging the score map**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157235124-17cdfe71-2fc5-499e-a76a-94ed0d3ce1a6.png" width='70%'></p>

- 높은 layer에 있던 activation map을 upsampling을 통해 해상도를 높이고 그에 맞춰 중간층의 activation map을 upsampling을 해서 가져와 concatenation한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157235409-a4252e4c-a0da-4f4e-a8c5-4bacf8831e24.png" width='40%'></p>

- 중간 단계의 feature들을 합쳐서 사용 것이 성능이 좋다는 것을 확인 가능하다.

## U-Net
- Nueral Net model 중 영상과 비슷한 사이즈의 출력을 가지는 모델 또는 Object detection, Semantic Detection처럼 영상 전체가 아닌 영상 일부분을 자세히 봐야하는 경우 U-Net의 기원이 있는 경우가 많다.
- Fully Convolutional
- 낮은 층과 높은 층의 feature map을 concatenation 하는 방법을 제안
  - skip connection과 비슷

**Overall architecture**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157236051-dfe9ae34-0f36-4880-8da2-2e124d391681.png" width='80%'></p>

- **Contracting Path**
  - 입력 영상을 Convolution Layer에 통과 시켜 Pooling을 통해 resolution를 낮추고 channel 수를 높이는 형태를 반복하여 작은 activation map을 구하고 영상의 전반적인 정보가 잘 녹아있다고 가정한다.
- **Expanding Path**
  - 점진적으로 activation map의 resolution을 높이고 channel size을 낮춰줘 Contracting Path에서 오는 대칭으로 대응되는 layer와 동일하게 맞춰 낮은 층의 activation map과 합쳐줄(Concatenation) 수 있도록 한다.

낮은 layer에서 전달된 특징이 localized information을 제공한다. : 공간적으로 높은 해상도와 입력이 약간 바뀌는 것 만으로도 민감한 정보를 제공하기 때문에 경계선이나 공간적으로 중요한 정보들을 뒤쪽 layer에 바로 전달하는 중요한 역할은 한다.

**An even number is required for input and feature sizes**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157237082-644d4d1c-988c-447c-a087-c2cef74f4d40.png" width='60%'></p>

원래 입력과 해상도 차이가 나게 될 수 있다. 따라서 중간의 어떤 layer에 대해서도 홀수 activation map이 나오지 않도록 유의해야한다.

**Pytorch cod for U-Net**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157237347-b5e3ac8a-7824-46b9-b64d-fed8474b2a07.png" width='15%'></p>

```python
self.dconv_down = double_conv(3, 64)
self.maxpool_2x2 = nn.MaxPool2d(kernel_size=2, stride=2)
```

```python
def double_conv(in_channels, out_channels):
  return nn.Sequential(
    nn.Conv2d(in_channels, out_channels, 3),
    nn.ReLU(inplace=True),
    nn.Conv2d(out_channels, out_channels, 3),
    nn.ReLU(inplace=True))
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157237841-3dd33b44-465f-43ac-918d-c96f3fb3cf2d.png" width='15%'></p>

```python
self.up_trans = nn.ConvTranse2d(in_channels=1024, out_channels=512, kernel_size=2, stride=2)
self.up_conv = double_conv(1024, 512)
```

- stride_size ==kernel_size로 checkerboard artifact가 생기지 않는다.

## DeepLab
- CRFs
- Atrous Convolution

**Conditional Random Fields(CRFs)**

- 후처리로 사용되는 tool
- pixel과 pixel 사이의 관계를 모두 이어주어, regulared pixel map을 그래프로 볼 수 있다 → 경계를 잘 찾을 수 있도록 모델링

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157238921-4f2f1835-dd6c-4eed-8121-625a8789d83d.png" width='60%'></p>

**Dilated Convolution**

- Convolution kernel 사이에 dilation factor만큼 일정 공간을 넣어준다.
  - 실제 Convolution kernel 보다 더 넓은 영역을 고려할 수 있게 한다.
  - Dilated Convolution Layer 을 여러번 반복함으로써, receptive field size가 exponential하게 증가한다.
- parameter 수는 변동 없다.

<p align='center'><img src="https://gaussian37.github.io/assets/img/dl/concept/dilated_residual_network/1.gif" width='60%'></p>


**Depthwise seperable convolution**

- 각 channel별로 convolution하여 값을 뽑아 channel별 각각의 activation map에 대하여 1x1 convolution을 통해 하나의 값에 출력되도록 합쳐준다.
  - Convolution의 표현력은 유지되면서 계산량은 줄어들게 된다.
- 계산량
![image](https://user-images.githubusercontent.com/57162812/157239856-bda8b284-e255-4c4e-9430-a05060e5178b.png)
