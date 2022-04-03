# WBF
`WBF`는 weighted boxes fusion으로 object detection의 여러 결과인 bounding box를 앙상블 하는 방법이다. 만약 여러 모델에서 각기 다른 예측값들을 효과적으로 앙상블할 수 있다면, 모델의 성능을 더욱 높일 수 있을 것이다.

이미지에 대한 모델의 예측은 bbox에 대한 4개의 좌표, 객체의 class, 0과 1사이의 확률의 6개의 값으로 이루어져 있다. 각각에 대해 여러가지 다른 모델들과 그에 따른 예측이 있다고 가정하자. 이때, 예측을 주어진 metric에 대해서 향상되는 방식으로 결합할 수 있는지가 중요하다.

이를 위해서는 `NMS(Non Maximum Supreesion)`방법과 `Soft-NMS extension`이 주로 사용된다. 또한 새로운 방법  `WBF`가 제안되었다. NMS와 Soft-NMS extension은 예측의 일부를 단순히 제거하는 방법이지만, WSF는 모든 예측된 사각형을 사용하므로, 결합된 사각형의 품질을 향상시킬 수 있다. 아래의 예시는 NMS는 부정확한 상자를 제외한 하나의 상자만 남겨두고, WBF는 3개의 상자 모두의 정보를 사용하여 문제를 해결한다. (빨간색 : 예측, 파란색 : 정답)

<p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FOAXfd%2FbtqFoQMa17d%2FUJjX5EApj2YTUx1UDNVKaK%2Fimg.png" width="50%"></p>

## Algorithm

- weighted_boxes_fusion(boxes_list, scores_list, labels_list, weights = None, iou_thr = 0.55, skip_box_thr = 0.0, conf_type = 'avg', allow_overflow = False)
  - iou_thr : iou 임계값
  - skip_box_thr : 각각 박스의 스코어는 이 임계값보다 작으면 버려지고
  - weight : 모델마다 다른 값을 갖는다.(default = 1)

1. 두 박스의 iou를 계산하여 iou가 iou_thr보다 크면 get_weighted_box(boxes, conf_type='avg')함수를 통해 두 박스가 융합된다. 
    1. 융합의 첫번째는 score를 매기는 것이다. 
    2. frame 좌표 융합의 경우, frame 좌표에 해당 score를 곱한 다음 합계를 융합 score로 나눈다.
    3. frame fusion c2와 같은 비선형 가중치를 사용하여 더 나은지 여부를 확인하고 융합된 모든 원본frame과 fusion 후 frame을 저장할 수 있다.
2. 융합된 frame score 크기를 조정한다. 즉, 융합된 score 값에 작은 값을 원래 frame 수와 총 모델 수로 곱한 다음 모든 모델 수로 나눈다.
    - weighted_boxes[i][1] = weighted_boxes[i][1] \* min(weights.sum(), len(new_boxes[i])) / weights.sum()

## 실험 결과
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/160106005-60e958f2-39c7-43a2-ad03-30a3f8cc7af0.png" width="50%"></p>

## CODE

```python
# 앙상블 대상 csv 파일
submission_files = ["/opt/ml/0.5711.csv",
                   "/opt/ml/0.5979.csv",
                   "/opt/ml/0.6172.csv",
                   "/opt/ml/0.6384.csv",
                   "/opt/ml/0.6704.csv",
                   "/opt/ml/0.5614.csv",
                   "/opt/ml/0.6032.csv",
                   "/opt/ml/0.6166.csv",
                   "/opt/ml/0.5703.csv"] # submission csv 파일 이름을 넣어주세요

submission_df = [pd.read_csv(file) for file in submission_files]

# test file
annotation = '/opt/ml/detection/dataset/test.json'
coco = COCO(annotation)
image_ids = submission_df[0]['image_id'].tolist()

# 앙상블 진행
prediction_strings = []
file_names = []
iou_thr = 0.5
skip_box_thr=0
conf_type = 'avg' # 'avg', 'max', 'box_and_model_avg', 'absent_model_aware_avg'
'''
param conf_type: how to calculate confidence in weighted boxes.
    'avg': average value,
    'max': maximum value,
    'box_and_model_avg': box and model wise hybrid weighted average,
    'absent_model_aware_avg': weighted average that takes into account the absent model.
'''

for i, image_id in enumerate(image_ids):
    prediction_string = ''
    boxes_list = []
    scores_list = []
    labels_list = []
    image_info = coco.loadImgs(i)[0]
    
    for df in submission_df:
        if df[df['image_id'] == image_id]['PredictionString'].tolist():
            predict_string = df[df['image_id'] == image_id]['PredictionString'].tolist()[0]
            predict_list = str(predict_string).split()
        
        if len(predict_list)==0 or len(predict_list)==1:
            continue
            
        predict_list = np.reshape(predict_list, (-1, 6))
        box_list = []
        
        for box in predict_list[:, 2:6].tolist():
            box[0] = float(box[0]) / image_info['width']
            box[1] = float(box[1]) / image_info['height']
            box[2] = float(box[2]) / image_info['width']
            box[3] = float(box[3]) / image_info['height']
            box_list.append(box)
            
        boxes_list.append(box_list)
        scores_list.append(list(map(float, predict_list[:, 1].tolist())))
        labels_list.append(list(map(int, predict_list[:, 0].tolist())))
    
    if len(boxes_list):
        # boxes, scores, labels = nms(boxes_list, scores_list, labels_list,iou_thr=iou_thr)
        # boxes, scores, labels = soft_nms(box_list, scores_list, labels_list, iou_thr=iou_thr)
        # boxes, scores, labels = non_maximum_weighted(boxes_list, scores_list, labels_list,iou_thr=iou_thr)
        # boxes, scores, labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list,iou_thr=0.5,conf_type='box_and_model_avg')
        boxes, scores, labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list, iou_thr=iou_thr, skip_box_thr=skip_box_thr)

        for box, score, label in zip(boxes, scores, labels):
            prediction_string += str(int(label)) + ' ' + str(score) + ' ' + str(box[0] * image_info['width']) + ' ' + str(box[1] * image_info['height']) + ' ' + str(box[2] * image_info['width']) + ' ' + str(box[3] * image_info['height']) + ' '
    
    prediction_strings.append(prediction_string)
    file_names.append(image_id)
 
# 앙상블 파일 저장
submission = pd.DataFrame()
submission['PredictionString'] = prediction_strings
submission['image_id'] = file_names
submission.to_csv('submission_ensemble5.csv')
```
