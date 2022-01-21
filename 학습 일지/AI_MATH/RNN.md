<div align='center'>
  <h1> RNN </h1>
</div>

## 시퀀스 데이터

- `시퀀스 데이터` : 순차적으로 들어오는 데이터이다. 즉, 시간 순서에 따라 나열된 데이터이다.  
  ex) 소리, 문자열, 주가
- 과거 정보 또는 앞뒤 맥락 없이 미래를 예측 혹은 문장을 완성하는 것은 불가능
- 시퀀스 데이터는 독립동등분포 가정을 잘 위배 → 순서를 바꾸거나 과거 정보에 손실이 발생하면 데이터의 확률분포도 바뀐다.  
  > 독립동등분포(i.i.d)  
  > : 확률변수가 여러 개 있을 때 (X1 , X2 , ... , Xn) 이들이 상호독립적이며, 모두 동일한 확률분포 f(x)를 가진다면 iid이다.
  
### 시퀀스 데이터 다루는 방법
- **조건부 확률**의 베이즈 정리를 이용하여 이전 시퀀스를 가지고 앞으로 발생할 데이터의 확률분포를 다룰 수 있다.

<img src="https://latex.codecogs.com/svg.image?P(X_1,X_2,...,X_k)=P(X_k|X_1,X_2,...X_{k-1})P(X_1,X_2,...X_{k-1})"/>  

위의 식을 연속적으로 사용해보면 다음과 같이 표현할 수 있다.

<img src="https://latex.codecogs.com/svg.image?P(X_1,X_2,...,X_k)"> 
<img src="https://latex.codecogs.com/svg.image?=P(X_k|X_1,X_2,...X_{k-1})P(X_1,X_2,...X_{k-1})">
<img src="https://latex.codecogs.com/svg.image?=P(X_k|X_1,X_2,...X_{k-1})P(X_{k-1}|X_1,X_2,...X_{k-2})P(X_1,X_2,...X_{k-2})">  
<img src="https://latex.codecogs.com/svg.image?=\Pi_{s=1}^{k}P(X_s|X_1,...,X_{s-1})"/>  

> 위의 식은 시퀀스 데이터를 분석할 때 이전의 모든 정보들을 사용하였지만 모든 시퀀스 데이터를 다룰 때 이전의 정보들을 반드시 모두 사용해야하는 것은 아니다.

- 조건부에 들어가있는 데이터의 길이는 가변적이다. 따라서, 시퀀스 데이터를 다루기 위해서는 길이가 **가변적인 데이터**를 다룰 수 있는 모델이어야 한다. 
  > AR 자기회귀모델   
  > : 고정된 길이 <img src="https://latex.codecogs.com/svg.image?\tau">만큼의 시퀀스만 사용하는 자기회귀모델
  
  > 잠재 AR 자기회귀모델  
  > : 바로 이전의 정보를 제외한 나머지 정보들을 <img src="https://latex.codecogs.com/svg.image?H_t> 잠재변수로 인코딩하여 활용하는 모델  
  > → RNN : 잠재변수를 신경망을 통해 반복하여 사용하여 시퀀스 데이터의 패턴을 학습하는 모델

## RNN 이해하기

- MLP 모델

<img src="https://latex.codecogs.com/svg.image?O=H{W}^{(2)}+{b}^{(2)}">  
<img src="https://latex.codecogs.com/svg.image?H=\sigma(X{W}^{1}+{b}^{1})">

- 변수들에 시간을 더해주면 다음과 같아진다.

<img src="https://latex.codecogs.com/svg.image?O_t=H_t{W}^{(2)}+{b}^{(2)}">  
<img src="https://latex.codecogs.com/svg.image?H_t=\sigma(X_t{W}^{1}+{b}^{1})">

