# 1. Synthetic Data

- 합성 데이터

## 1.1. Need for Synthetic Data

- 성능에 있어서 가장 중요한 것은 **Data**지만, **Real Data의 확보**는 어렵다.

  > **그렇다면 Real Data 확보 방법은?**
  >
  > 1. Public dataset 가져오기
  >    - 도메인에 따라 public dataset 규모가 충분하지 않다.
  > 2. 직접 만들기
  >    - 이미지 수집 (웹에서 수집 + 직접 촬영해서 수집)
  >    - Annotation 생성 : 난이도가 높고 비용이 많이 들어간다.

- 이때, **Synthetic Data**는 Real Data에 대한 부담을 덜어준다.

  1. **비용**이 훨씬 적게 든다.
  2. 개인 정보나 라이센스에 관한 **제약**으로부터 자유롭다.
  3. 더 세밀한 수준의 **annotation**도 쉽게 얻을 수 있다.

## 1.2. SynthText

- 가장 대표적인 합성 Dataset
- 800K dataset + 글자 이미지 합성 코드 제공 → Synthetic Dataset 직접 생성 가능

<p align="center"><img width="500" alt="image-20220420193211668" src="https://user-images.githubusercontent.com/57162812/164225488-607c1625-9fbc-44bf-abe8-a8b38ff334cd.png"></p>

- 합성에 필요한 Data = Image Data + 글자 Data
- 원본 이미지는 비경으로 인식되어 글자가 있더라도 annotation이 되어있지 않다. 즉, 원본 이미지는 글자를 포함하지 않도록 제한한다. 
- 적절한 위치에만, 표면 모양에 맞춰서 글자를 합성 → Realistic
  - Depth estimation을 통해서 이미지에 대한 depth map을 추론한다.
  - depth가 비슷한 위치끼리 묵으면 그룹이 만들어져 Text Region이 생성된다.
  - 동일한 text region에서 경계선에 물리지 않게 text를 합성해주어 현실감을 더해준다.

## 1.3. SynthText3D & UnrealText

- **SynthText3D** : 3D 가상 세계를 이용해 텍스트 이미지 합성
  - Word, illumination, Camera view를 결정한다.
  - 정해진 View 안에서 글자를 합성할 영역을 결정한다.
  - 글자의 내용과 스타일을 결정해 글자를 가상으로 배치
  - unrealengine을 이용해 이미지 rending
- **UnrealText** : 3D Virtual Engine을 이용
  - Camera view를 정할 때, 사람의 개입하는 Synthetic3D에 비해 실제로 있을 법한 View를 자동으로 탐색한다.

## 1.4. How to Use

- Pretraining

  - Target dataset만으로 학습할 때,

    ImageNet pretrained model로부터 backbone을 불러와서, 

    target dataset에 대해 fine-tuning 진행

  - 합성 데이터가 주어졌을 때,

    합성 데이터로 한번 더 pretraining 해주어서,

    fine-tuning 진행
  
  
<p align="center"><img width="400" alt="image-20220420195045984" src="https://user-images.githubusercontent.com/57162812/164225853-7857437e-e09a-461f-b77f-9c80b1d2b110.png">

- **Weekly Supervised Learning**

    - Character-level detection 수행하는 모델

      - character-level annotation 필요

      - Real dataset은 대부분 word-level annotation만 포함하기 때문에 full supervision을 줄 수 없다.

    - 학습 단계
      - 합성 데이터로 pretraining 된 모델을 생성
      - Real dataset에 적용해서 pseudo annotation 확보
      - Pseudo annotation을 이용해서 real dataset에 대한 fine-tuning 진행
    - 이를 통해 character-level annotation이 없어도 weakly supervised learning을 통해 word-level annotaiton이 생성 가능하다.

# 2. Data Augmentation

## 2.1. Image Data Augmentation

- 만약 데이터가 편향되어있을 경우, 데이터 증강을 통해서 데이터 균형을 올바르게 해준다.
- **관점에 따라** 데이터 균등화 시도
    - **색상** 분포 → Color Jittering
    - **촬영** 각도 → Rotation
    - 이미지 **크기** → Resize

- Image Data Augmentation = Geometric Transformation + Style Transformation + ⋯
    - Geometric Transformation : Global-level의 변화
      - RandomCrop, Resize, Rotate, Flip, Shear 등
    - Style Transformation : Local-level의 변화
      - ColorJitter, ChannelShuffle, Noise Filter 등
    - Other Transformations
      - Grid Distortion : 전체 이미지를 격자를 이용해 여러 구획으로 나누어, 각 구획 안에서 변형이 일어나지만 구획 경계에서는 변형이 없다.
      - Elastic Transformation : Grid Distortion + 유연성
      - Cutout : 이미지에 random mask를 생성해 일부가 가려진다.

## 2.2. Geometirc Transformations for Text Images

**항상 모든  Augmentation이 성능 향상에 도움이 되는 것은 아니다. 문제와 데이터에 따라 적합한 Augmentation을 찾아야 한다.**

- OCR task에서 augmentation시에 주의점
  1. 글자가 포함되지 않는 경우  
     Positive sample의 비중이 너무 낮으면 성능 저하가 발생할 수 있다.
  2. 글자가 잘려서 일부만 나타나는 경우
      Positive sample로 학습하면 모델에 혼동을 줄 수 있다.
 - 필요한 규칙

      1. Posirive ratio 보장

         최소 1개의 개체를 포함해야한다. 하지만, 글자와 멀리 있는 배경에서 hard negative sampling이 잘 되지 않는다.
         
         <p align="center"><img width="500" alt="image-20220420202441498" src="https://user-images.githubusercontent.com/57162812/164225960-ba40c759-0458-4524-8fbf-b1316eb3c475.png"></p>


         별도의 hard negative mining 기법을 도입해서 해결할 수 있다.

      2. 개체 잘림 방지

         잘리는 개체가 없어야 한다. 하지만, 밀집된 곳에서 sampling이 잘 되지 않는다. 즉, 밀도에 대한 bias 발생한다.

          <p align="center"><img width="400" alt="image-20220420202720109" src="https://user-images.githubusercontent.com/57162812/164226093-5e5b8e03-6367-4589-91b9-393057598dbb.png"></p>

          → 일단 최소 하나의 개체는 잘리지 않고 포함하게 한다. 또한, 잘린 것들은 masking해서 학습에서 무시한다.

- 실전에서는?

   - 도메인의 특징에 따라 다양한 문제가 발생할 수 있다.
   - 실제로 모델에 입력되는 이미지 관찰
   - 특히 loss가 크게 발생하는 영역들을 분석해서 Rule을 업데이트하는 피드백이 필요

# 3. Others

## 3.1. Multi-Scale Traning & Inference

- Naive Multi-Scale Training

  - 이미지를 다양한 크기로 바꿔가면서 입력
    - Crop & Resize augmentation
    - Image Pyramid
  - 문제점
    - 원래 작은 글자가 너무 작아지거나, 원래 큰 글자가 너무 커지는 경우가 발생하고, 성능 저하로 이어질 수 있다.

- SNIP - Scale Normalization for Image Pyramid

  - Training
    - 객체 크기의 적정 범위를 정해두고, 그 범위를 벗어나는 이미지에 대해서는 학습을 제외시킨다.
  - Inference
    - 여러 크기의 이미지에 모델을 적용하고 검출 결과 중 크기가 적정 범위에 있는 것만 취합한다.

- Naive Multi-Scale Inference

  - 다양한 크기의 개체를 검출하기 위해 이미지를 여러 크기로 조절해서 모델에 입력한다.
  - 문제점
    - 계산량이 많아져 비효율적이다.
    - 여러 크기에서의 false positive가 누적될 수 있다.

- Adaptive Scaling

  - Inference

    - 이미지에서 글자가 있을만한 영역만, 글자가 적정 크기로 나타나도록 조정해서 모델에 입력

    - 모델에 이미지를 2차례 입력

      1. 먼저 글자의 위치와 크기를 대략적으로 예측한다.

      2. 그 결과를 기반으로 재구성한 이미지를 다시 입력해서 Canonical KnapSackd을 통해 최종 결과를 얻는다.

  - Canonical KnapSack

    - 이미지를 바로 입력할 때에 비해 장점
      - 배경 영역에 대한 계산을 하지 않아 경제적이다.
      - 글자들의 크기가 적정 크기로 통일되어 scale variation으로 인한 성능 저하가 없다.

