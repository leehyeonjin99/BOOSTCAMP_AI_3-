# Object Detection
## Task
1. Classification
2. Object Detection
    - 이미지 속 객체의 위치와 class를 구분해는 task
    - 이미지 안에서 정답이 여러가지일 수 있다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159198522-05491931-ed00-44d7-9142-834ee441e725.png" width='20%'></p>

3. Semantic Segmentation : 이미지의 객체의 영역을 구분하는 task. 단, 같은 class는 구분하지 않는다.  
4. Instance Segmentation : 같은 class의 객체를 구분하여 영역을 구분한다.
## Real World
- 자율 주행
  - Tesla의 자율주행  자동차는 완전한 camera 기반의 객체 검출을 이뤄낼 것이라 하였다.
- OCR task
  - 사진 속에서의 글을 검출
- 의료
- CCTV

## History

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159198921-a0ed0ee6-dfdf-4b69-91ce-e4f9fd175a85.png" width='60%'></p>

## Evaluation
1. 성능
    - mAP
2. 속도
    - FPS
    - Flops
### mAP (mean average precision)
- 각 class 당 AP의 평균
> **Confusion matrix**
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159199067-bbb77dc0-37b2-4eef-8e0a-de62fa8bc8ab.png" width='60%'></p>

> **Precision**
> - model 관점
> - positive로 예측한 대상 중 실제로 positive인 대상의 비율
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159199230-5dc28557-4953-49c7-959f-89c39e5dc301.png" width='40%'></p>

> **Recall**
> - 정답 관점
> - positive case 중에서 model이 positive로 예측한 case의 비율
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159199366-b7caff56-f1ff-4289-8ec3-fcd13479f4bc.png" width='40%'></p>

> **Example**
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159199560-ed822234-8ea2-4e35-8ef2-bc7011098158.png" width='40%'></p>
> 
> - Precision
>   - 8개의 검출, 그 중 4개가 옳은 검출
>   - 4/8 = 0.5
> - Recall
>   - 5개의 GT, 그 중 4개 검출
>   - 4/5 = 0.8 

> **PR Curve**
> - Ground Truth : 10개의 객체
> - Predict : 10개의 객체
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159199716-ae16fd3c-8350-4f29-b265-0119f2debc3d.png" width='80%'></p>
>
> confidence 기준 내림차순으로 정렬한다.
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159199813-7c18b8a6-cfc2-4b6d-bdc6-bcb0b061b8db.png" width='80%'></p>
> - 누적 TP, 누적 FP 계산으로부터 Precision, Recall 예측
> - (Recall, Precision)의 쌍으로 PR curve를 그려줄 수 있다.
> <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159200156-536a86fa-f6f2-4e21-8bad-045d56222f27.png" width='50%'></p>

> **AP**
> - PR curve에서 선을 긋고 아래 면적을 구할 수 있다.
> <img src="https://user-images.githubusercontent.com/57162812/159200351-ed0606cc-53a6-4524-90ff-17b69a2e8d81.png" width="40%">
> <img src="https://user-images.githubusercontent.com/57162812/159200360-7700a101-aaa7-4829-a8ff-aac4094628eb.png" width="40%">

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159200520-27d7d7b9-9af7-4233-bf58-c306165f5439.png" width="20%"></p>

### IOU(Intersection Over Union)
- detection task에서 postive/ negative 기준?
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159200696-738effc4-18cd-4c3f-9c87-e0e83da202b9.png" width="40%"></p>
  
### FPS (Frame Per Second)
- 초당 처리하는 frame의 개수
  - 클수록 model의 속도가 빠르다.

### FLOPs(Floating Point Operation)
- Model이 얼마나 빠르게 동작하는지 측정하는 metric
- 연산량 횟수
  - 작을수록 빠른 model

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159200982-1139a3f4-8c61-44f6-b4a6-5f71e73d557e.png" width="80%"></p>

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159200994-b11c2502-375c-479c-aae0-b2839bbe81f4.png" width="80%"></p>

## Library
1. **MMDetection**
    - pytorch 기반의 object detection 오픈 소스
2. **Detectorn2**
    - pytorch 기반 object detection과 segmentation의 알고리즘 제공
3. **YOLOv5**
    - coco dataset으로 사전 학습 모델
    - Object Detection 모델
4. **EfficientDet**
    - EfficientNet을 응용해 만든 Object Detection 모델
