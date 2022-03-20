# NMS의 문제점
Soft-NMS는 NMS의 문제점을 개선하기 위해 제안되었다.
- 동일한 class를 지닌 여러 물체가 뭉쳐있는 겨웅에, 하나의 bbox만 검출하고, 나머지 bbox는 억제한다.
  <p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb1Tw98%2Fbtq3TWuSTxR%2FRZcdldIREjpRGNk4JU2k4K%2Fimg.png" width='60%'></p>
> NMS
> - object detector가 예측한 bounding box 중에서 정확한 bounding box를 선택하도록 하는 기법
>   <p align='center'><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F4NrVg%2FbtqSbaqnTce%2FA1Y34EQWB0NFbrEHp5tgEK%2Fimg.png" width="60%"></p>
> - 알고리즘 작동 단계
>   1. 하나의 class에 대한 bbox 목록에서 가장 높은 점수의 bbox를 선택하고 목록에서 삭제, 그리고 final box에 추가
>   2. 선택된 bbox를 bbox 목록에 있는 모든 bbox와 IOU를 계산하여 비교한다. IOU가 threshold보다 높으면, 즉 선택된 bbox와 목록 속 bbox가 겹치는 부분이 크다면 같은 물체를 detection한 것으로 판단해 bbox 목록에서 제거한다.
>   3. bounding box 목록에 아무것도 남지 않을 때까지 반복한다.
>   4. 모든 class에 대해서 위 과정을 반복한다.
> ```python
> import torch
> from IOU import intersection_over_union
>
> def nms(bboxes, iou_threshold, threshold, box_format = 'corners'):
>   assert type(bboxes) == list
>   
>   # bbox 점수가 threshold보다 큰것을 선별
>   # bbox = [class, score, x1, y1, x2, y2]
>   bboxes = [box for box in bboxes if box[1] > threshold]
>   bboxes = sorted(bboxes, key = lambda x : x[1], reverse = True)
>   bboxes_after_nms = []
>
>   # bboxes가 모두 제거될때까지 반복
>   while bboxes:
>     # score가 가장 큰 bbox 선택
>     chosen_box = bboxes.pop(0)
>     
>     # class가 같거나 iou가 iou_threshold보다 큰 bbox 제거
>     bboxes = [box for box in bboxes if box[0] != chosen_box[0] or intersection_over_union(torch.tensor(chosen_box[2:]), torch.tensor(box[2:]), box_format = box_format) < iou_threshold]
>     
>     bboxes_after_nms.append(chosen_box)
> ```
> [[Object Detection] 비-최대 억제(NMS,Non-maximum Suppression)](https://deep-learning-study.tistory.com/403?category=968059)

# Soft-NMS

**Soft-NMS는 bbox를 억제하는 것이 아닌, confidence를 감소시킨다. 기존의 NMS에서 억제되었던 bbox가 Soft-NMS를 적용하면 낮은 confidence로 검출된다.**

<p align="center"><img src="https://user-images.githubusercontent.com/57162812/159173065-cccc7e72-8392-4a1e-9fc4-d1a2820edfac.png" width = "40%"></p>

위의 그림의 초록색 bbox는 NMS에 의해서 억제되어야 하지만, Soft-NMS는 낮은 confidence를 부여한다. 기존의 confidence가 0.8인데, 0.4로 감소하여 표현하는 것이다.

## Soft-NMS의 알고리즘
<p align="center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdULWDy%2Fbtq3WnLWlN7%2FtVWSyH7qpjO9c3PUjVNwrK%2Fimg.png" width="50%"></p>

- `f(iou(M, bi))`
  - 기존 NMS 함수  
    <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbjQ4CU%2Fbtq30EMWf7W%2F9fW9jtihATtmLS9EKp3vjk%2Fimg.png" width="30%">
  - Soft NMS 함수  
    <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdIAyLX%2Fbtq3UcYTLMt%2FJ3mcxCmZuHlEkGLf94tFh1%2Fimg.png" width="50%">
    - M과 bi의 iou가 일정 값 이상일 때, score를 감소시킨다.
    - 단점 : 이 함수는 N_t 임계값 기준으로 score가 급격하게 변하여 연속형 함수가 아니다.
    <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmNkeg%2Fbtq3TVCLclC%2FNytS7jqUzw8KHG5LFqH1Jk%2Fimg.png" width="35%">
    - score가 연속형이다..
    - 가우시안 분포를 활용하여 sigma parameter가 하나 추가된다.
    - 실험 결과에서 gaussian soft-NMS가 더 좋은 성능을 보인다.

```python
def soft_nms(dets, box_scores, sigma = 0.5, thresh = 0.001, cuda = 0):
  # dets : bboxes coordinate tensor (format : [y1, x1, y2, x2])
  # box_score : box score tensor
  # sigma : variance of Gaussian function
  # thresh : score thresh
  # cuda : CUDA flag
  
  N = dets.shape[0]
  if cuda:
    indexes = torch.arrange(0, N, dtype = torch.float).cuda().view(N, 1)
  else:
    indexes = torch.arrange(0, N, dtype = torch.float).view(N, 1)
  # dets : [y1, x1, y2, x2, index]
  dets = torch.cat((dets, indexes), dim = 1)
  
  y1 = dets[:, 0]
  x1 = dets[:, 1]
  y2 = dets[:, 2]
  x2 = dets[:, 3]
  scores = box_scores
  areas = (x2 - x1 + 1) * (y2 - y1 + 1)
  
  for i in range(N):
    tscore = scores[i].clone()
    pos = i + 1
    
    if i !=N-1:
      maxscore, maxpos = torch.max(scores[pos:], dim=0)
      if tscore < maxscore:
        dets[i], dets[maxpos.item() + i + 1] = dets[maxpos.item() + i + 1].clone(), dets[i].clone()
        scores[i], scores[maxpos.item() + i + 1] = scores[maxpos.item() + i + 1].clone(), scores[i].clone()
        areas[i], areas[maxpos + i + 1] = areas[maxpos + i + 1].clone(), areas[i].clone()
        
    yy1 = np.maximum(dets[i, 0].to("cpu").numpy(), dets[pos:, 0].to("cpu").numpy())
    xx1 = np.maximum(dets[i, 1].to("cpu").numpy(), dets[pos:, 1].to("cpu").numpy())
    yy2 = np.minimum(dets[i, 2].to("cpu").numpy(), dets[pos:, 2].to("cpu").numpy())
    xx2 = np.minimum(dets[i, 3].to("cpu").numpy(), dets[pos:, 3].to("cpu").numpy())
    
    w = np.maximum(0.0, xx2 - xx1 + 1)
    h = np.maximum(0.0, yy2 - yy1 + 1)
    inter = torch.tensor(w * h).cuda() if cuda else torch.tensor(w * h)
    ovr = torch.div(inter, (areas[i] + areas[pos:] - inter))

    # Gaussian decay
    weight = torch.exp(-(ovr * ovr) / sigma)
    scores[pos:] = weight * scores[pos:]
    
  # select the boxes and keep the corresponding indexes
  keep = dets[:, 4][scores > thresh].int()

  return keep
```

[Soft-NMS, Improving Object Detection With One Line of Code](https://deep-learning-study.tistory.com/606)
