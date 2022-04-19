# DBNet
Real-tim Scene Text Detection with Differentiable Binarization
## Introduction
**Segmentation 기반의 방법**

- 👍🏻 good : 다양한 모양의 텍스트를 유연하게 잡아낸다.  
- 👎🏻 bad : 인접한 개체 구분이 어렵다.

<p align='center'><img width="594" alt="image" src="https://user-images.githubusercontent.com/57162812/163914806-f8a997fb-b23f-4346-8706-ce14b2eca8a0.png"></p>

**Pixel Embedding**
- 글자 영역별로 같은 영역 내의 화소끼르는 가깝게, 다른 영역의 화소끼리는 멀게 pixel embedding을 학습시켜, 글자 영역을 결정짓기 위한 후처리 작업에 pixel embedding 정보를 기반으로 clustering 기법 사용

<p align='center'><img width="528" alt="image" src="https://user-images.githubusercontent.com/57162812/163915998-2e0e9a54-2a2c-4d76-8c07-3b8512c249f1.png"></p>

- 네트워크의 출력 : `글자 영역` + `글자 영역의 중심` + `Pixel Embedding`

<p align='center'><img width="637" alt="image" src="https://user-images.githubusercontent.com/57162812/163916351-a6b9ca67-42f1-4ae9-8f96-28aeb9abd78f.png"></p>

**Progressive Scale Expansion(PSENet)**

- 반복적으로 글자 영역 중심으로 줄여나가, text의 center line에 가까운 영역을 추정 

<p align='center'><img width="571" alt="image" src="https://user-images.githubusercontent.com/57162812/163916469-f14bf30d-8db9-48b6-9dde-56bb2152a6d2.png"></p>

- 작은 영역부터 글자 영역을 확정지은 뒤, 차례로 다음 map 정보를 활용하여 글자 정보를 키워나가고 구분하다.

<p align='center'><img width="636" alt="image" src="https://user-images.githubusercontent.com/57162812/163916908-9e26a2b0-eb9a-47d6-985f-e95a794d91e9.png"></p>

**DBNet**

- 💡IDEA : 글자 영역 구분에 threshold 갑을 이미지 별로 모델이 알아서 정하도록 하자.
- 모델 출력 : `각 pixel이 글자 영역에 속할 확률값` + `이미지에 각 pixel별로 적용한 임계치`

> **임계치를 예측하는 방법은?**
>
>*”경계선 부분에서는 더 높은 값으로 임계치를 적용하면 영역 구분이 잘 되지 않을까?”* 

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163979801-3000f0da-8959-4d38-9087-7d277c83af1e.png" width="40%"></p>


1. `Won’t`와 `Will`과 같이 글자 영역이 가까이 있는 경우 임계치가 너무 낮으면 두 글자 영역이 하나로 합쳐질 수 있다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980209-b3336c4d-adba-4214-950d-b28c3518236e.png" width="60%"></p>

1. `Won’t`의 경우 임계치가 너무 높으면 한 글자 영역이 여러개로 나눠질 수 있다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980347-ea0a6a26-830e-4183-937c-cedf63c9eadd.png" width="60%"></p>


## Adaptive Thresholding

즉, 글자 영역 경계부분에서만 높은 임계치를 적용하고, 나머지 영역은 낮은 임계치를 적용한다.

## Differentiable Binarization

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980448-ac3ab01f-943e-4b59-9e1f-7442618b1f27.png" width="60%"></p>

## Training

**Loss function**

- Segmentation map, Binaryzation map : GT probability와 BCE loss 구성
- Threshold map : GT threshold map과 L1 loss 구성

# MOST

A Multi-Oriented Scene Text Detector with Localization Refinement

**EAST**

- 👍🏻 good : 단순하고 빠르다
- 👎🏻 bad : 종횡비가 큰 이미지에 대해 성능이 많이 떨어진다.
    - Receptive field의 한계
    - LA-NMS의 문제점

**MOST**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980553-49a98a5e-6198-46f7-9712-3d835e8b577c.png" width="60%"></p>

- Text Feature Aligned Module
    
    receptive field의 제약을 없애기 위해 Coarse Detections으로 대략의 위치를 알아낸 후 그에 맞게 Receptive field를 재조정하여 NMS 전 최종 검출 결과 확보
    
- Position-Aware NMS
    
    NMS에 필요한 글자 영역 내 화소들의 상대 위치 정보를 받아서 검출 결과에 PA-NMS 적용
    

## TFAM

- Localization Branchdp whswo
- Input : EAST의 geometry map의 출력 = ${W/4}\times{H/4}\times{5}(상,하,좌,우 텍스트 경계까지의 거리 및 각도)$

***Localization-based LB sampling***

- 글자 영역에 맞춰지는 방향으로 receptive field가 맞춰져 종횡비가 큰 경우에도 예측이 가능해진다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980691-c59a21a3-1a29-4eaa-9074-709c384090b9.png" width="60%"></p>

## Position-Aware NMS(PA-NMS)

**Locality-aware NMS**

- EAST에서 고안
- ROW first order로 detection bbox에 대한 merging
- 한계점
    
    Geometry map : 예측 점이 실제 경계에서 멀리 있을 수록 정확도가 낮아진다.
    
    <p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980790-372fc49a-633e-4704-8ca5-52308985871a.png" width="60%"></p>
    

**Position-Aware NMS**

- 실제 경계에서 가까운 곳에서 예측한 정보일수록 가중치를 많이 주자

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980865-2f44f987-5199-4a5a-8084-a0e16b39fe72.png" width="60%"></p>

## Training

**IoU loss** : 크기가 큰 텍스트는 더 많은 positive samples 포함, 즉 `bias` 발생

**Instance-wise IoU loss** : IoU loss에 텍스트 개체의 크기에 대한 정규화, 즉 기존 IoU loss와 weighted sum으로 섞어서 이용함.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163980943-c993701e-9309-42c8-b8e6-463917c01713.png" width="60%"></p>

# TextFuseNet

Scene Text Detection with Richer Fused Features

## Introduction

- 기존 **instance segmentation** 기반의 방법
- 일반 객체 검출의 `Mask RCNN`을 글자 영역 검출로 적용시킨 방법
    - `RPN`을 통해 text region proposal 추출
    - `RoI Align`을 거친 후, 각 RoI에 대하여 Faster RCNN을 거쳐 글자 영역 확인 및 bbox 정보를 추출한다.
    - 글자 종류를 뽑는 방식에는 2가지가 있다.
        1. `character segmentation` 기법 : 글자 영역 내의 글자가 무엇인지 instance segmentation 기반의 기법
        2.  글자 인식기에서 `Decoder` 부분만 붙여서 글자값을 뽑아낸다. 
        
        방식이 두가지 이므로, score 기반의 병합이 진행된다. 
        

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163981038-41c30571-73ef-46b6-a4bf-5e1149086702.png" width="60%"></p>

- 글자 영역부터 글자 종류까지 예측 가능한 end-to-end OCR이 가능해진다.

**대표적 실패 사례**

- 글자가 끊어지는 경우 다시 합치기 어렵다.
- 단어 기반, 즉 글자 기반의 한계
    
    <p align="center"><img src="https://user-images.githubusercontent.com/57162812/163981143-c9c97b73-88db-4bc1-a8c8-2eef4f4dadff.png" width="60%"></p>
    

## Multi-Level Feature

- semantic segmentation branch에서 global level feature를 추출한다.
    
    > **global level feature**
    이미지 전체에서 글자 영역을 추출하는 task를 수행하는 특징 map
    > 
- RPN과 RoI Align에서 global level feature을 사용하여 글자 영역과 글자 위치를 검출한다.
- mask branch에서 `Global`, `Word`, `Char` level feature를 활용하여 글자 영역 추출과 글자 추출 task를 수행한다.

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/163981217-9d1b2a6d-8e73-4e54-b41d-d22453d8f00a.png" width="60%"></p>

**Weakly supervised learning**

- Detection branch 학습에 character-level annotation이 필요하다.
    1. SyntText (full-supervision) pretraining
    2. Pseudo labeling
        
        GT 단어 영역의 넓이에 비해 예측 영역과 GT 단어 간에 겹치는 영역의 넓이가 80% 보다 큰 pseudo label만 학습에서 사용
        
    3. Fine-tuning
