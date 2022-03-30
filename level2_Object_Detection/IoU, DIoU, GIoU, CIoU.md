# IoU, GIoU, DIoU, CIoU

- `IoU` : 교집합 / 합집합
- `GIoU` : 두 박스를 모두 포함하는 최소 영역인 C 박스 활용
- `DIoU` : IoU와 중심점 좌표 함께 고려
- `CIoU` : DIoU와 geometric measure 함께 고려

## 1. IoU (Intersection over Union)
Predict bbox와 Ground Truth가 일치하는 정도를 0과 1 사이의 값으로 나타낸 값이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/160808396-bb43de49-cfdf-4fa3-ae85-a0a46a027b48.png" width ="30%"></p>

> 만약 IoU를 활용한 loss가 아닌 단순히 bbox의 좌표값으로 loss를 측정하면 어떻게 될까?
> <p align='center'><img src="https://giou.stanford.edu/_nuxt/img/f42a6d1.jpg" width ="50%"></p>
> 
> 사실상 왼쪽 그림과 오른쪽 그림을 비교해보았을 때, 오른쪽의 bbox가 object를 더 많이 포함하고 있을 것이다. 왼쪽 하단 거리와 오른쪽 상단의 거리가 동일할 때 MSE는 일정하다. 반면, box의 겹침 정도를 나타내는 IoU의 값은 다르다. 
>
> **Object Detection에서 단순히 box의 좌표 차이를 통해 loss를 구하는 것보다 IoU를 loss에 활용하는 것이 Regression loss에 더 적합할 수 있다.**


<p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbKsePv%2FbtrasUjk16H%2FgSC4SPpDicayWKTS2jqJmk%2Fimg.png" width ="70%"></p>

`IoU loss = 1 - IoU`

하지만, 세번째 예시처럼 두 박스가 겹치지 않을 때, 어느 정도의 오차로 교집합이 생기지 않는 것인지 알 수 없어 gradient vanishing 문제가 발생한다. 이를 해결하기 위한 방법이 `GIoU`이다.

## 2. GIoU (Generalized-IoU)

bbox와 ground truth를 모두 포함하는 최소 크기의 C 박스를 활용한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/160811466-976da00c-41ff-4809-81e8-64b8f4322040.png" width ="70%"></p>

C box는 A box와 B box를 모두 포함하는 가장 작은 box이고, C \ (A∪B)는 C box 영역에서 A box와 B box의 합집합을 뺀 영역이다. 기존 IoU의 값에서 C box 중 A와 B ㅁ도ㅜ와 겹치지 않는 영역의 비율을 뺀 값이 GIoU가 된다. 즉, GIoU가 클수록 좋은 prediction이 된다.

<p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcbfOcv%2FbtrazLzN8tV%2FKLKbW8mxBbzEhaeOebukM0%2Fimg.png" width ="70%"></p>

`GIoU loss = 1 - GIoU`

하지만, iteration에 따른 GIoU Loss의 bounding box 예측 과정을 보면 GT와 overlap을 위해 bbos 영역이 넓어지고, overlap된 후 IoU를 높이기 위해 bbox 영역을 줄이는 방식으로 수행된다. 이를 통해서 겹치지 않는 박스에 대한 gradient vanishing 문제는 개선했지만, 수렴 속도가 느리고 부정확하게 박스를 예측한다는 문제점이 존재한다. : horizontal과 vertical 정보 표현 무

이를 해결하기 위한 방법이 `DIoU`이다.

## 3. DIoU (Distance-IoU)

IoU와 중심좌표를 함께 활용한다.

<p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKBn08%2FbtraFFE4NPh%2FRQF9Ht0l8zkslKsb8BRYAK%2Fimg.png" width ="70%"></p>

겹쳐진 영역의 크기가 동일하고 bbox의 위치만 달라졌을 경우, IoU, GIoU는 bbox의 위치를 고려하지 않아 loss값이 변하지 않지만, 중심좌표를 활용하는 DIoU는 해당 좌표가 변함에 따라 loss값도 변하는 것을 확인할 수 있다.

<p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbHRLHI%2FbtraFE0tTYA%2FWsFEd4j0yH9Cv3lKtcSNhk%2Fimg.png" width ="70%"></p>

iteration에 따른 DIoU Loss의 bounding box 예측 과정을 보면, GT와 overlatp을 위해서 bbox 영역을 넓히는 GIoU와 달리 DIoUs느 중심 좌표를 비교하여 bbox 자체가 GT 쪽으로 이동하는 것을 확인할 수 있다.

<p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FoWUGH%2Fbtrav7Dq6WM%2FR12KmMK6LjxiPpZkw4GgLk%2Fimg.png" width ="70%"></p>

object detection에서 DIoU Loss를 사용하는 경우, 두 box가 겹치지 않았을 때, GIoU처럼 영역을 넓히지 않고 중심 좌표를 통해 박스의 거리 차이를 최소화함으로써 수렴 속도를 향상시켰다.

# 4. CIoU(Complete-IOU)

bbox에 대한 좋은 loss는 overlap area, central point distance, aspect ratio 세 요소를 고려한 것이라고 한다. 따라서, overlap area와 central point distance를 고려한느 DIoU에 추가적으로 aspect ratio를 고려하는 CIoU를 제안한다.


![image](https://user-images.githubusercontent.com/57162812/160824430-180dc50e-490f-4927-b31c-132b1da9584f.png)

![image](https://user-images.githubusercontent.com/57162812/160824466-940575d6-154c-448f-9ead-396c6b9d9747.png)

이때, v는 두 box의 ascpect ration의 일치성을 측정하는 역할이고, α는 positive trade-off parameter로 non-overlapping case와 overlapping case의 형을 조정하는 역할을 한다. 











