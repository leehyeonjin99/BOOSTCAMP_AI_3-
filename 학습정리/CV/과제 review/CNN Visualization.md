**Grammer : Visualizing Conv1**

- model의 parameter들
  ```python
  for name, module in model.named_parameters():
  names = name.split(".")
  if "backbone" in name:
    n = names[1]
  else:
    n = names[0]
  ```
  Classifer model에 `self.backbone = VGG11Backbone()`을 선언하였기 때문에 backbone의 parameter들은 backbone.modeul_name으로 name이 지정되고, 그 외에 Classifier model에서 생성된 Module들은 module_name으로 name이 지정된다.
  
- model의 module들
  ```python
  for name, module in model._modules.item(): 
    module_num += get_module_params_num(module)
  ```
  model의 modules는 backbone, gap, fc_out의 이름과 module을 반환한다.

**Grammer : Visualizing Model Activation**
- filter plot 하기
  ```python
  def plot_filters(data, title=None):
    """
    Take a Tensor of shape (n, K, height, width) or (n, K, height, width)
    and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)
    """
    
    # 만약 data의 channel 수가 4 이상이라면, resoultion을 유지하되 channle을 1로 reshape하자. (64,3,3,3)
    if data.size(1) > 3:
      data = data.view(-1, 1, data.size(2), data.size(3))
        
    data = image_tensor_to_numpy(data) # imshow(data)를 위해서 numpy로 설정 후 channel의 위치를 바꾼다. permute(0,2,3,1)
        
    # data를 MinMaxNormalize 진행
    data = (data - data.min()) / (data.max() - data.min())
    
    # force the number of filters to be square (n=2)
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),   # filter의 개수를 제곱수로 맞춰준다. why?
               (0, 2), (0, 2))                 # 오른쪽 2열 추가, 아래 2행 추가
               + ((0, 0),) * (data.ndim - 3))  # 마지막 dimension(channel dimmension)에는 추가하지 않는다.
    data = np.pad(data, padding, mode='constant', constant_values=1)  # padding에 대해 1로 채운다. (64,5,5,3)
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1))) # reshape : (8,8,5,5,3) → transpose : (8,5,8,5,3)
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:]) # (40,40,3)
    data = data.squeeze() # (40,40,3)
    
    # plot it
    plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.title(title)
    plt.imshow(data)
    ```
    ![image](https://user-images.githubusercontent.com/57162812/158024397-589a7581-a90b-410b-b065-1bc1a0650cd4.png)

- `functools.parial()` : 기존 파이썬 함수를 재사용하여 일부 위치 매개변수 또는 키워드 매개변수를 고정한 상태에서, 원래 함수처럼 작동하는 새로운 부분 객체를 반환한다. 
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158024874-67b43d65-4668-437b-b6d5-df5058f8d657.png" width="50%"></p>

- 중간 layer의 activation map을 Visualization : `register_hook()`, `register_forward_hook()`
  ```python
  def show_activations_hook(name, module, input, output):
    # conv/relu layer outputs (BxCxHxW)
    if output.dim() == 4:
      activation_list.append(output)
      plot_activations(output, f"Activations on: {name}")
      
  # activation map을 확인할, 즉 hook을 등록할 module을 선택한다.
  module_list  = [model.backbone.conv1, model.backbone.bn4_1]
  module_names = ["conv1", "bn4_1"]

  for idx, (name, module) in enumerate(zip(module_names, module_list)):
    hook = functools.partial(show_activations_hook, name) # name 매개변수를 고정
    module.register_forward_hook(hook) # forward를 진행한 후 실행
    
  _ = model(img)
  ```
  
  **Grammer : Visualizing Saliency**
  
  - ground_truth에 대한 gradient 구하기
    ```python
    def compute_gradient_score(scores, image, class_idx):
      """
      Returns the gradient of s_y (the score at index class_idx) w.r.t the input image (data), ds_y / dI. 

      class_idx에 해당하는 class에 대한 gradient인 s_y를 계산해야 합니다.
      전체 class의 개수의 길이를 갖는 scores에서 원하는 index의 score를 s_y로 얻은 다음, 해당 s_y를 back-propagate하여 gradient를 계산하는 코드를 완성해주세요.
      """
      grad = torch.zeros_like(image)
      
      s_y = scores[class_idx] # ground_truth에 대한 logit score값
      s_y.backward() # backward를 통해 s_y에 대한 image의 미분값 계산

      grad = image.grad
      assert tuple(grad.shape) == (1, 3, 224, 224)

      return grad[0]
    ```

- saliency visualization하기
  ```python
  def visualize_saliency(image, model):
    input = Variable(image.unsqueeze(0), requires_grad=True) # batch 단위를 추가하고 미분 가능하도록 requires_grad를 True로 설정
    output = model(input)[0] # batch 단위 제거
    max_score, max_idx = torch.max(output, 0) # class score 중에서 가장 큰 값과 그 index : 추정 class

    grad = compute_gradient_score(output, input, max_idx) # 추정 class에 대한 input(image)의 미분값 

    vis = grad ** 2 # 부호가 아니 변화되어야하는 정도를 파악 (3,224,224)
    vis, _ = torch.max(vis, 0) # 각 channel별 가장 큰 값 및 위치 반환
    
    return vis # (224,224)
 ```
 
**Grammer : Visualizing Grad-CAM**

```python
save_feat=[]
def hook_feat(module, input, output):
  save_feat.append(output)
  return output


save_grad=[]
def hook_grad(grad):
  """
  get a gradient from intermediate layers (dy / dA).
  See the .register-hook function for usage.
  :return grad: (Variable) gradient dy / dA
  """ 
  save_grad.append(grad)
  return grad


def vis_gradcam(vgg, img):
  """
  Imshow the grad_CAM.
  :param vgg: VGG11Customed model
  :param img: a dog image
  output : plt.imshow(grad_CAM)
  """
  vgg.eval()

  # (1) Reister hook for storing layer activation of the target layer (bn5_2 in backbone)
  vgg.backbone.bn5_2.register_forward_hook(hook_feat) # forward 진행시 bn5_2의 ouptut을 save_feat에 저장
  
  # (2) Forward pass to hook features
  img = img.unsqueeze(0) # batch 단위 추가
  s = vgg(img)[0]

  # (3) Register hook for storing gradients
  save_feat[0].register_hook(hook_grad) # bn5_2의 output의 img에 대한 미분값 저장하도록 register_hook
  
  # (4) Backward score
  y = torch.argmax(s).item() # img에 대한 추정값
  s_y = s[y] # 추정값에 대한 score
  s_y.backward()

  # Compute activation at global-average-pooling layer
  gap_layer  = torch.nn.AdaptiveAvgPool2d(1)
  alpha = gap_layer(save_grad[0][0].squeeze()) # grad의 각 channel 별 평균 계산 : channel별 중요도 (512,1,1)
  A = save_feat[0].squeeze() # batch단위 제거 : save_feat[0][0]과 동일 (512,14,14)


  # (1) Compute grad_CAM 
  # (You may need to use .squeeze() to feed weighted_sum into into relu_layer)
  relu_layer = torch.nn.ReLU()

  weighted_sum = torch.sum(alpha*A, dim=0) # 각 channel에 weight를 주어 feat와 곱하여 channel 방향으로 합한다. (14,14)
  grad_CAM = relu_layer(weighted_sum) # 양수만 취급 (14,14)

  grad_CAM = grad_CAM.unsqueeze(0) # (1,14,14)
  grad_CAM = grad_CAM.unsqueeze(0) # (1,1,14,14)

  # (2) Upscale grad_CAM
  # (You may use defined upscale_layer)
  upscale_layer = torch.nn.Upsample(scale_factor=img.shape[-1]/grad_CAM.shape[-1], mode='bilinear') 

  grad_CAM = upscale_layer(grad_CAM) # 원본 이미지의 크기로 Upsampling (1,1,224,224)
  grad_CAM = grad_CAM/torch.max(grad_CAM) # 0-1 사이의 값으로 변경
```
