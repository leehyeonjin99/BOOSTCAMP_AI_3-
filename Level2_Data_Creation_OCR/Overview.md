<p align='center'><img width="1089" alt="image" src="https://user-images.githubusercontent.com/57162812/164155487-92a3fc56-ae17-4746-8396-2006cd1550c2.png"></p>

스마트폰으로 카드를 결제하거나, 카메라로 카드를 인식할 경우 자동으로 카드 번호가 입력되는 경우가 있습니다. 또 주차장에 들어가면 차량 번호가 자동으로 인식되는 경우도 흔히 있습니다. 이처럼 OCR (Optimal Character Recognition) 기술은 사람이 직접 쓰거나 이미지 속에 있는 문자를 얻은 다음 이를 컴퓨터가 인식할 수 있도록 하는 기술로, 컴퓨터 비전 분야에서 현재 널리 쓰이는 대표적인 기술 중 하나입니다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/164155783-e6006818-6c6e-4d3b-a98c-c72bcdd7b311.png" width="50%"></p>

OCR task는 글자 검출 (text detection), 글자 인식 (text recognition), 정렬기 (Serializer) 등의 모듈로 이루어져 있습니다. 본 대회는 아래와 같은 특징과 제약 사항이 있습니다.

- 본 대회에서는 '글자 검출' task 만을 해결하게 됩니다.

- 예측 csv 파일 제출 (Evaluation) 방식이 아닌 model checkpoint 와 inference.py 를 제출하여 채점하는 방식입니다. (Inference) 상세 제출 방법은 AI Stages 가이드 문서를 참고해 주세요!

- 대회 기간과 task 난이도를 고려하여 코드 작성에 제약사항이 있습니다. 상세 내용은 베이스라인 코드 탭 하단의 설명을 참고해주세요.

- **Input** : 글자가 포함된 전체 이미지

- **Output** : bbox 좌표가 포함된 `UFO Format`
  > UFO Format
  > ```python
  > {
  >     "images" : {
  >         "X_google_058.jpg" : {
  >             "words" : {
  >                 "0" : {
  >                     "points" : [
  >                       [
  >                         0,
  >                         0
  >                       ],
  >                       [
  >                         100,
  >                         100
  >                       ],
  >                       [
  >                         200,
  >                         200
  >                       ],
  >                       [
  >                         300,
  >                         300
  >                       ]
  >                     ]
  >                 }
  >                 "1" : {
  >                     "points" : [
  >                       [
  >                         0,
  >                         0
  >                       ],
  >                       [
  >                         100,
  >                         100
  >                       ],
  >                       [
  >                         200,
  >                         200
  >                       ],
  >                       [
  >                         300,
  >                         300
  >                       ]
  >                     ]
  >                 } 
  >             }  
  >         }    
  >     }
  > }


## Data

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/164157121-21d145a0-2d2f-41a8-911a-f5d7f56f20bd.png" width="30%"> <img src="https://user-images.githubusercontent.com/57162812/164157372-6de862b9-4900-4cf9-83ed-d2c5597da199.png" width="30%"></p>

- 학습 데이터는 기본적으로 "ICDAR17_Korean"이라는 이름의 데이터셋이 제공됩니다.
- ICDAR17_Korean 데이터셋은 ICDAR17-MLT 데이터셋에서 언어가 한글인 샘플들만 모아서 재구성한 것으로 원본 MLT 데이터셋의 부분집합입니다.
- 본 대회는 데이터를 수집하고 활용하는 방법이 주요 내용이기 때문에, 성능 향상을 위해 공공 데이터셋 혹은 직접 수집한 데이터셋을 추가적으로 이용하는 것을 제한하지 않습니다.
