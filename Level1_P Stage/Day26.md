### 시도한 내용
- DeepFace를 이용하여 얼굴을 인식하여 자른 데이터로 학습을 시도했다

### 알게된 내용

- String으로 Class를 불러올 수 있을까?
[[python] 문자열을 파이썬 클래스 객체로 변환 하시겠습니까?](http://daplus.net/python-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%9E%98%EC%8A%A4-%EA%B0%9D%EC%B2%B4%EB%A1%9C-%EB%B3%80%ED%99%98-%ED%95%98%EC%8B%9C%EA%B2%A0%EC%8A%B5%EB%8B%88/)

  - class가 같은 창에 있을 경우 : eval("ClassName")
  - class가 외부에 있는 경우 : getattr(import_module("class가 있는 모듈"),"ClassName")

### 시도할 내용
- Multi Classifier를 시도해봐야겠다.
- Age > 60 에 대해서 augmentation을 사용해봐야겠다
- 사람을 구분하여 train, valid를 나누면 새로운 사람을 Test 때 볼 수 있어 Evaluation 환경과 비슷해질 수 있고, random 하게 split하면 더 많은 사람을 확인할 수 있다. 과연 어떤 것이 더 좋을까?
- 제출 시에는 가장 좋았던 모델을 train/val 로 나눈 것이 아니라 모든 data에 대해서 학습시킨 후에 제출해보는 것은 어떨까?
