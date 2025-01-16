ctrl + shift + p
한 후에 markdown 검색 =>
open preview to the side 선택

# 큰제목
## 중간제목
### 소제목
#### 소소제목

## 문단
첫 번째 문단입니다. 그냥 쓰면 문단입니다.
한 줄을 띄어도 이어집니다.

두 줄을 띄어야 나눠집니다.
가독성을 위한 것입니다.

알겠냐?

## 글자
*별을 하나만쓰면 기울임체*

**두 개 쓰면 볼드체**

***세 개 쓰면 기울이고 볼드체***

~~물결 두 개로 취소선 긋기~~

==형관펜 긋기 안되는 곳도 있음==

:kissing: 이모지 넣기

## 리스트
### 순서가 없는 리스트
-, *, +를 써서 만듬

- 순서가
* 없는
+ 리스트
- 입니다.

### To-do List

- [ ] 스타트캠프 1일차
- [x] 스타트캠프 2일차


### 순서가 있는 리스트
번호. 를 사용합니다.

1. 사과
2. 오렌지
875. 포도

아쉽게도 중간에 번호를 건너뛰는 방법은 없습니다.
영어 소문자, 로마자 리스트도 지원하지 않습니다.

꼬우면 HTML 쓰세요.

## 중첩된 리스트
- 리스트는
    - 두 칸을 띄어서
        - 중첩이 가능합니다

### 인용문
> 꺽쇠를 하나 쓰면 인용문.
> 여러 줄에 걸쳐서 쓸 수 있음
>
>> 꺽쇠 두 개로 인용문 안에 nest 가능

> ### 소제목
> - 리스트도 
> - 넣을 수 있다.

### 링크 넣기
[]() 대괄호와 소괄호를 같이 쓴다.

[네이버](https://www.naver.com)

### 이미지 넣기
느낌표, 대괄호, 소괄호

![랜덤이미지](https://picsum.photos/200/300)

---

대시를 3개 사용하면 가로 줄을 넣을 수 있음

## 코드넣기
백틱 세 개를 써서 넣을 수 있엉

```python
print("Hello")
```

```C
printf("hello")
```

파이썬에서는 `print("hello")`를 써서 문장 하나만 가능하다.

---

# 인터페이스란?
- 두 가지 서로 다른 시스템이 만나는 접점
- 상호 규칙을 정의 해야 함


## CLI <=> GUI
~/Desktop

~: 사용자의 기본 폴더(/c/Users/SSAFY)
/: 폴더와 폴더 사이

- pwd: 현재 디렉토리 출력
- ls: 현재 작업 중인 디렉토리의 폴더/파일 목록을 출력
- mkdir: 현재 디렉토리에 폴더 생성
- touch: 파일만들기
- cd: 이동(.하위폴더 ..상위폴더)
- start: 폴더/파일을 열기
- rm: 파일 삭제

## git
1.  pwd
2.  ls
3.  mkdir darkdown-test2
4.  mkdir marckdown-test2
5.  cd markdown-test2
6.  cd marckdown-test2
7.  cd ..  >> 상위디렉토리로 이동
8.  cd git-test
9.  mkdir git-test >> git-test라는 폴더 만듬
10.  cd git-test >> git-test 폴더로 이동
11.  ls
12.  git init >> git-test 폴더를 git 환경으로 초기화
13.  ls
14.  ls -a >> .이나 .. 찍힌 파일은 숨기는데 그것 까지 다 드러냄
15.  git status >> 현재 상태를 보여줌
16.  touch README.md >> README.md 파일 생성
17.  git status
18.  git add README.md >> README.md를 git에 올릴 수 있도록 준비
19.  git status
20.  git commit -m "first commit" 
21.  git config --global user.email "wkror7979@naver.com" >> 아이디 등록
23.  git config --global user.name "Sangwoo Jeon" >> 이름 등록
24.  git commit -m "first commit" >> 커밋: git에 전송
25.  git status
26.  git status
27. *그냥 친듯
28.  git status
29.  git add . >> 지금까지 한 작업 모두 커밋 준비
30.  git status
31.  git commit -m "second commit"
32.  git log
33.  git log -- oneline >> 로그를 한 라인씩 보여줌
34.  git log --oneline
35.  echo "Hello world" > sample2.txt // sample2에 글자 타이핑
36.  echo "Third line" > sample.txt
37.  echo "Third line" > sample.txt
38.  echo "Third line" >> sample.txt // 가장 아래 줄에 글자 타이핑
39.  echo "forth line" >> sample.txt
40.  git add .
41.  git commit -m"third commit"
42.  git log --oneline
43.  git log --graph --oneline
44.  git log --graph --oneline --decorate --all
45.  history >> 지금까지 명령어들 다 보여줌
46.  git commit --amend >> 가장 최근 commit만 수정할 수 있음 (i > insert 모드, esc > 모드 취소, :wq > 저장하고 나가기)
47.  git log --oneline
48.  git commit --amend
49.  git log
50.  git log --oneline
51.  vim b-function.txt >> vim파일 만듬: amend와 같은 창이 뜬다. 같은 방식으로 수정하면 된다.
53.  git commit --amend
54.  history
