## 1. Interative를 사용하는 이유
### 1.1 정적 시각화의 단점

- 정형 데이터에서 Feature가 10개 있다면
  - 각각의 관계를 살펴보는 데 10\*9/2=45개의 plot
  - **공간적 낭비**

- 각각의 사용자는 원하는 인사이트가 다를 수 있다.
  - 필요한 interaction(클릭, 무브, 확대)를 통해서 원하는 정보를 얻을 수 있다.
  - 설득을 위해서 **원하는 메세지를 압축해서 담는 것은 정적 시각화**의 장점

### 1.2 Interactive의 종류

- Select : mark something as interesting
- Explore : show me something else
- Reconfigure : show me a different arrangement
- Encode : show me a different representation
- Abstract : show me more or less detail
- Filter : show me shomething conditionally
- Connect : show me related items

하지만 모든것을 Python에서 제공하지 않는다. Library 사용을 좀 더 중점적으로 두자

### 1.3 Libaray 소개
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154197259-283c434a-ad2d-4c6c-91b8-f1c30364ef12.png" widht=300></p>

대표적 라이브러리 3개
- Plotly
- Bokeh
- AltairA

## 2. Interative Viz Libarary
### 2.1 Matplotlib

주피터 노트북 환경 또는 Local에서만 실행할 수 있다.
- 다른 라이브러리들은 웹 deploy 가능

### 2.2 Plotly

Python 뿐만 아니라 R, JS에서도 제공

- 통계 시각화 외에도 지리 시각화+3D 시각화+금융 시각화 등 다양한 시각화 기능 제공
- 형광 Color가 매력적

### 2.3 Plotly Express

- Plotly를 seaborn과 유사하게 만들어 쉬운 문법

### 2.4 Bokeh

- 문법은 Matplotlib과 더 유사한 부분이 있다.
- 비교적 부족화 문서화

### 2.5 Altair

- Vega 라이브러리를 사용하여 만든 Interactive
- 시각화를 + 연산 등으로 배치하는 것이 특징
- 데이터 크기에 5000개 제한
- Bar, Line, Scatter, Histogram에 특화

## Plotly 실습하기
### Scatter
```python
import plotly
import plotly.express as px

fig = px.scatter(iris,  # data
                 x='sepal_length', # x축
                 y='petal_length', # y축
                 color='species', # color 기준
                 size='sepal_length', # size 기준
                 range_x=[4,9], # xlim과 같은 기능
                 range_y=[0,8], # ylim과 같은 기능
                 hover_data=['sepal_width', 'petal_width'], # hover 추가 정보
                 hover_name='species', # hover 제목
                 marginal_y="violin",
                 marginal_x='box'              
            )

fig.show()
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154204778-55265ad1-01e2-401d-9395-43d50cd0729a.png" width=500></p>


- 회귀선도 그려줄 수 있다.
  - tradeline='ols'
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154205208-63ccfee1-5a75-40eb-a685-3ea34019dbf0.png" width=500></p>

- facet grid의 기능도 가능하다.
  - facet_col='기준 feature'
  - facet_row='기준 feature'

### Line
```python
fig=px.line(flights,
            x='year',
            y='passengers',
            color='month')
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154206062-7bac7eeb-0b88-472a-ad28-c44db32a9fe7.png" width=500></p>

### Bar
```python
fig=px.bar(models,
           x='nation',
           y='count',
           color=',medal')
```
- 자동적으로 stacked 형태를 취한다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154206229-0215db51-527b-4ab4-8557-2339c7f35bea.png" width=500></p>

- group 형태의 bar 그래프를 그릴 수 있다.
  -barmode='group'
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154206470-243cc2dc-f734-4e84-9fdc-565344dcac07.png" width=500></p>

### Part of Whole
- 데이터를 트리 구조로 살필 때, 유용한 시각화 방법론
  - Sunbrust
  - Treemap

```python
fig=px.sumburst(tips,
                path=['day','time','sex'], # 이 루트로 계층적으로 확인
                values='total_bill' # 값
                )
 
fig.show()
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154206823-5d0d0b61-f61e-4899-b2f2-255cbb5bb969.png" width=500></p>

```python
fig = px.treemap(tips, 
                  path=['day', 'time', 'sex'], 
                  values='total_bill')
fig.show()
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154206916-ae345e7b-1301-4891-bb9a-d2df99e40d63.png" width=500></p>

### Multidimensional
- parallel_coordinates
- parallel_categories
### Geo
- scatter_geo
- choropleth
