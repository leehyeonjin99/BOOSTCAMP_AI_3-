# Conditional generative model
## Conditional gernerative model

**Generative model vs. Conditional generative model**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158114762-690f9931-3afc-4ad1-870d-a71a4b6538a2.png" width = '70%'></p>

- `generative model`은 영상이나 sample을 생성할 수는 있지만, 조작은 할 수 업다.
- 생성이 유용하게 쓰이기 위해서 user의 의도가 반영이 된다면 더 많은 응용이 가능해진다. → `Conditional generative model`

**Example of conditional generative model - audio super resolution**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158114972-1f81befc-4fa1-4641-9979-60ee3ed7c970.png" width = '60%'></p>

- P(high resolution audio | low resolution audio)
- 저퀄리티 audio를 고퀄리티 audio로 높여주는 문제

**Example of conditional generative model - machine translation**

<p align='center'><img src="https://3.bp.blogspot.com/-3Pbj_dvt0Vo/V-qe-Nl6P5I/AAAAAAAABQc/z0_6WtVWtvARtMk0i9_AtLeyyGyV6AI4wCLcB/s1600/nmt-model-fast.gif" width = '60%'></p>

- P(English sentence | Chinese sentence)
- 한자로 주어진 중국어를 영어 문장으로 변역

**Example conditional generative model - article generation with the title**

- P(A full article | An article's title and subtitle)
- title과 subtitle로 나머지 article을 생성해내는 모델

**Recap : Generative Adversarial Network**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158115981-ebad21bc-d198-47ea-abe4-4c9cd366f3e1.png" width = '70%'></p>
 
- Discriminator과 Generative가 함께 좋아진다.

**(Basic) GAN vs. Conditional GAN**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158116339-e303dee9-90c1-4dd4-986c-fd403eb0b471.png" width = '70%'></p>

- Conditional GAN =  GAN + conditional 정보를 제공하기 위해 conditional input이 주어진다.

## Conditional GAN and image translation
**Image-to-Image translation**
- 이미지를 또다른 이미지로 translation
- Application : style transfer, super resolution, colorization

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158116586-b23f3e01-b260-45f7-a401-d6c13d13ca6c.png" width = '70%'></p>

## Example : Super resolution
**Example of conditional GAN - low resolution to high resolution**

- 입력 : 저해상도
- 출력 : 고해상도

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158116779-06183c1a-6a09-405c-8ef4-3e6dbf64630e.png" width = '50%'></p>

**Super Resolution GAN as an example of conditional GAN**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158116949-b3919abb-e546-4ec0-a260-91d000194178.png" width = '70%'></p>

**Difference between regression and conditional GAN for SR**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158117544-2ffeea52-d939-4fc9-b880-fd835a324956.png" width = '70%'></p>

Super Resolution 문제를 반드시 Conditional GAN으로 풀어야하는 것은 아니다. 이전에는 CNN 구조를 통해 SR을 할 때, Adversarial learning을 하지 않고 단순한 loss를 사용하여 학습을 시켰다. 주로, L1 또는 L2 loss를 사용했다.

**Comparision of MAE, MSE and GAN losses in a image manifold**
- regression을 사용한 결과, 해상도는 높아지지만 blury한 결과를 얻게 된다.
  - pixel 자체의 intensity 차이를 이용하여 평균 error를 구하다보니 출력 결과와 비슷한 error를 가지는 많은 patch들이 존재해 구분성이 떨어진다.
  - 적절하게 평균 양상을 생성해내는 것이 generator 입장에서는 편리한 해결책이 된다. 어느 하나에도 가깝지 않고 적당하게 떨어져 있어 error가 적당히 낮아져 안전한 예측이 된다.
- Adversarial loss를 사용하게 되면 이 문제가 해결된다. 

**Meaning of 'average answer' by an example**

- Condition 
  - Task : image를 coloring한다.
  - real image : 흰색 또는 검은색뿐
- L1 loss를 사용하여 Input image에 대해서 gray image를 생성해낸다.
- GAN을 사용하면, discriminator에 gray image가 들어오게 되는 경우 real data 중 본 적 없는 image로 real로 판별될 수 없다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158118564-23de666d-6006-4b1e-8ef1-e8f39ff1c194.png" width = '70%'></p>

**GAN loss for Super Resolution(SRGAN)**

- SRGAN은 MSE loss를 이용한 SRResNet보다 더 현실적인 image를 생성해낸다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/158118784-962a97ba-0235-4e57-b1cc-7ddf009c81f0.png" width="70%"></p>

# Image translation GANs
## Pix2Pix
- Image Translation은 한 image style을 다른 style로 변화하는 문제

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/158140965-2150245a-9ab9-4bcf-8b70-529f4565fc1c.png" width="70%"></p>

예를 들면, semantic segmentation map -> 일반적 이미지, 흑백->칼라, sketch -> 일반 사진 와 같은 task가 있다.

**Loss function of Pix2Pix**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/158141523-8b14a18e-31f5-42ce-a973-a231c944c3ab.png" width="50%"></p>

- L1 loss가 blury 영상을 만들 수 있지만 적당한 guide로 쓰기에는 적당하다.
  - <img src="https://user-images.githubusercontent.com/57162812/158141636-192227de-163f-47c0-8279-c5d450a6feed.png" width = "30%">
  - y : ground_truth
- GAN loss를 더해 realistic한 출력을 만들도록 유도한다.
  - <img src="https://user-images.githubusercontent.com/57162812/158143121-5ad56dcc-b603-4d9a-b753-29050ff38a95.png" width = "40%">


> **L1 loss를 사용하는 이유는?**
> 1. GAN loss만 사용하게 된다면, 입력된 두개의 pair를 직접 비교하지 않는다. x, y를 독립적으로 discriminate하여 real, fake를 판별해낸다. 따라서, 입력이 무엇이 들어와도 y와 직접 비교를 하지 않아, GAN만 사용하면 y와 비슷한 결과 를 만들어낼 수 없다. 따라서 L1 loss를 사용해서 기대하는 결과인 y와 비슷한 영상이 나오게 된다. 여기서 GAN을 이용해서 realistic한 영상을 만들도록 한다.
> 2. GAN만으로 학습한 것이 알고리즘 분석과 발전으로 많이 안정화 되었지만, GAN의 학습이 굉장히 불안정하고 어려웠다. 이것을 blury하지만 적절하게 L1 loss로 가이드를 제공해서 학습이 안정적으로 진행되도록 보조하는 역할을 한다.

> **GAN loss의 기존의 GAN의 adversarial loss와의 차이점은?**
> 1. G에 (x, z)가 모두 들어간다.

**Role of GAN loss in Pix2Pix**

다음은 loss를 바꿔가면서 실험한 결과이다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/158144294-16c3d808-320e-460c-ae1d-e089eb919a70.png" width="70%"></p>

- L1을 통해서 ground truth에서 변형이 적게 생성한다는 것을 알 수 있다.

## CycleGAN

- Pix2Pix는 pairwise data가 필요하다. 하지만, 항상 paired data를 얻는 것은 어렵다.
- unpaired data를 사용하는 방법은 없을까?
  - unpaired data : X라는 style의 영상과 Y라는 style의 영상들이 correspondence 없이 set으로만 주어진 경우

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/158145238-6243a0f1-efff-407f-a03d-1e88a93351ce.png" width="50%"></p>

**CycleGAN** [참고](https://velog.io/@mink555/GAN-Loss)
- domain간의 translation을 1:1 대응관계가 존재하지 않는 dataset 만으로 translation이 가능하도록 학습하는 방법 → 응용범위가 증가한다.
- 예를 들어, Monet의 그림들의 style들과 일반 사진들의 dataset을 잔뜩 주고 모네의 이미지 스타일에서 일반사진을 가는 방법, 일반 사진에서 모네의 이미지 스타일로 가는 방법 두가지를 모두 학습하는 방법이다.

**Loss function of CycleGAN**

`CyclGAN loss` = `GAN loss(in both direction)` + `Cycle-consistency loss`

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/158148610-b76f1b25-6132-4e1f-b444-4feff696953b.png" width="50%"></p>

- GAN loss : X→Y 방향과 Y→X의 방향을 동시에 학습한다.
- Cycle-consistency loss : X→Y→X'일 때, X와 X'이 비슷해야한다.

**GAN loss in CycleGAN**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158151340-08437673-8ed6-46f7-99cf-84bc93589e34.png" width='20%'></p>

- CycleGAN은 양방향에 대해서 각각의 GAN loss를 가진다.
- G, F : generator
- D_X, D_Y : discriminator
- GAN loss = L(D_X) + L(D_Y) + L(G) + L(F)
 - ? : L(G, G_Y, X, Y) + L(F, D_X, Y, X)

**만약 GAN loss만 사용한다면?**
- `Mode Collapse` : input에 상관없이 하나의 output만 출력
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158152105-4ae0d50b-4328-42e4-82e7-136b1d9dfb53.png" width='50%'></p>

**Solution : Cycle-consistency loss to preserve contents**

- X를 Y로 translate하여 output을 다시 X로 translate한다. 이때, 원본으로 복원이 되어야한다.
- loss를 구하는 과정에는 어떠한 supervision도 들어가지 않는다. : self-supervision

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158152822-8d142914-f25c-4b22-bcd9-f35cf66f63b3.png" width='70%'></p>

## Perceptual loss

GAN은 alternating training을 필요로 하므로 train하는 데에 힘들다. 그렇다면 L1, L2 loss보다 high-quality image를 얻는 다른 방법은? **Perceptual loss**

**Perceptual loss, yet another approach for achieving high quality output**
- Adversarial loss = GAN loss
  - alternating 과정으로 상대적으로 training과 coding이 어렵다.
  - 어떤 pre-trained network가 필요 없고 학습 과정 중 Generator와 Discriminator가 균형을 맞춘다.
  - pre-trained network가 요구되지 않기 때문에 다양한 application의 제약 사항 없이 데이터만 주어지면 활용 가능하다.
  - 하지만, data dependency가 발생한다.
- Perceptual loss
  - 학습과 coding에 있어서 편하다. simple forward + backward computation
  - learned loss를 측정하기 위해서 pre-trained network를 사용해야한다.

**Perceptual loss**
- pre-trained 이미지 classification model의 filter를 보면, filter의 response와 형태가 human's visual perception과 유사하다는 관찰이 있다.
- pre-trained perception이라 할 수 있다. image를 perceptual space로 변환한다. perceptual space에서 특징들을 민감하게 다뤄야하는 것과 우리 눈에서 신경쓰지 않는 것을 구분해서 연관지을 수 있지 않을까?

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158154717-57315bb5-11d9-478c-b04c-edc586dcf4cd.png" width='50%'></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158155649-41b292c3-75fd-4db4-b8de-6e1957fcee55.png" width='70%'></p>

perceptual loss를 사용해서 generator 역할을 하는 Image Transform Net을 학습하는 방법
- Image Transform Net. : input image가 주어지면 원하는 하나의 style로 transform하는 network
- Loss Network
  - 학습된 loss를 측정하기 위해서 VGG16을 사용한다.
  - VGG16 network로 생성된 이미지의 중간 중간의 layer에서 feature들을 추출한다.
  - 그 후, Style target과 Content Target을 이용해 loss를 측정한다.
  - Image Transform Net이 학습하는 동안에는 FIx되어 update되지 않는다.

**Feature reconstruction loss**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158155739-dc6e863e-2901-4e83-9667-6fa87f941950.png" width='70%'></p>

- transform된 이미지 Y^이 Content target의 Content를 그대로 유지하고 있는지를 권장하는 Loss
- Content target은 원래 X를 넣어주는 것이 일반적이다.
- transform image와 content target을 VGG16에 넣어 중간 level의 feature map을 추출해 두 feature map의 L2 loss를 구한다.
- image recognition network인 VGG는 중간 level의 feature를 추출하게 되면 semantic content를 관찰하게 되는데, 두 content를 인식했을 때의 대상이 비슷해야한다는 조건을 주게 된다.

**Style reconstruction loss**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158159090-82a403fa-3bbe-42a1-8ee6-ffdb55867be6.png" width='70%'></p>

- style을 transfer하도록 하는 loss
- transform image와 Style target을 VGG16에 넣어 중간 level의 feature map을 추출해 두 feature map을 뽑는다. : 3D tensor 형태
- Style을 담기 위해서 style이 무엇인지를 정의하는 Gram matrices를 통해 L2 loss를 구한다.
  > **Gram matrices**
  > - 위치 정보를 제외한 feature map의 통계적 특징을 담으려 디자인
  > - style은 위치에 따라 다른 것이 아닌 전반적인 경향으로 위치 정보를 제외한 이미지 전반에 걸치 통계적 특징을 담는다.
  > - how? (C, H, W)에서 (C, H\*W)의 형태로 reshape를 하여 (C, H\*W)와 (H\*W, C)의 곱을 통해 (C, C) gram matrices를 생성하게 된다. : 상대적인 channel간의 연관관계를 coding
  > - what? feature map의 각 channel은 고유한 detector 역할을 하는데, style target 이미지가 들어왔을 때 각 detector가 동시에 비슷하게 response가 크게 나오면 두 경향성이 동시에 발생하는 경우가 많다는 이야기이다. 패턴을 포함하고 있다.

# Various GAN application
**Deepfake**

사람의 얼굴과 목소리 생성

**Enthical concerns about Deepfake**
GAN을 통한 범죄를 막기 위한 challenge들이 생기고 있다.

**Face anonymization with passcode**
passcode를 모두 올바르게 입력했을 때에만 원본의 이미지가 나오도록 설계
![image](https://user-images.githubusercontent.com/57162812/158161519-04675949-5e33-4838-a367-bc1d90f5477d.png)
