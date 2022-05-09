# SMP
SMP는 `segmentation models pytorch`의 약자로 pytorch를 기반으로 Image Segmentation을 위한 Neural Network의 python 라이브러리이다.

## 🛠 Installation

```python
pip install -U segmentation_models_pytorch
```

## ⏳ 실행 방법

- segmentation model : Unet
- encoder : resnet34

```python
import segmentation_models_pytorch as smp
model = smp.Unet(
    encoder_nmae = "resnet34",
    encoder_weights = "imagenet",
    in_channels = 1,
    classes = 3
)
```

## 📦 Segmentation Models

- [ ] Unet
- [ ] Unet++
- [ ] MAnet
- [ ] Linknet
- [ ] FPN
- [ ] PSPNet
- [ ] PAN
- [ ] DeepLabV3
- [ ] DeepLabV3+

### Parameter
- `encoder_name` : encoder로 사용할 classification의 이름
- `encoder_depth` : encoder에서 사용되는 stage의 수
- `encoder_weight` : pretrained weight
- `classes` : class 수

## 🏔 Encoders

- [ ] ResNet
- [ ] ResNeXt
- [ ] ResNeSt
- [ ] Res2Ne(X)t
- [ ] RegNet(x/y)
- [ ] GERNet
- [ ] SE-Net
- [ ] SK-ResNe(X)t
- [ ] DenseNet
- [ ] Inception
- [ ] EfficientNet
- [ ] MobileNet
- [ ] DPN
- [ ] VGG

### swin transformer
