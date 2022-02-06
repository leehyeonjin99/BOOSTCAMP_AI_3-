## Facet
- Facet이란?
  - 분할
  - 화면 상에 VIew를 분할 및 추가하여 다양한 관점을 전달
    - 같은 데이터 셋의 **서로 다른 인코딩**
    - **같은 방법으로 동시에** 여러 feature
    - **부분 집합을 세세하게**

## Matplotlib에서 Facet

1. Figure와 Axes
(1) 순차적으로 진행
```python
fig= plt.figure()
ax=fig.add_subplot(121) # 1 row, 2 column으로 분할 후 첫번째
ax=fig.add_subplot(122) # 1 row, 2 column으로 분할 후 두번째
```

(2) 개별적으로 분배

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
```

2. Figure Color

```python
fig,ax=plt.subplots()
fig.set_facecolor('lightgray')
```

3. subplot끼리 x축, y축 공유하기

(1)
```python
fig=plt.figure()
ax1=fig.add_subplot(121)
ax1.plot([1,2,3],[1,4,9])
ax2=fig.add_subplot(122, sharey=ax1)
ax2.plot([1,2,3],[1,2,3])
```

(2)
```python
fig, axes=plt.subplots(1,2,sharey=True)

axes[0].plot([1, 2, 3], [1, 4, 9])
axes[1].plot([1, 2, 3], [1, 2, 3])
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691251-92a91072-a5e9-4d63-ba82-c6936e724961.png" width=200></p>

3. Squeeze와 flattern
  -  Squeeze : 항상 2차원 배열을 받을 수 있어, 가변 크기에 대해 반복문을 사용하기에 유용
    - 단점 : 2차원일 경우에만 가능
  -  Flattern : 1중 반복문을 사용하기에 유용

```python
n,m=2,3
fig, axes = plt.subplots(n, m, figsize=(m*2, n*2))

for i, ax in enumerate(axes.flatten()):
    ax.set_title(i)
    ax.set_xticks([])
    ax.set_yticks([])
```

4. aspect : subplot의 가로 세로 비율 결정

```python
ax1 = fig.add_subplot(121, aspect=1)
ax2 = fig.add_subplot(122, aspect=0.5)
```

5. Gridspec : 서로 다른 크기의 subplot을 추가하는 데에 유용

```python
gs = fig.add_gridspec(3, 3) # make 3 by 3 grid (row, col)

ax = [None for _ in range(5)]

ax[0] = fig.add_subplot(gs[0, :]) 
ax[0].set_title('gs[0, :]')

ax[1] = fig.add_subplot(gs[1, :-1])
ax[1].set_title('gs[1, :-1]')

ax[2] = fig.add_subplot(gs[1:, -1])
ax[2].set_title('gs[1:, -1]')

ax[3] = fig.add_subplot(gs[-1, 0])
ax[3].set_title('gs[-1, 0]')

ax[4] = fig.add_subplot(gs[-1, -2])
ax[4].set_title('gs[-1, -2]')

for ix in range(5):
    ax[ix].set_xticks([])
    ax[ix].set_yticks([])
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691530-7e69c375-3f45-45ae-8a7f-c7204e52d694.png" width=300></p>

