# DBNet
Real-tim Scene Text Detection with Differentiable Binarization
## Introduction
**Segmentation 기반의 방법**

- 👍🏻 good : 다양한 모양의 텍스트를 유연하게 잡아낸다.  
- 👎🏻 bad : 인접한 개체 구분이 어렵다.

<p align='center'><img width="594" alt="image" src="https://user-images.githubusercontent.com/57162812/163914806-f8a997fb-b23f-4346-8706-ce14b2eca8a0.png"></p>

**Pixel Embedding**
- 글자 영역별로 같은 영역 내의 화소끼르는 가깝게, 다른 영역의 화소끼리는 멀게 pixel embedding을 학습시켜, 글자 영역을 결정짓기 위한 후처리 작업에 pixel embedding 정보를 기반으로 clustering 기법 사용

<p align='center'><img width="528" alt="image" src="https://user-images.githubusercontent.com/57162812/163915998-2e0e9a54-2a2c-4d76-8c07-3b8512c249f1.png"></p>

- 네트워크의 출력 : `글자 영역` + `글자 영역의 중심` + `Pixel Embedding`

<p align='center'><img width="637" alt="image" src="https://user-images.githubusercontent.com/57162812/163916351-a6b9ca67-42f1-4ae9-8f96-28aeb9abd78f.png"></p>

**Progressive Scale Expansion(PSENet)**

- 반복적으로 글자 영역 중심으로 줄여나가, text의 center line에 가까운 영역을 추정 

<p align='center'><img width="571" alt="image" src="https://user-images.githubusercontent.com/57162812/163916469-f14bf30d-8db9-48b6-9dde-56bb2152a6d2.png"></p>

- 작은 영역부터 글자 영역을 확정지은 뒤, 차례로 다음 map 정보를 활용하여 글자 정보를 키워나가고 구분하다.

<p align='center'><img width="636" alt="image" src="https://user-images.githubusercontent.com/57162812/163916908-9e26a2b0-eb9a-47d6-985f-e95a794d91e9.png"></p>

**DBNet**
- 💡IDEA : 글자 영역 구분에 threshold 갑을 이미지 별로 모델이 알아서 정하도록 하자.
- 모델 출력 : `각 pixel이 글자 영역에 속할 확률값` + `이미지에 각 pixel별로 적용하 임계치`
- 임계치 정답은 이렇게 나
