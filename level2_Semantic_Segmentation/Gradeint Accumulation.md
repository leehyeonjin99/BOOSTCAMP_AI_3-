# Gradient Accumulation
**목적** : 큰 모델 학습 시 `배치 사이즈`를 늘리는 효과를 볼 수 있다.
- 단일 GPU로 학습하는 경우 메모리에 제한이 있어 큰 배치 사이즈를 가지지 못한다.
- 병렬 16개의 GPU로 1024의 배치 사이즈를 처리하는 경우 배치 사이즈를 64로 나누어 처리할 수 있다.
- 큰 배치 사이즈를 사용하는 이유는 학습시에 `정보의 노이즈를 제거`하고 더 나은 gradient descent를 수행할 수 있다.

> 하지만, 매우 큰 배치 사이즈는 SGDㄱ 수렴되느 속도와 최종 모델의 성능에는 부정적이 형향을 끼친다.

## 동작 원리

<img src="https://user-images.githubusercontent.com/57162812/167540332-7014eca5-28d7-4019-b2cc-520e4d2eb39c.png" width="80%">

**일반적 방법**
- batch size 만큼의 이미지를 통해서 한번의 `forward pass`, `back propagation`을 진행한다.

**Gradient Accumulation 방법**
- 미니 배치르 통해 구해진 gradient를 n-step동아 global gradient에 누적시킨 후, 한번에 업데이트한다.
  > - batch size = 16
  > - n-step = 16
  > 
  > → batch size 16으로 16번의 gradient 축적을 통해서 한번의 forward/back propagation을 실행하여 batch size 256을 사용하 효과를 얻을 수 있다.

## CODE

**baseline**
```python

for epoch in range(epochs):
  avg_cost = 0
  
  for input, target in train_loader:
    input = input.to(device)
    target = target.to(device)
    
    optimizer.zero_grad()
    hypothesis = model(input)
    loss = criterion(hypothesis, target)
    loss.backward()
    optimizer.step()
    
    avg_cost += cost / len(train_loader)

```

**Gradient Accumulation**
```python
accumulation_step = 10
for epoch in range(epochs):
  avg_cost = 0
  
  for idx, input, target in enumerate(train_loader):
    input = input.to(device)
    target = target.to(device)
    
    optimizer.zero_grad()
    hypothesis = model(input)
    loss = criterion(hypothesis, target)
    loss.backward()
    
    if (idx+1) % accumulation_step == 0:
      optimizer.step()
      model.zero_grad()
      avg_cost += loss / len(train_loader)
    
```

