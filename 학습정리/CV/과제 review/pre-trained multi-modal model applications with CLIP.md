# 과제 목표
1. CLIP 모델 Architecture의 정성적 이해
2. 학습된 CLIP 멀티모달 모델을 활용한 Image Classification 
3. 학습된 CLIP 멀티모달 모델을 활용한 Image-Text Matching Task
4. 학습된 CLIP 멀티모달 모델을 응용한 Text2Image 모델 학습 및 활용

# Multi-Modal Model인 CLIP의 학습 과정
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159131381-ce826ed1-527a-4667-8363-29e1129e9425.png" width = '90%'></p>

1. (Image, Text) 쌍에 대해서 각각 Image Encoder와 Text Encoder를 통해 같은 size의 embeded vector를 생성한다. 
2. 학습을 통해 image feature vector와 text feature vextor의 내적인 행렬의 파란색 square 부분을 최대화하고, 회식 square 부분을 최소화한다.
3. image와 text를 model에 넣어주면, image와 각 text에 대한 feature vector를 추출해 내적을 통해 similarity를 구해 가장 놓은 similarity를 보이는 문장이 input image와 가장 유사한 의미의 문장이라고 볼 수 있다.

## CLIP에 필요한 package 설치
```python
!git clone https://github.com/openai/CLIP.git
pip install git+https://github.com/openai/CLIP.git
```

## CLIP model 불러오기
```python
import clip
model, preprocess = clip.load("VIT-B/32", device = device)
```

- clip에서 사용할 모델을 parameter로 넣어준다.
- `clip.available_models()`를 통해 가능한 모델들을 확인할 수 있다.
- preprocess는 image encoder에 넣을 수 있도록 (224, 224)로 Resize해주고 Normalization해준다.

## clip 모델을 통해 image와 text 사이의 유사도 구하기
```python
from PIL import Image
# 전처리, batch dimension 추가 및 device로 보내준댜.
image = preprocess(Image.open(image_path)).unsqueeze(0).to(device) 
# test할 임의의 문장이나 어구
text_dataset = ["a diagram", "a dog", "a cat"]
# 각 단어들을 숫자로 변환해준다.
text = clip.tokenize(text_dataset)

with torch.no_grad():
  # image와 각 text간의 유사도를 구해준다.
  logits_per_image, _ = model(image, text)
  # softmax를 통해 확률값으로 표현해준다.
  probs = logits_per_image.soft_max(dim = -1).cpu().numpy().flattern()
```



