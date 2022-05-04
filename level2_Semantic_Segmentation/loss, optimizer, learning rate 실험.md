# ✔️ 실험
### 실험 목표
- 해당 task에서 가장 적합한 loss, optimizer, learning rate를 발견할 수 있다.
### 과정
- loss, optimizer, learning rate의 모든 조합을 확인하기에는 시간적인 부담이 있기에 다음과 같이 진행했다.
  - optimizer와 learning rate가 셋 중에서는 가장 높은 상관관계가 있다 생각하여 둘의 조합을 먼저 실험하였다.
  - 그 후, 최적의 optimizer + learning rate의 조합을 이용해 loss를 실험하였다.
- optimizer
  - [ ] Adam
  - [ ] Adamax
  - [ ] ASGD
  - [ ] Adam
- learning rate는 Adam 계열보다 SGD에서 높은 값에서 더 잘 나오는 경향이 있다.
- loss
  - [ ] Cross Entropy Loss
  - [ ] Focal Loss
  - [ ] Dice Loss
  - [ ] Lovasz Loss

- model : `deeplabv3+resnet50` 고정

### 결과

- optimizer + learning rate

|  | optimizer | val mIoU |
| --- | --- | --- | 
| 현진 | adamax(0.00006) | 0.5335 |  
|  | adamax(0.0005) | 0.6132 |  
|  | adamax(0.0001) | 0.6101 |  
|  |  |  |  
| 정균 | ASGD(0.1) | 0.6084 |  
|  | ASGD(0.05) | 0.6215 |  
|  | ASGD(0.01) | 0.5158 |  
|  |  |  |  
| 진혁 | admaw(0.00006) | 0.5315 |  
|  | admaw(0.0005) | 0.4479 |  
|  | admaw(0.0001) | 0.5323 |  

해당 실험에서는 ASGD 0.05에서 가장 높은 val mIoU 값을 가졌다. 해당 learning rate가 비교적 큰 편이기에 local minima에 빠져 수렴이 빠르게 되었을것이라 예상하였지만, 아니었다. learning rate가 큰 만큼 local optima에서도 잘 빠져나올 수 있었으며 더 최적의 loss로 수렴할 수 있었다 생각되어진다. 

- loss 실험
예상의 실험 과정과는 다르게 시간 관계상 중간에 가장 높았던 AdamW 0.0001을 기준으로 loss를 실험하였다.

| decoder loss | auxiliary loss | val miou | LB score |
| --- | --- | --- | --- |
| focal | focal | 0.6027 |  |
| dice | dice | 0.4816 |  |
 | lovasz_loss | lovasz_loss | 0.486 |  |
 | cross entropy | cross entropy | 0.5323 |  |
 | focal | cross entropy | 0.5999 | 0.5928 |
 | focal+cross entropy | focal+cross entropy | 0.6084 | 0.5922 |
 | 0.3 focal + 0.7 dice | 0.3 focal + 0.7 dice | 0.5452 |  |
 | 0.5 focal + 0.5 dice | 0.5 focal + 0.5 dice | 0.5519 |  |
 | 0.6 focal + 0.4 dice | 0.6 focal + 0.4 dice | 0.55 |  |
 | 0.7 focal + 0.3 dice | 0.7 focal + 0.3 dice | 0.5845 |  |
 | 0.8 focal + 0.2 dice | 0.8 focal + 0.2 dice | 0.5819 |  |

해당 실험에서는 다양한 loss를 적용해 보았다. focal loss는 class imbalance에 좋으며 dice loss는 경계 부분을 잘 잡아내는 loss로 알려져 있다. 따라서 이 둘의 조합을 사용한 실험도 진행하였다. 해당 실험에서는 decoder loss에서는 focal loss를 auxiliary loss에는 cross entropy loss를 사용한 실험이 가장 효과적이었다. 이는 합을 이용해 진행한 결과보다 더 좋았다. 이 부분의 해석에 있어서는 더 고민이 필요하다.
