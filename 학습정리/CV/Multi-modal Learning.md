# Overview of multi-modal learning
## Oerview of multi-modal learning
- `uni=modal` : 하나의 type의 data에만 집중하는 것
- `multi-modal learning` : 한 type의 data가 아닌 다른 type의 data들을 같이 활용하는 학습법 
  - text data + sound data + image data
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158508397-e5f35a94-1b98-4cfb-92dc-598d22cb451b.png" width =60%></p>

**Chanllenge(1) - 서로 다른 modality의 data 표현 방법이 다르다.**
- Audio : 1D signal의 wave 형태
- Image : 2D array 또는 3D array의 intensity 값이 있는 형태
- Text : word에 대응되는 embedding vector를 구해서 사용한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158510690-c97c6a3f-c6cf-4079-86ea-ea4cb29bc7ff.png" width =60%></p>

**Challenge(2) - 서로 다른 modality에서 오는 정보의 양과 feature space의 특징들이 unbalance하다.**

> 예시. 우리가 text로 'An armchair in shape of avocado'를 요구하면, avocado shape의 armchair들의 형태는 visual data 기준으로는 굉장히 많을 가능성이 있다. → **1:N matching** 
> 
> 또한 image 하나가 text 하나로 matching이 되지는 않는다.
> 
> 즉, **unbalance**하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158511173-f34eaa73-8ebf-4f65-999b-bb1b2b03d348.png" width =60%></p>

**Challenge(3) - model을 사용해 학습시, 특정 modality에 대해 편향된다.**
 
쉬운 data에 대해서 편향되고 까다로운 data는 쓰지 않게 되어 하나의 modality에 bias한 상황이 쉽게 발생한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158512652-485deacf-7efa-4e4c-8bd2-0c4836036565.png" width =60%></p>

> action을 탐지하기 위해 visual data와 sound data를 함께 사용하는 video data를 가정하자.  
> 대부분의 action은 visual을 통해서 판단이 되며, 가끔씩 노래를 부르거나 소리를 지르는 상황에서는 sound를 통해서 판단이 된다.  
> → 대부분의 경우는 visual data로 쉽게 판단이 되기 때문에 Neural network가 visaul data로 bias된다.

**이러한 challenge에도 불구하고, multi-modal learning은 종요하며 해결 가능성이 높아진다.**

- multi-modal learning의 일정한 pattern
1. `Matching` : 서로 다른 type을 공통된 space로 보내 서로를 matching 가능한 구조로 유도
2. `Translating` : 하나의 modality data를  또다른 modality data로 translation한다.
3. `Referencing` : 하나의 modality에서부터 또다른 modality data를 참조함으로써 결론을 도출하는 상호적 작용
 
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158513110-0b8966db-27ce-4598-8c0f-77ea9a498948.png" width =60%></p>

# Multi-modal task(1) - Visual data & Text
## Text embedding
**Example**
- Maching Learning 관점에서는 characer를 사용하는 것이 어렵다.
- 일반적으로 word level을 사용한다 또한, text를 `dense vector`(embedding map) 형태로 표현한다.
  - vector의 각 값들이 multi-deimensional한 의미있는 실수 값들 갖도록 표현한다.
- embedding vector가 주어져 2D로 나타내보면
  - 비슷한 단어들은 가까이 있다.
    > cat은 kitten<dog<house 순의 거리를 가진다.
  - 같은 의미로 대조되는 단어들의 쌍에 대한 차이가 같다. 즉, `일반화`의 능력이 있다.
    > king + (woman - man) = queen 
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158513770-3c093ce7-065d-47ea-848d-a3cc7a17005e.png" width =60%></p>

**word2vec - Skip-gram-model**

- W와 W`을 learn
- W의 각 row들이 word embedding vector가 된다.
  - Input의 dimentional vector들은 각각 하나의 word를 의미한다.
    > cat이라면 cat에 해당하는 dimension은 1 이고 이외는 0이다. [0,...,0,1,0,...,0]
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158518703-5e046722-1bc2-4f27-8c09-8d261ec1be74.png" width =40%></p>
- task : 주변의 N개의 word를 prediction
  - 하나의 word에 대해서 주변 word와의 관계성을 학습
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158518858-20d924bc-96db-44b2-b517-e5dba9d291ee.png" width =60%></p>

## Joint embedding
- Matching을 하기 위한 공통 embedding vector를 학습하는 방법
**Application - Image tagging**
- 주어진 이미지에 대해서 tag를 생성하거나, 반대로 tag를 통해서 이미지를 생성한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158519112-ec6c5c2d-e3c6-4857-8cf3-a4c270ee3c7d.png" width =60%></p>

**Image tagging - Combining pre-trained unimodal models**
- pre-trained unimodal model들을 합친다.
  - text data는 text model을 사용하여 feature vector를 추출하고, image data는 image model을 사용하여 feature vector를 추출하여 두 feature vector들을 같은 d dimension feature vector로 표현을 하여 호환성이 있도록 Joint embedding space를 학습해준다.
  - 두 feature vector의 연관성에 따라 embedding vector의 거리를 조절해주는 특성을 갖게 된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158519673-a4ebcf04-80de-44f0-ad78-b330bb995d72.png" width =60%></p>

**Image tagging - Metric learning in visual-semantic space**

- Joint Embedding space를 학습하기 위해서 matching되는 text와 image가 주어졌을 때, 같은 embedding space에 mapping하여 embedding 간의 distance를 줄여주는 방향(`push`)으로 학습한다. matching되지 않는 text와 image에 대해서는 distance가 커지는 방향으로 penalty를 주어(`pull`) 학습시킨다.
  - `push`와 `pull`과 같은 operation을 통해서 학습하는 것을 `metric learning`이라 한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158519880-1c7523e5-2b89-4642-8f89-406c1fb4592d.png" width =30%></p>

**Image tagging - Interesting property**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158520983-f7defe2f-b937-4364-bfc1-de1e6b76a41e.png" width =50%></p>

> **image embedding vector - word embedding vector + word embedding vector → image**
> 
> 잔디밭에 있는 개의 image에 대한 embedding space의 vector에서 dog라는 word의 emdedding vector를 빼고 cat이라는 word의 embedding vector를 더해줬더니, 가장 가까운 이미지는 잔디밭에 있는 고양이 사진이 나왔다.

**Application - Image & food recipe retrieval**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158521294-da13083d-e614-4e61-9dac-655bdc5c3946.png" width =50%></p>

> Query Image를 넣어주었을 때 recipe를 연결시켜준다. 반대로, recipe를 입력했을 때 음식 이미지를 연결시켜준다.

**Recipe text(sentence) vs. food image**

- recipe에는 순서가 있는 text이다. 
  - ingredient-encoder : 재료가 어떤 순서로 추가가 되는지를 RNN 계열의 Nueral Network를 통해 fixed vector를 만들어 준다.
  - instruction-encoder : 지침이 어떤 순서로 추가 되는지를 RNN 계열의 Nueral Network를 통해 fixed vector를 만들어 준다.
  - 두 fixed vector를 concatnate로 하나의 fixed dimensional vector를 만들어 준다. : recipe를 대표하는 embedding vector가 된다.
- image는 CNN backbone network를 이용해 feature map → fixed vector를 만들어 준다.
- recipe와 image의 fixed vector의 `cosine similarity loss`를 사용해 Joint Embedding 학습
- cosine similarity loss로 해결되지 않는 high-level semantic을 incoporation 하기 위한  `semantic regularization loss`
  > 에를 들어 recipe와 image가 'fried fish'라는 공통의 카테고리를 공유한다. 즉, 전체 정보 중 일부의 정보라도 중요하게 catch하기 위한 loss

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158521824-d73fd1f6-ae7b-4f2f-a02b-0678547ce77b.png" width =60%></p>

## Cross modal translation

**Application - Image captioning**
- Image가 주어지면 Image를 가장 잘 설명하는 text description을 생성

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158523488-3cfc2378-7bbc-42e9-ab23-07ddb0dc38a5.png" width =60%></p>

**Captioning as Image-to-sentence - CNN for image & RNN for sentence**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158523630-e9890edf-6111-4ca7-baca-b305faa65dba.png" width =60%></p>

- Image를 입력하기 위해서는 CNN을 사용하고 text를 출력하기 위해서는 RNN을 사용한다. 이때, CNN과 RNN을 합치는 것이 중요하다.

**CNN과 RNN을 합친 방식 : Show and tell**

- Image가 들어오면 fixed dimensional vector로 변환하기 위헤 `Encoder`가 필요하다.
  - ImageNet에서 pre-trained된 CNN model 사용
- fixed dimensional vector가 완성되면 이것을 conditional로 제공하며, LSTM의 시작 token을 넣어준다.
  - Image conditional과 시작 token으로 단어들을 출력하게 된다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158524116-a072c092-9311-472d-af72-eaaac3c32c48.png" width =60%></p>

- 하나의 fixed vector에서 image caption 전체를 한번에 예측한다. 

**Show, attend, and tell - Example results**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158524668-8f2a7844-1950-43e3-a844-01e467d2d741.png" width =60%></p>

> 첫번째 사진에서 woman을 이야기 할 때 image 위치별 중요도와 frisbee를 이야기할 때 image 위치별 중요도가 다르다.  
> 따라서 하나로 표현하기 보다 국지적인 중요도를 매번 다르게 reference를(attention이 다르도록) 하도록 구현하느 것이 show, attend, and tell이다.

**Show, attend, and tell**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158525379-a51c5db7-96af-4ecc-8d06-b480e335c39e.png" width =60%></p>

1. Input image를 CNN에 넣어준다.
    > fixed dimensional vector 하나로만 출력하는 것이 아닌, 14x14의 공간 정보를 유지하고 있는 feature map 형태로 추출한다.
2. Feature map을 RNN에 넣어준다.
3. RNN은 반복해서 하나의 word를 생성할 때 마다, 14x14 feature map을 referencing해서 어떤 단어를 출력해야할지, 다음에 어디를referencing해야하는지를 attention한다.

**Show, attend, and tell - Attention & Soft Attention**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158525772-e72e58fb-daf3-423f-91c2-3a2c3bd1c2f6.png" width =60%></p>

> (좌) 사람의 얼굴 사진을 본다고 할 때, 사람들은 검은색 선으로 연결된 것처럼 시선이 이동한다.
> 
> (우) feature가 들어오게 되면 RNN을 통과시켜 어디를 referencing을 해야하는지 heatmap으로 만들어주게 되고, feature와 heatmap을 잘 결합하여 z라는 vector를 만들어준다. : `Soft Attention` 

**Show, attend, and tell - Inference**

caption 추론 과정은 다음 그림과 같다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158526842-890e3138-28c2-41bf-9c84-0c6b0c9692cc.png" width =60%></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158526917-8400bddb-7af2-448b-9086-904ccef338c2.png" width =60%></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158526993-9b418d77-b196-418b-ba54-0789fcd1b932.png" width =60%></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158527094-9b94d331-1951-4f92-a936-5963bee33fbf.png" width =60%></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158527271-50b22077-328a-49a0-8e31-5e1b093d84f1.png" width =60%></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158527328-377f2079-2638-4e31-b33c-1997fbbef3f6.png" width =60%></p>

**Text-to-image by generative model - Example**

- text가 주어졌을 때, 상상 가능한 단 하나의 unique한 영상이 아니다. 따라서 1 to many mapping이다. 즉, `generative model`이 꼭 필요하다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158527701-c28c1efe-44e6-40bf-9360-02554852cedc.png" width =40%></p>


**Text-to-image by generative model**
- Generator
  1. text 전체를 fixed dimensional vector로 만들어준다.
  2. fixed dimensional vector의 일부에 Gaussian random code를 붙여준다.
      - output 결과가 항상 같은 것을 방지해준다. 즉, 다양한 output이 나올 수 있도록 해준다.
  3. decoder을 거쳐 이미지를 generate한다.

- Discriminator
  1. 생성 image가 들어오면 encoder를 통한 low dimensional spartial feature와 image를 만드는 데에 사용한 sentence 정보(condition)로 true, false를 판단한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158528500-6d5a0f13-c5e8-4d53-aeca-d181e5dd801a.png" width =60%></p>

## Cross modal reasoning
- 다른 modality를 참조해서 결론을 도출한다.

**Visual question answering - Multiple streams**
- 영상이 주어지고 질문이 주어지면 답을 도출한다.
- `Image Stream` : pre-trained Nueral Network를 통해 fixed dimensional vector를 출력한다.
- `Question Stream` : text의 sequence로 RNN을 통해 fixed dimensional vector를 출력한다.
- 두 fixed dimensional vector를 point-wise multiplication을 통해 두 embedding feature가 interaction할 수 있도록 한다. (하나의 Joint Embedding feature라고 할 수 있다.)
- FC layer를 통해 답을 출력한다.
- 모두 differenciable로 end-to-end 형태이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158529470-5f4a3279-a489-44bc-9ad5-9223786943a1.png" width =60%></p>

# Multi-modal tasks(2) - Visual data & Audio
## Sound representation
**Sound representation**
- data가 처음에는 시간축에 대한 `waveform`의 1D signal이다.
- ML에서 사용하기 위해서는 Spectogram이나 MFCC 형태의 Aucostic feature로 변환한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158530287-dc6cea7a-5904-44e0-b953-11108af8de9a.png" width =60%></p>


**Sound representation - Fourier transform**
- waveform에서 spectogram으로 변환시키기 위한 방법
- `Short-time Fourier transform(STFT)`
  - 시간 축 t에 대한 wave form 전체에 대해 FT를 적용하게 되면 주파수 축으로 옮겨가게 된다. 하지만, 주파수 축으로 모두 옮기게 되면 시간에 따른 변화를 파악할 수 없다.
  - 따라서 제안된 방식이 STFT이다.
  - window 구간 내에 대해서만 FT를 적용한다.
    - Hamming window를 통해 boundary에 대한 weight를 약하게 주고 가운데 부분을 강조한다.
    > 아래 그림에서 빨간색 박스 구간만 window 구간으로 생각하고 FT를 적용하여 spectogram으로 만든다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158531298-b9d35f2c-7374-42e4-a687-e3a716bf5a33.png" width =60%></p>

**FT를 하는 이유?**

- time 축의 input signal이 주어지면, FT를 통해서 주파수에 대한 삼각함수가 어느 정도로 들어있는지 분해하는 분해적 기능이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158531681-59404c35-a7b3-4e4d-84ef-b67ffa2d5786.png" width =60%></p>


**Sound representation - Spectogram**
- spectrum 하나하나를 window에서 구하게 되면 세로로 stacking을 하여 시간에 따른 주파수 성분을 확인할 수 있다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158531989-11e3700b-e803-4029-a5f1-8ba25132bcae.png" width =60%></p>

## Joint embedding

**Application - Scene recognition by sound**
-sound를 통해서 장면을 인식한다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158532383-24482ba1-f4a8-47a6-bfb4-01ad8f711450.png" width =60%></p>

**SoundNet**

- audio의 표현을 어떤 식으로 학습할지 제시
  1. unlabeled video dataset이 주어진다.
  2. video의 frame들을 pre-trained visual recognition network에 넣어준다. + video의 auuio를 raw waveform 형태로 추출해 1D CNN 구조에 넣어준다. 
    > spectrum이 아닌 waveform을 사용한다.
  4. Image CNN을 통해 Object(물체) Distribution을 출력 + Places CNn을 통해 Scene(장면) Distribution 출력
  5. 1D CNN의 마지막에 2개의 head로 분리해준다. : Scene Distribution을 따라하는 head + Object Recognition을 따라하는 head
  6. KL divergence loss를 통해서 Sound branch 쪽만 학습된다.
  7. `Teacher-student manner`
- visual knowledge를 sound에게 transfer했다. : `Transfer learning`

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158532465-6423c5a2-ab65-4e74-aa3a-0fc6e2361d8e.png" width =60%></p>

- 학습된 SoundNet Network를 pre-trained network로써 target task에 응용 가능하다.
- pool5 layer를 추출하여 사용한다. : pool5의 output은 sound를 표현하는 representation이다.
  - 1D CNN의 마지막 Conv8은 Object Distribution과 Scene Distribution을 따라하기 때문에 Pool5가 더 일반화된 semantic info를 가진다.
- pool5에 classifier를 추가해 풀고 싶은 target task를 classifier만 학습해 사용하게 된다.

## Cross modal translation

**Speech2Face**
- 음성을 듣고 얼굴을 상상하는 모델이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158559071-aed557ac-b9f4-4d63-af01-30324823b5a4.png" width =60%></p>

**Speech2Face - Module network**

- Module network 활용
  > **Module network**  
  > 각자 담당하고 있는 미리 학습된 network들을 조합하는것
1. VGG-Face Model
    - 얼굴 이미지가 들어오면 fixed dimensional vector로 표현
2. Face Decoder
    - face feature가 들어오면 무표정의 정면의 이미지를 instruction한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158559916-0ac59355-9d32-4db6-94ad-3b6b59c4a858.png" width =60%></p>

**Speech2Face - Training**

- 인터뷰 비디오의 얼굴과 목소리를 이용한다.
  - Face Image를 Face Regcognition에 넣어 Face Feature를 추출한다.
  - Voice Data를 Speech2Face 모델을 통과시켜 Feature vector를 추출한다.
- Face feature와 Voice feature이 호환 가능하도록 학습시킨다.
  - Voice feature vector가 Face feature vector를 따라하도록 한다.

**Application - Image-to-speech synthesis**
- 이미지로부터 speech를 만든다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158560947-7056a679-e11a-4838-9c25-39006b39adb7.png" width =60%></p>


**Image-to-speech synthesis - Module networks**

1. Image가 들어오면 CNN을 통해 14x14 feature map을 만들어준다.
2. Show, Attend, and Tell 구조를 활용해 word가 아닌 sub-word unit을 출력한다.
3. unit으로부터 음성을 보관하는 Unit-to-Speech Model을 TTS를 이용해 학습시킨다.
    > TTS는 text to speech로 Text(sub-word unit)에서 Speech로 변화시켜주는 network이다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158561131-eafde1d7-e061-4358-8510-8f6a82d7a744.png" width =60%></p>



## Cross modal reasoning

**Application - Sound source localization**
- 사람의 소리와 이미지를 주었을 때, 소리가 어디서 났는지 이미지에 localization한다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158562074-986ccd6d-9e7c-40fb-99b9-6e912ba363f9.png" width =60%></p>

**Sound source localization**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158566959-23307b78-9bd1-4370-b18a-46f87fb096bd.png" width =60%></p>
- Visual net은 공간 feature를 유지하는 spatial feature를 제공한다.
- localization score를 추출하기 위해서 두 feature vector를 내적한다.
- **Fully supervised version**
  - GT가 존재하여 loss를 사용하여 학습시킨다.
- **Unsupervised version**
  - image의 feature vector와 Localization score를 element-wise multiplication을 통한 평균으로 Attended visual feature를 출력한다.
  - attended visual feature와 audio feature가 같은 비디오에서 나왔다면 비슷하게, 다른 비디오였다면 다르게 한다. `unsupervised metric learn.loss`
- **Semi-supervised version**
  - supervised loss와 unsupervised loss를 모두 사용한다.


# Further Question

(1) Multi-modal learning에서 feature 사이의 semantic을 유지하기 위해 어떤 학습 방법을 사용했나요?

(2) Captioning task를 풀 때, attention이 어떻게 사용될 수 있었나요?

(3) Sound source localization task를 풀 때, audio 정보는 어떻게 활용되었나요?

