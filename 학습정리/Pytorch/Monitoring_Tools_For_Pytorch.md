# Monitoring Tools For Pytorch

## Tensorboard
- TensorFlow의 프로젝트로 만들어진 시각화 도구
- Pytorch와의 연결이 가능
- 학습 그래프, metric, 학습 결과 시각화 지원

### 저장하는 값들
- scaler : accuracy, loss, precision, recall과 같은 상수값을 epoch의 단위로 표시
- graph : computational graph 표시
- histogram : weight와 같은 값의 분포 표시
- image, text : 예측값과 실제값을 비교 표시
- mesh : 3차원 형태의 데이터 표현

```python
# Tensorboard 기록을 위한 directory 생성
import os
logs_base_dir="logs"
os.makedirs(log_base_dir, exist_ok=True)

# 기록 생성 객체 SummaryWriter 생성
from torch.utils.tensorboard import SummaryWriter
writer=SummaryWriter(log_base_dir)

# 기록
for n_iter in range(100):
    # Loss/trin : loss category에 train값
    # n_iter : x축
    writer.add_scaler('Loss/train',np.random.random(),n_iter)
    writer.add_scaler('Loss/test',np.random.random(),n_iter)
writer.close()
```

```python
for i in range(100):
    # log_base_dir 밑에 run_14h_xsin 파일 생성 후 로그 기록
    writer.add_scalars('run_14h', {'xsinx':i*np.sin(i/r),
                                    'xcosx':i*np.cos(i/r),
                                    'tanx': np.tan(i/r)}, i)
writer.close()
```

### tensorboard 실행 방법
```python
# 1
%load_ext tensorboard
# 2
%tensorboard --logdir{log_base_dir}
```

## Weight&bias
- 머신러닝 실험을 워놜히 지원
- MLOps의 대표적인 툴

 
```python
congif={"epochs" : EPOCHS, "batch_size" : BATCH_SIZE, "learing_rate" : LEARNIGN_RATE}
wandb.init(project="my-test-project", config=config)
```
- you could add `wandb.init()` to the beginning of your training script as well as your evaluation script, and each piece would be tracked as a run in W&B.

```
# tensorboard의 add_ 함수와 동일
wandb.log({"accuracy":train_acc,"loss":train_loss})
```
