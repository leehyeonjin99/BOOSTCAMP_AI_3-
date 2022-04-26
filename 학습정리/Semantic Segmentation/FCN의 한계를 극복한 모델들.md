## Decoder를 개선한 모델
### DoconvNet

<img width="1060" alt="image" src="https://user-images.githubusercontent.com/57162812/165232921-d662f5d6-327a-4bc6-b040-44983287addd.png">


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

![Uploading image.png…]()

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

## 5개의 Maxpool을 통해 resolution이 1/32배가 되었다.

# deconv5
self.unpool5 = nn.MaxUnPool2d(2, stride=2)
self.dcbr5_3 = CBR(512, 512, 3, 1, 1)
self.dcbr5_2 = CBR(512, 512, 3, 1, 1)
self.dcbr5_1 = CBR(512, 512, 3, 1, 1)

## 5개의 MaxUnPool을 통해 resolution이 32배가 되었다.

# Score
self.score_fr = nn.Conv2d(64, num_classes, 3, 1, 1, 1)
