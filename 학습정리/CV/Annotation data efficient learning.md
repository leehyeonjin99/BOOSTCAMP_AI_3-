# Data augmentation
## Learning representation of dataset
- dataset는 거의 항상 편향되어있다.
  - Image taken by camera(training data) ≠ real data
  - 즉, training dataset은 real data의 일부분이다.
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156971805-c574f987-0eb2-4cb5-9d38-65ae86b7f0db.png" width="50%"></p>

- data augmentation : fill more space and to close the gap
  - training dataset에 기본적인 augmentation기법을 통해 채워나간다.
    - brightness
    - rotate
    - crop, etc...
  
# Data augmentation
**Image data augmentation**
- dataset에 다양한 image transformation을 적용한다.
- OpenCV와 Numpy에 구현되어있다.

## Various data augmentation method
**Brightness adjustment**
```python
def brightness_augmentation(img):
  # numpy array img : RGB value 0~255 for each pixel
  img[:,:,0] = img[:,:,0] + 100 # add 100 to R value
  img[:,:,1] = img[:,:,1] + 100 # add 100 to G value
  img[:,:,2] = img[:,:,2] + 100 # add 100 to B value
  
  img[:,:,0][img[:,:,0]>255] = 255 # clip R values over 255
  img[:,:,1][img[:,:,1]>255] = 255 # clip G values over 255
  img[:,:,2][img[:,:,2]>255] = 255 # clip B values over 255
  
  return img
```

**Rotate, flip**
```python
img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img_flipped = cv2.rotate(img, cv2.ROTATE_180)
```

**Crop**
```python
y_start = 500
crop_y_size = 400
x_start = 300
crop_x_size = 800
img_cropped = img[y_start:y_start + crop_y_size, x_start:s_start + crop_x_size,:]
```

**Afine tranformation**
- 이미지의 `line`, `length ratio`, 그리고 `parallelism`이 유지된다.
```python
rows, cols, ch = image.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1, pts2)
shear_img = cv2.warpAffine(img, M, (cols, rows))
```

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156975589-3bce636f-665f-42e4-8917-23e8d1039d7b.png" width="70%"></p>

**CutMix**
- 두 사진을 잘라서 합성한다.
- label 또한 합성한다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156975795-7371af32-22fa-460b-a4b5-87c5729f912e.png" width="70%"></p>

## Modern augmentation techniques
**RandAugment**
- best augmentation 조합을 찾는 것은 어렵다.
- Automatically finding the best sequence of augmentaiton to apply
- Random sample, apply, and evaluate augmentation

**Example of augmented images in RandAug**
- Augmentation policy
  - 어떤 augmentation 적용?
  - 얼마나 많은 이지미에 augmentation 적용?

# Leveraging pre-trained information
## Transfer learning
**Benefits when using tranfer learning**
기존의 미리 학습된 model로 연관된 새로운 task에 적은 노력으로도 높은 성능에 도달 가능하다.

**Motivation observation** : 비슷한 dataset이 공통된 information을 공유한다.
- 한 dataset에서 배운 지식을 다른 dataset에서 적용할만한 공통된 지식이 많지 않을까? 하는 가정에서 시작

**Approach 1 : pre-trained task에서 새로운 task로 knowledge를 변경한다.**
- FC layer만 변경하고 학습시킨다.
- Conv layer는 freeze
- Data가 적을 때 유용

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156977284-8e215ec4-6238-44a2-9ec0-98eb81698975.png" width="70%"></p>

**Approach 2 : 전체 모델을 Fine-tuning**
- Conv layer에는 low learning rate
- FC layer에는 high learning rate
- Data가 좀 더 있을 때 유용

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156977437-bdb3eb38-53d8-4c88-a404-d5375e303aa9.png" width="25%"></p>

## Knowledge distillation

**Teacher-student learning**
- 이미 학습된 teacher network의 지식을 더 작은 모델인 student network에 주입하여 학습
- 즉, 큰 모델에서 작은 모델로 지식을 전달함으로써, 모델 압축에 유용하게 사용
- 최근에는 teacher에서 생성된 출력은 unlabeled된 data의 pseudo label(가짜 label)로 자동 생성되는 mechanism으로 사용
  - 더 큰 student network를 사용할 때, 더 많은 데이터를 사용하게 되기 때문에 regularization 역할로 사용

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156978086-07705e4d-df95-430c-9e52-864c82142cf8.png" width="50%"></p>

**Teacher-student network structure**

1. pre-trained network = Teacher model
2. 아직 학습되지 않은 student model initialization
3. 같은 입력에 대해서 Teacher model과 Student model에 동시에 feeding해 출력을 만들게 한다.
4. 둘의 차이를 KL div. Loss를 통해 측정하여 backpropagation으로 Student Model만 학습을 한다.
  - KL div. Loss는 두 출력의 distribution을 비슷하게 만들도록 학습시킨다.
  - label을 사용하지 않았으므로 `unsupervised trianing` 이라고 생각할 수 있다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156978552-d687551c-d21a-493f-914e-c6a9d682bc2f.png" width="75%"></p>

**Knoledge distillation with labeled data**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156980550-2f10b720-46a1-48fa-a2d0-6f7cd5a55627.png" width="75%"></p>

- `student loss` : ground truth label를 사용한 loss
- `distillation loss` : teacher를 따라하게 만드는 KL div. Loss
- student loss와 distillation loss의 weighted sum을 통해 학습한다. 단, Student model만 학습

> **Hard label vs. Soft label**
> - Hard label : One-hot vector
> - Soft label : softmax를 통한 label 표현
> 
> <img src="https://user-images.githubusercontent.com/57162812/156979194-ef66b6e0-bef6-4117-a7fc-720b876e83cb.png" width="35%">
> distillation에서는 각각의 값들의 전반적인 경향성이 knowledge를 나타낸다고 가정하고, 하나의 모델이 입력을 보고 어떤 생각을 하고 있는지 soft prediction을 통해서 살펴보기 위해 soft label을 사용한다.

> **Softmax with temperature(T)**
> softmax는 값을 극단적으로 벌려놓기 때문에 큰 값인 T로 나눠줌으로써 좀 더 smooth하게 만들어 줄 수 있다.
> 
> <img src="https://user-images.githubusercontent.com/57162812/156979603-9cbc582f-5553-403e-8494-27b8e20e8639.png" width="65%"> 

> **Intuition about distillation loss and student loss**
> - Distillation Loss
>   - KL div. Loss (Soft label, Soft prediction)
>   - Loss = teacher와 student의 inference 차이
>   - teacher network가 알고 있는 것을 따라하게 만드는 loss
> - Student Loss
>   - Cross Entropy Loss (Hard label, Soft prediction)
>   - Loss = sutdent network의 inference와 true label의 차이
>   - 옳은 답을 배우게 하는 loss

# Leveraging unlabeled dataset for training
## Semi-supervised learning
- unlabeled 엄청 큰 dataset + labeld 적은 수의 dataset

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156981172-8ed81c71-4f39-4ee4-9fb8-bafe56f5b9e7.png" width="70%"></p>

1. label dataset으로 pre-training
2. unlabel data의 pseudo label 생성 → pseudo-labeled dataset
3. labeled dataset + pseudo-labeled dataset 으로 model을 re-train 한다.

## Self-training
- Augmentation + Teacher-Student networks + semi-supervised learning

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156981394-2e757fe4-3dde-4809-9431-73d2b6523e1d.png" width="70%"></p>

1. ImageNet dataset으로 teacher network 학습
2. teacher network를 통해 300M unlabeled dataset → 300M pseudo-labeled dataset
3. ImageNet 1M labeled dataset + 300M pseudo-labeled dataset 으로 RandAugment와 함께 student model 학습 
4. Student 모델의 학습이 끝나면 해당 모델을 Teacher Model로 한다.
5. 2-4를 반복한다.
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/156981958-e78e9f5a-7a0a-4c0a-895d-8c12ea175c0d.png" width="70%"></p>



