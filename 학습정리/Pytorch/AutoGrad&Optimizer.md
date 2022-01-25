# Pytorch_Structure

## AutoGrad&Optimizer

### [torch.nn.Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html?highlight=torch%20nn%20module#torch.nn.Module)

- 모든 neural network modules의 basic class이다. 즉, deep learning을 구성하는 layer들의 basic class이다.
- Input,Output, Forward, Backward를 정의한다.
- 학습의 대상이 되는 parameter를 정의한다.

```pyhton
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))
```

### [torch.nn.Parameter](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter)
- module parameter로 여겨지는 Tensor의 한 종류이다.
- Parameter은 Tensor의 subclass이다.
- parameters
  - data : Tensor
  - requires_grad : bool : if the parameter requires gradient
  
```python
class Liner(nn.Module):
    def __init(self, in_feature, out_feature, bias=True):
        super().__init__()
        self.out_feature=out_feature
        self.in_feature=in_feature
        self.weight=nn.Parameter(torch.randn(in_feature,out_feature))
        if bias:
            self.bias=nn.Parameter(torch.randn(out_feature))
        else:
            self.bias==nn.Parameter(torch.zeros(out_feature)
        
    def forward(self,x:Tensor):
        return x@self.weight+self.bias
```

### [Backward](https://pytorch.org/docs/stable/generated/torch.Tensor.backward.html?highlight=backward#torch.Tensor.backward)

- Layer에 있는 각 Parameter에 대하여 미분을 수행
- DL에서는 예측값(Forward의 결과값)과 실제값간의 Loss에 대해 미분을 수행하여 Parameter의 값을 업데이터 해준다.

```python

for epoch in range(epochs):
    optimizer.zero_grad() # 초기화 : 이전의 gradient값이 현재의 gradient값에 영향을 미치지 않기 위한 작업
    outputs=model(input) # 예측값
    loss=criterion(outputs,labels) # 손실함수에 따른 loss 측정
    loss.backward() # parameter에 대한 loss의 미분값
    optimizer.step() # parameter값 업데이트
    
```

