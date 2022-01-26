# 모델 불러오기

## model.save()
- 학습 결과 저장
  - 모델 형태 저장
  - 모델 파라미터 저장
  - 모델 형태를 저장하게 되면 **코드**를 공유하는것이며, 모델의 파라미터를 저장하게 되면 **결과**를 공유하게 되는 것이다.
- 모델 학습 중간 과정을 저장하여 가장 최적의 결과모델 선택

#### `torch.save()` : 모델 형태 및 파라미터 저장
```python
torch.save(model, os.path.join(MODEL_PATH,"model.pt"))
```

#### `torch.load()` : 모델의 형태와 함께 로드
```python
torch.load(os.path.join(MODEL_PATH,"model.pt"))
```

#### `model.state_dict` : 모델의 파라미터 표시
```python
torch.save(model.state_dict(), os.path.join(MODEL_PATH,"model.pt"))
 ```
 > pt : pytorch에서 모델을 저장할 떄의 저장 확장자

- OrderedDict 객체를 사용하면 모델을 dict type으로 저장 가능하다.

#### `model.load_state_dict` : 모델의 파라미터 로드
```python
new_model=TheModelClass()
new_model.load_state_dict(torch.load(os.path.join(MODEL_PATH,"model.pt")))
```

- 같은 형태의 모델에 대해서만 가능

## checkpoint
- 학습의 중간결과를 저장함으로써 최선의 결과를 선책한다.
- Early Stopping기법 사용시 이전 학습의 결과물을 저장하게 된다.
  - 어떤 일정한 epoch 수를 거듭하면서 계속해서 오차가 증가하면 학습을 중단한다.
- 일반적으로 epoch,loss,metric을 함께 저장하여 확인한다.

#### `torch.save()` : 모델의 정보 저장
```python
torch.save({
            'epoch' : epoch,
            'model_state_dict' : model.state_dict(),
            'optimizer_state_dict' : optimizer.state_dict(),
            'loss' : epoch_less},
           f"saved/checkpoint_model_{e}_{epoch_loss/len(dataloader)}_{epoch_acc/len(dataloader)}.pt")
```

> tip : 모델 정보 저장 파일의 이름에는 모델의 정보를 함께 명시하는 것이 좋다.

#### `torch.load()` : 모델 정보 불러오기
```python
checkpoint=torch.load(PATH)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch=checkpoint['epoch']
loss=checkpoint['loss']
```

## pretrained model : Transfer learning
- 다른 데이터셋으로 만든 모델을 사용
- 대용량의 데이터셋으로 만든 모델을 사용함으로써 적은 데이터셋을 가진 모델에 적용
- backbone architecture가 잘 학습된 모델에서 일부분만 변경하여 학습 수행
  - ex) label의 개수에 따라 nn.Linear()을 추가해준다.
- Freezing : trained model을 활용할 때 모델의 일부분을 frozen 시킨다.
  - frozen된 부분은 back-propagation 진행시 전달되지 않아 파라미터 값이 바뀌지 않는다.
  ![image](https://user-images.githubusercontent.com/57162812/151166222-cbd979e5-7a68-4da4-9401-c48409f309c1.png)\
  
```python
# vgg16 모델을 vgg에 할당
vgg=torchvision.models.vg16(pretrained=True).to(device)

class MyNewNet(nn.Module):
    def __init__(self):
        super(MyNewNet, self).__init__()
        self.vgg19=torchvision.models.vg19(pretrained=True)
        self.linear_layers=nn.Linear(1000,1) #vg모델은 class의 종류가 1000개이며, 개vs고양이 분류 문제에서는 하나의 표현으로 분류 가능하다.
        
    def forward(self, x):
        x=self.vgg19(x)
        return self.linear_layers(x)
     
#  마지막 Linear layer을 제외하고 frozen시킨다.
for param in my_model.parameters():
    param.requires_grad=False
for param in my_model.linear_layers.parameters():
    param.requires_grad=True
```

 - frozen 부분의 for loop은 model을 생성할때 마다 선언해주어야 한다.
