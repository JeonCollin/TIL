# Back tracking
- 해를 찾는 중에 해가 없다고 판단되면 돌아간다
- DFS는 갈림길에 있는 모든 루트를 거쳐서 돌아간다
- 백트래킹은 필요 없는 길은 지나친다

## 부분집합
```py
def backtrack(a, k, n):
    c = [0]*MAXCANDIDATES

    if(k == n):
        process_solution(a,k)

    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k+1, n)

def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a,k):
    for i in range(k):
        if(a[i] == True):
            print(num[i], end = '')
    print()
```
- ex: 백트래킹을 이용한 부분집합의 합
```py
def f(i,N,s,t):
    if i == N:
    #     # 원하는 길이의 원소를 선택한 경우   
 
    # elif s == t:
    #     # i-1 원소까지의 합이 찾는 값인 경우
    #     print(bit)
    
    # elif s > t:
    #     #남은 원소를 고려할 필요가 없는 경우
    #     return

    else:
        # 남은 원소가 있고, 고려해야하는 경우

        # i 원소 포함하는 경우
        subset[i] = 1
        f(i+1, N, s+A[i], t)

        # i 원소 미포함 경우
        subset[i] = 0
        f(i+1, N, s, t)

# 총 원소가 10개라면 최악의 경우에는 1024번 돌게됨
# 근데 보통은 100번대로 돌게됨
```

```py
def subset(idx):
    # 재귀호출을 이용한 부분집합

    # N개 선택 여부를 결정완료
    if(idx == N):
        # 여기서 부분집합이 완성됨
        print(used)
        # [0,0,0,0,0] [0,0,0,0,1] [0,0,0,1,0] ...

    else:
        # 현재 원소를 선택하는 경우
        used[idx] = 1
        subset(idx+1)
        # 현재 원소를 선택하지 않는 경우
        used[idx] = 0
        subset(idx+1)

myset = [1, 2, 3, 4, 5]
N = len(myset)
used = [0]*N
```

## 순열
- 백트래킹을 이용하여 {1,2,3...,NMAX} 순열 구하기
- 첫 번째 자리, 두 번째 자리 ... 정해놓고 호출한다
- 그 후로도 자리 정해놓고 재귀호출
```py
def permutation(i, N):
    if i == N:
        # 순열 완성
        # P = [1,2,3] [2,1,3] [3,2,1] ...

    else:
        # 현 위치부터 오른쪽으로 차례대로 swap
        for j in range(i, N):
            # p[i]를 첫 번째로 결정
            # p[j]와 자리를 바꾼다
            P[i], P[j] = P[j], P[i]
            f(i+1,N)
            # P[i] 복구
            P[i], P[j] = P[j], P[i]

P = [1,2,3]
```

```py
def permutation(idx):
    # 재귀구조를 이용한 nPr = 5P3

    # R개를 모두 선택했다면 순열 출력
    if(idx == R):
        # 여기서 순열이 완성된다
        print(P)
        # [1,2,3] [1,2,4] [1,2,5] ...

    else:
        # myset을 순회하며 순열로 포함할 원소를 선택
        for i in range(N):
            # 사용하지 않은 원소라면 선택한다
            if(used[i] == 0):
                # 사용 기록
                used[i] = 1
                # 순열에 넣기
                P[idx] = myset[i]
                # 그 뒤에서 선택하도록 순열 호출
                permutation(idx+1)
                # 사용기록 초기화: 새로운 순열 생성
                used[i] = 0
                
myset = [1, 2, 3, 4, 5]
N = len(myset)
used = [0]*N
R = 3
P = [0]*R
permutation(0)
```

## 중복순열
- 순열이랑 비슷한데, 방문처리만 안하면 된다
```py
def PI(idx):

    # 중복순열이 완성된다
    if(idx == R):
        print(PI)
        # [1,1,1] [1,1,2] [1,1,3] ...

    else:
        for i in range(N):
            PI[idx] = myset[i]
            PI(idx+1)

PI(0)
```