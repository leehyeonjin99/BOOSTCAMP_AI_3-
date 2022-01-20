<div align='center'>
  <h1> CNN </h1>
</div>

## fully connected MLP : 각 뉴런들이 선형모델과 활성함수로 모두 연결된 구조  

<img src="https://latex.codecogs.com/svg.image?h_i={\sigma}(\sum_{j=1}^{p}W_{ij}x_j)" />

- <img src="https://latex.codecogs.com/svg.image?\sigma"> : 활성 함수  
- <img src="https://latex.codecogs.com/svg.image?W" > : 가중치 행렬

<img src="https://user-images.githubusercontent.com/57162812/150366377-db9ef6ed-350f-4275-b4ea-f7d876eb4616.png" width=200>

각 성분 <img src="https://latex.codecogs.com/svg.image?h_i"> 에 대응하는 가중치 행 <img src="https://latex.codecogs.com/svg.image?W_i"> 이 필요로 한다.   
∴i가 바뀌게 되면 사용되는 가중치 행 <img src="https://latex.codecogs.com/svg.image?W_i"> 또한 바뀐다.

## Conoultion 연산

Convoultion 연산은 **고정된 가중치 행렬**인 `커널(kernel)`을 입력벡터 상에서 움직여 가면서 선형모델과 합성함수가 적용되는 구조

<img src="https://latex.codecogs.com/svg.image?h_i={\sigma}(\sum_{j=1}^{k}V_{j}x_{i+j-1})" />

- <img src="https://latex.codecogs.com/svg.image?\sigma"> : 활성 함수  
- <img src="https://latex.codecogs.com/svg.image?V" > : 커널 벡터
- <img src="https://latex.codecogs.com/svg.image?k" > : 커널의 사이즈

<img src="https://user-images.githubusercontent.com/57162812/150368414-be6468b2-07a5-4287-b910-3fdebff02692.png" width=200>

모든 i에 대해 적용되는 커널은 <img src="https://latex.codecogs.com/svg.image?V" >로 같고 커널의 사이즈 <img src="https://latex.codecogs.com/svg.image?k" >만틈 <img src="https://latex.codecogs.com/svg.image?\overrightarrow{x}" > 상에서 이동하면서 적용

convolution 연산도 **선형 변환**에 속한다.

>수학적 의미  
>- 신호를 **커널을 이용해 국소적으로 증폭 또는 감소**시켜 정보를 추출 또는 필터링 한다.  
>- 정확한 명칭으로는 cross-correlation이 된다.  
> - Continous :  
>    <img src="https://latex.codecogs.com/svg.image?[f*g](x)=\int_{{R}^{d}}f(z)g(x-z)dz=\int_{{R}^{d}}f(z-z)g(z)dz=[g*f](x)">  
> - Distrete :  
>    <img src="https://latex.codecogs.com/svg.image?[f*g](i)=\sum_{a{\in}{{Z}^{d}}}f(a)g(i-a)=\int_{{a}{\in}{{Z}^{d}}}f(i-a)g(a)=[g*f](i)">
> <img src="https://latex.codecogs.com/svg.image?f"> : 커널 함수, <img src="https://latex.codecogs.com/svg.image?g"> : 신호 함수

커널은 정의역 내에서 움직여도 변하지 않고(**translation invariant**) 주어진 신호에서 **국소적(local)** 으로 적용한다.

## 다양한 차원에서의 Convoultion

convolution 연산의 차원은 확장 가능하다.

- 1D-conv
  <img src="https://latex.codecogs.com/svg.image?[f*g](i)=\sum_{p=1}^{d}f(p)g(i+p)">
- 2D-conv
  <img src="https://latex.codecogs.com/svg.image?[f*g](i,j)=\sum_{p,q}f(p,q)g(i+p,j+q)">
- 3D-conv
  <img src="https://latex.codecogs.com/svg.image?[f*g](i,j,k)=\sum_{p,q,r}f(p,q,r)g(i+p,j+q,k+r)">
  
다차원에서도 마찬가지로 i,j,k가 바뀌어도 커널은 변함이 없다.

## 2차원 Convoultion 연산

다음과 같이 2차원에서의 convolution 연산이 진행될 수 있다.

<img src="https://user-images.githubusercontent.com/57162812/150372443-18acf3de-1964-4b03-b048-8e4fe8f7819d.png" width=200>

<img src="https://latex.codecogs.com/svg.image?[f*g](0.0)=0{\times}0+1{\times}1+2{\times}3+3{\times}4=19">

<img src="https://user-images.githubusercontent.com/57162812/150372934-74a5f53a-4f00-4730-917e-24ae7f7f942e.png" width=200>

<img src="https://latex.codecogs.com/svg.image?[f*g](0.0)=0{\times}1+1{\times}2+2{\times}4+3{\times}5=25">

- 입력 크기 : <img src="https://latex.codecogs.com/svg.image?(H,W)"> , 커널 크기 : <img src="https://latex.codecogs.com/svg.image?(K_H,K_W)">  <img src="https://latex.codecogs.com/svg.image?\rightarrow">  <img src="https://latex.codecogs.com/svg.image?({O_H}=H-{K_H}+1,{O_W}=H-{K_W}+1)">

## 3차원 Convolution 연산

채널이 여러개인 2차원 입력의 경우 2차원 Convoultion을 채널 개수만큼 적용한다고 생각하면 된다.

<img src="https://user-images.githubusercontent.com/57162812/150374487-0e1c9f24-a905-4792-b62e-5eee2d88dc51.png" width=400>

하지만, 채널이 여러개인 2차원의 입력의 경우 2차원 Convolution을 채널 개수만큼 적용하면 된다. 각 Convolution은 다를 수 있다.

<img src="https://user-images.githubusercontent.com/57162812/150374837-6d68a83c-49db-412c-aaaf-668e6990dcbe.png" width=400>

각 채널에서의 convolution 연산을 더해주면 출력값이 된다. 텐서를 직융면체 블록으로 이해하면 좀 더 이해하기 쉽다.

<img src="https://user-images.githubusercontent.com/57162812/150375178-4f60569d-5dd8-4755-bdb6-1c9d84cb5411.png" width=400>

만약 출력 또한 텐서로 만들고 싶다면 <img src="https://latex.codecogs.com/svg.image?(K_H,K_W,C)"> 커널의 개수를 <img src="https://latex.codecogs.com/svg.image?O_C">개 만큼 만들면 된다.

<img src="https://user-images.githubusercontent.com/57162812/150375795-47ef2ad4-ea07-472e-8d0e-5238527bb7e9.png" width=400>

## Convolution 연산의 역전파

- 모든 입력데이터에 공통된 Convolution 연산이 적용되기 때문에 역전파를 계산할 때도 convolution 연산이 나온다.

<img src="https://latex.codecogs.com/svg.image?\frac{\partial}{\partial{x}}[f*g](x)={\int}_{{R}^{d}}f(y)g(x-y)dy=int_{{R}^{d}}f(y)\frac{\partial}{\partial{x}}g(x-y)dy=[f*g'](x)">

- <img src="https://latex.codecogs.com/svg.image?o_1">으로 가는 입력값은 <img src="https://latex.codecogs.com/svg.image?x_1,x_2,x_3">가 있다.

![image](https://user-images.githubusercontent.com/57162812/150377530-f2d5fbff-1484-4ece-b82d-6963b5c6f9fa.png)

전체적인 연산 방향을 보면 다음과 같다.

![image](https://user-images.githubusercontent.com/57162812/150377798-cb52b0b5-ca3b-4d07-b98b-aaef41a828b1.png)

즉, <img src="https://latex.codecogs.com/svg.image?o_i=\sum_{j}w_jx_i+j-1">의 식을 도출해낼 수 있다.

역전파 방향을 살펴보자.

![image](https://user-images.githubusercontent.com/57162812/150378167-a47a491b-7143-497b-a5e6-ec6ffab7ceb3.png)

![image](https://user-images.githubusercontent.com/57162812/150378218-ca8eade1-dc16-4d0b-ba29-7c8ed752ca88.png)

![image](https://user-images.githubusercontent.com/57162812/150378251-b369e4cf-514a-406b-8e08-f71d1eff98da.png)

![image](https://user-images.githubusercontent.com/57162812/150378307-2afb4aa7-d6e4-4b9e-9f31-b18e4ff6cd83.png)

역전파도 convolution 연산과 마찬가지로 각 커널에 들어오는 모든 그레디언트를 더해준다.

