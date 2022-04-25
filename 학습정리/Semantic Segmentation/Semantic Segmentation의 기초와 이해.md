<div align="center">
  <h1>Semantic Segmentation의 기초와 이해</h1>
</div>

## 1. 대표적인 딥러닝을 이용한 세그멘테이션 FCN
- `Fully Convollutional Network`
   1. VGG Network backbone(feature extracting network) 사용
   2. VGG Network의 FC layer(nn.Linear)를 Convolution으로 대체
   3. Transposed Convolution(resolution을 증가시킴)을 이용해서 Pixel Wise prediction 수행
### 1.1. VGG
- 3x3 conv를 deep하게 쌓음으로써 적은 param으로 효과적으로 receptive field를 넓혔다.

<p align="center"><img width="483" alt="image" src="https://user-images.githubusercontent.com/57162812/165024812-76b075f8-5c5b-4ee5-9b78-2c07d7832d34.png"></p>

<p align="center"><img width="700" alt="image" src="https://user-images.githubusercontent.com/57162812/165024835-78c89191-6d7f-4045-99ef-8660c4fcde9d.png"></p>

> VGG를 backbone으로 사용하였다?
> - pretrained network를 사용할 수 있다. 

### 1.2. Fully Connected Layer vs. Convolution Layer

- Convolution Layer
  - 각 pixel의 **위치 정보**를 해치지 않은채로 특징 추출
  - 임의의 입력값에 대해서도 param의 변경이 필요없다. 즉, 입력 인자의 height, width와 상관이 없다.
  <p align="center"><img width="400" alt="image" src="https://user-images.githubusercontent.com/57162812/165025364-3c039773-9114-40ce-9690-5428cc810746.png"></p>

- Fully Connected Layer
  - flatten 이후에 fc layer를 적용하기에 각 pixel의 위치 정보르 해침
  - label에 대한 정보만 얻을 수 있다.
  - 입력값에 따라서 param의 변경이 필요하다.
  <p align="center"><img width="400" alt="image" src="https://user-images.githubusercontent.com/57162812/165025434-ada7a5f1-5954-478d-8d26-6bad8c5e8c96.png"></p>

### 1.3. Transposed Convolution

- VGG는 5개의 max pooling을 통해서 image resolution을 낮춘다.
- `upsampling` pixel 단위의 prediction이 필요하므로, 줄어든 이미지의 크기를 원래의 크기로 늘려주어야 한다.
- `Transposed Convolution` 또는 `Decovolution`이라 불린다.

> **3x3 Transpose Convolution strid 1**
> - input : 2x2 
> - kernel : 3x3
> <img width="1276" alt="image" src="https://user-images.githubusercontent.com/57162812/165026492-97505ee5-6d23-4713-9408-e53b5af2cd5a.png">

### 1.4. FCN에서 성능을 향상시키기 위한 방법

- backbone : VGG Network

<p align="center"><img width="1372" alt="image" src="https://user-images.githubusercontent.com/57162812/165028225-34fcb98a-68ab-46f5-8385-c56254a210c4.png"></p>

- Conv(CBR)
  ```python
  def CBR(in_channels, out_channels, kernel_size=3, stride=1, padding=1):
    return nn.Sequential(nn.Conv2d(in_channels = in_channels,
                                   out_channels = out_channels,
                                   kernel_size = kernel_size,
                                   stride = stride,
                                   padding = padding),
                         nn.ReLU(inplace=True)
                         )
                         
  # conv1
  self.conv1_1 = CBR(3, 64, 3, 1, 1)
  self.conv1_2 = CBR(64, 64, 3, 1, 1)
  self.pool1 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
  
  # conv2
  self.conv2_1 = CBR(64, 128, 3, 1, 1)
  self.conv2_2 = CBR(128, 128, 3, 1, 1)
  self.pool2 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
  
  # conv3
  self.conv3_1 = CBR(128, 256, 3, 1, 1)
  self.conv3_2 = CBR(256, 256, 3, 1, 1)
  self.conv3_3 = CBR(256, 256, 3, 1, 1)
  self.pool3 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
  
  # conv4
  self.conv4_1 = CBR(256, 512, 3, 1, 1)
  self.conv4_2 = CBR(512, 512, 3, 1, 1)
  self.conv4_3 = CBR(512, 512, 3, 1, 1)
  self.pool4 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
  
  # conv5
  self.conv3_1 = CBR(512, 512, 3, 1, 1)
  self.conv3_2 = CBR(512, 512, 3, 1, 1)
  self.conv3_3 = CBR(512, 512, 3, 1, 1)
  self.pool3 = nn.MaxPool2d(2, stride=2, ceil_mode=True)
  
  # fc6
  self.fc6 = CBR(512, 4096, 1, 1, 0)
  self.drop6 = nn.Dropout2d()
  
  # fc7
  self.fc6 = CBR(4096, 4096, 1, 1, 0)
  self.drop6 = nn.Dropout2d()
  
  # Score
  self.score_fr = nn.Conv2d(4096, num_classes, 1, 1, 0)
  
  # UPScore using deconv
  self.upscore32 = nn.ConvTranspose2d(num_classes, num_classes, kernel_size=64, stride=32, padding=16)
  ```
  
  > 한번에 32배 deconv 하는 것은 좋을까?
  > <p align="center"><img width="1183" alt="image" src="https://user-images.githubusercontent.com/57162812/165030557-ba3b8dbb-3fa5-44cd-acc1-bf1a0cc09425.png"></p>
  > - GT 대비 detail한 부분의 정보들이 사라진다.
  > - 해결방안 : 이전의 output과 summation하는 `Skip Connection` 사용

1. MaxPooling에 의해 잃어버린 정보를 복원해주는 작업을 진행
2. Upsampled Size를 줄여주기 좀 더 효율적인 이미지 복원 가능

<p align="center"><img width="1056" alt="image" src="https://user-images.githubusercontent.com/57162812/165031670-e96ae909-dc88-4cce-a0ba-4815b4c5f7b0.png"></p>

```python
# score pool4 (channel 512 → num_classes)
self.score_pool4_fr = nn.Conv2d(512, 
                                num_classes, 
                                kernel_size = 1, 
                                stride = 1, 
                                padding = 0)
                                
# upscore2 using deconv (resolution 1/32 → 1/16)
self.upscore2 = nn.ConvTranspose2d(num_classes,
                                  num_classes,
                                  kernel_size = 4,
                                  stride = 2,
                                  padding = 1)
                                  
# upscore16
self.upscore16 using deconv
self.upscore16 = nn.ConvTranspose2d(num_classes, 
                                    num_classes,
                                    kernel_size=32, 
                                    stride=16,
                                    padding=8)
                                  
# Sum
def forward(self, x):
  h = x
  h = self.conv1_1(h)
  h = self.conv1_2(h)
  h = self.pool1(h)
  
  (중략)
  
  # sum
  h = upscore2 + score_pool4_fr
```

- conv4의 결과뿐 아니라 conv3의 결과도 이용하여 디테일을 살릴 수 있다.
<p align="center"><img width="1379" alt="image" src="https://user-images.githubusercontent.com/57162812/165034275-b9ac0854-f920-4b5c-8ade-ea67df3a56ff.png"></p>


### 1.5. 평가지표

<p align="center"><img width="597" alt="image" src="https://user-images.githubusercontent.com/57162812/165034773-2c3dcc85-a9de-48e5-bb0f-561b25d9238b.png"></p>

- Pixel Accuracy = (TP + TN) / (TP + TN + FP + FN) = *True pixel* / *Total pixel*

  - True pixel : 22
  - Total pixel :25
  - Pixel Accuracy = 88%

## 2. 결론
### 2.1. Further Reading

- 본래의 fc6의 연산이 7x7 conv를 가진다. 하지만, 이 때 문제가 생긴다.
  - 입력 이미지의 크기가 달라진다. 7x7 resolution → 1x1 resolution
    - 100 zero padding 추가!! 하지만, 그렇더라도 이미지 크기가 맞지 않는다.
    - crop하도로 한다.
