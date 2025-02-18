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