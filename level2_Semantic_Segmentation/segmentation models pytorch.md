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
swin transformer가 encoder로 등록되어 있지 않아서 따로 등록해주었다. 그 중 swin large를 등록해보았다.

- swin.py 생성
[Swin Transformer github](https://github.com/microsoft/Swin-Transformer/blob/main/models/swin_transformer.py)

- swin transformer large encoder 등록

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/167435667-73ded0aa-5d99-44c2-bd81-c24766b8abf6.png" width = "80%"></p>


```python
from swin import SwinTransformer
from segmentation_models_pytorch.encoders._base import EncoderMixin
from typing import List

# Custom SwinEncoder 정의
class SwinEncoder(torch.nn.Module, EncoderMixin):

    def __init__(self, **kwargs):
        super().__init__()

        # A number of channels for each encoder feature tensor, list of integers
        self._out_channels: List[int] = [192, 384, 768, 1536]

        # A number of stages in decoder (in other words number of downsampling operations), integer
        # use in in forward pass to reduce number of returning features
        self._depth: int = 3

        # Default number of input channels in first Conv2d layer for encoder (usually 3)
        self._in_channels: int = 3
        kwargs.pop('depth')

        self.model = SwinTransformer(**kwargs)

    def forward(self, x: torch.Tensor) -> List[torch.Tensor]:
        outs = self.model(x)
        return list(outs)

    def load_state_dict(self, state_dict, **kwargs):
        self.model.load_state_dict(state_dict['model'], strict=False, **kwargs)

# Swin을 smp의 encoder로 사용할 수 있도록 등록
def register_encoder():
    smp.encoders.encoders["swin_encoder"] = {
    "encoder": SwinEncoder, # encoder class here
    "pretrained_settings": { # pretrained 값 설정
        "imagenet": {
            "mean": [0.485, 0.456, 0.406],
            "std": [0.229, 0.224, 0.225],
            "url": "https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_large_patch4_window12_384_22kto1k.pth",
            "input_space": "RGB",
            "input_range": [0, 1],
        },
    },
    "params": { # 기본 파라미터
        "pretrain_img_size": 384,
        "embed_dim": 192,
        "depths": [2, 2, 18, 2],
        'num_heads': [6, 12, 24, 48],
        "window_size": 12,
        "drop_path_rate": 0.3,
    }
}
```


