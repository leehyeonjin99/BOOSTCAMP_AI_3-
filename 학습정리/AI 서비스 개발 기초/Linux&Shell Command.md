## 1. Linux
### 1.1 Linux
### 1.2 Linus를 알아야 하는 이유
서버에서 자주 사용하는 Free OS로 여러 버전이 존재해 나만의 버전을 만들 수 있다. 또한 안정성, 신뢰성을 보장하며 Shell Command, Shell Script로 작성된다. 
### 1.3 CLI, GUI
- CLI : Command Lne Interface : Terminal
- GUI : Graphic User Interface : DeskTop
### 1.4 대표적인 Linux 배포판
- Debian : 온라인 커뮤니티에서 제작해 배포
- Ubuntu : 쉽고 편한 설치로 초보자들이 쉽게 접근 가능
- Redhat
- CentOS : Redhat이 공개한 버전을 가져와 브랜드와 로고를 제거하고 배포한 버전

## 2. Shell Command
### 2.1 Shell의 종류
- Shell : 사용자가 문자를 입력해 컴퓨터에 명령할 수 있도록 하는 프로그램
- Terminal / Console : 쉘을 실행하기 위해 문자 입력을 받아 컴퓨터에 전달, 프로그램의 출력을 화면에 작성
- sh : 최초의 Shell
- bash : Linux 표준 Shell
- zsh : Mac 카탈리나 OS 기본 Shell

### 2.2 기본 Shell Command
- **man python**
  - Shell Command의 manual을 보고 싶은 경우
- **mkdir**
  - make directory
  - ex. mkdir linux_test
- **ls**
  - list segment
  - 현재 접근한 폴더의 폴더, 파일 확인
- **pwd**
  - print working directory
  - 현재 폴더 경로를 절대 경로로 보여줌
- **cd**
  - change directory
  - ex. cd linux_test
- **echo**
  - Python의 print처럼 터미널에 텍스트 출력
    - ex. echo "hi"
  - echo "Shell Command" 입력시 Shell Command의 결과를 출력
    - ex. echo `pwd`
- **vi**
  - vim 편집기로 파일 생성
  - ex. vi vi_test.sh
  - ESC를 누른 후 :wq (write and quit), :wq! (강제로 저장하고 나오기), :q(그냥 나가기)
- **bash**
  - Shell Script 실행
  - ex. bash vi_test.sh (echo "hi") → "hi" 출력
- **sudo**
  - superuser do
  - 관리자 권한으로 실행하고 싶은 경우 command 앞에 sudo를 붙인다.
- **cp**
  - copy
  - 파일 또는 폴더 복사하기
  - ex. cp vi_test.sh vi_test2.sh
- **mv**
  - move
  - 파일, 폴더 이동하기(또는 이름 바꿀 때도 활용)
  - ex. mv vi_test.sh vi_test3.sh
- **cat**
  - concatenate
  - 특정 파일 내용 출력
  - 여러 파일을 인자로 주면 합쳐서 출력
- **clear**
  - 터미널 창을 깨끗하게 해준다.
- **history**
  - 최근에 입력한 Shell Command History 출력
  - 결과에서 !를 붙이고 숫자 입력시 그 Command를 다시 활용할 수 있다.
- **find**
  - 파일 및 디렉토리를 검색할 때 사용
  - find . -name "File" : 현재 폴더에서 File이란 이름을 가지는 파일 및 디렉토리 검색
- **export**
  - export로 환경 변수 설정
  - export water="물" #띄어쓰기 주의
  - echo $water → 물이라 출력된다.
  - terminal이 꺼지면 사라지게 된다. 매번 쉘을 실행할 때마다 환경변수를 저장하고 싶으면 .bashrc, .zshrc에 저장하면 된다.
    - vi ~/.bashrc 하고 제일 하단에 export water="물"을 저장하고 나온다. 그 후, source~/.bashrc
- **alias**
  - 기본 명령어를 간단히 줄일 수 있다.
  - ex. alias ll2="ls -l"
- **head, tail**
  - 파일의 앞/뒤 n행 출력
  - ex. head -n 3 vi_test.sh
- **sort**
  - 행 단위 정렬
  - cat fruits.txt|sort
- **uniq**
  - 중복된 행이 연속으로 있는 경우 중복 제거
  - sort와 함께 사용
  - "-c" : 중복 행의 개수 출력
  - cat fruits.txt|sort|uniq
- **grep**
  - 파일에 주어진 패턴 목록과 매칭되는 라인 검색
- **cut**
- 파일에서 특정 필드 투툴
- "-f" : 잘라낼 필드 지정
- "-d" : 필드를 구분하는 구분자
- cat cut_file|cut -d : -f 1,7 # 1번째, 7번째 값을 가져옴
### 2.4 Redirection & Pipe
- Redirection : 프로그램의 출력(stdout)을 다른 파일이나 스트림으로 전달
  - > : 덮어쓰기(Overwrite)
  - >> : 맨 아래에 추가하기(Append)

**연습 문제**
- test.txt 파일에 "Hi!!!!"을 입력해 주세요.
  - echo "Hi!!!!" > test.txt
- test.txt 파일 맨 아래에 "kkkkk"를 입력해 주세요.
  - echo "kkkkk" >> test.txt
- test.txt의 라인 수를 구해주세요.
  - cat test.txt | wc -l
### 2.5 서버에서 자주 사용하는 Shell Command
- **ps**
  - process status
  - 현재 실행되고 있는 프로세스 출력하기
- **curl**
  - Client URL
  - Command Line 기반의 Data Transfer 커맨드
- **df**
  - Disk Free
  - 현재 사용중인 디스크 용량 확인
- **scp**
  - Secure Copy
  - SSH를 잉ㅇ해 네트워크로 연결된 호스트 간 파일을 주고 받는 명령어
  - ex. scp local_path user@ip:remote_directory
- **chmode**
  - change mode
  - 파일의 권한을 변경하는 경우 사용
  - r:1, w:2, x:4

**Special Mission**
카카오톡 그룹 채팅방에서 옵션 - 대화 내보내기로 csv로 저장 후, 쉘 커맨드 1줄로 카카오톡 대화방에서 2021년에 제일 메세지를 많이 보낸 TOP 3명 추출하기!

csv로 저장하는 방법은 찾지 못해 txt 파일로 저장하여 진행하였다.
```python
 cat KakaoTalk.txt | grep "\[" | cut -d ] -f 1 |sort | uniq -c | sort
```
