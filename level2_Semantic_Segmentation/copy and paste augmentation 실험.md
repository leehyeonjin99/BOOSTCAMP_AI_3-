# ✔️실험
### 실험 목표

- data imbalace를 해결하기 위한 augmentation
- 적은 양의 class dataset을 증가시키면 해당 class의 mIoU가 증가할 수 있으며, 이는 전체 mAP에 대해서 큰 영향을 미칠 수 있다.
- 많은 양의 데이터에 대해서는 overfitting 없이 데이터 증강을 할 수 있다

### 동기<img width="1388" alt="image" src="https://user-images.githubusercontent.com/57162812/165701995-ca998f75-48b4-4ea9-a26a-ead9ea03ca16.png">


- dataset의 imbalance가 크다는 것을 확인하였다.

  <img width="486" alt="image" src="https://user-images.githubusercontent.com/57162812/165696948-d1fad54b-d96b-405d-a321-da7d064a0acb.png">
  
  이렇게 되면 battery의 경우에는 validation set에 battery가 거의 0에 가까운 개수를 가지고 있을 수 있다. 시험을 예로 든다면, 10개 중에서 하나를 못 맞추면 10점이 감점되는 것이지만 3개 중에서 하나를 못 맞추게 된다면 33점이 감점된다. 
  
  Class별 IoU를 확인해보면 dataset이 적을수록 IoU가 낮은 경향을 보이는 것을 확인할 수 있다.
  
  |Class|IoU|
  |:-:|:-:|
  |Backgroud|0.9373|
  |General trash|0.3143|
  |Paper|0.6348|
  |Paper pack|0.2658|
  |Metal|0.3096|
  |Glass|0.4178|
  |Plastic|0.3831|
  |Styrofoam|0.4962|
  |Plastic bag|0.7577|
  |Battery|0.0035|
  |Clothing|0.5724|
  <img width="800" alt="image" src="https://user-images.githubusercontent.com/57162812/165701854-743f824a-d3a1-478e-9de0-039d612bc65b.png">
  
  만약 test dataset에도 battery가 아주 소량이 들어있다면, mIoU를 계산하는 데에 있어서 하나에 대한 정답 유무가 큰 차이를 보일 것이다. 따라서 우리는 batery와 같이 적은 class의 dataset에 대해서 잘 맞출 수 있도록 증가시키도록 할 것이다.

### 과정

**[Copy Paste Aug](https://github.com/conradry/copy-paste-aug)** 사용

- 간단하게 설명하면, 이미지의 객체를 복사하여 다른 이미지로 붙여넣기를 한다.
- 해당 방법은 paste된 이미지의 ground truth를 제공한다.
- 이때, 완전히 가려진 mask는 제거하고 부분적으로 가려진 mask는 갱신한다.

<img src="https://user-images.githubusercontent.com/57162812/165757436-16207294-365a-43bb-89dd-ea66b347bd5d.png" width="80%">

- 해당 코드는 dataloader에 적용하였다.

```python
class CustomCPDataLoader(Dataset):
    """COCO format"""
    def __init__(self, dataset_path, data_dir, sorted_df, mode = 'train', transforms = None):
        super().__init__()
        self.mode = mode
        self.transforms = transforms
        self.coco = COCO(data_dir)
        self.dataset_path = dataset_path
        self.data_dir = data_dir
        self.sorted_df = sorted_df
        ## Copy Paste Dataset 생성
        self.data = CocoDetectionCP(
                            self.dataset_path, 
                            self.data_dir, 
                            self.transforms
                        )
        print("dataset init")
        
    def __getitem__(self, index: int):
        # 해당 인덱스의 데이터 불러오기
        tmp_data = self.data[index]

        # dataset이 index되어 list처럼 동작
        image_id = self.coco.getImgIds(imgIds=index)
        image_infos = self.coco.loadImgs(image_id)[0]
        
        # cv2 를 활용하여 image 불러오기
        images = tmp_data["image"].astype(np.float32)
        images /= 255.0
        
        if (self.mode in ('train', 'val')):
            ann_ids = self.coco.getAnnIds(imgIds=image_infos['id'])
            anns = self.coco.loadAnns(ann_ids)

            # Load the categories in a variable
            cat_ids = self.coco.getCatIds()

            bboxes = tmp_data['bboxes']
            box_classes = np.array([b[-2] for b in bboxes])
            mask_indices = np.array([b[-1] for b in bboxes])
            mask = np.array(tmp_data["masks"])[mask_indices]
            area = [np.sum(m) for m in mask]
            big_idx = np.argsort(area)[::-1]
            # masks : size가 (height x width)인 2D
            # 각각의 pixel 값에는 "category id" 할당
            # Background = 0
            masks = np.zeros((image_infos["height"], image_infos["width"]))
            # General trash = 1, ... , Cigarette = 10
            for i in big_idx:
                masks[mask[i] == 1] = box_classes[i]
                # print(len(mask), len(box_classes))
            masks = masks.astype(np.int8)

            bboxes = []
            for ix, obj in enumerate(anns):
                bboxes.append(obj['bbox'] + [obj['category_id']] + [ix])
            
            # transform -> albumentations 라이브러리 활용
            transform = A.Compose([
                        ToTensorV2()
                        ])
            transformed = transform(image=images, mask=masks)
            images = transformed["image"]
            masks = transformed["mask"]
            return images, masks, image_infos
        
        if self.mode == 'test':
            # transform -> albumentations 라이브러리 활용
            if self.transform is not None:
                transformed = self.transform(image=images)
                images = transformed["image"]
            return images, image_infos
    
    def __len__(self) -> int:
        # 전체 dataset의 size를 return
        return len(self.coco.getImgIds())
```        
- 또한 코드 수정을 통해서 부족한 class를 가진 이미지에 대해서만 copy paste를 진행하도록 수정 가능하였다.

### 결과
- CopyPaste의 `pct_object_paste`, `p` hyper parameter에 대한 실험
  - `pct_object_paste`는 copy할 이미지에서 몇 퍼센트의 object를 paste할지 결정하는 인자이다.
  - `p`는 총 dataset에서 몇개의 이미지에 해당 기법을 적용할 것인지를 결정하는 인자이다.

|  | copy_pct | copy_p | Valid |  |
| --- | --- | --- | --- | --- |
| 현진 | 0.3 | 0.2 | 0.4979 |  |
| 현진 | 0.5 | 0.2 | 0.4982 |  |
| 현진 | 0.7 | 0.2 | 0.5034 |  |
| 정균 | 0.3 | 0.4 |  |  |
| 정균 | 0.5 | 0.4 | 0.5032 |  |
| 정균 | 0.7 | 0.4 | 0.5024 |  |
| 진혁 | 0.3 | 0.6 | 0.4891 |  |
| 진혁 | 0.5 | 0.6 | 0.4931 |  |
| 진혁 | 0.7 | 0.6 | 0.4982 |  |
|  | 0.3 | 0.2 | 0.5103 | battery noise 제거 |
|  | 0.5 | 0.5 | 0.4963 |  |
|  | x | x | 0.5111 |  |

`pct_object_paste = 0.7`과 `p = 0.2`일 때, 가장 좋은 결과를 보이는 것을 확인할 수 있다. p가 작을수록 좋아진 이유는 아무래도 paste를 하는 과정에 있어서 기존의 object를 완전히 가려버리는 부분이 있었기 때문이며, pct_object_paste가 큸록 좋았던 이유는 class imbalance가 조금이나마 해결이 되었기 때문이라 생각한다.

- 위의 실험은 battery class의 이미지들을 붙여 넣어주었다면, 해당 실험에서는 class 구분없이 random하게 붙여넣어주었다.

|  | 종류 | copy_pct | copy_p | Valid |
| --- | --- | --- | --- | --- |
| 현진 | every | 1.0 | 0.3 | 0.507 |
| 현진 | every | 1.0 | 0.6 | 0.5036 |
| 현진 | every | 1.0 | 0.9 | 0.5068 |
| 진혁 | various(cloth battery glass metal) | 0.7 | 0.6 | 0.5068 |
| 진혁 | every | 0.7 | 0.3 | 0.5097 |
| 진혁 | every | 0.7 | 0.6 | 0.5022 |
| 진혁 | every | 0.7 | 0.9 | 0.5053 |

- 해당 실험으로는 battery만 추가했을 때보다 더 좋은 valid mIoU 값이 나왔다. 이는 가장 적은 class인 battery만 추가해주면 class imbalance를 해결해 줄 것이라는 가설에 위배된다. 해당 사실에 대해서는 추가적인 고민이 필요할 것 같다.
