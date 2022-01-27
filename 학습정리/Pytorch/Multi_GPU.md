# Multi_GPU

### 개념 정리
- Single vs Multi  

  ▶ Single :  1개  
  ▶ Multi : 2개 이상
- GPU vs Node  

  ▶ Node(=System) : 컴퓨터 개념  
  EX) 1대의 Node에 1대의 GPU를 사용한다.  
- Single Node Single GPU  

  ▶ 1대의 Node에 1대의 GPU  
- Single Node Multi GPU  

  ▶ 1대의 Node에 여러대의 GPU    
  <img src="https://user-images.githubusercontent.com/57162812/151361115-4af80329-0294-471f-ac9e-033f3f241a1c.png" width=150>
- Multi Node Multi GPU  

  ▶ 여러대의 Node에 여러대의 GPU  
  <img src="https://user-images.githubusercontent.com/57162812/151361381-47665570-cde1-45d8-b00c-365e125be73f.png" width=200>

### Model Parallel
- 다중 GPU에 학습을 분산하는 방법

  1️⃣ 모델 나누기 ex) alexnet  
  
    ![image](https://user-images.githubusercontent.com/57162812/151363044-931b582e-aff6-4cd7-a95f-7cad8d654fed.png)
      
    ▶ In this case, **only one GPU functions at a time**.This results in a **longer duration of training cycles** due to **inter-GPU communications** (during theforward and backward propagation phases)
      
    ![image](https://user-images.githubusercontent.com/57162812/151363394-9fbfacd7-c879-41b6-ab14-56df307a0463.png)

     ▶ **Pipeline distribution** of the model with splitting of the data batches, which enables the CPUs to work **concurrently**. As a result, **the execution time is reduced** to the equivalent in mono-GPU.
     
  → 모델의 병목, 파이프라인의 어려움 등으로 인해 모델 병렬화는 고난이도 과제가 되었다.
      
  2️⃣ 데이터 나누기
  
    ![image](https://user-images.githubusercontent.com/57162812/151364380-ab815801-28e4-470c-a14f-f6d56fd6e676.png)
    
    ▶ Forward and Backward passes with Data Parallel : Taking average of the loss and gradient after sharing data to each of the GPU.

#### Model Parallel

```python
class ModelParallelResNet50(ResNet):
    def __init__(self, *arg, **kwarg):
        super(ModelParallelResNet50, self).__init__(Bottleneck,[3,4,6,3], num_classed=num_classes, *args, **kwargs)
        
        # 첫번째 모델을 cuda 0 에 할당
        self.seq1=nn.Sequential(self.conv1, self.bn1, self.relu, self.maxpool, self.layer1, self.layer2).to('cuda:0')
        
        # 두번째 모델을 cuda 1 에 할당
        self.seq1=nn.Sequential(self.layer3, self.layer4, self.avgpool).to('cuda:1')
        
        self.fc.to('cuda:1')
        
    def forward(self, x):
        x=self.seq2(self.seq1(x).to('cuda:1'))
        return self.fc(x.view(x.size(0),-1))
```

▶ 단순히 모델을 연결해주었기 때문에 병목 현상이 발생한다.

#### Data Parallel

- Pytorch에서 두 가지 방식 제공
  - **DataParalle**
  
    ▶ 문제점1. 단순히 데이터를 분배한 후 평균을 취한다. → GPU 사용 불균형으로 폭발 문제가 발생할 수 있다.   
    ▶ 문제점2. GIL(Global Interpreter Lock) : Python code를 실행할 때 여러 thread를 사용할 경우, 단 하나의 thread만이 Python object에 접근할 수 있도록 제한
  - **DistributedParallel** : 각 GPU마다 process를 생성하여 개별 GPU에 할당 → 기본적으로 DataParallel로 하나 개별적으로 연산의 평균을 낸다.

```python
train_sampler=torch.utils.data.distributed.DistrubutedSampler(train_data)
shuffle=False
pin_memory=True

trainloader=torch.utils.data.DataLoader(train_data, batch_size=20, shuffle=True, pin_memory=pin_memory, num_workers=3, shuffle=shuffle, sampler=train_sampler)

def main():
    n_gpus=torch.cua.device_count()
    torch.multiprocessing.spawn(main_worker, nproc=n_gpus, args=(n_gpus, ))
    
def main_worker(gpu, n_gpus):
    image_size=224
    batch_size=512
    num_worker=8
    
    batch_size=int(batch_size/n_gpus)
    num_worker=int(num_worker/n_gpus)
    
    # 멀티 프로세싱 통신 규약 정의
    torch.distributed.init_process_group(...)
    
    model=MODEL
    
    torch.cuda.set_device(gpu)
    model=model.cuda(cpu)
    # Distributed DataParallel 정의
    model=torch.nn.parallel.DistributedDataParallel(model, device_ids=[gpu])
