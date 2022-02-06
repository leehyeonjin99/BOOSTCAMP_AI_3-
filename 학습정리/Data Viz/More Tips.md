## Grid 이해하기

- color : 색은 다른 표현들을 방해하지 않도록 **무채색**
- zorder : 항상 Layer 순서 상 **맨 밑**에 오도록 조정
- which='major','minor','both' : **큰** 격자/ **세부** 격자
- axis='x','y','both' : X축, Y축, 동시에

```python
ax.grid(zorder=0, linestyle='--', which='both', axis='both', linewidth=0.5)
```

### 다양한 형태의 Grid

1. x+y=c

```pyhton
x_start = np.linspace(0, 2.2, 12, endpoint=True)

for xs in x_start:
    ax.plot([xs, 0], [0, xs], linestyle='--', color='gray', alpha=0.5, linewidth=1)
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691708-ec965ffd-3169-4b2a-a69f-5e3d7e8c7813.png" width=200></p>

2. y=cx

```python
radian = np.linspace(0, np.pi/2, 11, endpoint=True)

for rad in radian:
    ax.plot([0,2], [0, 2*np.tan(rad)], linestyle='--', color='gray', alpha=0.5, linewidth=1)
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691757-5d23f560-c8f4-4487-a649-15b914108c9f.png" width=200></p>

3. 동심원

``python
rs = np.linspace(0.1, 0.8, 8, endpoint=True)

for r in rs:
    xx = r*np.cos(np.linspace(0, 2*np.pi, 100))
    yy = r*np.sin(np.linspace(0, 2*np.pi, 100))
    ax.plot(xx+x[2], yy+y[2], linestyle='--', color='gray', alpha=0.5, linewidth=1)
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691783-92bcbf57-9269-4a28-9f1e-2227a003b7ca.png" width=200></p>

## Line, Span

1. Line

```python
ax.axvline(0, ymin=0.3, ymax=0.7, color='red', linestyle="--") # 첫번째 parameter : 위치
ax.axhline(0, xmin=0.3, xmax=0.7, color='green', linestyle='--')
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691893-2433e24d-852c-41eb-86bb-87e7cc8d905b.png" width=200></p>

2. Span

```python
ax.axvspan(0,0.5, ymin=0.3, ymax=0.7, color='red', alpha=0.5) # 시작 위치, 두께
ax.axhspan(0,0.5, xmin=0.3, xmax=0.7, color='green', alpha=0.5)
```
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152691986-a23c2ee3-3f4e-4210-a17c-800a19eb74eb.png" width=200></p>

3. Spines

```
fig = plt.figure(figsize=(12, 6))

_ = fig.add_subplot(1,2,1)
ax = fig.add_subplot(1,2,2)
ax.spines['top'].set_visible(False) # 시각화 여부
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5) # Spine 두께
ax.spines['bottom'].set_linewidth(1.5)
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152692023-f136a25c-b1cd-411b-8c1b-45a685e48a21.png" width=400></p>

```python
_ = fig.add_subplot(1,2,1)
ax = fig.add_subplot(1,2,2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_position('center') # 위치 조정 : 그래프 그릴 때 유용할 듯,,,
ax.spines['bottom'].set_position('center')
```

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/152692057-207a0651-11fb-4cea-b8d2-94d7b742bf13.png" width=400></p>

4. Setting

```python
# 영구적
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.linestyle'] = ':'
```

```python
# 
with plt.style.context('fivethirtyeight'):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)))
``` 
