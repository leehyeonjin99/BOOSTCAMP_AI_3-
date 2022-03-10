## Exercise. Autograd
**Saliency test**
 
class score에서부터 input domain의 gradient를 구하는 것이 최종적인 목표로 backpropagation된 gradient를 accumulation하거나 visualization함으로써 salienct map을 구할 수 있다.

**AutoGrad**
- Automatic gradient, Automatic Differentiation
- function의 집합인 API
- DL library들의 고유한 기능
  - DL library들은 많은 Convolution operation이나 DL에 최적화된 operation들을 제공하지만 기본적으로는 행렬 연산을 하는 library
    - 행렬 연산을 하는 DL library는 기존에 많은데 DL library와의 차이점은? **AutoGrad**
    - Autograd는 forward와 backward pass가 가능하게 한다.
    - 다양한 process를 거쳐 하나의 값을 계산에 사용되는 많은 변수들에 대해 gradient를 쉽게 계산할 수 있도록 한다.
    - 과거에는 forward를 backward를 손으로 구현하여 계산하였다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157641184-2d12dacf-287b-430f-820d-612b28cf0d0d.png" width='40%'></p>

terminal node(종말단)에서부터 L에 도달하기까지 어떤 연결성을 가지고 계산이 되었는지를 저장한다. 왜냐하면 backpropagation을 진행하기 위해서!! by **Chain Rule**

**Autograd - Tutorial**
- Automatically computing gradients of y w.r.t x
  ```python
  x = torch.randn(2, requires_grad = True)
  y = x * 3
  gradients = torch.tensor([100, 0.1], dtype = torch.float)
  y.backward(gradeints)
  print(x.grad)
  ```
  ➡ tensor([300.0000, 0.3000])
  
**Autograd - Tutorial(requires_grad)**

`requires_grad`를 True로 해주면 해당 변수의 gradient를 계산하고 저장하기 위함이다. 만약, False로 지정한다면 backward 시에 해당 변수가 gradient를 저장할 수 없기 때문에 RuntimeError가 발생한다.

**Autograd - Tutorial(backward)**

만약 backward를 두번 호출하게 되면 RuntimeError가 발생한다. backward가 한번 호출되면 중간에 계산된 computation graph를 항상 저장하고 있으면 heavy하기 때문에 지워버린다. 즉, 중간 자원들을 버린다. 

Solution으로는 `retain_graph`를 True로 걸어준다. 그렇다면 gradient를 accumulate한다. → 매 batch마다 optimizer.zero_grad()를 하는 이유

**Autograd - Tutorial(grad_fn)**

```python
x = torch.randn(2, requires_grad = True)
y = x * 3
z = x / 2
w = x + y
```

```python
w. y, z
```
➡(tensor([6.2272, 2.3273], grad_fn=\<AddBackward0\>), 
  tensor([4.6704, 1.7455], grad_fn=\<MulBackward0\>), 
  tensor([-.7784, 0.2909], grad_fn=\<DivBackward\>)


`grad_fn`이 어떤 연산의 Backward가 어떻게 구현이 되여야하는지를 생성자를 의미한다.


**hook : register_forward_hook**

어떤 function call을 했을 때 두 개의 component 사이의 message를 낚아채는 것을 hooking이라 한다. 여기서 `register_hook`이라는 것은 backward가 call 될 때, backward 중간의 정보를 빼온다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157647305-376541dd-77ce-4b51-b896-a2571d04f490.png" width='30%'></p>

```python
class SimpleNet(nn.Module):
  def __init__(self):
    self.conv1 = nn.Conv2d(1, 10, 5)
    self.pool1 = nn.MaxPool2d(2, 2)
    self.conv2 = nn.Conv2d(10, 20, 5)
    self.pool2 = nn.MaxPool2d(2, 2)
    self.fc = nn>Linear(320, 50)
    self.out = nn.Linear(50, 10)
 
  def forward(self, input):
    x = self.pool1(F.relu(self.conv1(input)))
    x = self.pool2(F.relu(self.conv2(x)))
    x = x.view(x.size(0),-1)
    x = F.relu(self.fc(x))
    x = F.relu(self.out(x))
    
    return x
```
  
1) hook될 function을 정읳나다.
  ```python
  def hook_func(self, input, output):
  print('inside' + self.__class__.__name__ + 'forward')
  print('')
  print('input :', type(input))
  print('input[0] :', type(input[0]))
  print('output :', type(output))
  print('')
  ```
2) hook을 등록한다.
  ```python
  net = SimpleNet()
  net.conv1.register_forward_hook(hook_func)
  net.conv2.register_forward_hook(hook_func)
  ```
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/157648064-efc27810-a1bc-4bce-93c8-bd870f1c90ac.png" width="20%"></p>

3) forwarding pass가 잔행되면서, hook function은 자동적으로 호출된다.
  ```python
  input = torch.randn(1, 1, 28, 28)
  out = net(input)
  ```
  <img src="https://user-images.githubusercontent.com/57162812/157648435-1b3c3bd2-d371-44a3-98ab-b2071f4d7bd9.png" width="30%"></p>

**register_forward_pre_hook**

forward pass 전에 hook_fun이 실행된다.

```python
def hook_pre(self, input):
  print('inside' + self.__class__.__name__ + 'forward')
  print('')
  print('input :', type(input))
  print('input[0] :', type(input[0]))

net = SimpleNet()
net.conv1.register_forward_pre_hook(hook_pre)

input = torch.randn(1, 1, 28, 28)
out = net(input)
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157649160-29a4a5a4-7e50-4a87-98dc-50acdd6c370d.png" width="20%"></p>

**register_backward_hook**

module input에 대한 gradient가 계산될 때, hook_func가 실행된다.
- 단, grad_input과 grad_output을 변경해서는 안된다.
- 만약 변경하고 싶다면, 선택적으로 return하여 변경시킨다.

```python
def hook_grad(self, grad_input, grad_output):
  print('inside' + self.__class__.__name__ + 'backward')
  print('inside class' + self.__class__.__name__)
  print('')
  print('grad_input :', type(grad_input))
  print('grad_input[0] :', type(grad_input[0]))
  print('grad_output :', type(grad_output))
  print('grad_output[0] :', type(grad_output[0]))

net = SimpleNet()
net.conv1.register_backward_hook(hook_grad)

input = torch.randn(1, 1, 28, 28)
out = net(input)

target = torch.tensor([3], dtype = torch.long)
loss_fn = nn.CrossEntropyLoss()
err = loss_fn(out, target)
err.backward()
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/157650089-027b286b-3041-46b1-8aeb-24f9d05da8f8.png" width="20%"></p>

**remove**

```python
net = SimpleNet()
h = net.conv1.register_forward_hook(hook_func)
input = torch.randn(1, 1, 28, 28)
out = net(input)
```
```python
h.remove()
out = net(input)
```

**Toy activation example**

register_hook으로 중간의 activation을 가져올 수 있다.

1) hook func를 정의한다.

```python
save_feat = []
def hook_feat(module, input, output):
  save_feat.append(output)
  return output
```
모델의 각각의 module들을 for문을 통해 하나씩 방문하여 target layer와 같다면 hook을 등록한다.
```python
for name, module in model.get_model_shortcuts():
  if name == 'target_layer_name':
    module.register_forward_hook(hook_feat)
```

2) Input이 들어오면 forward 한다. forward call을 하면서 target layer를 지나갈 때, feature가 실행이되어 save_feat에 output feature가 저장된다.

```python
img = img.unsqueeze(0)
s = model(img)[0]
```



