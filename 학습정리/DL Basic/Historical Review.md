## Introduction
- 좋은 deep learner로 만드는 것은?
  - 구현 실력
  - 수학 실력(특히, 선형대수 및 확률론)
  - 최신의 논문을 많이 아는 것
---
- Artificial Intelligence : 사람의 지능 모방
- Machine Learning : 데이터를 통해 학습
- Deep Learning :  Neural Network라는 구조를 활용하여 데이터를 통해 학습

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152758427-ed9a8ea5-56ba-48c4-a378-3afd031e3483.png" width=300></p>

∴Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence

---
- Deep Learning의 구성 요소
  - data : 모델이 학습할 수 있도록 하는 요소
  - model : 데이터를 레이블로 변형
  - loss function : 모델의 badness를 측정 ex) regression-L2norm, classification-Cross Entropy Loss
  - algorithm : Loss를 최소화하는 parameter를 맞추다 ex) Adam

1. Data

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152758839-cf5525c2-da4a-47d3-9fbe-64d979d8c24b.png" width=400></p>

- Classification
- Semantic Segmentation : Dense classification으로 이미지의 pixel별로 분류
- Detection : image에 대한 bounding box 분류
- Pose Estimation : 2차원, 3차원의 skeleton
- Visual QnA : 질문에 대한 답

2. Model

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152759220-91ce5c24-5c38-4224-8383-82b773dd0420.png" width=400></p>

3. Loss : proxy of what we want to achieve

-  loss function이 줄어든다 해서 우리가 원하는 것을 반드시 이루는 것은 아니다.
  - ex) noise가 많은 데이터에 대한 Regression : MSE의 경우 error가 큰 경우 제곱이 전체적인 network 학습을 줄이게 된다. 따라서 MSE 대신의 L1-norm 또는 Robust minimization과 같은 적절한 대안이 필요하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152759743-1a81c257-7aa9-4917-9c78-57fa2ee5d39e.png" width=400></p>

3. Optimization Alogrithm

![Gradient Descent](https://user-images.githubusercontent.com/57162812/152761666-8fd80c0f-3c5d-4bac-a143-5114b26fdc18.gif)

- Dropout
- Early stopping
- k-fold validation
- Weight decay
- Batch normalization
- MixUp
- Ensemble
- Bayesian Optimization

## Historical Review
- 2012 : AlexNet
- 2013 : DQN
- 2014 : Encoder/Edcoder, Adam
- 2015 : GAN, ResNet
- 2017 : Transformer
- 2018 : Bert
- 2019 : Big Language Models(GPT-X)
- 2020 : Self-Supervised Learning
