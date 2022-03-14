# Instance segmentation
## What is instance segmentation?

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158098194-709c1484-62c2-4658-a152-2ab64886b52a.png" width = '70%'></p>

- 같은 물체의 class라도 instance가 다르면 구분, 즉 `Instace segmentation` = `Semantic segmentation` + `distinguish instances`
- 실제 응용 사례에 사용할 가능성 ↑
- 개체의 구분은 object detection을 통해서 가능, segmentation이 object detection을 기반으로 하고 있는 경우가 많다.

## Instance segmentaters
**Mask R-CNN** [논문 review](https://herbwood.tistory.com/20)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158099516-aa439727-9f91-410e-9e4e-90565eee7f26.png" width = '70%'></p>

- Faster RCNN과 거의 동일한 구조
  - Faster RCNN은 RPN에서 나온 bbox proposal을 이용하여 ROI pooling에 전달
  - Faster RCNN의 ROI pooling은 정수 좌표만을 지원한다.
- Mask R-CNN은 `ROI Align`이라는 새로운 pooling layer 제안
  - interpolation을 통한 정교한 (소수점 pixel level인) subpixel의 pooling을 지원
  - 정교한 feature extraction 가능
- Mask R-CNN = Faster R-CNN + `Mask branch`
  - 7x7에서 14x14로 Upsampling하며 channel dimension은 2048에서 256으로 줄인다.
  - 각 class별로 binary mask를 prediction한다.
  - 하나의 bounding box에 대해서 일괄적으로 모든 class에 대한 mask를 일단 생성하여, classification head에서의 prediction class를 이용하여 mask를 참조한다.

**Summary of the R-CNN family**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158099686-e0f26da6-ed0d-408d-b2ae-279f76229804.png" width = '100%'></p>

**YOLACT(You Only Look At CoefficienTs)** [논문 review](https://byeongjokim.github.io/posts/YOLACT,-Real-time-Instance-Segmentation/)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158101418-a3a822ef-4615-4c68-ae80-711e7404c811.png" width = '70%'></p>

- Real-Time의 sementic semgmentation이 가능한 single stage network
- backbone 구조는feature pyramid 구조를 가져와 사용 : 고해상도의 feature map을 가지고 사용 가능
- mask의 prototypes을 추출하여 사용
  - Mask R-CNN에서는 실제로 사용하지 않더라도 각각의 class를 고려하고 있다고 하면, bounding box마다의 각 class의 독립적인 mask를 한번에 생성한다
  - prototype은 mask는 아니지만 mask를 합성해낼 수 있는 기본적인 여러 물체의 soft segmentation component들이다.
  - mask를 span 가능한 basis
- prediction head에서 각 detection에 대한 prototype를 잘 합성하기 위한 coefficient들을 출력하여 계수들과 prototype의 선형 결합을 통해 각 detection에 적합한 mask response map을 생성한다.
- **ket point** : 효율적인 mask의 생성을 위해 prototype의 개수를 object(class)의 개수와 상관없이 작게 설정하는 대신에 그것의 선형 결합으로 다양한 mask를 생성할 수 있다.

**YolactEdge**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158102061-6ea42e58-ba9c-4087-b34c-df30a185d967.png" width = '100%'></p>

- real-time으로 동작할만큼 빠르지만 edge device에 올릴만큼 소형화 되어있지 않다. → YolactEdge
- 이전 frame 중에서 key frame에 해당하는 frame의 feature를 다음 frame에 전달하여 feature map의 계산량을 획기적으로 줄인다.

# Panoptic segmentation
## What is panoptic segmentation
**Semantic segmentation vs. Panoptic segmentation**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158104803-426f4340-5c31-4af3-a417-95a3cdd87558.png" width = '70%'></p>

- Semantic segmentation : 배경에는 관심이 없고 그저 움직이는 작은 물체에 대해서만 관심을 가진다.
- Panoptic segmentation : 배경 정보 뿐만 아니라 관심을 가질만한 물체들의 instance까지 구분해서 segmentation

**UPSNet**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158104908-8c1f3201-3a28-428b-8bd5-805573ce3e8a.png" width = '70%'></p>

- FPN 구조를 사용하여 고해상도의 feature map을 추출한다.
- Semantic Head : Fully convolution 구조로 semantic map을 prediction
- Instance Head : Class classification, Box Regressor, Mask branch
- Panoptic Head : 하나의 segmentation map으로 출력

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158105184-738a4cbd-9c4b-4426-a972-7c3884fd2d5f.png" width = '70%'></p>

- `Y_i` : Instance에 해당하는 mask
- `X_thing`, `X_stuff` : 각 물체들과 배경을 예측하는 mask

배경을 나타내는 mask response는 최종 출력으로 바로 들어간다. 또한 각 insance를 bounding box 형태가 아닌 전체 영상에 해당하는 위치에 다시 넣으면서 보강하기 위해서 semantic head의 물체 부분을 masking해서 instance response와 더해 최종 출력에 삽입한다. 여기서, Instance head의 출력이 실제 물질 크기와 일치한다고 하면 전체 영역에서 어디에 위치해야하는지를 조정(resize, pad)해서 넣어주게 된다. instance와 배경에 관련된 물체 이외에 소속되지 않는 unknown-class의 물체들을 고려하기 위해서 물체의 semantic mask map에 instance로 사용된 부분들을 제외해서 모두 unknown class로 합쳐서 한 channel로 추가한다.

**VPSNet (for video)**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158107225-9911e81d-77af-41e1-8f9c-2520eb2c131c.png" width = '70%'></p>

1. reference feature을 target feature map에 pixel level로 맞춘다.
  - 시간 차이를 가지는 두 영상 사이의 pie라는 motion map을 사용해서 각 frame에서 나온 feature map을 motion에 따라서 warping을 해준다. 즉, motion map이라는 것은 두 영상이 있다면 한 영상의 모든 pixel들에 대해서 다음 영상에 point가 어디로 가는지 대응 관계를 가지고 있는 motion을 나타내는 map이다.
  - reference frame에서 추출된 feature를 Target frame에 따라서 feature들을 옮겨(tracking) Target frame에서 찍힌 feature와 합쳐 사용한다.
  - 현재 frame에서 추출된 feature만으로 더 높은 detection 성공률이 얻어진다. 여러 frame의 feature를 합쳐 시간 연속적으로 smooth한 segmentation이 가능해진다.
2. 서로 다른 object instance를 연관짓는다.
- VPN을 통해 ROI들의 feature를 추출해서 tracing head를 통해 기존 ROI들과 현재 ROI들이 어떻게 연관되어있는지, 이전에 몇번 ID를 가졌던 물체였는지를 찾아 연관성을 만들어진다.
- tracking되지 않은 것들은 새로운 ID를 제공한다.
3. Fused-and-tracked modules are trained to synergize each other

# Landmark localization
## What is landmark localization

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158108141-e0b00dee-1e97-4e15-9a9b-b2553c0f3ecf.png" width = '60%'></p>

- 사람의 얼굴이나 pose를 추정하고 tracking하는 데에 사용
- 특정 물체에 대해서 중요하다고 생각하는 특징 부분들 land mark를 정의하여 추정하고 tracking하는 것을 lanmark localization이라 한다.

## Coordinate regression vs. heatmap classification

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158108573-4d41921d-26aa-4ae6-b29b-32fab58f7aae.png" width = '70%'></p>

- `coordinate regreesion` : 각 point의 x, y 위치를 2 dimension으로 예측
  - 부정확하고 일반화의 문제가 생긴다.
- `heatmap classification` : semantic segmentation처럼 한 channel들이 key point를 담당하고, 각 key point마다 하나의 class로 생각해서 key point가 발생할 확률 map을 각 pixel별로 classification하는 방법으로 대신 해결
  - 모든 pixel에 대해서 판별해야하므로 계산량이 많다.

**Landmark location to Gaussian heatmap**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158109536-7d554ed4-322b-4801-b0e0-11373325d77a.png" width = '30%'></p>

```python
size = 6 * sigma + 1 # 영상 크기
x = np.arange(0, size, 1, float)
y = x[:, np.mewaxis]
x0 = y0 = size // 2
if type == 'Gaussian' : 
  g = np.exp(-((x - x0) ** 2 + (y - y0) ** 2) / (2 * sigma ** 2))
elif type == 'Cauchy' : 
  g = sigma / (((x - x0) ** 2 + (y - y0) ** 2 + sigma ** 2) ** 1.5)
```

## Hourglass network

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158110051-59e36746-3b8d-40d5-b47a-d5cb75bf43ba.png" width = '70%'></p>

- UNet과 비슷학 구조를 여러개 쌓았다.
- 모래시계처럼 생겼다고 해서 `Stacked hourglass module`이라 불린다.
- Why stacked hourglass module? 
  - 영상 전체 작게 만들어 receptive field를 키워 영상 전반적인 큰 그림을 보고 land mark를 찾는 것이 좋겠다고 생각했다.
  - receptive field를 크게 가져가 큰 영역을 보면서도 skip connection을 통해 low level feature를 참고해서 정확한 위치를 참고하도록 유도
  - 한번에 하는 것보다 여러번 거쳐 점점 더 큰 그림과 detail을 함께 구체화해나가며 결과를 개선해나간다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158110137-b8391e04-440c-4cd7-b3b5-686b720e37c1.png" width = '70%'></p>

Unet과의 다른 점은 skip connection에서 plus 연산을 통해서 합쳐 dimension이 늘지 않는다. 또한 한번의 Conv layer를 통과해 전달된다.

## Extensions
**DensePose**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158110823-0787ae90-d715-4c15-a3e2-e56e22a9faae.png" width = '70%'></p>

- 신체 모든 부위의 land mark 위치를 알게되면 3D를 알게되는 것과 같다.
- 우측의 표현을 UV map 표현이라 한다.

> **UV map**
> 
> <img src="https://user-images.githubusercontent.com/57162812/158110920-9d646703-b88c-4f61-9504-deeadc084fb2.png" width = '40%'>
> - 표준 3D 모델의 각 부위를 2D로 펼쳐 이미지 형태로 만들어 놓은 좌표 표기법이다.
> - UV map에서의 한 점은 3D mash의 한 점과 1:1로 matching
> - 각 point와 triangle들이 고유의 ID를 갖기 때문에 1:1 matching이 되는 것인데, 이 그래프에서 3D mash가 움직여도 tracking을 통해 보존된다. 즉, UV map과 3D mash의 관계는 변하지 않는다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158111745-238f53aa-0f91-4802-83e8-f015386636b9.png" width = "70%"></p>

- DensePose R-CNN = Faster R-CNN + `3D surface regression branch`

**ReinaFace**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158112006-13e6449d-d933-4ab6-a001-6161e098395f.png" width = "70%"></p>

# Detecting objects as keypoints
## CornerNEt & CenterNet
**CornerNet**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158112603-20ec5257-8f16-455a-b038-3da59bdc3dd8.png" width = "70%"></p>

- Bounding box = {Top-left, Bottom-right} corners
- backbone network에서 나온 feature map을 heatmap 표현을 통해 두 점을 detection하고, embedding이라는 통해 각 point가 가지는 정보를 표현하는 head을 두어, 학습시 두 corner에 대해서 나온 embedding point는 서로 같아야한다는 조건을 걸어 학습을 한다.
- single stage detection과 가까워 속도가 빠르다.

**CenterNet(1)**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158112901-c731cd92-e813-4619-a471-130d6de18ee1.png" width = "70%"></p>

- Bounding box = {Top-left, Bottom-right, Center} points

**CenterNet(2)**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158112947-b3d558c6-f4df-4e4c-a7e0-9d08b67fe98b.png" width = "70%"></p>

- Boudning box의 정보의 촤소화
- Bounding box = {Width, Hegiht, Center}


# Further Question 

(1) Mask R-CNN과 Faster R-CNN은 어떤 차이점이 있을까요? (ex. 풀고자 하는 task, 네트워크 구성 등)

(2) Panoptic segmentation과 instance segmentation은 어떤 차이점이 있을까요?

(3) Landmark localization은 human pose estimation 이외의 어떤 도메인에 적용될 수 있을까요?
