# Visualizing CNN
## What is CNN visualization
**CNN is a black box**

1) What is inside CNN(black box)?
  - CNN은 여러 단계의 학습을 통해 정해진 weight들의 조합 : 복잡, 해석 어려움 → black box system
  - Visualization을 통해서 내부를 파악해보자
2) Why do they perform so well
3) How would they be improved

∴ Neural Network을 Visualization = Debugging tool을 갖는다 = 안에 무엇이 들어있나?, 왜 좋은 성능이 나오는가?, 언제 실패를 하는가?, 어떤 개선이 필요한가?를 알 수 있는 단서들 제공

**ZFNet example : the winner of ImageNet Challenge 2013**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157572711-c94dc20a-760d-45fd-9f31-98493b5be821.png" width="80%"></p>

- CNN layer들이 각 위치에 따라서 어떤 지식을 배웠는지를 convolution의 역연산인 deconvolution을 이용하여 visualization
- low level에서는 방향성이 있는 선을 찾는 filter 혹은 동그란 block을 찾는 기본적인 영상 처리 filter처럼 생긴 것들이 분포
- 높은 계층으로 갈수록 의미가 있는 표현을 학습했다.

## Vanilla example : filter visualization

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157573350-1bcd9326-b162-475d-a8cf-312bd8f38609.png" width="70%"></p>

- AlexNet의 첫번째 layer의 Conv filter : 11x11 size with 3 channels → color image 형태 출력 가능
  - 영상 처리 filter와 같은 color edge detector, 각도 detector, block detector와 같은 다양한 기본적 operation 학습이 된 것을 알 수 있다.
  - 입력에 Convolution을 취한 Activation map에서는 각 filter마다 처리가 하나의 channel로 나오기 때문에 흑백으로 표현
- 왜 두번째 혹은 높은 계층의 layer는 이렇게 해석하지 않을까?
  - 뒤쪽 layer는 filter 자체의 차원수가 높다. : 3 channel의 컬러로 image visualization 가능한 형태가 아니다. 즉, 3 초과의 channel 수 → 사람의 직관적인 해석이 힘들다. 추상적!!
  - Nueral Network를 해석하기 위해서는 조금더 복잡한 방법이 필요

## Ho wto visualize nueral network

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157574210-8b16d191-48e6-4b36-919c-b772366170da.png" width="70%"></p>

모델 자체의 특성을 분석하는데에 강점 vs. 하나의 입력 데이터에서부터 모델이 어떤 결론을 내었을 때 결론의 이유를 분석하는 방법

# Analysis of model behaviors
## Embedding feature analysis 1
**Nearest Neighbors(NN) in a feature space - Example**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157574586-70080113-c598-44ff-882a-1304dcd024a6.png" width="70%"></p>

- DataBase 내의 분석을 위한 예제 Dataset을 많이 저장해 놓는다.
  - 위의 그림들이 DB에 저장되어있던 Dataset sample들이다.
- Query Image가 들어오게 되면 비슷한(이웃하는) 영상들을 찾기 위해 DB 내에서 검색을 한다.
- 유사한 이미지들을 거리에 따라서 정렬하게 된다. Top-6 Neighbors in the feature space
- 해석의 여지가 주어진다.
  - 의미론적으로 비슷한 concept들이 clustering 되어 있다.
  - 질의 영상이 들어왔을 때, pixel별 비교를 통해 영상 검증도 가능하다. → 위치가 다르거나 다른 pose의 경우 찾지 못할 수 있다.
- 학습된 feature가 물체의 위치 변화에 가능하면서 concept를 잘 학습했다는 것을 알 수 있다.

**Nearest Neighbors in a feature space**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157575342-dec7b90c-87d1-4e5a-bf5a-2f9b8788e278.png" width="70%"></p>

- 고차원 공간의 embedding feature vector들 : 각각의 vector들에 해당하는 영상들이 존재한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157575891-b65be9b6-ebf4-4349-b86d-500cd1879698.png" width="70%"></p>

- 실제 구현에서는 미리 학습된 Neural Network를 준비한다.
- 제일 뒤쪽의 특징을 추출할 수 있도록 fc layer를 제거한다. : query 영상을 넣어주면 고차원 공간에 존재하는 특징이 추출된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157575992-ac9e98d8-a3d6-4c5f-a384-6faac0cb3e14.png" width="70%"></p>

DB의 모든 Image들에 대해 특징을 뽑아놓아 DB에 저장한다. : feature들은 원래의 영상들과 연결이 되어있을 것이다. : 각 위치의 특징들을 해당하는 영상들이 존재하는 형태이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157576315-8f700ec6-824f-4a79-ba77-d02086cf39fb.png" width="70%"></p>

Query Image들을 넣게 되면 특징을 뽑게 되고, 특징과 거리가 가까운 영상들을 찾아서 return을 해주면 embedding vector를 통해서 주변 예제를 분석할수 있게 된다.

근처의 feature vector들이 있고 근처에 있다는 사실을 알기 떄문에  original DB에서 근접한 Image들과 연관된 이미지들을 찾아서 가져오게 된다.

- 검색된 예제를 통해서 분석하는 방법은 전체적인 그림을 파악하기 어려운 단점이 있다.

## Embedding feature analysis 2
**Dimensionality Reduction**

- backbone network를 활요해 feature를 추출하게 되면 굉장히 고차원의 vector가 나와 해석과 상상이 힘들다.
- 하지만 3차원까지는 상상하기 쉽다.
- 따라서, 고차원 space의 분포들을 차원 축소를 통해 쉽게 확인 가능한 분포를 얻어낸다.

1) t-distributed stochastic neighbor embedding(t-SNE)
  - Manifold 알고리즘 중 하나
  - 탐색적 데이터 분석에 유용
  - IDEA : 데이터 포인트를 2차원에 무작위로 표현한 후 원본 특성 공간에서 가까운 포인트는 가깝게, 멀리 떨어진 포인트는 멀어지게 만드는 것
  - 이웃 데이터 포인트에 대한 정보를 보전
  > **Manifold**
  >
  > - 데이터가 있을 때,고차원 데이터를 데이터 공간에 뿌리면 sample들을 잘 아우르는 subspace가 있을 것이라는 가정에서 학습을 진행하는 방법
  > - manifold를 통해 차원 축소가 가능하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157584004-b0693226-42a4-417b-988d-795b188784ce.png" width="40%"></p>

## Activation Investigation 1

**Layer activation** : Behaviors of mid-level to high-level hidden units

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157584750-2b72391d-828b-435b-b0e0-32d9abd7f77d.png" width="40%"></p>

- Layer의 activation을 분석함으로써 모델의 특성을 파악하는 방법
- AlexNet의 Conv5 layer의 138번째 channel의 activation을 적당한 값으로 thresholding 후 mask를 만들어 영상에 overlay를 해본 결과 : 위의 두 그림과 같다.
- 각 activation의 channel들을 hidden node라 할 수 있다. : 이 channel은 얼굴을 찾는 node구나!! : 해석적
- CNN은 hidden unit들이 간단한 detection들을 다층으로 쌓고 조합을 통해 물체를 인식한다고 해석할 수 있다.


## Activation Investigation 2
**Maximal activatin patches** : Example

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157585045-910a542d-cf15-462b-9aaf-8cd4439ab2ec.png" width="40%"></p>

- patch를 뜯어서 사용하는 방법
- hidden node에서 가장 높은 값을 가지는 근방의 patch를 뜯는다.
- 중간 계층을 분석하는 데에 더 적합하다. (why) 큰 그림을 보기보다 일부를 본다.

**Maximal activation patches** - patch acquisition

1) 분석하고자 하는 특정 layer를 정한다. (Conv5 layer의 256개의 channel 중 14번째 channel)
2) 예제 data를 backbone network에 넣어 각 layer의 activation을 뽑아 원하는 layer의 chnanel의 activation을 저장한다.
3) 저장된 channel에서 가장 큰 값을 갖는 위치를 파악해 입력 domain의 maximum 값을 도출해낸 receptive field를 계산하여 receptive field에 대한 해당 영상의 patch를 뜯어온다.

## Activation Investigation 3
**Class visualization** : Example

예제 data를 사용하지 않고 network가 기억하고 있는 이미지가 무엇인지 분석하는 방법!! 예를 들어, 각 class를 판단할 때 network가 상상하는 모습을 확인하는 방법

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157586042-2b44d596-82ef-42a4-9ac2-98d54b39c8b8.png" width="40%"></p>

해석
- 모델은 새로운 것을 판단하기 위해 해당 물체뿐만 아니라 주변 상황까지 찾고 있다.
- 학습에 사용된 dataset이 bias가 되어있는 부분도 파악 가능하다. 순수한 해당 물체만 들어있는 data만을 가지고 학습한 것이 아니라는 것을 알 수 있다.

**Class visualization** : Gradient Ascent

<img src="https://user-images.githubusercontent.com/57162812/157586526-9c240d92-0ef9-44ef-9279-c1aef2b7143e.png" width="30%">

- I : 영상 입력
- f : CNN model

1) 임의의 영상(black or random initial)을 CNN의 모델에 넣어주어 target class에 대한 prediction score를 추출한다.
2) Backpropagtion을 통해 입력단의 gradient를 구한다.
  - 입력이 어떻게 바뀌어야 target class의 score가 높아지는지를 찾는다.
  - target score가 높아지는 방향으로 input image 업데이트 : gradient를 더해준다.
  - loss를 측정할 때, 마이너스를 붙어 내려가는 방향으로 만들어, gradient를 계산하면 Gradient Descent 방식을 그대로 활용 가능해진다.
3) 다시 위의 과정을 update image에 대해 반복해준다.

입력 영상은 어떤 이미지여도 상관없지만 gradient descent는 현재 영상에서 어떻게 업데이트 할지 local search를 하기 때문에 그 입력에 대해서 적절하게 바뀐 영상이 나오게 된다. 즉, 초기값에 따라 다양한 결과를 얻을 수 있다. 

# Model decision explanation
## Saliency test 1

영상이 주어졌을 때, 그 영상이 제대로 판정되기 위한 각 영역의 중요도를 추출하는 방법

**Occlution map**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157588908-3bbf59bd-4864-48d5-8ad3-63ad259a522c.png" width="60%"></p>

큰 Patch를 이용해 Occlusion으로 가려 이미지를 넣어주었을 때, target class에 대한 CNN score
- 어떤 위치를 Patch로 가려주냐에 따라 score가 바뀌게 된다.
- 물체의 중요한 부분을 가리면 score가 떨어지며, 물체와 관련 없는 부분을 가리면 score에 영향을 주지 않는다.
- 위치에 따라서 변하는 socre를 heatmap으로 나타낸다.

## Saliency test 2

**via Backpropagation** : Example

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157589161-37b2a83e-038b-4bc8-a658-0a2e2ea62329.png" width="25%"></p>

특정 image를 classification하여 최종 결론이 나온 class에 결정적인 영향을 미친 부분이 어디인지 heatmap으로 나타내는 기법

**via Backpropagation** : Derivatives of a class score w.r.t input domain

1) 입력 영상을 넣어 하나의 class score를 얻는다.
2) Backpropagation을 입력 domain까지 진행한다.
3) 얻어진 gradient를 절댓값 혹은 제곱값을 취해 visualization
  - 왜 절댓값 혹은 제곲을 취할까?
    - gradient의 크기가 입력 부분에 대해서 많이 변해야하는지에 대한 정보를 담고 있어서 민감한 영역으로 부호보다는 절대적인 크기를 중요하게 생각하기 때문이다.

Gradient Ascent를 통한 Class Visualization과의 차이는?
- 입력으로 의미 없는 random image를 넣어준 반면, 현재 data가 어떻게 해석되는지를 보여준다.

## Backpropagation-based saliency
**Rectified unit(backward pass)**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157589868-f3d0fb03-6cd7-4b47-bf57-173ed3d7ef03.png" width="78%"></p>

기존
1) ReLU를 사용할 때, forward pass에서 음수가 나온 부분은 0으로 masking된다.
2) backpropagation을 할 때, 양수와 음수가 합쳐진 gradient가 오면 음수 마스크로 저장되어있던 pattern mask로 masking을 해준다.

Deconvolution
1) backward 연산 시에 ReLU를 적용한다

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157590594-fcff5888-786c-464e-9dcc-0b8ef8f658ff.png" width="78%"></p>

**Guided backpropagtion**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157590659-9757c130-401b-45e4-86cc-1a1de9c2d8a4.png" width="70%"></p>

**Comparision**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157590816-333193cf-1ea6-48f9-913a-c85b68a209f7.png" width="70%"></p>

## Class activation mapping
**Class activation mapping(CAM)** : Example

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157591355-960d80d9-8aa0-4052-90b1-487d3d4f06da.png" width="70%"></p>

어떤 부분을 참조해서 결과가 나왔는지 heatmap 형태로 표현한다. thresholding을 통해 bbox까지도 가능하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157591343-2e61d1d7-5ec2-4d74-943d-e3ffb566d1db.png" width="70%"></p>

Nueral Net의 일부 개조
- Conv part의 마지막 layer에서 나온 feature map을 fc layer에 바로 통과시키지 않고 GAP(global averaging pooling)을 하도록 바꿔준다.
- 그 후 fc layer를 한번만 통과 시켜준다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157591967-eee74238-ede0-4eeb-985b-4e18f5d178ff.png" width="50%"></p>

단점
- architecture를 바꿔서 re-training

**Grad-CAM** : Example

- architecture 변경 없이 사용 가능

**SCOUTER** : Example

- 왜 해당 class가 맞는지 부터 왜 다른 class가 아닌지까지 검출해낼 수 있다.




