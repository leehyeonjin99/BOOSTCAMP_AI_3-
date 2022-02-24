- String으로 Class를 불러올 수 있을까?
[[python] 문자열을 파이썬 클래스 객체로 변환 하시겠습니까?](http://daplus.net/python-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%9E%98%EC%8A%A4-%EA%B0%9D%EC%B2%B4%EB%A1%9C-%EB%B3%80%ED%99%98-%ED%95%98%EC%8B%9C%EA%B2%A0%EC%8A%B5%EB%8B%88/)

  - class가 같은 창에 있을 경우 : eval("ClassName")
  - class가 외부에 있는 경우 : getattr(import_module("class가 있는 모듈"),"ClassName")
