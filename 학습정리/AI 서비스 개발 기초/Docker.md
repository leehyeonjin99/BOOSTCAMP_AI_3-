## 1. Docker 소개
### 1.1 가상화란?
- 문제점
  - 개발할 때, 서비스 운영에 사용하는 ㅓㅅ버에 직접 들어가서 개발하지 않는다.  
    즉, Local 환경에서 개발하고, 완료되면 Staging 서버, Production 서버에 배포
  - 따라서, 개발을 진행한 환경과 Production 서버 환경이 다를 수 있다.
    - OS가 다르기 때문에 라이브러리, 파이썬 등 설치할 때 다르게 진행해야 한다.
- 해결방법
  - 다양한 설정을 README 등에 기록하고 항상 실행하도록 하는 방법
    - 사람이 진행하는 일이라 Human Error 발생
    - 매번 이런 작업을 해야하는 과정이 귀찮다.
  - 서버 환경까지도 모두 한번에 소프트웨어화 할 수 없을까?
- 이 부분에서 나온 것이 **가상화**
  - 특정 소프트웨어 환경을 만들고, Local, Production 서버에서 그대로 활용
  - 개발과 운영 서버의 환경 불일치가 해소
  - 어느 환경에서나 동일한 환경으로 프로그램 실행 가능
  - 개발 외에 Research도 동일한 환경을 사용할 수 있다.
 
### 1.2 Docker 등장하기 전

- 가상화 기술로 주로 **VM(Virtual Machine)** 사용
  - VM은 호스트 머신이라고 하는 실제 물리적인 컴퓨터 위에 OS를 포함한 가상화 소프트웨어를 두는 방식
  - ex) 호스트 머신은 Window인데, Window에서 Linux를 실행
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154069332-8fb232fa-1ab8-420d-b278-21cc2751bd9b.png" width=300></p>

- GCP의 COmputer Engine 또는 AWS EC2가 이런 개념을 활용
  - 클라우드 회사에서 미리 만든 이미지를 바탕으로, Computing 서비스를 통해 사용자에게 동일한 컴퓨팅 환경 제공
  - 그러나 OS 위에 OS를 하나 더 실행시키는 점에서 VM은 굉장히 리소스를 많이 사용한다. 즉, **무겁다**.

- Container
  - VM의 무거움을 크게 덜어주면서, 가상화를 좀 더 경량화된 프로세스릐 개념으로 만든 기술
  - Container의 등장으로 이전보다 빠르고 가볍게 가상화 구현 가능

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154070148-e6a3f50d-34bf-490f-aa8a-ff0be61c4e30.png" width=300></p>


### 1.3 Docker 소개

Container 기술을 쉽게 사용할 수 있도록 나온 도구가 바로 **Docker** 이다.
- 비슷한 느낌  
  PC방에서 특정 게임만 설치하고, 고객이 특정 프로그램을 깔아도 재부팅할 때 항상 PC방에서 저장해둔 형태로 다시 복구  
  = Docker Image로 만들어두고, 재부팅하면 Docker Image 상태로 실행
  
**Docker Image** : 컨테이너를 실행할 때 사용할 수 있는 "템플릿"으로 Read Only  
**Docker Container** : Docker Image를 활용해 실행된 인스턴스로 Write 가능

<p align='center'><img src="https://user-images.githubusercontent.com/57162812/154070745-f8b9e6c7-850d-4110-9ed2-c1fdd5434c63.png" width=400></p>

### 1.4 Docker로 할 수 있는 일

1. 다른 사람이 만든 소프트 웨어를 가져와서 바로 사용할 수 있다.
  - ex. MySQL을 Docker로 실행
  - ex. Jupyter Notebook을 Docker로 실행
  - 다른 사람이 만든 소프트웨어를 **Docker Image**라 하며 OS, 설정을 포함한 실행환경이다. Linux, Window, Mac 어디에서나 동일하게 실행할 수 있다.
2. 자신만의 이미지를 만들면 다른 사람에게 공유할 수 있다.
  - 원격 저장소에 저장하면 어디서나 사용할 수 있다.
  - 원격 저장소 : Container Registry
    - 회사에서 서비스를 배포할 때는 원격 저장소에 이미지를 업로드하고, 서버에서 받아 실행하는 식으로 진행


## 2. Docker 실습하며 배워보기
### 2.1 설치하고 실행하기

```python
# docker pull "이미지 이름:태그"
# mysql 8버전의 이미지 다운
docker pull mysql:8

# 다운 방은 이미지 확인
docker images

# docker run "이미지 이름:태그"
# 다운받은 이미지 기반으로 Docker Container를 만들기
# --name : 컨테이너 이름
# -e : 환경변수 설정(사용하는 이미지에 따라 설정이 다르다)
# -d : 백그라운드 모드
# -p : 포트 지정(로컬 호스트 포트 : 컨테이너 포트)
docker run --name mysql-tutorial -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:8

# docker ps
# 실행한 Container 확인
docer ps

# docker exec -it "컨테이너 이름" /bin/bash
# MySQL이 실행되고 있는지 확인하기 위해 컨테이너 진입
docker exec -it mysql-tutorial /bin/bash

# mysql -u root -p
# MySQL 프로세스로 들어가 MySQL 쉘 화면이 보인다.
mysql -u root -p


# docker rm "컨테이너 이름"
# 멈춘 컨테이너 삭제
docker rm mysql-tutorial
```
