### 서버의 원격 저장소
- origin 이라고 부름
- 주소: https://github.com/JeonCollin/git-test.git
- 비어있는 상태(커밋 X, 브랜치 X)

- git push -u origin master: origin 서버에 master란 이름의 브랜치를 만들면서 로컬의 master 브랜치를 서버의 master 브랜치와 연결

- 로컬저장소를 서버에 최초로 푸시할 때는 -u origin master 옵션을 붙이고 그 다음부터는 필요 없음(이미 연결되어있으므로로)

### 로컬 저장소
- 최초의 커밋을 하면 기본 브랜치 master에 커밋 되는 것
- master 브랜치에 커밋이 쌓여있음.

---

To git remote add origin https://github.com/JeonCollin/git-test.git

[new branch] master -> master
branch 'master' set up to track 'origin/master'

master: 로컬의 master 브랜치
origin/master: 서버의 master 브랜치

---

## git push -u origin master
- 서버의 원격 저장소가 비어있는 경우, 한 번만 할 수 있음
- 팀장이 제일 처음 원격 저장소를 만들고,
 나머지 팀원들은 git clone을 통해 원격 저장소를 복제하여 사용해야 함



55. remote add origin https://github.com/JeonCollin/git-test.git
56. git status
57. git add .
58. git commit -m "b-function"
59. git status
60. git log --oneline
61. git push -u origin master
62. git push -u origin master
63. git remote add origin https://github.com/JeonCollin/git-test.git
64. git branch -M master
65. git push -u origin master
66. git remote -v
67. touch new-file.txt
68. git add .
69. git commit -m "new-file"
70. git push
71. git log --oneline
72. git pull
73. git log
74. cd ..
75. git clone https:github.com/JeonCollin/git-test.git git-clone
76. git clone https:github.com/JeonCollin/git-test.git git-clone
77. git clone https://github.com/JeonCollin/git-test.git git-clone
78. cd git-clone
79. git log --oneline
80. ls
81. history

---
## gitignore
- 추적에서 제외할 파일/폴더들의 목록

- 현재 디렉토리에는 보이지만 git에 추적되지 않으므로 향후 저장소에 저장되지 않음

- 이미 추적되는 파일은 .gitignore에 추가해도 해제가 안되므로 gitignore를 먼저해아한다

    - 커밋을 하지 않고 git add만 한 상황이라면 명시적으로 git rm --cached <파일명>으로 해당 파일을 해제해야한다.

    - 커밋을 했다면(add + commit) git rm --cached를 해도 기존에 저장소에 추가된 파일을 삭제하는 커밋이 새로 만들어지면서 추적해제

    - 삭제하는 커밋은 추가로 생성되지만,  이전 커밋을 보면 기존에 커밋에 저장된 파일을 볼 수 있음

## gitignore 관련 명령 정리
```
echo "문자열" > 파일명: 해당 문자열을 내용으로 하는 파일 생성

echo "문자열" >> 파일명: 기존 파일의 마지막 줄에 "문자열" 추가

echo "a.txt" >> gitignore: gitignore 파일에 a.txt를 추가

echo "a.txt" > gitignore: gitignore 파일을 만들고 a.txt를 추가
```

**스테이징 영역에서 추적 제외하기**
```
git add b.txt: b.txt를 스테이지 영역에 추가(git이 계속 이 파일을 추적함)

git rm --cached b.txt: b.txt를 스테이지 영역에서 삭제, 추적에서도 제외
```

**커밋 후 추적 제외하기**
```
git add c.txt

git commmit -m "c.txt added": c.txt를 커밋함(기록에 남음)

git rm --cached c.txt: 추적에서 제외됨. 새로 커밋하면 c.txt는 제외되는데 과거 기록은 남아있음

git add . : c.txt를 삭제하고, 추적에서 제외하는 변경사항이 스테이징 영역에 올라감

git commit -m "c.txt deleted": c.txt가 삭제되는 커밋이 만들어짐. 그래도 기록에는 남음
```

## git checkout
- git checkout <커밋해시번호>: 해당 커밋으로 돌아감
    - HEAD 포인터가 해당 커밋으로 이동
    - master 브랜치 포인터는 그대로
    - 해당 커밋 당시의 폴더 내용이 보임
    - git checkout master: 마스터의 최근 커밋으로 다시 이동
    - 커밋의 해시번호를 확인하려면 git log --oneline


97. touch a.txt
98. git status
99. touch .gitignore.
100. git status.
101. git status.
102. touch b.txt.
103. git add ..
104. echo "b.txt" >> .gitignore.
105. cat .gitignore.
106. cat .gitignore.
107. git rm --cached b.txt.
108. git status

a384750 (HEAD -> master, origin/master, origin/HEAD) d.txt deleted & untracked

4d19fa8 d.txt added

3e6c787 gitignore c.txt

6e0cccb c.txt removed

12c7b2e commit c.txt

커밋의 번호 
- head: 현재 커밋을 가리키는 포인터
- origin/HEAD: 원격저장소에서 가장 최근 커밋을 가리키는 포인터터
- master, origin/master: 브랜치(커밋을 가리키는 포인터)
- 현재 체크아웃된 브랜치에서 커밋을 하면, 커밋과 함께 브랜치가 이동
- master, origin/master 브랜치가 가장 최근 커밋을 가리키고 있음

커밋을 한 번 하면 마스터 포인터가 생김. 커밋을 또 하면 마스터 포인터가 옮겨감.

---

## git revert
- 특정 커밋을 무효화하는 새로운 커밋을 만듬

- 무효화 되었지만 이전 커밋은 그대로 남아있다.

- git checkout <커밋해시번호> : 이전 커밋으로 돌아가기

- ls -l: 파일 목록 확인

- git checkout master: 마스터의 최근 커밋으로 돌아가기

## git reset
- 과거로 돌아감. 되돌아간 commit 이후의 모든 commit은 삭제됨.

- 근데도 기록은 남음

- git reset --hard 해시: 
    - 작업 영역에서도 삭제
    - stage 영역에 없음
    - 커밋 기록 삭제

- git reset --mixed 해시
    - 작업 영역 그대로(삭제x)
    - stage 영역에 없다(추적X)
    - 커밋 기록이 삭제됨

- git reset --soft 해시
    - 작업 영역 그대로: ls -1
    - 삭제된 것은 stage 영역에 남아있음: git status
    - 커밋 기록은 삭제됨(데이터베이스에는 남음): git log --oneline

## git restore 파일명
- 이미 커밋된 파일이 있는 경우
- 해당 파일을 수정했는데, 수정한게 마음에 안들어서 커밋된 파일로 복원하고 싶은 경우
- 커밋에 들어있는 파일을 복사해서, 작업 영역에 있는 파일에 덮어쓰기

### unstage 하고 싶을 때
- git add를 했는데 취소하고 싶을 때!
- git rm --cached: commit이 없을 때
    - stage 영역에서 제외하면서, commit된 게 있으면 삭제하는 커밋을 만들게됨
- git restore --staged: commit이 있을 때도 가능
    - stage 영역에서만 삭제, 작업 영역은 그대로
    - git restore: 커밋에서 복사해서 작업 영역 내용 덮어쓰기(복원)

* 요약: git rm은 git reset --hard와 비슷하다
    - git rm은 다음 커밋에서 삭제
    - git reset --hard는 커밋해버림
    - **git add를 취소하고 싶다면 git restore --staged 파일명 을 사용해라**
