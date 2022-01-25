# PyTorch Structure

## Dataset&Dataloader

### model에서의 data 전달 과정

![image](https://user-images.githubusercontent.com/57162812/150978134-c6c7118d-a831-4f30-8c73-d6cb0c95667c.png)

- Dataset, transforms, DataLoader class는 필요에 따라 override 

### Dataset Class
- 데이터 입력의 형태 정의

```
import torch
from torch.utils.data import Dataset

class CustDtasets(Dataset):
    # 초기 데이터 생성 방법
    def __init__(self, text, labels):
        self.labels=labels
        self.text=text
     
    # 데이터 전체 길이
    def __len__(self):
        return len(self.labels)
    
    # index 값을 주었을 때 반환데는 데이터 형태
    def __getitem__(self, idx):
        label=self.labels[idx]
        text=self.text[idx]
        sample={'Text':text,'Class':label}
        return sample
        
```

- Dataset 클래스 생성시 유의점
  - 데이터의 형태에 따라 각 함수들이 달라진다.
  - 모든 것을 데이터 생성 시점 __init__ 에서 처리할 필요 없다. : 학습 시점에 처리하면된다.
  - 최근에는 [HuggingFace](https://huggingface.co/datasets)와 같은 표준화된 라이브러리 사용한다.

### DataLoader Class
- Data의 Batch 생성한다.
- 학습 직전 GPU에게 넘겨주기 전 데이터의 변환을 책임진다.
- Tensor로 변경+Batch 처리

```python
class SimpleCustomBatch:
    def __init__(self, data):
        transposed_data = list(zip(*data))
        self.inp = torch.stack(transposed_data[0], 0)
        self.tgt = torch.stack(transposed_data[1], 0)

    # custom memory pinning method on custom type
    def pin_memory(self):
        self.inp = self.inp.pin_memory()
        self.tgt = self.tgt.pin_memory()
        return self

def collate_wrapper(batch):
    return SimpleCustomBatch(batch)

inps = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)
tgts = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)
dataset = TensorDataset(inps, tgts)

loader = DataLoader(dataset, batch_size=2, collate_fn=collate_wrapper, pin_memory=True)

for batch_ndx, sample in enumerate(loader):
    print(sample.inp.is_pinned())
    print(sample.tgt.is_pinned())
```

-parameters
```python
DataLoader(dataset, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, *, prefetch_factor=2,
           persistent_workers=False)
```
  - collate_fn : merges a list of samples to form a mini-batch of Tensor(s). Used when using batched loading from a map-style dataset.
  - batch_sampler : like sampler, but returns a batch of indices at a time. Mutually exclusive with batch_size, shuffle, sampler, and drop_last.
  - sampler : defines the strategy to draw samples from the dataset. Can be any Iterable with __len__ implemented. If specified, shuffle must not be specified.
