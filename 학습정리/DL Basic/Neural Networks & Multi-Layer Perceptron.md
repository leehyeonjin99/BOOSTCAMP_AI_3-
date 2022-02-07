## Neural Networks
- Neural Network?
  - computing systems vaguely inspired by the biological neural networks that constitute animal brain
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/152762657-383d67fd-a5e8-4ccf-8b49-fbc0a636e6d0.png" width=300></p>

  - 하지만 인간의 지능을 모방하고 싶다고 해서 뉴런과 똑같이 이행될 필요는 없다.
    - why? 하늘을 날고 싶다고 해서 비행기가 새와 똑같이 생겨야 할 필요는 없다.
    <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152762795-8a16d015-27ca-4bfc-bc37-3e0fad7b6a4a.png" width=400></p>
    
  - Neural Network란 affine transformation과 nonlinear transformations이 반복적으로 일어나는(stack) function approximators
    - 데이터→모델→레이블

## Linear Neural Networks

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/152763281-2cc151a7-1066-4509-a13b-930e1ba65f8d.png" width=300></p>

<img src="https://user-images.githubusercontent.com/57162812/152763382-9bae8374-d1a9-46af-9d9d-1533e6296934.png" width=200></p>

- back propagation을 통한 partial derivative로 model의 Loss를 최소화 하는 Parameter를 학습한다. 

  - partial derivate w.r.t. **W** <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152763672-86fe16aa-918f-4d40-a52c-1eca1cefe983.png" width=250></p>  
  - partial derivate w.r.t. **b** <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152763889-caf1a663-610e-40e7-8027-af62cab4c6a8.png" width=250></p>
  - iteratively update the optimization variables <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152764497-b51c6d63-0243-4d1b-a4d8-ee992ae945f8.png" width=250></p>


- multi dimensional iput과 output에 대해서도 가능하다.
<p align="center"><img src="https://user-images.githubusercontent.com/57162812/152764635-1fb49019-ee87-4552-9ce3-4cd075fb2b27.png" width=300></p>

  - W 행렬의 의미 : 두개의 vector space 간의 선형 변환
  - 계속해서 쌓아가면 어떨까? : 또 다른 matrix를 만들어 낼뿐 여전한 선형 변환이다. <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152764913-2dc39adb-795e-4066-aba9-4eabfd8ba763.png" width=300></p>
  - 따라서, nonlinearity가 필요하다. : 활성화 함수 <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152765018-d3def7b2-e7e5-4625-b210-6a678a9aebda.png" width=300></p>
    - 활성화 함수 <p align="center"><img src="https://user-images.githubusercontent.com/57162812/152765133-30d5553e-d41b-4c29-9eea-e711caa9b64a.png" width=460></p>

## Multi-Layer Perceptron

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/152765419-a8e05b17-3c19-432b-95ae-f78c255ed874.png" width=350></p>

- Loss Functions?  
<img src="https://user-images.githubusercontent.com/57162812/152765744-11eaca17-f866-4718-b8f9-67111dab2a26.png" width=500></p>
