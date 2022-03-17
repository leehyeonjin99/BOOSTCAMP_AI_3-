# Seeing the world in 3D perspective
## Why is 3D important?
**We live in a 3D sapce**

- 3D 공간에 대한 이해가 중요하다.

**3D application**
- AR/VR  
  <img src="https://user-images.githubusercontent.com/57162812/158722954-0c742f94-8c77-4106-8242-c71b181dbfb3.png" width="20%">

- 3D printing  
  <img src="https://user-images.githubusercontent.com/57162812/158722968-22947fa0-5eef-4f60-b749-c80abf055613.png" width="20%">

- Medical applicatoin  
  <img src="https://user-images.githubusercontent.com/57162812/158722996-c4d00909-2b70-4790-bc7a-14ae4b42d327.png" width="20%">
## The way we observe 3D
**An image is a projection of the 3D world onto a 2D space**
- 3D 물체가 있더라도 우리가 보는 것은 이미지와 같이 2D space로 projection된 것이다.
D
**A camera is a projection device of the 3D scene onto a 2D image plane**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158723556-0650563d-2efe-4dda-9a18-aee3ed5e7e27.png" width = "20%"></p>

**Triangulation - The way to obtain a 3D point from 2D images**
- projection 사진 2개가 있다면 3D를 복원할 수 있다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158723661-3329e837-fdff-4242-b883-c7dc02202aa8.png" width = "20%"></p>

- 더 많은 Multiple view로부터 3D를 복원 가능하다.

## 3D data representation
**How is 3D data represented in computer?**
- 2D image는 2D array의 각 pixel에 RGC 값들로 표현된다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158723989-291dd0dc-3de7-47a3-ab9b-b61b48e2ddff.png" width = "40%"></p>

- 3D의 표현은 unique하지 않다.
  - Multi-view imaeges : 3D의 여러 view 각도에서 사진을 촬영해 보관
  - Volumetric : 3D space를 적당한 격자로 나눠 격자가 3D object를 차지하고 있는지 0과 1로 표현
  - Part assembly : 3D object를 기본적 도형들의 parametric 집합으로 part를 표현
    - 아래의 사진의 경우 6개의 사각형 상자의 조합으로 3D를 표현
  - Point cloud : 3D 상의 point들의 집합을 이용해 표현 : (x, y, z) 실제로 저장될때는 (점의 개수, 3)의 list로 저장
  - Mesh
    - Triangle Mesh : 3개의 (x,y,z) vertex를 삼각형으로 연결한다. 즉, vertex와 edge의 set으로 mesh가 표현된다.
  - Implicit shape : 고차원의 function으로 표현해 function이 0이 되는 좌표들을 연결하면 3D가 된다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158724835-c34ab8f2-3e4a-4bb1-9a14-40f088720540.png" width = "60%"></p>

## 3D datasets
**ShapeNet**
- 3D object가 33개의 category에 대해서 51,300개의 data가 있다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158726124-f1283fc1-5803-4278-9ec0-419c146f2e5a.png" width = "60%"></p>

**PartNet**
- 하나의 object에 대해서 detail이 annotation 되어있다. : `Fine-grained dataset`
  - 26,671개의 3D 모델들에 대해서 573,585개의 part instance들로 구분되어있다.
  - segmentation에 유용하다.
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158726345-4ab80536-fac9-4bf9-98db-b42b23c83ab8.png" width = "60%"></p>

**SceneNet**
- 500만개의 RGB-Depth random하게 generation한 synthetic indoor images
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158726446-9782c9f2-4cc1-46fa-a0b1-5cc8d9028d24.png" width = "60%"></p>

**ScanNet**
- 실제 scan으로부터 얻은 250만개 view의 RGB-Depth dataset
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158726707-5bba1527-7a4c-4626-8042-01b39f6c28f7.png" width = "60%"></p>

**Outdoor 3D scene datasets**
- 무인차 application을 염두한 dataset
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158726836-550ccba4-b281-42b3-9069-acb91cf5a14f.png" width = "60%"></p>

# 3D tasks
## 3D recognition
**3D object recognition**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158727152-ab4a8e2f-2a66-417c-8522-2dd469458c14.png" width = "60%"></p>

## 3D object detection
**3D object detection**
- image 또는 3D space에서의 3D object localization을 탐지
- 3D bbox를 찾는다.
- 무인차 application에서 유용

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158727378-29f7dd55-d34f-4271-88f1-06c3041da840.png" width = "60%"></p>

## 3D semantic segmentation
**3D semantic segmentation**
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158727505-7b052500-c9ed-4c29-82aa-27a2e83798e0.png" width = "60%"></p>

## Conditional 3D generation
**Mesh R-CNN**
- Input : 2D image
- Output : 3D meshes

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158727621-6cbf164c-a765-456c-bb2b-ac03d85d1d7e.png" width = "60%"></p>

**Recap : Branches in Mask R-CNN**
- bbox, class, mask를 prediction하는 3개의 branch
- output을 inference할 때, 하나의 ROI share해서 feature로부터 각각의 출력을 prediction

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158727703-4b965617-f704-4a87-bf80-b0164fe4b7b7.png" width = "60%"></p>

**Mask R-CNN vs. Mesh R-CNN**
- `Mesh R-CNN` = `Mask R-CNN` + `3D branch`
- 3D branch가 3D mesh를 출력해준다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158727974-8a148e35-02f5-474c-bdbb-22068edf82ae.png" width = "60%"></p>

**More complex 3D reconstruction models**
- 3D object를 여러개의 sub-porblem으로 분해한다.
- Sub problem : 물리적 의미있는 분리 : Surface normal, depth, silhouette 이런 것들을 합성해 full 3D를 만들어낸다.

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158728373-71fcc360-fbe7-49ee-bd58-74a0e255982e.png" width = "60%"></p>

# 3D application example
## Photo refocusing
- 하나의 image를 depth map을 기반으로 defocusing 혹은 refocusing한다.
**Implement the post-refocusing feature in your phone**
- "prtrait mode" : focuse를 바꿔서 찍어준다.
- 하지만, 찍을 당시에 focus를 맞춰서 찍으면 focus를 바꾸는 데에 있어서 불편하다.
- origin image를 사용해 depth map(depth sensor 또는 neural network)을 사용해 foucsing

![image](https://user-images.githubusercontent.com/57162812/158728799-43205407-d018-4089-9c4c-93fd4782b43b.png)

**Defocusing a photo using depth map**

1. focus를 맞추고 싶은 depth threshold range [D_min, D_max]를 정한다.
2. Depth map thresholing을 통해서 mask를 만든다. range 내의 영역은 `focusing area`, range 외의 영역은 `defocusing area`로 측정한다.
    ```python
    focus_mask = depth_map[...,:] > threshold_value
    defocus_mask = depth_amp[...,:] <= threshold_vlaue
    ```
3. input image의 blur version을 만든다.
    ```python
    blurred_image = cv2.blur(origin_image, (20,20))
    ```
4. focused area에 대한 이미지의 mask와 defocused area에 대한 mask를 만든다.
    ```python
    focused_with_mask = focus_mak * origin_image
    defocused_with_mask = defocus_mask * blurred_image
    ```
5. 두개를 blending을 통해 refocusing image를 만든다.
  ```python
  defocused_image = focused_with_mask + defocused_with_mask
  ```

