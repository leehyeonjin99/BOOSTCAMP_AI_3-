## FCN 한계점
1. 객체으 크기가 작거 크 경우 예측을 잘 하지 못한다.
        - 큰 object의 경우 지역적인 정보만으로 예측 ⇒ 같은 object여도 다르게 labeling
        - 이유는 receptive field가 작아서?
        - 작은 object는 무시되는 경우도 발생

2. Detail한 모습이 사라지느 문제 발생
        - Deconvolution 절차가 간단해 경계르 학습하기 어렵다.
        - Skip connection을 통해 Tranpose convolution 진행하였지만 아지 부족하다...

## Decoder를 개선한 모델
### DoconvNet

<img width="1060" alt="image" src="https://user-images.githubusercontent.com/57162812/165232921-d662f5d6-327a-4bc6-b040-44983287addd.png">

1. 1x1 Conv를 중심으로 Encoder와 Decoder가 `대칭`의 형태를 지닌다.
2. backbone : `VGG 16`
3. Conv = Conv2d + BatchNorm + ReLU
4. Deconv = TranposeConv2d + BatchNorm + ReLU

> **Unpooling이란?**
> 
> <img width="637" alt="image" src="https://user-images.githubusercontent.com/57162812/165340318-960cdbed-1cb9-4773-b808-e93ed4ead78c.png">
>
> MaxPool의 경우 kernel size만큼의 값들 중 위치와 관계없이 최댓값을 뽑아오게 된다. 이때, 위치 정보를 잃어버리게 된다. 따라서 MaxPool시 위치 정보 `max indices`를 저장해두어 Unpooling시 사용한다. 즉, 지워진 경계르 기록했다가 복원이 가능해진다. maxunpool을 거친 activation map은 대부분이 0인 sparse activation map이기 때문에 Tranposed Convolution을 수행하여 채워주게 된다.
> 
> 따라서, (Unpooling + Deconv)를 반복적으로 수행하게 되다며 츠으이 구조가 다양하 수준의 모양을 잡아낼 수 있다. 얕은 층에서는 전반적인 특징을 잡아내고, 깊은 층에서는 복잡한 패턴으 잡아내게 된다.


```python
## Encoder Conv
def CBR(in_channels, out_channels, kernel_size=3, stride=1, padding=1):
    return nn.Sequential(
        nn.Conv2d(in_channels = in_channels,
                  out_channels = out_channels,
                  kernel_size = kernel_size,
                  stride = stride,
                  padding = padding),
        nn.BatchNorm2d(out_channels),
        nn.ReLU())
        
## Decoder Conv
def DCB(in_channels, out_channels, kernel_size=3, stride=1, padding=1):
    return nn.Sequential(
        nn.ConvTransposed2d(in_channels = in_channels,
                            out_channels = out_channels,
                            kernel_size = kernel_size,
                            stride = stride,
                            padding = padding),
        nn.BatchNorm2d(out_channels),
        nn.ReLU())
```

```python
# conv1 224x224 input
self.conv1_1 = CBR(3, 64, 3, 1, 1)
self.conv1_2 = CBR(64, 64, 3, 1, 1)
self.pool1 = nn.MaxPool2d(kernel_size = 2, stride = 2, ceil_mode=True, return_indices=True)

# conv2 112x112 input
self.conv2_1 = CBR(64, 128, 3, 1, 1)
self.conv2_2 = CBR(128, 128, 3, 1, 1)
self.pool2 = nn.MaxPool2d(kernel_size = 2, stride = 2, ceil_mode=True, return_indices=True)

# conv3 56x56 input
self.conv3_1 = CBR(128, 256, 3, 1, 1)
self.conv3_2 = CBR(256, 256, 3, 1, 1)
self.conv3_3 = CBR(256, 256, 3, 1, 1)
self.pool3 = nn.MaxPool2d(kernel_size = 2, stride = 2, ceil_mode=True, return_indices=True)

...

# conv5 14x14 input
self.conv5_1 = CBR(512, 512, 3, 1, 1)
self.conv5_2 = CBR(512, 512, 3, 1, 1)
self.conv5_3 = CBR(512, 512, 3, 1, 1)
self.pool5 = nn.MaxPool2d(kernel_size = 2, stride = 2, ceil_mode=True, return_indices=True)

# fc6 7x7 input
self.fc6 = CBR(512, 4096, 7, 1, 0)
self.drop6 = nn.Dropout2d(0.5)

# fc7 1x1 input
self.fc7 = CBR(4096, 4096, 1, 1, 0)
self.drop7 = nn.Dropout(0.5)

# fc6-deconv 7x7 output
self.fc6_deconv = DBC(4096, 512, 7, 1, 0)

# unpool15 14x14 output
self.uppool15 = nn.MaxUnpool2d(2, stride=2)
self.deconv5_1 = DGC(512, 512, 3, 1, 1)
self.deconv5_2 = DGC(512, 512, 3, 1, 1)
self.deconv5_3 = DGC(512, 512, 3, 1, 1)

...

# unpool13 56x56 output
self.uppool13 = nn.MaxUnpool2d(2, stride=2)
self.deconv3_1 = DGC(256, 256, 3, 1, 1)
self.deconv3_2 = DGC(256, 256, 3, 1, 1)
self.deconv3_3 = DGC(256, 128, 3, 1, 1)

# unpool12 56x56 output
self.uppool12 = nn.MaxUnpool2d(2, stride=2)
self.deconv2_1 = DGC(128, 128, 3, 1, 1)
self.deconv2_2 = DGC(128, 64, 3, 1, 1)

# unpool12 56x56 output
self.uppool12 = nn.MaxUnpool2d(2, stride=2)
self.deconv2_1 = DGC(64, 64, 3, 1, 1)
self.deconv2_2 = DGC(64, 3, 3, 1, 1)

# Score
self.score_fr = nn.Conv2d(64, num_classes, 1, 1, 0)
```

```python
def forward(self, x):
  ...
  h, loc_indices5 = self.maxpool5(self.conv5_3(self.conv5_2(self.conv5_1(h))))
  ...
  h = self.deconv5_3(self.deconv5_2(self.deconv5_1(self.unpool5(h, loc_indices5))))
```

## SegNet

<img width="1130" alt="image" src="https://user-images.githubusercontent.com/57162812/165236643-c24bfbf7-0441-49a2-9dcb-3c8f9181e220.png">

1. 자율 중해에서 사용하기 위해서는 빠르고 정확하게 예측 가능해야한다.
        - DeconvNet의 가운데 fc layer를 제거한다. → 파라미터 수 감소 및 수행 속도 증가
        - Unpooling의 output으 Deconv가 아닌 Conv를 통과시킨다.

```python
def CBR(in_channels, out_channels, kernel_size=3, stride=1, padding=1):
    return nn.Sequential(
        nn.Conv2d(in_channels = in_channels,
                  out_channels = out_channels,
                  kernel_size = kernel_size,
                  stride = stride,
                  padding = padding),
        nn.BatchNorm2d(out_channels),
        nn.ReLU())
        
## conv1
self.cbr1_1 = CBR(3, 64, 3, 1, 1)
self.cbr1_2 = CBR(64, 64, 3, 1, 1)
self.pool1 = nn.MaxPool2d(2, stride=2, ceil_code=True, return_indices=True)

# 5개의 Maxpool을 통해 resolution이 1/32배가 되었다.

# deconv5
self.unpool5 = nn.MaxUnPool2d(2, stride=2)
self.dcbr5_3 = CBR(512, 512, 3, 1, 1)
self.dcbr5_2 = CBR(512, 512, 3, 1, 1)
self.dcbr5_1 = CBR(512, 512, 3, 1, 1)

## 5개의 MaxUnPool을 통해 resolution이 32배가 되었다.

# Score
self.score_fr = nn.Conv2d(64, num_classes, 3, 1, 1, 1)
```

## DeconvNet vs. SegNet

<img width="659" alt="image" src="https://user-images.githubusercontent.com/57162812/165342084-ebe7a82d-0e02-4b9c-be18-9c3cd6f11447.png">

# Skip Connection을 적용한 모델
## FC DenseNet

> **Skip Connection**
