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
  > : 바로 이전의 정보를 제외한 나머지 정보들을 <img src="https://latex.codecogs.com/svg.image?H_t"> 잠재변수로 인코딩하여 활용하는 모델  
  > → RNN : 잠재변수를 신경망을 통해 반복하여 사용하여 시퀀스 데이터의 패턴을 학습하는 모델

## RNN 이해하기

- MLP 모델
  <img src="https://latex.codecogs.com/svg.image?O=H{W}^{(2)}+{b}^{(2)}">  
  <img src="https://latex.codecogs.com/svg.image?H=\sigma(X{W}^{(1)}+{b}^{(1)})">

- 변수들에 시간을 더해주면 다음과 같아진다.
  <img src="https://latex.codecogs.com/svg.image?O_t=H_t{W}^{(2)}+{b}^{(2)}">  
  <img src="https://latex.codecogs.com/svg.image?H_t=\sigma(X_t{W}^{(1)}+{b}^{(1)})">
  
  <img src="https://user-images.githubusercontent.com/57162812/150450222-a7b27809-bcd5-4ad3-a533-09fd3ab2a938.png" width=150>

  > 이 모델은 과거의 정보 없이 현재의 정보만으로 다루고 있다.
  
- 따라서, RNN은 이전 순서의 잠재변수와 현재의 입력을 활용하여 모델링한다.
  <img src="https://latex.codecogs.com/svg.image?O_t=H_t{W}^{(2)}+{b}^{(2)}">  
  <img src="https://latex.codecogs.com/svg.image?H_t=\sigma(X_t{W_X}^{(1)}+H_{t-1}{W_H}^{(1)}+{b}^{(1)})">

  <img src="https://user-images.githubusercontent.com/57162812/150450576-b6ffde3c-003e-4e42-a0c9-f7ccfa31f9ec.png" width=200>

  > 잠재변수 <img src="https://latex.codecogs.com/svg.image?H_t">를 복제해 다음 순서의 잠재변수를 인코딩하는데에 사용한다.
 
- RNN의 역전파는 잠재변수의 연결 그래프에 따라 순차적으로 계산한다. : `Backpropagation Through Time(BPTT)`
  
  <img src="https://user-images.githubusercontent.com/57162812/150450844-c78b0972-1c45-472b-a9b1-1b18165b154b.png" width=200>

### BPTT

<img src="https://latex.codecogs.com/svg.image?L(x,y,w_h,w_o)=\sum_{t=1}^{T}l(y_t,o_t)">  
<img src="https://latex.codecogs.com/svg.image?{\partial}_{w_h}L(x,y,w_h,w_o)=\sum_{t=1}^{T}{\partial}_{w_h}l(y_t,o_t)=\sum_{t=1}^{T}{\partial}_{o_t}l(y_t,o_t){\partial}_{h_t}g(h_t,w_h)[{\partial}_{w_h}h_t]">

> <img src="https://latex.codecogs.com/svg.image?h_t=f(x_t,h_{t-1},w_h)">
> 
> <img src="https://latex.codecogs.com/svg.image?o_t=g(h_t,w_o)">

<img src="https://latex.codecogs.com/svg.image?{\partial}_{w_h}h_t={\partial}_{w_h}f(x_t,h_{t-1},w_h)+\sum_{i=1}^{t-1}(\Pi_{j=i+1}^{t}f(x_j,h_{j-1},w_h)){\partial}_{w_h}f(x_i,h_{i-1},w_h)">

위 식에서 시퀀스 길이가 길어질수록 <img src="https://latex.codecogs.com/svg.image?\Pi_{j=i+1}^{t}f(x_j,h_{j-1},w_h)">은 불안정해진다.
- 가장 큰 문제에는 기울기 소실이 발생할 수 있다.: 과거 정보 소실이 발생할 수 있다.

### truncated BPTT

시퀀스 길이가 길어지는 경우 BPTT를 통한 역전파 알고리즘의 계산이 불안정하기 때문에 이를 완화하기 위해 길이를 끊는 것이 필요하다.

<img src="https://user-images.githubusercontent.com/57162812/150459040-8c1c44ae-ba01-4ff2-bb97-fc2565a6c924.png" width=200>

> 이 방법은 완전한 해결 방안이 되지 못하기 때문에 이를 위해 등장한 RNN 네트워크가 LSTM, GRU이다.
