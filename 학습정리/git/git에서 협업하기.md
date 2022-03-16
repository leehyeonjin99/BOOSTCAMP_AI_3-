## 깃에서 협업하기

- Git
  - version은 `로컬 저장소`와 `원격 저장소` 모두에 존재한다. 
  - 둘 중 하나가 날라가도 한쪽에는 version이 남아있다.
  - 인터넷이 끊겨도 version을 만들 수 있다.

**두개의 실험 환경을 생성해 실습해보기**

<p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158403920-81fee1d7-8757-4e80-8b24-a623c3c174f5.png" width="30%"></p>

- 환경
  - `left`
  - `right`

- **가정1. 두 환경이 동시에 서로 다른 파일을 업로드 하려 한다.**
  - `left`가 left.txt를 create하여 작성 후 먼저 commit → push를 하였다.
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158405202-14d3c909-e8ec-415c-a97d-5d4db7c7833c.png" width="30%"></p>
  - `right`가 right.txt를 create하려 작성 후 commit → push를 하려 한다.
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158407222-61d6996f-248a-4162-8fc4-a48e743ca23f.png" width="30%"></p>
  - 하지만, 이 상태에서 rigth.txt를 push하면 오류가 발생한다. 따라서 pull을 하여 `원격 저장소`의 상태와 동일하게 만든 후, push를 진행한다.
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158407745-63244ee7-517c-49d8-970b-14c47e2fc273.png" width="60%"></p><p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158407835-36dbecac-5571-4751-89e4-99bff1e2c9cb.png" width="60%"></p>

- **가정2. 두 환경이 동시에 서로 같은 파일의 다른/같은 부분을 업로드 한다.**
  <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158408602-303263a7-1985-4a17-988c-633b90660889.png" width="15%"></p>
  
  - `left`가 2와 4를 L2와 L4로 변경하여 먼저 commit → push를 하였다.  
    <img src="https://user-images.githubusercontent.com/57162812/158409185-42a3b2a0-2623-4f86-b7c1-24946aa8183a.png" width="15%">
    <img src="https://user-images.githubusercontent.com/57162812/158409249-fe502452-bd50-4bfd-b741-6fb3c2030ba6.png" width="50%">

  - `right`가 3와 4를 R2와 R4로 변경하여 commit → push를 하려 한다.
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158409498-71ab20e2-6894-477c-a315-37cc0f5cc6ba.png" width="15%"></p>
  - 하지만, 이상태에서 common.txt를 push하면 conflict가 발생한다.  
    > 이때, 2와 3은 conflict가 발생하지 않는다.
    > `left`와 `right`의 공통 조상인 `BASE`를 참조하기 때문이다.
    <img src="https://user-images.githubusercontent.com/57162812/158409873-b2773e36-7cf1-4920-b3cb-6843582e4e70.png" width="45%">
    <img src="https://user-images.githubusercontent.com/57162812/158409969-223f493d-068e-49e7-b765-6d5c312bbc64.png" width="45%">
  - `<<<<<<<HEAD`는 현재 저장소에서 변경한 내용이고 `>>>>>>>534db0`은 원격 저장소에 저장되어있는 버전의 내용이다. 따라서 둘을 위의 4가지 옵션에 따라서 merge하여 commit → push를 한다.  
    <img src="https://user-images.githubusercontent.com/57162812/158410720-5cb36906-9308-42d4-92ab-a78a30813de1.png" width="10%">
    <img src="https://user-images.githubusercontent.com/57162812/158411146-aad8ea4a-b1d4-48b9-bd30-1219ad0c3781.png" width="60%">
    
## Branch
**Head는 Working directory가 어떤 버전과 같은지 가리킨다.**
> head는 git graph에서 비어있는 동그라미이다.
<p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158412402-075f94e8-0902-4802-ad81-0f04839b8d8e.png" width="50%"></p>

- `Working directory`는 코드를 작성하는 공간이다.
- 선택적인 commit을 위해 `Stage Area`가 존재한다.
- `.git`은 repository이다. push를 해갈 때, Working directory가 아닌 Stage Area에서 진행된다.

<p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158413157-6246a91c-702d-422b-8657-23ca2056ad88.png" width="70%"></p>

- `master`는 마지막 commit을 가리킨다.
- `HEAD`는 현재 commit을 가리킨다.
  - 만약 원하는 버전으로 working directory 옮기고 싶으면 HEAD를 옮기면 된다.
  - HEAD는 `Checkout`을 통해 옮긴다. 다시 돌아올 때는 특별한 이유가 없다면 `Branch Checkout`/`git checkout master`을 한다.
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158413842-6a8bd65a-ba45-4b6a-8dce-4eeb47299c20.png" width="50%"></p>
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158413917-6bc98b42-0d9c-4db5-83db-80e0956fecb0.png" width="50%"></p>
    <p align = 'center'><img src="https://user-images.githubusercontent.com/57162812/158414013-a3791a48-321c-450a-9b17-b03cd037e35e.png" width="50%"></p>

**HEAD가 version을 직접 가리킬때는?**

1. A, B, C version이 순서대로 만들어 졌다. `HEAD → master → C`
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158414853-d5a777fc-a59e-4f3d-936d-353be95eea80.png" width="40%"></p>
  
2. D version을 생성하였다. `HEAD → D` (Detached HEAD state with `git checkout D`), `master → D` : master와 HEAD가 분리되었다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158415288-f6887ea2-cc4f-4b83-b782-9448e79da747.png" width="40%"></p>
  
3. E version을 commit → push 를 한다면? HEAD가 직접 E를 가리키게 된다. `master → D`, `HEAD → E`
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158415662-e82f7516-ffad-43db-9120-8f78d5ad207d.png" width="40%"></p>
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/158417426-0f0f752a-926f-478e-a7f6-74d4d29057a8.png" width="40%"></p>
  
4. 여기서 HEAD를 `git checkout master`을 한다면? E version의 정보가 모두 날라간다.            
   - 만약 실험적인 작업을 할때라면, 쉽게 버리게 되기 때문에 좋은 기능일 수 있다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158416427-bd257e77-1f21-4c10-ae7e-7fc5ae6ff194.png" width="40%"></p>
    
5. 만약 실험을 성공하였다면? create branch로 새로운 branch를 만들어 작업을 하면 된다.  
    - 만약 일상적 작업으로 돌아가려면, git checkout master를 하면 된다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158416363-a6a8c706-e88b-4b76-b78d-65d65fa2e3cf.png" width="40%"></p>
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158417556-83da0101-b8b8-4ad2-8f97-556089c23a07.png" width="40%"></p>
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158418250-4a1ad7af-28bf-4294-9b6e-fd81544aff89.png" width="40%"></p>
  
     `git checkout exp`를 하고 push를 한다면 git repository에도 exp branch가 생성된다.
  <p align='center'><img src="https://user-images.githubusercontent.com/57162812/158417815-90b3e89c-1c11-4852-99d2-dd513aa2da58.png" width="30%"></p>








