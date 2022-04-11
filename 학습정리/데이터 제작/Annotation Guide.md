# 1. 좋은 데이터셋의 선결 조건, 가이드라인
## 1.1 가이드라인이란?
- `Guideline` : 좋은 데이터를 확보하기 위한 과정을 정리해 놓은 문서  
  > 좋은 데이터란?
  > 1. [Raw Data] 골고루 모여있다.
  > 2. [Ground Truth] 일정하게 라벨링된 데이터

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/162670914-288ee3e7-5d0c-4d73-b2af-886d632b3d49.png" width="40%"></p>

- 자주 보게 되는 sample : 작업 가이드를 만들 때 인지 → **노이즈가 적다**
- 드물게 관찰되는 sample : 작업 가이드에서 다루지 않을 가능성 높음 & 작업자 별로 상이 → **노이즈가 크다**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/162671368-b8092174-ab5f-4bf7-83d0-aaee1a94098c.png" width="40%"></p>

1. 해당 경우를 발견하고 해당 sample을 확보
2. 이를 포함한 라벨링 가이드 작성

**가이드 라인의 구성**
1. 데이터 구축의 `목적`
2. 라벨링 `대상 이미지` 소개
3. 기본적인 `용어 정의`
4. `Annotation 규칙`

**Guideline의 필요성**
1. 학습 목적
    - 학습 목적에 따라 Annotation 규칙이 달라지지만, 목적에 맞게 `일관되게` 해야한다.
2. 데이터의 일관성
  - 원하는 작업명을 명확하게 언급하는 것이 일관성 측면에서 더 좋다.
  - ex. 추가 가이드 없음 vs. 글자가 잘리지 않는 한도에서 최대한 타이트 하게

**Guideline의 필수 요소**
1. `특이 케이스` : 가능한 특이 케이스가 모두 고려되도록
2. `단순함` : 작업자들이 숙지가 가능하도록
3. `명확함` : 동일한 가이드 라인에 대해서 같은 해석이 가능하도록

## 1.2 학습 데이터셋 제작 파이프라인

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/162671998-ae45b8e5-1c9b-4bf8-8e89-abd7667cf4dd.png" width="60%"></p>

1. 서비스 요구사항
  > "영수증 인식에 사용할 OCR 엔진 개발"
2. 제작 목적 설정
  > 1. 모든 영수증? 모든 글씨?
  > 2. 검출기+ 인식기 혹은 검출기 인식기 따로?
  > → 모든 글자는 다 인식하는 범용 OCR
  > 3. 사람이 못 알아보는 글자는? 모든 언어? 뒤집힌 글자도?
3.  가이드라인 제작
4.  Raw image 수집
    - 크롤링 : 좋은 키워드 선정 → 필터링
    - 크라우드 소싱

# 2. General OCR Dataset 예제로 알아보는 가이드라인 작성법
## 2.1 개요

**Guideline 제작 과정**

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/162672917-d26de8d9-b4cd-49c5-af37-96fdf9a046f7.png" width="50%"></p>

- 초기에 많은 QnA
- 따라서, 처음에 아주 소량의 dataset으로 pilot 라벨링 작업을 통해 가이드의 완성도를 빠르게 올리는 것이 중요

## 2.2 노하우

**용어**
- `HOLD`
  - 작업 진행 X, 이미지 전체를 제외
- `Points`
  - 글자 영역에 대한 표시 방법
- `Transcription`
  - Points 안에 존재하는 글자 시퀀스
- `lilegibility`
  - 글자를 정확히 알아보기 힘들 경우 모델이 의도적으로 무시하도록 표시
  - 영역 단위의 처리, transcription 대상이 되는 Points처럼 타이트하게 영역을 지정할 필요 없음
- Image_Tags
  - 이미지 자체에 특이사항이 있는 경우
- Word_Tags
  - 글자 영역의 특이사항이 있는 경우
- \<UNK\>
  - 글자 영역 내에 글자가 있지만 특수하거나 출력이 어려운 글자의 경우
  - 특수기호, 한글이나 알파벳이 아닌 글자

**Annotation 규칙**
1. 구부러진 글자 영역
  - 짝수개의 점들로 이루어진 polygon 형태의 Points : (위 6개 + 아래 6개)12개로 제한
  - 글자의 위아래에 점이 쌍을 이루게 하여, 점들의 기준으로 사각형 모양의 박스가 만들어지도록

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/162674993-914a8b33-b0e5-443e-ad48-95aba5e1a0b6.png" width="50%"></p>

2. BBOX 작업방식 정의 : 진행 방향 및 그에 따른 좌표 순서

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/162675070-b62cb5de-96ac-469a-b568-9fe85ba5ba1e.png" width="50%"></p>

3. 작업 불가 영역
  - 글자를 알아보기 어려울 정도로 밀도가 높거나, 글자가 일부 뭉개져서 알아보기 어려운 영역에 대해서 `illegibility : True`
  - 글자가 겹쳐져 있어서 육안 상 글자를 정확하게 입력할 수 없다면 `illegibility : True`
  - `illegibility : True`인 영역은 tight하게 영역을 지정할 필요 없음
  - 글자와 유사하지만 글자가 아닌 경우에는 Points 표기하지 않음

**가이드라인에서의 우선순위**
1. 읽을 수 있는 글자 영역 전부 Points 표시
2. Points 표시의 일관성 유지 및 transcription 정확히 하기
3. 글자는 존재하지만 육안상 알아보기 어려운 `illegibility : True` 영역 ("don't care") annotation
4. 각종 태그
  - 언어, 글자 진행 방향, 이미지 태그 및 단어 태그
