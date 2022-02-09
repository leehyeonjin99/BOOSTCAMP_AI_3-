# Transformer
## Sequential Model

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153181381-f183e93f-c7e8-4e3a-b617-4b2f1b18497f.png" width=400></p>

- Sequential 모델은 경로 탈락, 순서 뒤바뀐 data에 대한 모델링이 어렵다.
- Solution : Transformer

## Transformer
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153181566-17b5e065-3d08-4202-8273-2402a5f2b10d.png" width=400></p>

- Transformer는 attention을 기반으로 한 첫번째 sequence transduction model이다.
- RNN처럼 Sequence Data를 다루지만 재귀적인 구조는 없다.
- 또한, 기계어 번역 뿐 아니라 이미지 분류, detection에도 사용된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153182182-2cc32774-3335-4c3c-aa57-50c86f2673bb.png" width=400></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153183144-3426558a-0b63-4f1f-af4f-cbebc4e22a25.png" width=400></p>

- input sequence와 output sequence의 길이 및 도멘인이 다를 수 있다.
- Decoder 부분 : Self Attention 구조 : 각 단어의 vector들끼리 서로간의 관계가 얼마나 중요한지 점수화
  - n개의 단어를 한 번에 처리할 수 있다.
  - Transformer가 잘 작동되는 이유!!
- 동일한 구조를 갖지만 Network parameter가 다르게 학습되는 Encoder/ Decoder가 Stack되어 있다.
- Question?
  1. n개의 단어를 한 번에 처리할까?
  2. decoder와 encoder 사이에 어떤 정보를 주고받을까?
  3. Decoder가 어떻게 generation할까?
---

**Self-Attention at a high level**

<img src="https://user-images.githubusercontent.com/57162812/153184548-7d0845c7-41ed-4145-8e6c-5796f682708f.png" width=500>

'it'이라는 단어를 encoding할 때, 다른 단어들과의 관계성을 보게 되고 학습된 결과를 보면 'it'이 'animal'과 높은 관계가 있다고 알아서 학습되어 있다. : self-attention

---
**작동 방법에 대해 알아보자**

1. 각 단어를 표현하는 Embedding vector를 나타낸다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153183385-6e1e84d3-e5cc-42b2-aa91-218754294ea6.png" width=400></p>

2. Transformer는 각 단어를 Self-Attention을 통해 feature vector로 encoding한다.
  - n개의 단어가 주어지고, 즉, n개의 x가 주어지고 각각의 z를 찾는데 나머지 (n-1)개의 x를 함께 고려한다.  
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153183797-a72c8952-f72e-4417-8446-a3f666bd5f6e.png" width=400></p>

---

**2개의 단어로 실습해보자**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153184077-ccf6e6ae-e4a7-436b-b845-1a61d9f518cf.png" width=400></p>

- Thinking과 Machine이 있다고 가정하자.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153185097-60add766-2d3b-4645-a198-f140e734c9a8.png" width=500></p>

1. 각 단어들에 대한 Query, Key, Value가 측정된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153185337-435f0a49-9767-4e4a-8cab-a0e3f7547870.png" width=500></p>

2. Query vector와 모든 word에 대한 Key Vector의 내적으로 Score를 구한다.
  - Key Vector와 Query Vector의 차원은 같아야한다.
3. Score를 Key Vector의 dimension의 제곱근 값으로 나눠준다.
4. 변형된 Score에 Softmax를 적용시킨다.
5. Softmax와 Value vector를 곱해준다.
6. 앞서 계산한 vector들을 더해준다.

---

**앞선 계산을 matrix로 진행하자**

1. embedding vector와 W^Q, W^K, W^V를 matmul해 Query vector, Key vector, Value vector을 계산한다. 
  - W^Q, W^K, W^V를 찾아내는 Multilayer Perceptron이 존재한다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153191604-b8a54d10-154b-4911-af0d-f21fc9fdb015.png" width=500></p>

2. Q, K, V를 계산한다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153191753-6ae606d7-c257-468b-b80f-1816ff87e6a1.png" width=500></p>

- Transformer은 왜 잘될까?
  - Transforemr은 하나의 input이 고정되어 있다 하더라도(network가 fix되어있다 하더라도) Encoding 하려는 단어와 그 옆에 있는 단어들에 따라서 Encoded vector가 달라진다. 즉, **flexible**하다. 
  - 따라서, 훨씬 더 많은 것들을 표현할 수 있다.
  - 하지만, 그 만큼 더 많은 operation이 필요하다.
    - Computational Bottleneck
    - n개의 단어가 주어지면 nxn짜리 attention map이 필요하다.
    - Sequence가 길어질수록 처리에 한계가 생긴다.

---

** Multi-headed attention(MHA)** : allow Transformer to focus on differnet positions.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153192019-c62cc99b-b54a-4820-8533-802b2ae27c68.png" width=500></p>

- 서로 다른 head를 사용하여, attention head의 개수만큼의 encoded vector를 얻게 된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153192189-ba3f3223-88a7-4ac2-a95f-422250c50294.png" width=500></p>

- 서로 다른 encoded vector를 concatenate하여 model과 함께 train된 weight matrix를 곱해준다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153193310-df4fd1c1-ee96-403c-9c10-f0ee67d8de6a.png" width=500></p>

---

** 실제로 사용되는 Code는 MHA를 사용하는 방법이 다르다**

원래 주어진 embedding의 dimension이 100이라 하자. 10개의 head를 사용하게 된다면, 100 dimension을 10개로 나눈다.  
따라서, Q, K, V 벡터를 만드는 것은 10 dimension 입력만 가지고 돌아가게 된다.

---

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153198645-a3310501-6c6f-4d4b-b3d6-322ca635f494.png" width=500></p>

Positional Encoding을 Embedding에 더해줘야한다.

왜 **Positional Encoding**이 필요한가?  
self-attention의 동작 방식을 살펴보면, ABCD, BCDA, DCBA처럼 같은 word로 구성되었지만 순서가 다른 sequence에 대해서 똑같이 encoding한다. 즉, order에 independent하다. 따라서 positional encoding이 필요하다.

---

**Encoder는 Decoder에게 어떤 정보를 줄까?**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153199578-a70f74ee-a7cb-41e2-b701-eb49d056b90d.png" width=500></p>

- Topmost Encoder의 Key와 Value를 Decoder에게 전달하한다.
- Decoder에서 학습할 때, 미래의 정보를 활용하지 않기 위해 masking하여 이전 단어들에만 dependent하게 한다.
- 지금 Decoder에 있는 단어도 이전 generation 단얼 Query를 만들고 Key, Value는 Encoder에서 주어지는 vector를 사용한다. 
- 마지막 Layer는 단어들의 분포를 만들어서 단어 하나를 매번 sampling한다.

### Vision Transformer

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153216484-1de5e13e-458a-4f49-8fae-974272ccda33.png" width=500></p>

이미지들을 특정 영역으로 나누고 각각 영역에 있는 subpatch들을 linear layer를 통과시켜 하나의 입력인 것 처럼 활용한다. 물론, positional embedding이 들어간다. 

