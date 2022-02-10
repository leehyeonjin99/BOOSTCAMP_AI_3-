# Generative Models
## Introduction
- What does it mean to learn a **generative model**?
  - GAN이나 VAE를 가지고 새로운 image 혹은 문장을 만든다??? 이게 다가 아니다!!!!

## Learning a Generative Model

가정 : 개 이미지 set이 주어졌다.

- Want : probability distribution **p(x)** 를 학습한다.
  - **Generation** : x_new~p(x)를 sampling하면 x_new는 개의 그림처럼 보여야한다.
  - **Density Estimation** : 만약 x가 개처럼 보인다면 p(x)는 높아야하고 아니라면 낮아야한다.(anomaly detection) : 이상 감지 행동에 활용가능
    - Explicit Model : 확률 값을 얻어낼 수 있는 
  - **Unsupervised Representation Learning** : 이미지들의 공통점을 학습해야한다.(feature learning)

### Basic Discrete Distribution
- Bernoulli distribution
  - D={heads, tails}
  - P(X=Heads)=p, P(X=Tails)=1-p
  - X~Ber(p) : 분포를 나타내는 parameter는 1개

- Categorical distribution
  - D={1, ..., m}
  - P(X=i)=p_i with p_1+...+p_m=1
  - X~Cat(p_1, ...,p_m) : m-1개의 parameter
 
 - Example
  - Modeling an RGB joint distribution (of a single pixel) <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153416311-1f0deded-fa5b-4335-8400-0f0bdd9e1912.png" width=220></p>
    - (r, g, b)~p(R, G, B)
    - the number of cases = 256*256*256
    - the number of parameters = 256*256*256-1
    - 하나의 RGB pixel을 Fully Describe하기 위해 필요한 parameter의 수는 매우 크다.
  - X_1, ..., X_n of n binary pixels (a binary image) <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153416575-79b46246-11f7-45ca-988e-64f120833bff.png" width=220></p>
    - the number of possible states = 2^n
    - p(x_1, ..., x_n)에서 Sampling하면 하나의 이미지를 생성한다.
    - the number of parameters = 2^n-1

### Structure Through Independent

the number of parameter를 줄이고 싶다 ➡ 가정 : n개의 pixel이 independent하다.

즉, x_1, ..., X_n이 independent하다.
- p(x_1, ..., x_n)=p(x_1)p(x_2)...p(x_n)
- the number of possible state = 2^n
- the number of parameters = n

하지만, **independent**의 가정은 불가능하다. why? 이미지의 pixel을 생각하면 주변의 pixel에 영향을 받기 때문에

### Conditional Independent

- **Chain Rule** : p(x_1, ...,x_n)=p(x_1)p(x_2|x_1)p(x_3|x_1,x_2)...p(x_n|x_1,...,x_(n-1))
- **Bayes' Rule** : p(x|y)=p(x,y)/p(y)=p(x)p(y|x)/p(y)
- **Conditional Independence** : z가 주어졌을 때 x와 y가 independent하다면, p(x|y,z)=p(x|z)

Chain Rule을 사용하면 p(x_1, ...,x_n)=p(x_1)p(x_2|x_1)p(x_3|x_1,x_2)...p(x_n|x_1,...,x_(n-1))이다.
- the number of parameter
  - p(x_1) : 1
  - p(x_2|x_1) : 2 why? p(x_2|x_1=0), p(x_2|x_1=1)
  - p(x_3|x_1,x_2) : 4
  - Total parameter : 1+2+4+2^(n-1)=2^n-1

이제 Independent를 가정해보자. 즉, x_i는 x_(i-1)에 dependent하고 x_1~x_(i-1)에는 independent하다.  
Chain Rule을 사용하면 p(x_1, ...,x_n)=p(x_1)p(x_2|x_1)p(x_3|x_2)...p(x_n|x_(n-1))
- the number of parameter = 1+2+2+2+...+2=2n-1

Markow 가정을 통해서 parameter의 수를 지수적으로 감소시켰다.

**Auto-Regressive Model**은 Conditional Independency를 활용한다.

## Auto-Regressive Model

가정 : 28x28 binary pixel이 있다.

목표 : p(x)=p(x_1, x_2, ..., x_784) with x_iϵ{0,1}

- p(x)를 파라미터화하는 방법은?
  - Chain Rule 사용 : p(x_(1:784))=p(x_1)p(x_2|x_1)p(x_3|x_(1:2))...
  - 이것을 **Auto-Regressive Model**이라 한다.
    - Markov Assumption을 통해서 i번째 pixel이 i-1번째 pixel에만 dependent한 것도 autoregressive model이지만, i번째 pixel이 1부터 i-1번째 까지의 pixel에 dependent 한 것도 autoregressive model이라 할 수 있다.
  - 이미지 domain에 autoregressive model을 활용하기 위해서 중요한 것은 ordering이다.
    - why? 순서를 정해야한다. 순서를 어떻게 정하냐에 따라서 성능이 달라질 수 있고, 방법론이 달라질 수 있다.

### NADE : Neural AutoRegressive Density Estimator

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153422674-cd22b37f-0bd0-4015-852c-4a60b8112ccd.png" width=500></p>
          
- i번째 pixel의 probability distribution : p(x_i|x_(1:i-1))=σ(αh_i+b_i) where h_i=σ(Wx_(1:i-1)+c)
- i번째 pixel은 i-1개의 입력에 dependent하다. 즉, Neural Network 입장에서는 입력의 차원이 계속 달라진다. 
  - weight가 계속해서 커진다.
  - 100번 pixel에 대한 확률 분포를 만들 때에는 99개의 입력을 받을 수 있는 Neural Network가 필요하다.

NADE는 입력에 대한 **density**를 계산할 수 있는 **explicit model**이다.

그렇다면 주어진 이미지에 대한 **density**는 어떻게 계산할까?
- 784개의 binary pixel을 가진 binary image가 있다고 하자. {x_1, x_2, ..., x_784}
- joint probability = p(x_1, x_2, ..., x_784)=p(x_1)p(x_2|x_1)p(x_3|x_(1:2))...p(x_784|x_(1:783))

Continuous random variable의 경우에는 Gaussian mixture 모델을 통해 Continuous Distribution을 생성할 수 있다.

### Pixel RNN

Auto Regressive model에 RNN을 사용할 수 있다.

nxn RGB image가 있다고 가정하자.

<img src="https://user-images.githubusercontent.com/57162812/153425284-bb7942c7-3b86-43db-8a35-8d8b53e943c7.png" width=400></p>

ordering에 따라 Pixel RNN에 두가지 architecture가 있다.
1. Row LSTM
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153425779-92fbca68-6351-4209-aca9-91e1ae7e9cc3.png" width=100></p>

2. Diagonal BiLSTM
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153425953-758c4d90-c566-4d09-a88d-75a5f92ecdc6.png" width=100></p>
---

## Latent Variable Models
### Variational Auto-Encoder

- Variational Inference(VI)
  - VI의 목적은 posterior distribution을 가장 잘 근사할 수 있는 Variational Distribution을 찾는 것이다.
    - Posterior Distribution : <img src="https://user-images.githubusercontent.com/57162812/153437460-3c305b8e-1019-428d-bfe9-ac45cbba2af8.png" width=50> observation이 주어졌을 때, 나의 관심있어하는 random variable의 확률 분포 with z는 latent vector이다.
    - Variational Distribution : <img src="https://user-images.githubusercontent.com/57162812/153438131-a773cea1-89ae-4ed5-ac87-ff6a33b65fc5.png" width=50> 일반적으로 Posterior Distribution을 계산하기에는 어렵다. 따라서 학습 가능한 분포인 Variational Distribution으로 근사한다.
  - 최적화 하기 위한 Loss Function : KL divergence를 활용하여 posterior distribution과 variational distribution의 거리를 줄인다.

- VI의 목적인 Variational Distribution을 찾는 것이 **Encoder**이다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153438807-0668135c-4009-4d0d-a2f0-6b55aecbe37b.png" width=300></p>
  - 뭔지도 모르는 Posterior Distribution을 어떻게 근사할까? VI에 있는 ELBO 부분으로 가능해진다.  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153439317-3e51e5ab-b121-4be5-9895-71bfde6d14cd.png" width=400></p>
  - ELBO를 maximizing함으로써 Posterior Distribution과 Variational Distribution 사이의 거리를 minimizing 가능해진다.
  - ELBO는 분해 가능하다. ELBO= Reconstruction Term-Prior Fitting Term <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153440925-7bcf05e6-e684-4552-a078-fe10e12dd927.png" width=400></p>
    - Reconstruction Term : Encoder를 통해서 x를 latent space로 보냈다가 다시 Decoder로 돌아오는 Reconstruction Loss를 줄이는 것
    - Prior Fitting Term : 많은 양의 x을 latent space에 올려놨다. latent space의 점들이 이루는 분포가 prior distribution와 비슷하게 만들어 주는 것

**VI Model의 한계**
- 어떤 입력이 주어졌을 때 likelihood를 알기 어렵다. : intractable model
- KL Divergence는 closed form이 되기 어렵다. 대부분의 Variational Auto-Encoder는 Gaussian 분포를 사용한다.
- 따라서, isotropic Gaussian을 사용한다.  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153445825-6922ef68-95b6-4b61-afe9-a66450038c4b.png" width=300></p>

### Adversarial Auto-Encoder

VAE의 가장 큰 단점은 encoder를 활용할 때, prior fitting term이 KL Divergence를 활용한다. 따라서, Gaussian이 아닌 경우 활용하기 힘들다. 

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153446689-fa2cde35-8b9b-4d96-ab91-2d145cd9b00a.png" width=400></p>

그렇다면 prior distribution으로 Gaussian을 활용하고 싶지 않다면? → Adversarial Auto-Encoder(AAE)

GAN을 사용해서 latent distribution 사이의 분포를 맞춰준다. prior fitting term을 GAN objective로 바꿨다.

## Generative Adversarial Network(GAN)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153447102-e3005758-cce2-4e0b-97ad-0c610dc2f592.png" width=400></p>

Want : Generator

Generator 학습 결과로 나오는 Generator를 학습하는 Discriminator가 점차 좋아진다. fixed Discriminator를 통해서 generator가 학습하는 것이 아니라 Discriminator가 Generator를 통해서 점차 좋아지기 때문에 Generator도 성능이 같이 올라가 좋은 이미지를 만들어낼 수 있다.

### GAN vs. VAE

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153448788-7d899aea-d2a1-4af6-b661-552daff15336.png" width=500></p>

- VAE
  - 학습 : x라는 이미지(input domain)이 들어오면 Encoder를 통해서 latent space로 갔다가 Decoder를 통해서 x라는 domain으로 간다. 
  - Generation 단계 : latent distribution에서 z를 sampling 해서 Decoder를 통해서 나오는 x가 generation 결과

- GAN
  - z라는 latent distribution으로 시작해서 Genorator를 통해서 Faker가 나오고, Discriminatior은 Fake 이미지와 Real 이미지를 분류하는 분류기를 학습하고, Generator는 학습된 Discriminator의 입장에서 True가 나오도록 학습하고를 반복한다.

### GAN Objective

- **Generator**와 **Discriminator**의 two player minmax game
- Discriminator의 입장 : Generator의 결과인 Fake 이미지를 모두 0으로 분류 하겠다.  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153449513-ca10755a-1577-4dcb-9fad-8ada54a9ec91.png" width=350></p>
  - optimal discriminator : <img src="https://user-images.githubusercontent.com/57162812/153449830-b716771f-a408-441e-86b2-e5e7eaa06d48.png" width=170></p>
- Generator의 입장 : Generator의 결과인 Fake 이미지를 Discriminator가 모두 1로 분류하도록 하겠다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153450189-6b377973-1428-458f-9887-d6733a5b9e4b.png" width=350></p>

목적식에 optimal discriminator를 대입해보자.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153450408-6f531d3b-a692-4c3e-a8dd-5bd268df4b04.png" width=400></p>

GAN의 objective가 많은 경우에 우리의 True data Distribution과 내가 학습한 data Distribution 사이의 Jenson-Shannon Divergence(JSD)를 최소화 하는 것이다.



