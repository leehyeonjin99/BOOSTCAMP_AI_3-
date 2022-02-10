# Pie Chart 
## Pie Chart
- 원을 부채꼴로 분할하여 표현하는 통계 차트
  - 전체를 백분위로 나타낼 때 유용
-단점
  - 비교 어려운
  - 유용성 떨어짐
  - 오히려 bar plot이 더 유용(각도 <<< 길이)

## Pie Chart 응용
### Donut 차트

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153341063-9dc96c43-fd93-48c2-b913-7b689576c4b8.png" width=300></p>

- 중간이 비어있는 Pie Chart
  - 디자인적으로 선호
  - 인포그래픽에서 종종 사용
  - Plotly에서 쉽게 사용 가능

파이 차트보다 가독성이 떨어지고 비교하기 어려워 EDA를 진행에 있어 사용을 지양한다. 만약 presentation, story telling에서 추천!!

### Sunburst Chart
- 햇살을 닮은 차트
- 계층적 데이터 시각화하는 데 사용
  - 구현 난이도에 비해 화려
  - 오히려 TreeMap 추천
  - but 가독성이 떨어지고 실제로 유용성이 좋지 않다.
  - Plotly로 쉽게 사용 가능

## 실습
### Basic Pir Chart
- `pie()`

```python
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
ax.pie(data
       ,labels=labels
      )
plt.show()
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153341544-6e6eeb42-29d5-4b9e-9929-524adb1dae52.png" width=300></p>

### Pie Chart vs Bar Chart
- 장점 : 비율 정보에 대한 정보를 제공할 수 있다.
- 단점 : 구체적인 양의 비교가 어렵다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153341698-8cbc01d5-ad14-4fc4-927f-beeeca760e59.png" width=500></p>

### Pie Chart Custom
- `startangle=` : 시작 위치
- `explode=` : 원하는 부분 강조 가능, 튀어 나와 있다.
- 'shadow' : 그림자 : 가독성이 떨어질 수도 있다.
- `autopct` : 데이터 값 표시
- `labeldistance` : 파이차트와 label의 거리 조정
- `rotatelabels` : label의 각도
- `counterlock` : data의 방향
- `radius` : 원의 크기 조정 가능

```python
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
explode = [0, 0, 0.2, 0]

ax.pie(data, labels=labels, explode=explode, startangle=90,
      shadow=True, autopct='%1.1f%%')
plt.show()
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153342475-0906fa80-79d7-41bd-af7f-2736678394a1.png" width=500></p>

## Pie Chart 변형
### Donut Chart
- 중앙에 background 색과 같은 원을 그려준다.

```python
fig, ax = plt.subplots(1, 1, figsize=(7, 7))


ax.pie(data, labels=labels, startangle=90,
      shadow=True, autopct='%1.1f%%', pctdistance=0.85, textprops={'color':"w"})

# 좌표 0, 0, r=0.7, facecolor='white'
centre_circle = plt.Circle((0,0),0.70,fc='white')
ax.add_artist(centre_circle)

plt.show()
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/153342724-499e8557-ab65-46a7-a80b-68c3bab049a4.png" width=500></p>

