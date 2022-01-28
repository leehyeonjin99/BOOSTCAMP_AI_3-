<div align='center'>
  <h1> CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features </h1>
</div>

## Abstract
- Regional Dropout stratgies

  ☑ black pixel이나 random noise로 구성된 patch를 덧붙여 training image의 의미있는 pixel 삭제
  
  ☑ **Plus**
    1. Network Generalization : Trained net could classify data from the same class as the learning data that it has never seen before.
    2. Object Localization Cpabilities
  
  ☑ **Minus**   
    1. Information Loss   
    2. Inefficiency Duriong Training

  → 따라서 **CutMix** augementaion strategy이 제안되었다.  
    : patch를 잘라 training image에 붙인다. 이때, 정답 label 또한 patch label과 합쳐진 영역의 비율로  mix된다.
  
## Cutmix vs. Other data augmentaion
  
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151478564-071b878c-b3fb-4b25-a0db-a624d078c3dd.png" width=400></p>  

- Mixup

  ☑ 두 데이터와 라벨을 일정 비율로 섞어 새로운 데이터 생성
  
  ☑ **Plus**
    1. classification 능력 향상
  
  ☑ **Minus**
    1. detection과 localization에는 좋은 성능을 보이지 못한다.
    2. Ambiguous and Unnatural : CutMix가 단점을 보완

- Cutout

  ☑ 이미지에서 일정한 크기의 box를 잘라내고 box를 noise로 채우는 방법
  
  ☑ **Plus**
    1. classification 능력 향상
  
  ☑ **Minus**
    1. detection과 localiztion에는 좋은 성능을 보이지 못한다.

- CutMix
   
  ☑ training data들을 자르고 합치는 방식으로, 각각이 합쳐진 label들 또한 영역에 따라 변경  
  
  ☑ **Plus**
    1. 모델이 객체의 차이를 식별할 수 있는 부분에 집중하지 않고, 덜 구별되는 부분 및 이미지의 전체적인 구역을 보고 학습  
       → Generalization과 localization 성능 향상
    2. OOD(Out of Distribution : train set과 test set의 분포가 다른 경우)와 이미지가 가려진 sample, adversarial smaple에 대하여 robust
  
  ☑ **Minus**  
    1. 추가적인 연산 필요

### CAM : Class Activation Map

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151483634-21d8a74e-ea84-4dc6-99d9-13b22e818da3.png" width=400></p>  

▶ 위의 실험을 보면, CutMix의 경우 'St. Bernard'의 CAM에 대해서는 Bernard가 있는 곳에 히트맵이 올라오게 되며, 'Poodle' 의 CAM에서는 Poddle이 있는 곳에 히트맵이 올라오게 된다. 즉, CutMix는 이미지의 mixed region에 대해 강점을 가진다. 하지만 그에 반해 Cutout은 아니다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/151480814-97ce776b-ea6e-419a-ac4f-5ca0205eaeac.png" width=400></p>

## CutMix
### Algorithm

![image](https://user-images.githubusercontent.com/57162812/151485011-72618d7e-3c73-4676-98ad-35eb7eefdb82.png)

### Expression

<img src="https://user-images.githubusercontent.com/57162812/151482722-db1a20dc-047c-4c9f-8a1e-f3d81275343f.png" width=250>  <img src="https://user-images.githubusercontent.com/57162812/151484404-d9962757-7505-440a-9adf-35eaeaa46e1c.png" width=500>

- binary mask는 x_A의 영역에서는 1의 값을, x_B의 영역에서는 0의 값을 갖는다.
- 이번 실험에서는 α=1로 하여 λ는 uniform distribution (0,1)를 따른다.
- x_A의 넓이와 x_B의 넓이의 비율에 따라 λ가 결정된다. 즉, 1-λ=(x_A의 넓이)/(x_B의 넓이)
  <img src="https://user-images.githubusercontent.com/57162812/151484777-02f07a42-e155-4d8b-a145-fb0e738a58a1.png" width=200>


<img src="https://user-images.githubusercontent.com/57162812/151483489-da42ee19-851c-4e12-897a-9ea37f6ff593.png">

## WSOL : Weakly Supervised Object Localization

  ☑ object의 정확한 위치가 아닌 label이 정답으로 주어지는 경우
  
  ☑ 동작 방식 : feature map이 어떤 부분이 active되는지에 따라 localization 진행
  
  ☑ target의 작은 특징이 아닌 전체적인 object regions로부터 단서를 추출해내는 CNN일수록 target localization의 성능이 좋다.
  
<img src="https://user-images.githubusercontent.com/57162812/151486558-857c51e7-b749-44d8-a0f2-952d7f089538.png" width=300>

  ▶ CutMix+WSOL : **효과적**
  
  ▶ CutOut+WSOL : **효과적**
  
  ▶ MixUp+WSOL : **비효과적** : 모호하며 자연스럽지 못한 이미지 sample이 classifier를 discriminative part에 더 집중하여 cue를 찾아내게 만들기 때문이다.
  
    
  
