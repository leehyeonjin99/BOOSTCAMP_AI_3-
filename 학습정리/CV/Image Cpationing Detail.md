<div align='center'>
  <h1>Image Captioning</h1>
</div>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158566456-db9cb0f1-bb2a-46ed-90cd-8c19b5d644b9.png" width = "300" ></p>

Image Captioning Model의 구조는 크게 Encoder와 Decoder로 구분된다.

## Encoder

```python
class Encoder(nn.Moduel):
  def __init__(self.encoded_image_size = 14):
    super(Encoder, self).__init__()
    self.enc_image_size = encoded_image_size
    
    resnet = torchvision.models.resnet101(pretrained = True)
    
    modules = list(resnet.children())[:-2] # classification를 하지 않기 때문에 linear와 pooling layer를 제거한다.
    self.resnet = nn.Sequential(*modules)
```

## Decoder

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158568597-ec0a3ddc-661a-4671-b7c7-aea17f4e1d46.png" width = "800"></p>


어디를 참고하고 출력해야할지 attention map을 계속해서 넣어준다.

## Beam Search

- parameter k : 각 decoder step에 대해서 top 3 를 고른다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158569446-330cd4ea-baee-44ff-bb28-396ddcb183d9.png" width = "800"></p>
