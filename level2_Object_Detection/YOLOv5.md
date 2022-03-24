## Conver2Yolo

- COCO dataset type과 YOLOv5 dataset type이 다르다. 따라서 변환해주어야 한다.
- 이때, 사용하는 library가 `Convert2Yolo`이다.

### 사용 방법

1. convert2Yolo를 다운받는다.
    ```python
    git clone https://github.com/ssaru/convert2Yolo
    ```
2. root folder인 convert2Yolo에 train folder 생성
3. class 종류를 정의하는 names.txt를 복사
4. command 실행하여 COCO data format json을 yolov5 label로 변환한 파일과 image path를 담고 있는 manifest 파일을 생성 각각 train/val 파일 생성
    ```python
    python3 example.py --datasets COCO --img_path /opt/ml/detection/dataset/train1 --label /opt/ml/detection/dataset/train.json --convert_output_path ./ --img_type ".jpg" --manifest_path ./ --cls_list_file names.txt
    ```
그렇다면, 다음과 같이 train folder에 label과 bounding box를 정의하는 txt 파일이 생성된다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159856733-6579e32e-251d-43cb-93d1-37e8836e3e43.png" width = "30%"></p>

> **0005.txt**
> 
> <p align="center"><img src="https://user-images.githubusercontent.com/57162812/159856887-9bf95617-514f-443c-a17a-53fc66967deb.png" width="20%"></p>

## Yolov5
<p align="center"><img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/splash.jpg" width="50%"></p>

### 사용 방법
1. Yolov5를 다운받는다.
    ```python
    git clone https://github.com/open-mmlab/mmdetection.git
    ```
2. Yolov5에 image, label 파일들을 생성해준 후, convert2Yolo로 생성해준 txt 파일과 image 파일을 넣어준다.
    - dataset/train/images
    - dataset/train/labels
    - dataset/val/images
    - dataset/val/labels
3. yolov5/data에 custom_data.yaml을 생성해준다. (data 경로 설정 및 class_num 설정)
    ```yaml
    # cutom_data.yaml
    train: /opt/ml/detection/yolov5/dataset/train
    val: /opt/ml/detection/yolov5/dataset/val

    nc: 10
    names: ['General trash', 'Paper', 'Paper pack', 'Metal', 'Glass', 'Plastic', 'Styrofoam', 'Plastic bag', 'Battery', Clothing]
    ```
    
4. yolov5 folder로 directory를 설정 후, train.py를 실행시킨다.
      ```python
       python train.py --data ./data/custom_data.yaml --cfg ./models/yolov5x.yaml --weight yolov5x.pt --batch 16 --workers 4 --epochs 100 --name yolov5x_100
       ```
       - data : custom_data 경로
       - cfg : 사용할 모델 : yolov5/models에서 확인 가능
       - weight : 사용할 모델의 pretained weight

### inference
```python
python detect.py --source /opt/ml/detection/dataset/test --weight {model 저장 경로} --save-txt  --save-conf
```
### 출처
- [object-detection-level2-cv-10](https://github.com/boostcampaitech2/object-detection-level2-cv-10/tree/main/yolov5)
- [YOLOv5 in PyTorch - Train Custom Data 따라하기](https://www.youtube.com/watch?v=y3FkRXZqE2s)
- [[YOLOv5] train + inference 자세하게 알아보자](https://danny0628.tistory.com/65)

# Cross Validation

# Ensemble
[Model Ensemble Tutorial](https://github.com/ultralytics/yolov5/issues/318)

```python
python detect.py --weights yolov5x.pt yolov5l6.pt --img 640 --source data/images
```
