# Cross Validation
- train dataset으로 훈련, test dataset으로 평가
- test dataset으로 모델 성능을 검증하면, test dataset에 overfitting이 된다.
- 따라서, train dataset을 train dataset + valid dataset으로 나누어 교차검증을 진행한다.

# 문제점

object detection dataset는 이미지마다 label 수와 category의 분포도가 다르다. 우리의 목표는 train datset과 valid dataset을 나누었을 때, category의 분포가 같아야한다. 하지만, 단순히 image를 8:2로 나누게 된다면 두 dataset의 category 분포가 다르게 될 것이다.

# 해결 방법

[stratified_group_kfold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold)

`Stratified Group KFold` from skitlearn

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159852572-0e2def92-9837-405d-84c4-4c5b74f71156.png" width="50%"></p>

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159852725-596c17ea-02a7-4f09-a964-e98878749474.png" width="80%"></p>

`StratifiedGroupKFold`는 group은 유지하되, y의 값의 비율을 유지하여 X를 나누는 방법이다.

```python
import json 
import numpy as np 
from sklearn.model_selection import StratifiedGroupKFold 

# load json annotation = {dataset file 경로} 

with open(annotation) as f: data = json.load(f)

var = [(ann['image_id'], ann['category_id']) for ann in data['annotations']]
X = np.ones((len(data['annotations']),1)) y = np.array([v[1] for v in var])
groups = np.array([v[0] for v in var]) 

cv = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=411) 

for train_idx, val_idx in cv.split(X, y, groups): 
    print("TRAIN:", groups[train_idx])
    print(" ", y[train_idx])
    print(" TEST:", groups[val_idx])
    print(" ", y[val_idx])
```

```
# check distribution 

def get_distribution(y): 
    y_distr = Counter(y)
    y_vals_sum = sum(y_distr.values()) 

    return [f'{y_distr[i]/y_vals_sum:.2%}' for i in range(np.max(y) +1)]



distrs = [get_distribution(y)]
index = ['training set']

for fold_ind, (train_idx, val_idx) in enumerate(cv.split(X,y, groups)): 
    train_y, val_y = y[train_idx], y[val_idx]
    # train_gr, val_gr = groups[train_idx], groups[val_idx]

    assert len(set(train_gr) & set(val_gr)) == 0 distrs.append(get_distribution(train_y)) 

    distrs.append(get_distribution(val_y))
    index.append(f'train - fold{fold_ind}')
    index.append(f'val - fold{fold_ind}')
    
categories = [d['name'] for d in data['categories']] 
pd.DataFrame(distrs, index=index, columns = [categories[i] for i in range(np.max(y) + 1)])
```

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159853730-f4bacbeb-a594-480d-8e08-46b34ebdc20b.png"></p>

확인 결과 train dataset과 valid dataset의 category 분포가 비슷하다는 것을 알 수 있다.
