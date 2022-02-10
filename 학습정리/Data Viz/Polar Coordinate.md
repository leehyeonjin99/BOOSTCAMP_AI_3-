# Polar Coordinate
## Polar Plot
### Polar Plot

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153335739-85e71d96-0300-40e4-a43d-f4d93b793183.png" width=300></p>

- Polar Coordinate를 사용하는 시각화
  - 거리(R), 각도(Theta)를 사용하여 Plot
- 회전, 주기성 등 표현에 적합


<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153335838-eb66154a-2afc-44e4-b671-769fb66e1609.png" width=400></p>

- Matplotlib의 로고에도 polar plot이 사용되었다.
  - Bar 또는 Area chart를 통해 표현 가능

### Data Converting

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153335976-e7733af7-2993-4d6a-9780-e5052b9e8dcf.png" width=300></p>

- 직교 좌표계 X, Y에서 변환 가능하다.
  - X=R\*cosθ
  - Y=R\*sinθ

## Radar Plot
### Radar Chart

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153336253-e7119fb9-d12d-42f8-bdb1-199c514b7883.png" width=400></p>

- 극좌표계를 사용하는 대표적 차트
- 별 모양으로 생겨 Star Plot으로도 불린다.
- 중심점을 기준으로 N개의 변수 값을 표현할 수 있다.

- 데이터의 Quality를 표현하기에 좋다
  - 캐릭터의 강함
  - 운동선수 분석
  - 비교에도 적합

### Radar Chart의 주의점
- 각 feature는 독립적이고 척도가 같아야한다.
  - 순서형 변수와 수치형 변수가 함께 있다면 고려 필요

- 다각형의 면적이 중요해보이지만 feature의 순서에 따라 달라진다.  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153336406-7da5db47-4036-4ba6-824e-cd99d5184e87.png" width=400></p>

- Feature가 많아질수록 가독성이 떨어진다.  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/153336460-3f438732-c195-488c-aad8-499741b99861.png" width=300></p>

## 실습
### Polar Coordinate 생성하기

- **projection=polar** 추가하여 사용
  ```python
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='polar')
  plt.show()  
  ```
- **polar=True** 추가하여 사용
  ```python
  fig=plt.figure()
  ax=fig.add_subplot(111, polar=True)
  plt.show()
  ```
### Polar Coordinate 조정하기
- `set_ramx` : 반지름 최댓값 조정
- `set_rmin` : 반지름 최솟값 조정
- `set_rticks` : 반지름 표기 grid 조정
- `set_rlabel_position` : 반지름 label 적히는 위치의 각도 조정

```python
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_rlabel_position(-90)
ax.set_rmax(1)
ax.set_rticks([0,0.2,0.4,0.6,0.8,1.0])  
plt.show()
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153337424-be7be01f-b587-42a1-ba62-7f6d18dad609.png" width=300></p>

- 각도를 조종하여 부채꼴 모양 사용
  - `set_thetamin()` : 각도의 min값
  - `set_thetamax()` : 각도의 max값
 
```python
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

ax.set_thetamin(45)
ax.set_thetamax(135)
plt.show()
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153337563-f9500b56-3e50-4e9f-9bd0-f1af1abd205c.png" width=300></p>

### Radar Chart

- `set_thetagrids` : 각도에 따른 그리드 및 ticklabels 변경
- `set_theata_offset` : 시작 각도 변경

```python
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='polar')

values = pokemon.iloc[0][stats].to_list()
values.append(values[0])

ax.plot(theta, values)
ax.fill(theta, values, alpha=0.5)

ax.set_thetagrids([n*60 for n in range(6)], stats) # 60도 간격으로 thetagrid 레이블 변경
ax.set_theta_offset(np.pi/2) # 90도부터 시작
ax.set_rlabel_position(0)

plt.show()
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153338695-90c08c12-04a9-47dc-a95a-c62006fa41d4.png" width=300></p>

