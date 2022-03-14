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

# Further Question

(1) Mask R-CNN과 Faster R-CNN은 어떤 차이점이 있을까요? (ex. 풀고자 하는 task, 네트워크 구성 등)

(2) Panoptic segmentation과 instance segmentation은 어떤 차이점이 있을까요?

(3) Landmark localization은 human pose estimation 이외의 어떤 도메인에 적용될 수 있을까요?
