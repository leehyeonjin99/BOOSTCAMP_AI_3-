## 시도한 내용
- 한 사람에 대해서 train과 valid dataset에 나눠지지 않도록 하였다
- resnet, efficientnetb4 네트워크 사용

## 알게된 사실
- dataloader의 parameter인 num_workers에 따라 acc값이 달라졌다.
- 모델을 한번 훈련시킬 때 마다 gpu에 메모리가 남아있기 때문에 재실행해야한다. : Cuda Out of Memory 에러 발생
## 시도할 내용
- 다양한 Loss 함수 
