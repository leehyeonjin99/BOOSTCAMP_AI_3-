`segmentation` : CNN구조는 channle의 정보를 encoding한다.

**Structure**

![image](https://user-images.githubusercontent.com/57162812/158006469-8087ade3-07e6-48ae-97bd-a867e1a3cf48.png)


**Grammer**

- Upsampling
  ```python
  torch.nn.Upsample(scale_factor=16, mode='bilinear', align_corners=False)
  ```
  Backbone을 통해서 Downsampling된 이미지에 대해서 Segmentation을 하기 위해서는 원본 이미지 크기로 Upsampling이 필요하다.
  <img src="https://user-images.githubusercontent.com/57162812/158006677-d0dcb155-a458-4b0c-962c-f7f0755eed66.png" width="70%">

  
- fc layer의 weight를 fully convolution layer의 weight에 copy
  ```python
  reshaped_fc_out = fc_out.weight.detach()
  reshaped_fc_out = torch.reshape(reshaped_fc_out, (7,512,1,1))
  self.conv_out.weight = torch.nn.Parameter(reshaped_fc_out)
  ```
  Conv layer의 weight는 (512,7,1,1)이며 FC layer의 weight는 (512,7)이다. FC layer의 weight parameter 수와 Conv layer의 weight parameter 수는 같기 때문에 reshape를 통해서 copy해줄 수 있다.
 
- highlight 부분 골라내기
  ```python
  res = modelS(img)[0] # activation map

  heat = res[label[0]] # ground truth chanel의 activation map
  resH = heat.cpu().detach().numpy() 
  heatR, heatC = np.where(resH > np.percentile(resH, 95)) # activation map의 상위 5%의 값을 가지는 위치 -> dim=0 위치, dim=1 위치
  
  seg = torch.argmax(res, dim=0) # 각 pixel별 channel의 값 중 가장 큰 값을 가진 channel
  seg = seg.cpu().detach().numpy() 
  [segR, segC] = np.where(seg == np.int(label[0].cpu())) # 가장 큰 값을 가진 channel이 ground truth channel인 위치 -> dim=0 위치, dim=1 위치

  resS = np.zeros((224,224))
  for i, r in enumerate(heatR):
    c = heatC[i]
    if (r in segR) and (c in segC):
      resS[r,c] = 1 # channel중 가장 큰 값이 ground truth channel이면서 상위 5%의 값을 가지는 위치를 hightlight 하겠다.
  ```

