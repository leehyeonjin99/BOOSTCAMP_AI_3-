### Matplotlib에서 Text
- 시각화에서 Text란?
  - Visual representation들이 **줄 수 없는 많은 설명 추가**
  - 잘못된 전달에서 생기는 **오해 방지**
  - **BUt** 너무 과한 Text 사용은 이해 방해 가능성 제기
- Anatomy of a Figure(Text Ver.)

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152689213-92e40c5d-c621-4081-966d-73ed51a39a5e.png" width=250></p>

  - **Title** : 주제
  - **Label** : 축 데이터 정보
  - **Tick label** : 축 눈금을 사용하여 스케일 정보를 추가
  - **Legend** : 한 그래프 위 서로 다른 데이터를 분류하기 위해 사용
  - **Annotation(Text)** : 그 외의 시각화에 대한 설명 추가

### Text Properties

#### Text API in Matplotlib

```python
fig, ax=plt.subplots()

ax.plot([1,2,3],label='legend')
ax.legend()

ax.set_title('Ax Title')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

ax.text(x=1,y=2,s='Text') # 절대적 위치값으로 지정
fig.text(0.5, 0.6, s='Figure Text') # 상대적 위치값으로 지정
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152689409-c85ee707-c416-4ab5-9178-ab7a369942c2.png" width=250></p>

#### Text Properties
1. Font Components : family, size, style, weight

```python
# x,y축의 범위 지정
ax.set_xlim(0,1)
ax.set_ylim(0,1)

ax.text(x=0.5, y=0.5, s="Text\nis Important",
        fontsize=20, # 글씨 크기
        fontweight='bold', # 글씨 두께
        fontfamily='serif') # 글씨체
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152689573-2cea9542-b86f-4fad-a0ac-d9315015b1f1.png" width=250></p>

2. Details : color, linespacing, backgroundcolor, alpha, zorder, visible

```python
ax.text(x=0.5, y=0.5, s='Text\nis Important',
        fontsize=20,
        fontweight='bold',
        fontfamily='serif',
        color='royalblue', # 글씨 색
        linespacing=2, #글자 간격
        backgroundcolor='lightgray', # 글씨 배경색
        alpha=0.5) # 글씨 투명도 조정
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152689748-1f7a6ede-4355-4a55-b752-82bf839f8027.png" width=250></p>

3. Alignment : ha, va, rotation, multialignment
  - text는 위치를 정해주면 그 위치로부터 오른쪽 위로 생성된다. 

```python
ax.text(x=0.5, y=0.5, s='Text\nis Important',
        fontsize=20,
        fontweight='bold',
        fontfamily='serif',
        color='royalblue',
        linespacing=2,
        va='center', # top, bottom, center # vertical alignment
        ha='center', # left, right, center # horizonral alignment
        rotation=45 # vertical?
       )
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152689933-1cff0d75-af73-47d9-a1cc-c3d84437ffc0.png" width=250></p>

4. Advanced : bbox
  - bbox는 dictionary 형태로 정의된다.

```python
ax.text(x=0.5, y=0.5, s='Text\nis Important',
        fontsize=20,
        fontweight='bold',
        fontfamily='serif',
        color='black',
        linespacing=2,
        va='center', # top, bottom, center
        ha='center', # left, right, center
        rotation='horizontal', # vertical?
        bbox=dict(boxstyle='round', facecolor="wheat", ec="blue", alpha=0.4,pad=0.5) # 박스 스타일, 배경색, 테두리 색, 투명도, padding 정도
       )
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152690044-0c498605-8c83-48ae-a4dc-74c735ee1472.png" width=250></p>

### 추가 사용법

1-1. 축 제거 방법

```python
# 오른쪽 라인, 위쪽 라인 제거
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

1-2. 모든 축 제거 방법

```python
ax.set(frame_on=False)
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152690181-c88867d0-78a7-452d-ba04-4407f5f34db0.png" width=200></p>

2. 제목 위치 조정

```python
ax.set_title('Score Relation', 
             loc='right', va='bottom',
             fontweight='bold', fontsize=15
            )
```

3. 범례 제목, 그리자 달기, 위치 조정

```python
ax.legend(
    title='Gender', # legend 제목
    shadow=True, # 그림자 여부
    labelspacing=1.2, # 줄간 간격
    #loc='lower right' # 위치1
    bbox_to_anchor=[1.2, 0.5], # 위치2
    ncol=2 # label column
)
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152690371-2b811a55-775d-4f26-bf06-de36f23bb21b.png" width=200></p>

4. Annotate : 화살표 사용하기

```python
bbox = dict(boxstyle="round", fc='wheat', pad=0.2)
arrowprops = dict(arrowstyle="->")

ax.annotate(s=f'This is #{i} Studnet',
            xy=(student['math score'][i], student['reading score'][i]), # 화살표 위치
            xytext=[80, 40], # 박스 위치
            bbox=bbox, # 박스 모양
            arrowprops=arrowprops, # 화살표 모양
            zorder=9
           )
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152690546-27958617-b1df-43f4-bc8c-6ded728a1bdf.png" width=200></p>
