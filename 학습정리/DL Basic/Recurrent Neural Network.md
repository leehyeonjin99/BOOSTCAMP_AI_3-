# Recurrent Neural Network

## Sequential Model
- Sequential Data : Audio, Vedio, Motion
  - 길이가 어디까지인지 모른다. 즉, 차원을 알 수 없다.
  - Sequential Data를 input으로 받는 모델은 몇개의 입력이 들어오던지 동작해야한다.
- Naive Sequential Model <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153164405-8d49a258-192d-4fff-a2ee-d6f20fb24a1d.png" width=400></p>
  - 입력이 여러번 들어왔을 때 다음번 입력을 예측한다.
    - 고려해야하는 conditioning vector의 수가 점점 늘어난다.
- Autoregressive model <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153164848-697aaf6f-a4f3-4232-a03a-be02d8b8ecfd.png" width=400></p>
  - 과거의 몇개만 본다.
    - AR(1) : 과거의 정보 1개만 본다.
    - AR(2) : 과거의 정보 2개만 보다.
- Markov model (First-order autoregressive model) <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153165075-71f494db-4042-4cff-ba42-f28ec870b2fa.png" width=400></p>
  - 가정 : 현재는 바로 이전 과거에만 dependent하다.
  - 많은 정보를 버리게 된다.
  - 장점 : Joint Distribution을 표현하기 쉽다.
- Latent autoregressive model
  - 과거의 정보를 summary하는 hiddent state를 중간에 넣는다.

## Recurrent Neural Network

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153166485-61c37e11-a1b4-4016-8dcb-7c68e7edc5d8.png" width=400></p>

- Short-term dependencies
  - 하나의 fixed rule로 정보를 취합한다.
    - 이전의 먼 과거 정보가 미래까지 살아남기 힘들다.
    - 즉, 몇 스텝 전은 잘 고려하지만 먼 스텝의 정보는 잘 고려되지 못한다.
    - 모델의 사고가 제한적이 된다.
  - Solution : LSTM

- Vanishing / Exploding Gradient <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153167117-91516775-ad51-49c6-8d58-3cf5540d88c0.png" width=400></p>
  - Sequence Length가 길어지게 되면
    - Activation이 **Sigmoid**인 경우 0과 1 사이의 값이 계속해서 곱해지면 0에 가까워지기 때문에 Vanishing이 발생할 수 있다. 즉, 먼 스텝의 정보가 고려되지 못한다.
    - Activation이 **ReLU**의 경우 값이 계속해서 1보다 크다면 계속해서 곱해지면서 Exploding gradient가 발생할 수 있다.

## Long Short Term Memory
### Recurrent Neural Network

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153168445-26670d19-2362-432e-b471-be57972b971d.png" width=400></p>

### Long Short Term Memory



<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153169196-80595988-9d1b-4876-a24a-2e18c6d92008.png" width=400></p>

- Forget Gate : 어떤 정보를 가져갈지 정한다. 즉, 어떤 정보를 버릴지 정한다.
- Input Gate : 어떤 정보를 cell state에 저장할지 결정한다.
- Update Gate : cell state를 업데이트 한다.
  - x_t와 h_(t-1)로 구성된 임시 cell state와 이전 cell state를 합쳐 x_t까지의 정보가 들어있는 cell state를 업데이트 한다.
- Output Gate : 업데이트된 cell state를 사용하여 output을 만든다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153170335-12e81fed-6521-46bd-a5da-715a00c815c4.png" width=500></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153170436-67379e1a-845e-4dd0-96cd-ad2e3f16c6cf.png" width=500></p>

### Gated Recurrent Unit

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153172482-ec46bcd0-7f3b-4292-9d81-ca9098f1f3cf.png" width=400></p>

- **Reset gate**와 **update gate** 2개의 gate를 가진 architecture이다.
- LSTM과 다르게 cell state 없이 hidden state로만 동작된다.

## Further Question
1. LSTM에서는 Modern CNN 내용에서 배웠던 중요한 개념이 적용되어 있습니다. 무엇일까요?
  - Skip-Connection of ResNet
  - Concatenation of DenseNet
2. Pytorch LSTM 클래스에서 3dim 데이터(batch_size, sequence length, num feature), batch_first 관련 argument는 중요한 역할을 합니다. batch_first=True인 경우는 어떻게 작동이 하게되는걸까요?
  - `batch_first=False`(default)인 경우 output 값의 사이즈는 (seq, batch, feature)로 나온다. 하지만, `batch_first=True`인 경우 output 값의 사이즈는 (batch, seq, feature)가 된다. 


