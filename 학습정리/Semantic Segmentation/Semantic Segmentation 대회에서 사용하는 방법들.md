# Ⅰ. Baseline

## EfficientUNet Library

- 라이브러리 : `segmentation models pytorch (smp)` → 다양한 형태의 Encoder, Decoder Structure를 적용할 수 있다.
1. 설치 방법
    
    ```python
    pip install https://github.com/qubvel/segmentation_models.pytorch.git
    ```
    
2. 모델 불러오기
    
    ```python
    model = smp.UNet(
    			encoder_name = "efficientnet-b0",
    			encoder_weight = "image_net",
    			in_channels = 3,
    			classes = 11
    	)
    ```
    

## 실험해봐야 하는 실험들

1. 디버깅 모드 → 실험 환경이 잘 설정되어 있는지 확인
    - 데이터 샘플링을 통해서 확인
    - Epoch를 1-2로 설정해서 Loss 감소 확인
2. 시드 고정
    - torch 외의 `numpy`, `os` 관련 시드 고정
    - validation 검증셋의 시드 고정
3. 실험 기록
    - notion
4. 실험은 한번에 하나씩
    - 실험을 할 때, 하나의 조건만 변경해가며 실험
5. 팀원 역할 분재
    - 하나의 베이스라인 코드 + 상이한 실험
    - 독립적인 베이스라인 코드 + 앙상블 → 최소 2개의 baseline을 만들어 각자 실험해보자
    - EDA, 코드 만들기, solution 조사, discussion 조사

## Validation이 중요한 이유

1. 제출 없이 모델의 성능 평가 가능
2. Public 리더보드 성능에 오버피팅되지 않도록 도와준다.

> **Hold Out**
> 
> - Dataset = 8 Train + 2 Valid
> - Train 학습 + Valid 검증
> - 학습한 Model로 추론
> - 장점 : 빠른 모델 속도로 모델 검증 가능
> - 단점 : 모든 데이터가 학습에 참여하지 못함

> **K-Fold**
> 
> - 8:2의 Train Dataset과 Valid Dataset
> - 단, Split 개념을 사용해 모든 데이터가 학습에 참여 → Split 수만큼 독립적 모델 학습
> - 각각 inference 후 앙상블
> - 장점 : 모든 데이터셋 학습 참여, 신뢰성 있는 검증 결과, 앙상블로 인한 성능 향상
> - 단점 : 시간 비용, k를 선택해야 한다.

> **Stratified K-Fold**
> 
> - 기존의 k-fold는 class distribution이 고려되지 않는다.
> - Stratified k-fold는 Fold마다 class distribution을 동일하게 split → class imbalance에서 사용하기 좋다.

> **Group K-Fold**
> 
> - 만약, 환자 3명이 각각 3종류의 CT 사진을 갖고 있다 가정하자.
> - 이때, Stratified K-fold를 사용하게 되면 각 환자의 사진들은 다른 fold에 들어가게 된다. 하지만, 같은 환자의 CT 간에는 correlation이 존재할 것이다. 같은 환자의 이미지가 train, valid로 나눠지게 된다면 힌트를 보고 문제를 푸는 것과 같다.
> - 따라서 Group K-Fold는 각 환자들의 사진을 그룹으로 묶어 하나의 fold로 들어가도록 한다.

## Augmentation을 하는 이유

1. 데이터 수 증가
2. 일반화 강화
3. 성능 향상
4. Class Imbalance 문제 해결

- 하지만, 모든 Augmentation이 모든 domain에 맞는 것이 아니다. 이것을 실험을 통해 알아볼 수 있다.

> **Cutout**
> 
> - 이미지의 특정 영역이 제한된 상황에서도 classification을 잘 하도록 학습
> - 하지만, random 성향을 띄고 있기 때문에 객체를 모두 가리거나, 하나도 가리지 않을 수 있다.
> 
> ```python
> A.CoarseDropout
> ```
> 

> **Gridmask**
> 
> - cutout의 경우 객체의 중요 부분 혹은 context information을 삭제할 수 있다는 단점 해결
> - 규칙성 있는 box를 통해 cutout
> 
> ```python
> A.GridDropout
> ```
> 

> **Mixup**
> 
> - Dataset의 두 이미지를 섞는다.
> - $x_{new} = {\lambda}\times{Plastic} + {(1-\lambda)}\times{Glass}$

> **Cutmix**
> 
> - Dataset의 두 이미지를 일부분을 잘라 원본 이미지의 크기에 맞춰 붙인다.
> 
> ```python
> from cutmix.cutmix import Cutmix
> from cutmix.utils import CutMixCrossEntropyLoss
> ```
> 

> **SnapMix**
> 
> - CAM을 이용해 이미지, 라벨링 mixing
> - Cutmix는 영역 크기만 고려했다면, SnapMix는 영역의 의미적 중요도 또한 고려한다.

> **CropNonEmptyMaskIfExist**
> 
> - Object가 존재하는 부분을 중심으로 crop → model의 효율적인 학습
> 
> ```python
> A.augmentations.crops.transforms.CropNonEmptyMaskIfExists(height = 256, width = 256)
> ```
> 

## SOTA Model

- HRNet

## Scheduler

learning rate

- 높다면 loss의 발산
- 낮다면 학습 시간 소모 및 local optima에 빠지게 된다.
- 따라서, 스케쥴러가 필요로 한다.
    - 빠른 수렴 속도
    - 높은 정확도
- `CosineAnealingLR`, `ReduceLROnPlateau`, `Gradual Warmup`

## Batch Size

- 높다면, 학습속도 상승 & 일반화 성능 상승
- but GPU 메모리 문제
1. Gradient Accumulation
    
    모델의 weight를 step마다가 아닌, 일정 step동안 gradient를 누적하여 이를 기반으로 weight 업데이트 → batch size를 키운 효과
    

## Optimizer

- Adam
- AdamP
- AdamW
- Radam
- Lookahead Optimizer → k번의 forward 후 처음 시작 방향으로 1번 back : local minima에서 빠져나올 수 있다.

## Loss

- Dice + Focal Loss
- Dice + Topk Loss

# Ⅱ. Baseline 이후 실험 요소들

## 앙상블

1. **K-Fold Ensemble**
    
    5-Fold CV를 통해 5개의 모델을 앙상블 하는 방법
    
2. **Epoch Ensemble**
    
    학습이 완료된 후, 마지막부터 N개의 Weight를 이용해 예측한 후 결과를 Ensemble하는 방법
    
3. **SWA(Stochastic Weight Averaging)**
    
    각 step마다 weight를 업데이트시키는 SGD와 달리 일정 주기마다 weight를 평균내는 방법
    
    즉, `일반화`가 강해진다.
    
    - Case1. constant learning rate
    - Case2. Cyclic learning rate
    
    75%의 학습이 진행된 후 Average CNN weight + Update BN
    
    ```python
    # AveraageModel : 모델의 SWA를 track하는 wrapper
    # SWALR : Learning Scheudler
    from torch.optim.swa_utils import AverageModel, SWALR
    
    loader, model, optimizer, criterion = ...
    swa_model = AverageModel(model)
    scheduler = CosineAnealingLR(optimizer, T_max=100)
    swa_start = 5
    swa_scheduler = SWALR(optimizer, swa_lr = 0.05)
    
    for epoch in range(100):
    	for input, target in loader:
    		optimizer.zero_grad()
    		criterion(model(input), target).backward()
    		optimizer.stop()
    	if epoch > swa_start:
    		swa_model.update_parameters(model)
    		swa_scheduler.step()
    	else:
    		swa_scheduler.step()
    
    torch.optim.swa_utils.update_bn(loader, swa_model)
    preds = swa_model(test_input)
    ```
    
4. Seed Ensemble
    
    random한 요소를 결정짓는 seed만 바꿔가며 여러 모델을 학습시킨 후 Ensemble하는 방법
    
    → lucky seed로 인한 public score에서는 높고 private score에서는 낮은 일반화 성능 하락 현상에 대해서 대비 가능하다.
    
5. Resize Ensemble
    
    Input 이미지의 Size를 다르게 학습해 Ensemble하는 기법
    
6. TTA(Test Time Augmentation)
    
    Test set으로 모델의 성능을 테스트할 때, augmentation을 수행하는 방법
    
    - 해당 모델은 위의 Resize Ensemble과 다르게 동일한 모델에 대해서 실행
    - 또한, rotate augmentation을 수행하였을 경우, pixelwise 계산이 필요하므로 원본의 형태로 돌려놓아야한다.
    
    > 학습 때와 다른 size의 input 이미지를 이용해 Test 하는 방법
    > 
    
    ```python
    # TTA Library : ttach
    import ttach as tta
    
    transforms = tta.Compose(
    	[
    		tta.GorizontalFlip(),
    		tta.Rotate90(angles=[0, 100],
    		tta.Scale(scales = [1, 2, 4]))
    	]
    )
    
    tta_model = tta.SegmentatinoTTAWRapper(model, transform)
    masks = tta_model(images)
    ```
    
    - Compse 오브젝트는 입력으로 주어진 TTA들을 조합해서 여러가지 TTA case 설정
        
        > 2(Flip o/x) × 2(Rotate) × 3(Scale) = 12가지 TTA
        > 
    - SegmentationWrapper object는 model과 Compose의 결과물을 입력으로 받아 한 이미지에 대해 12가지 TTA를 적용하고 결과물을 `평균 내어 return`
        
        > Merge modes
        > 
        > - mean
        > - gmean(geometric mean)
        > - sum
        > - max
        > - min
        > - tsharpen(temperature sharpen with t=0.5)

## Pseudo Labeling

- 모델 학습 진행 후, test dataset inference
- 성능이 가장 좋은 모델에 대해 Test 데이터셋에 대한 예측을 진행
    
    > Test Image 1 : [0.04, 0.9, 0.05, 0.01]
    Test Image 2 : [0.1, 0.6, 0.05, 0.01]
    Test Image 3 : [0.02, 0.4, 0.08, 0.5]
    Test Image 4 : [0.02, 0.95, 0.01, 0.02]
    > 
    - 예측값이 threshold(0.9)보다 높은 결과물을 이용
- 2단계에서 예측한 Test 데이터셋과 Train 데이터셋을 결합해 새롭게 학습 진행
- 3단계에서 학습한 모델로 Test 데이터셋 예측

## 외부 데이터 활용

## 그 외

**Classification 결과를 활용하는 방법**

- Encoder Head 마지막 단에 Classification  Head를 달아서 같이 활용

**한정된 시간을 효율적으로 사용**

- 코드 돌리는 시간에 다른 작업 진행
- 작은 샘플로 실험 콛가 문제 없는지 미리 확인
- 자는 시간, 쉬는 시간 등 GPU가 쉬지 않도록 미리 실험용 코드 작성

# Ⅲ. 대회에서 사용하는 기법들

## 최근 딥러닝 이미지 대회 Trend

1. 학습 이미지가 많고 큰 경우에는 네트워크를 한번 학습하는데 시간이 오래 걸려서 충분한 실험을 하지 못함
    
    > Mixed Preciison Training of Deep Neural Networks
    > 
    > - 속도를 높이기 위한 FP16 연산과 정확도를 유지하기 위한 FP32 연산을 섞어서 학습
    > 
    > ```python
    > net = make_moedl(in_size, out_size, num_layers)
    > optimizer = torch.optim.SGD(net.parameters(). lr=0.001)
    > # GradScaler는 AMP 활용 시 발생할 수 있는 underflow라는 문제 방지
    > scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
    > 
    > start_timer()
    > for epoch in range(epochs):
    > 	for input, target in zip(data, targets):
    > 		with torch.cuda.amp.autocast(enabled=use_amp):
    > 			output = net(input)
    > 			loss = loss_fn(output, target)
    > 		# loss.backward()
    > 		scaler.scale(loss).backward()
    > 		# optimizer.step()
    > 		scaler.step(optimizer)
    > 		scaler.update()
    > 		optimizer.zero_grad()
    > ```
    > 
    
    > 가벼운 상황으로 실험
    > 
    > - 일부 데이터 사용
    > - 단일 Fold로 검증
    >     - 단 LB와 Validation Score 간의 어느정도 상관관계가 있어야함
    
    > 가벼운 모델로 실험
    > 
    > - efficientnet-b0 → efficientnet-b7
2. data인 image의 크기가 매우 큰 경우 model이 학습하는 시간이 오래 걸림
    
    > Resize
    > 
    > - 주어진 data를 모두 resize시켜 학습 → test set에 대해 예측된 Mask를 원본 size로 복원
    > - 하지만, Image가 지나치게 크다면 Resize 기법에 의해 Resolution 감소
    
    > Sliding Window(Overlapping/None-overlapping)
    > 
    > - Image size가 크기 때문에 window 단위로 잘라서 input으로 넣는 기법
    >     - `window size > stride size` → Overlapping
    >         
    >         ![image](https://user-images.githubusercontent.com/57162812/166694479-fb8b6140-8fb6-46ba-bbbf-3cde9f6a5589.png)
    >         
    >     - `window size = stride size` → Non-overlapping
    >         
    >         ![image](https://user-images.githubusercontent.com/57162812/166694527-94f40197-0cd3-4256-b417-8cefca86c4be.png)
    >         
    > - 단, Sliding Winsow 적용시 얼마의 window size 및 stride를 어떻게 설정하는지 중요
    >     - window size↑ → input image 크기↑ & 정보↑
    >     - stride↓ → input image 수↑ & 겹치는 영역↑ & 다양한 정보 ↑
    >     - but, 일반적으로 겹치게 자르게 되면 다양한 정보를 얻을 수 있지만, 학습 데이터의 양이 많이 늘어나게 될 수 있으며, 중복되는 정보가 많아 학습 데이터가 늘어나는 양에 비해서 성능의 차이는 적고 학습 속도가 오래 걸리는 문제 발생
    > - training에 사용된 sliding window의 크기와 inference에 사용되는 sliding window의 크기가 동일할 필요 없음 → inference의 sliding window의 크기가 클 때, 성능 향상 가능성 증가
3. 전체 이미지에서의 유의미하지 않은 영역들이 잡히는 경우가 많음
    - object detection을 통해 object 부분을 먼저 찾은 후 Crop → Segmentation
4. Task가 Binary Classification인 경우
    - 추가로 구분해야 할 class가 오직 2개인 경우 threshold(hyper-paramter)를 잘 search하면서 실험 진행

## model 개선을 위한 Tips

1. Output Image 확인
    - 큰 object 예측을 잘하는지?
    - 작은 ojbect 예측을 잘하는지?
    - 특정 class에 대해서 잘 맞추는지?
        
        → class가 많은 경우 각각의 class를 찾아서 확인하기 어렵기 때문에 validation set에서의 IoU 값 확인
        
2. 실제 Segmentation task를 진행하다 보면 label Noise가 빈번함
    - Boundary 부분 label miss
    - 올바르지 않은 label
    - 원인?
        - 일반적인 segmentation에서의 annotation task는 pixel 단위로 이루어지기 때문에 어려움
        - 사람마다의 기준 상이
        - 사람이기 때문에 annotation 오류 발생
    
    > **Label Smooting**
    > 
    > - Hard target → Soft target : [0, 0, 1, 0] → [0.025, 0.025, 0.925, 0.025]
    > - Cross Entorpy Loss, BCE Loss → Soft CrossEntropy Loss, Soft BCE Loss
    
    > **Pseudo-labeling을 활용한 Label Preprocessing**
    ex. 3Fold  → 각 이미지 별 mIoU → Noise Image의 mIoU는 낮을 것이다. → mIoU가 낮은 순서대로 정렬할 때, 낮은 mIoU의 이미지는 Noise Image일 가능성이 높다. →  Pseudo Labeling
    > 
    
    ## 최근 딥려닝 이미지 대회 평가 Trend
    
    1. Accuracy, mIoU 이외의 다양한 평가 방식을 추가
        - 학습 시간의 제한 → 앙상블이 어렵다 →한가지 모델 Epoch 앙상블, SWA로 대체하자.
        - 추론 시간의 제한
        - 속도 평가
    
    ## Monitoring Tool
    
    1. Weights & Bias
        
        → 모델에 대해서 inference 결과를 web에서 확인 가능
