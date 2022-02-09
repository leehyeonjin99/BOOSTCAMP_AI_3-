#  Computer Vision Applications
## Semantic Segmentation
- image에 대해 pixel마다 분류한다. (Dense classification) <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153099750-a09c5e0f-5800-4259-b48d-7311ff0faa9a.png" width=400></p>
- 자율 주행에서 주로 활용된다. 

### Fully Convolutional Network
ordinary한 CNN은 Convolution Layer와 Dense Layers로 이루어져 있다. Dense Layer를 없애고 Convolution Layer를 추가하여 Label을 생성한다. 이를 **fully convolutional network**라 한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153100948-b9c431d2-8714-42e0-ac3d-2bbdf274a949.png" width=350> <img src="https://user-images.githubusercontent.com/57162812/153101008-583744e4-5b27-42a6-b355-31fa9dbb8727.png" width=350></p>

또한, 아래의 그림처럼 Dense Layer들을 Convolutional Layer로 바꾸는 과정을 **Convolutionalization**이라 한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153101119-d5013b3c-6a0f-46be-8144-6963a60d1963.png" width=500></p>

- The Number of parameters
  - Left : 4x4x16x10=2,560
  - Right : 4x4x16x10=2,560
- 파라미터의 수는 같다. 그렇다면 Convolutionalization을 통해 얻는 이점은?
- Fully Convolutional Network는 input의 spatial dimension에 독립적이다. 
  - input이 커지게 되면 뒷단의 network가 비례해서 커지게 된다.
  - How?
    - Covolutinal Network의 shared parameter의 성질
  - Heatmap과 같은 효과가 나타난다. <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153103601-c2e19402-264f-4f38-b2ac-7d83347196a7.png" width=400></p>

- FCN은 어느 size의 input에 대해서도 동작하지만 일반적으로 output dimension은 subsampling에 의해 줄어든다. 
- 따라서, coarse output을 dense pixel로 연결해줄 방법이 필요하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153109309-34886199-569f-4c1d-8f72-a97012bcf0ff.png" width=300></p>

-즉, Convolutional 연산으로 인해서 작아진 size를 다시 키워줘야한다. : **Upsampling**

### Deconvolution (Conv Transpose)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153109572-6b2b6b98-2a52-4cca-b556-aa8c4c5234cc.png" width=500></p>

- Deconvolution은 Convolution 연산과 똑같이 진행되지만, Padding을 많이 줘서 연산 결과 dimension을 증가시킨다.

## Detection

image 안에서 어느 물체가 어디에 있는지 bounding box를 찾는다.

### R-CNN

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153110425-84f5f00e-70ce-4ea5-b100-9bdd5158d358.png" width=600></p>

1. 이미지를 넣는다.
2. 크기가 다 다른 Region Proposal를 뽑는다.
3. 똑같은 크기로 맞춘다.
4. AlexNet을 통해 CNN feature를 Compute한다.
5. SVM을 통해 분류한다.

**R-CNN의 단점은?**  
이미지 안에서 bounding box(Region Proposal)을 2000개를 뽑으면 2000개의 patch를 모두 CNN에 통과시킨다. 즉, 2000번의 CNN을 돌려야 하나의 이미지를 학습시킬 수 있다. 따라서 학습 시간이 오래걸린다.

### SPPNet

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153110786-d9ffb29c-e8e5-42f6-9c36-ef70d97ba8c0.png" width=400></p>

- 목적 : 하나의 이미지에 대해 CNN을 한번만 돌리자
- How?
  - 이미지 안에서 bounding box를 뽑고 이미지 전체에 대해서 Convolutional feature map을 만든 다음에 뽑힌 bounding box의 위치에 해당하는 Convolutional feature map의 tensor만 띄어온다.
  - subtensor를 뜯어오는 것을 region별로 한다.
- R-CNN보다 속도가 훨씬 빨라진다.

### Fast R-CNN

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153111388-2bedfd43-8e86-463a-9976-a04127b8d778.png" width=400></p>

SPPNet의 방법과 비슷하다.

1. Take an input and a set of bounding boxes
2. Gnerated convolutional feature map : 한번의 CNN을 돌린다.
3. For each region, get a fixed length feature from ROI pooling
4. Two Output : **Class** and **Bounding Box Regressor**

### Faster R-CNN

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153111905-03edc0ff-0d70-4dca-8731-778dc0f0a781.png" width=300></p>

Faster R-CNN = Region Proposal Network + Fast R-CNN

Region Proposal Network는 이미지를 통해서 bounding box를 뽑아내는 resion proposal을 학습을 한다.

#### Region Proposal Network

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153112165-513df64d-b683-4ac6-b438-c2fc2c5d9494.png" width=450></p>

이미지에서 특정 영역 patch가 bounding box로서의 의미가 있을지, 안에 물체가 있는지를 알려준다.

- 특징 
  - k개의 미리 정해진 size의 dectection box인 anchor box를 정해놓은다.

### YOLO

이미지 한장에서 바로 Output이 나온다. 즉, bounding 박스와 class probability를 동시에 예측한다.

- 이미지가 들어오면 SxS로 나누게 된다.
- 따라서, 이미지 안에 찾고 싶은 물체의 중앙이 해당 grid 안에 들어가면 그 grid cell이 해당 물체의 bounding box와 해당 물체가 무엇인지를 같이 예측한다.
