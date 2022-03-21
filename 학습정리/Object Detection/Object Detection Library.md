# Object Detection을 위한 라이브러리
## Overview
- 통합된 라이브러리의 부재
- 실무/캐글에서는 아래 두 라이브러리를 주로 활용
  - MMDetection
  - Detectron2

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159211248-9e8b6d46-8918-4c03-acf4-8e8fb6efd9e8.png" width="60%"></p>

# MMDetectuib
- pytorch 기반의 Object Detection 오픈소스 라이브러리

**Pipeline**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159211562-2cbbd30e-4fae-4a13-9542-ae47a4021c28.png" width="50%"></p>

- config 파일을 이용해 통제한다.
- Backbone : 입력 이미지를 feature map으로 변형
- Neck : backbone과 head를 연결, feature map을 재구성
- DenseHead : feature map의 dense location을 수행
- RoIHead : RoI 특징을 입력으로 받아 box 분류, 좌표 회귀 등을 예측


**Pipeline 미리보기**
- 라이브러리 및 모듈 import하기
  ```python
  from mmcv import Config
  from mmdet.datasets import build_dataset
  from mmdet.models import build_detector
  from mmdet.apls import train_detector
  from mmdet.datasets import (build_dataloader, build_dataset, replace_ImageToTensor)
  ```
  
- config 파일 불러오기
  ```python
  cfg = Config.fromfile('./configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py')
  ```
  
- config 수정하기
  ```python
  classes = {"UNKNOWN", "General trash", "Paper", "Paper pack", "Metal", "Glass",
             "Plastic", "Styrofoam", "Plastic bag", "Battery", "Clothing"}
  
  cfg.data.train.classes = classes
  cfg.data.train.img_prefix = PREFIX
  cfg.data.train.ann_file = PREFIX + 'train.json'
  cfg.data.train.pipeline[2]['img_scale'] = (512, 512)
  
  cfg.data.val.classes = classes
  cfg.data.val.img_prefix = PREFIX
  cfg.data.val.ann_file = PREFIX + 'val.json'
  cfg.data.val.pipeline[1]['img_scale'] = (512, 512)
  
  cfg.data.test.classes = classes
  cfg.data.test.img_prefix = PREFIX
  cfg.data.test.ann_file = PREFIX + 'test.json'
  cfg.data.test.pipeline[1]['img_scale'] = (512, 512)
  
  cfg.data.samples_per_gpu = 4
  
  cfg.seed = 2020
  cfg.gpu_ids = [0]
  cfg.work_dir = './work_dirs/faster_rcnn_r50_fpn_1x_trash'
  
  cfg.model.roi_head.bbox_head.num_classes = 11
  
  cfg.optimizer_config.grad_clip = dict(max_norm = 35, norm_type = 2)
  ```
  
- 모델, 데이터셋 build
  ```python
  model = build_detector(cfg.model)
  datasets = [build_dataset(cfg.data.train)]
  ```

- 학습
  ```python
  train_detector(model, datasets[0], cfg, distributed = False, validate = True)
  ```

## Config File
- configs를 통해 데이터셋부터 모델, scheduler, optimizer 정의 가능
- configs/base/ 폴더에 가장 기본이 되는 config 파일이 존재
  - dataset, model, scheduler, default_runtime
- 각각의 base/ 폴더에는 여러 버전의 config들이 담겨 있다.
  - Dataset : COCO, VOC, Cityscape
  - Model : faster_rcnn, retinanet, rpn

## Dataset

- Data pipeline
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/159232955-d798ca5b-6965-4d7f-b7d7-a630c4470baf.png" width ="100%"></p>

```python
train_pipeline = {
    dict(type = "LoadImageFromFile"),
    dict(type = "LoadAnnotations", with_bbox = True),
    dict(type = "Resize", img_scale = (1333, 800), keep_retio = True),
    dict(type = "RandomFlip", flip_ratio = 0.5),
    dict(type = "Normalize", **img_nrom_cfg),
    dict(type = "Pad", size_divisor = 32).
    dict(type = "DefaultFormatBundle"),
    dict(type = "Collect", keys = ['img', 'gt_bboxes'. 'gt_labels'])
    }
```

## Model
**2stage model**

```python
model = dict(
    # model 유형
    type = "FasterRCNN", 
    
    # Backbone : input image를 feature map으로 변형해주는 network
    backbone = dict( 
        type = "ResNet",
        depth = 50,
        num_stages = 4,
        out_indices = (0, 1, 2, 3),
        frozen_stage = 1,
        norm_cfg = dict(type = "BN", requires_grad = True).
        norm_eval = True,
        stype = 'pytorch',
        init_cfg = dict(type = 'Pretrained', checkpoint = "torchvision://resnet50"))
        
    # Neck : Bakcbone과 head를 연결, feature map을 재구성
    neck = dict( 
        type = "FPN",
        in_channels = [256, 512, 1024, 2048],
        out_channels = 256,
        num_outs = 5),
        
    # RPN_head : Region Proposal Network
    rpn_head = dict(
        type = "RPNHead",
        in_channels = 256,
        feat_channels = 256,
        anchor_generatro = dict(
            type = 'AnchorGenerator',
            scales = [8],
            ratios = [0.5, 1.0, 2.0],
            stride = [4, 8, 16, 32, 64]),
        bbox_coder = dict(
            type = "DeltaXYWHBBoxCoder",
            target_means = [.0, .0, .0, .0],
            target_stds = [1.0, 1.0, 1.0, 1.0]),
        loss_cls = dict(
            type = 'CrossEntropyLoss', use_sigmoid = True, loss_weight = 1.0),
        loss_bbox = dict(type = 'L1Loss', loss_weight = 1.0)),
    
    # RoI Head : Region of Interest
    roi_head=dict(
        type='StandardRoIHead',
        bbox_roi_extractor=dict(
            type='SingleRoIExtractor',
            roi_layer=dict(type='RoIAlign', output_size=7, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        bbox_head=dict(
            type='Shared2FCBBoxHead',
            in_channels=256,
            fc_out_channels=1024,
            roi_feat_size=7,
            num_classes=80,
            bbox_coder=dict(
                type='DeltaXYWHBBoxCoder',
                target_means=[0., 0., 0., 0.],
                target_stds=[0.1, 0.1, 0.2, 0.2]),
            reg_class_agnostic=False,
            loss_cls=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
            loss_bbox=dict(type='L1Loss', loss_weight=1.0))))
```

## Runtimes settings
- Optimizer
  - SGD, Adam
  ```python
  optimizer = dict(type = "SGD", lr = 0.02, momentum = 0.9, weight_decay = 0.0001)
  optimizer_config = dict(grad_clip = None)
  ```
- Training Schedules
  ```python
  lr_config = dict(
      policy = 'step',
      warmup = 'lienar',
      warmup_iters = 500,
      warmup_ratio = 0.001,
      step = [8, 11])
  runner = dict(type = 'EpochBaseedRUnner', max_epochs = 12) 
  ```
  
# Detectron2
- Facebook AI Research의 Pytorch 기반 라이브러리

**Pipeline**
- Setup Config
- Setup Trainer
  - build_model
  - buile_detectron_train/test_loader
  - build_optimizer
  - build_lr_scheduler
- Start Training

**Pipeline 미리보기**
```python
import os
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.engine  import DefaultTrainer
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.data.datasets import register_coco_instances

# data 등록하기
register_coco_instances("coco_trash_train", {}, "/home/data/data/train.json", "/home/data/data/")
register_coco_instances("coco_trash_val", {}, "/home/data/data/val.json", "/home/data/data/")

# config 파일 불러오기
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"))

# config 수정하기
cfg.DATASETS.TRAIN = ("coco_trash_train", )
cfg.DATASETS.TEST = ("coco_trash_val", )

cfg.DATALOADER.NUM_WORKERS = 2

cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml")

cfg.SOLVER.IMS_PER_BATCH = 4
cfg.SOLVER.BASE_LR = 0.0001
cfg.SOLVER.MAX_ITER = 3000 # epoch = max_iter * batch_size / total_num_images
cfg.SOLVER.STEP = (1000, 15000)
cfg.SOLVER.GAMMA = 0.05

cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE 128
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 11

cfg.TEST.EVAL_PER100 = 500

# Augmentation mapper 정의
# 직접 Augmentation을 만들어야한다. 따라서 자유롭다.
# 사전에 정의된 Augmentation module 외에는 응요이 어렵다.
def MyMapper(dataset_dict):
    dataset_dict = copy.deepcopy(dataset_dict)
    ...
    return dataset_dict

class MyTrainer(DefaultTrainer):

  @classmethod
  def build_train_loader(cls, cfg, sampler = None):
      return build_detection_train_loader(cfg, mapper = MyMapper, sampler = sampler)
      
  @classmethod
  def build_evaluator(cls, cgf, dataset_name, output_folder = None):
    if output_folder is None:
        os.makedirs("./output_eval", exist_ok = True)
        output_folder = "./output_eval"
    return COCOEvaluator(dataset_name, cfg, False, ouptut_folder)
    
# 학습
os.makedirs(cfg.OUTPUT_DIR, exist_ok = True)
trainer = MyTrainer(cfg)
trainer.resume_or_load(resume = False)
trainer.train()
```
