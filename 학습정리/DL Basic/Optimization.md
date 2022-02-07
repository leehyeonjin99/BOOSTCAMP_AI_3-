## Important Concepts in Optimization
### Generalization

- 학습의 목적 : 일반화 성능을 높이는 것
  - 일반화 성능 : 학습 데이터와 테스트 데이터 사이의 차이가 얼마나 나는가
- Generalization Performance가 좋다고 해서 test data의 성능이 좋다고 할 수 없다.
  - train data의 성능이 좋지 않으면서 test data 사이의 차이가 적을 수 있기 때문이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152766421-0d9d7283-5523-4558-8adc-6283d9f9559b.png" width=400></p>

### Under-fitting vs. Over-fitting

- Overfitting이란?
  - train data의 성능은 좋지만 test data에 대한 성능은 낮다. 즉, generalization performance가 좋지 못하다.
- Underfitting이란?
  - train data의 성능이 좋지 못한 것
  - 원인은?
    - network가 너무 간단하다.
    - training의 양이 너무 적다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152766820-305c2a68-ce8c-4a5b-97ec-e0aa07ec9a48.png" width=500></p>

### Cross Validation

- Cross Validation : a moodel validation technique for assessing how the model will generalize to an independent(test) data
- 학습 데이터를 K개로 나누어서
  - K-1개의 데이터셋으로 학습
  - 1개의 데이터셋으로 검증
- 즉, K번의 iteration 필요
- 언제 사용할까?
  - Cross Validation을 통해서 최적의 hyperparameter set을 찾고 hyperparameter를 고정한 상태에서 학습시킬 때는 모든 dataset을 사용
- **Test Data를 통해서 학습 및 검증에서 절대 사용해서는 안된다** : 치팅하는 것

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152767293-eda9b809-89c4-4b95-8874-c2a1e75f623d.png" width=300></p>

### Bias-variance tradeoff

- Bias: 평균적으로 얼마나 true target에 접근하는가?
  - 평균적으로 true targe에 접근하면 low bias
- Variance : 같은 입력에 대해서 얼마나 출력이 일관적인가?
  - 여러변의 입력에 대해서 출력이 일관되면 low variance

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152767937-292c85a2-b08d-460b-9fb4-6c44b043ce1a.png" width=260></p>

- Cost는 3개(Bias, Variance, Noise)의 부분으로 분해할 수 있다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/152768389-dcf533d8-a338-4ee2-97b9-7a3a383d81b0.png" width=350></p>


### Booststrapping

- Bootstrap이란?
  - 복원추출을 통한 여러개의 random sample을 사용하여 여러 모델/metric을 만들어 사용

### Bagging and Boosting

- Bagging(**B**ootstrapping **Agg**regat**ing**)
  - Bootstrapping을 통해 학습되어진 여러개의 모델
  - Base Classifier은 여러 모델의 예측을 총계 내어(Voting, 평균) random subset에 학습한다.

- Boosting
  - 분류하기 힘든 training sample들에 집중한다.
  - A strong model is built by combining weak learners in sequence where each learner learns from the mistakes of the previous weak learner : 이전 모델에서 잘 분류하지 못한 training data에 대한 새로운 model을 만든다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152769592-6f3151af-39bc-46aa-a32b-864adfe90c31.png" width=400></p>


## Practical Gradient Descent Method

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152773977-8f8ffa58-32a1-47c0-9abc-9f443e7aeb7c.png" width=400></p>

### Gradient Descent Methods
- Stochastic gradient descent : update with the gradeint computed from a single sample
- Mini-batch gradient descent : update with the gradeint computed from a subset of data
- Batch gradient descent : update with the gradient computed from the whole data

### Batch-size Matters
- batchsize가
  - 너무 크면 sharp minimizer에 도달하게 된다.
  - 너무 작으면 flat minizer에 도달하게 된다.
- sharp minimizer에 도달하는 것보다 falt minimizer에 도달하는 것이 낫다.
  - (why?) flat minimum의 경우 조금 벗어나더라도 gerneralization gap이 적지만, sharp minimum의 경우 조금만 벗어나도 generalization gap이 커진다. 즉, flat minumum에서의 generalization performance가 더 높다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152770528-2f261958-ccf2-42de-bac2-9a2ed0b27baa.png" width=450></p>

### Stochastic gradient descent

<img src="https://user-images.githubusercontent.com/57162812/152771103-9535af37-b7bf-4963-8137-3b55facd1ca6.png" width=250>

### Momentum
- Momentum : 이전 gradient 방향의 정보를 다음 gradient 방향에 이용
- 장점?
  - 한번 흘러가기 시작한 gradient 뱡향을 어느정도 유지시켜주기 때문에, gradient가 굉장히 많이 변동해도 어느정도 잘 학습된 효과가 있다.
<img src="https://user-images.githubusercontent.com/57162812/152771196-e5a81584-cdc6-42e1-a09f-7f19951191d7.png" width=300>

### Nesterov accelerated gradient

- Momentum : 스텝을 계산해서 움직인 후, 이전에 내려 오던 관성 방향으로 다음 스텝을 밟는다.
- NAG : 일단 관성 방향으로 먼저 움직이고, 움직인 자리에서 스텝을 계산한 뒤 다음 스텝을 밟는다.

<img src="https://user-images.githubusercontent.com/57162812/152771482-98959a0f-7940-4f63-8252-4345266a5f07.png" width=250>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152772533-6655d338-016e-4df0-868c-c82267bad7a5.png" width=420></p>


### Adagrad

- 지금까지 aprameter들이 얼마나 변했는지를 제곱해서 더한 값을 추가한다.
  - 이전에 많이 변화한 parameer는 적게 변화시킨다.
- 단점 : training이 많이 진행될수록 'Sum of gradient squares' G가 커져 W의 updat가 되지 않아 학습이 잘 진행되지 않을 것이다.

<img src="https://user-images.githubusercontent.com/57162812/152772902-b4ac172b-df9d-466a-9ada-c16191a7d609.png" width=300>

### Adadelta

- Adagrad의 learning rate가 0에 수렴하는 것에 대한 대안책
- 특징 : learning rate가 없다.

<img src="https://user-images.githubusercontent.com/57162812/152773198-30a451b5-cda4-4932-85c3-b6071a4d926e.png" width=400>

### RMSprop

- 논문으로 밢되지 않았다.

<img src="https://user-images.githubusercontent.com/57162812/152773417-56dc74c0-0916-4521-a284-c595d6e5003a.png" width=400>

### Adam

- Momentum(이전 gradient의 경향 사용 알고리즘) + RMSprop(이전 learning rate의 경향 사용 알고리즘)

<img src="https://user-images.githubusercontent.com/57162812/152773810-bb4e668b-8e36-448d-9c8b-a97853e62ed7.png" width=400>
