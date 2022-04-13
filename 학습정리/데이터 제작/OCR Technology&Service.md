# OCR Technology
## OCR
OCR `optical character recognition` → STR  `scene text recognition` (scene 속의 모든 글씨 인식) 성능 향상

OCR = `글자 영역 찾기` + `영역 내 글자 인식`

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163227218-0ebb0136-d63d-470b-845f-64c7affc234d.png" width="60%"></p>

- offline OCR : 이미지 입력 → 글자값 출력
- online OCR : 좌표 시퀀스 입력 → 글자값 출력

## Text Detector
글자 검출기 = 글자 영역 다수 객체 검출 → (글자 O/X) 단일 클래스 문제

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163227506-d79588f6-4fe8-478f-b3c7-2e78ee5c2f56.png" width="60%"></p>

객체 검출과의 차이점?
1. 영역의 종횡비
2. 객체 밀도

## Text Recognizer
글자 인식기 = 하나의 글자 영역 이미지에 해당 영역 글자열을 출력

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163227784-39f97766-0b26-4729-82aa-85d73e5d2602.png" width="60%"></p>

글자 인식기 ∈ CV ⋂ NLP

why? 이미지 입력으로부터 글자열을 출력하기 때문

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163227963-6b9f3a5c-513c-4bf7-9851-483c7e801f21.png" width="60%"></p>

ex. 유사한 task : `Image Captioning` 이미지를 설명하는 text 생성

## Serializer

정렬기 : OCR 결과값을 자연어 처리하기 편하게 일렬로 정렬하는 모듈

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163228238-647877ac-e416-432b-b170-2b8151b658cc.png" width="60%"></p>

자연어 처리 모듈
1. 금칙어 처리
2. 요약
3. 글자 의미 파악

## Text Parser
자연어 처리 모듈 중에서 가장 많이 사용되는 것은 기 정의된 key들에 대한 value 추출

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163228612-9cc2c195-1c6e-4d8d-b210-c96d3236fca6.png" width="70%"></p>

BIO 태깅을 활용한 개체명 인식
- B : begin
- I : inside
- O : outer

# OCR Service
1. Copy & Paste
2. + Search
3. + Matching : ex. 이미지를 통해 뮤직 플레이리스트 옮기기
4. + 금칙어 처리
5. + 번역

