## Memoization
- 일반적인 재귀는 중복호출이 매우 많다
- memoization: 계산한 값을 메모리에 저장하여 중복 호출을 줄이는 기법

- 일반적인 피보나치: 시간복잡도 2^n
```py
def fibo(N):
    if(N == 0):
        return 0

    elif(N <= 1):
        return 1

    else:
        return fibo(N-1) + fibo(N-2)
```

- memoization 사용: 시간복잡도 n
```py
def fibo1(N):
    global memo

    # 함수를 호출하는데, 없는 새로운 값이라면
    # memo에 저장된 값을 이용해서 가져온다
    if(>= 2 and memo[n] == 0):
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

# memo스택 저장
memo = [0]*(n+1)
# 피보나치 수 초기값
memo[0] = 0
memo[1] = 1
```

## DP
- 작은 부분 문제를 해결하고 그 해를 이용하여 큰 문제를 해결한다
- DP구현: 재귀 방식 fibo1, 반복 방식 fibo2
- 반복방식이 더 효율적
- **수열의 점화식을 찾아야 한다**

- 피보나치: DP 사용
```py
def fibo2(N):
    # 저장할 공간
    f = [0]*(n+1)
    # 작은문제: 앞에 있는 두 수를 합치면 되네?
    f[0] = 0
    f[1] = 1

    #그러면 그냥 더하자
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]
```

## DFS
- **갈 수 있는 가장 깊은 경로까지 갔다가 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아온다**

- 왔다갔다 반복해야 하므로 후입 선출 구조의 스택을 사용할 수 있다
```py
# 1단계: 초기화
# visited[], stack[] 초기화
# visited 초기화는 False로 한다

def DFS(v):
    # 2단계: 시작점 v 방문 -> True
    visited[v] = True

    while True:
        # 3단계: 인접 지점 방문
        if('v의 인접 정점 중 방문 안한 w가 있다면'):
            push(v) #w가 아니라 v push
            v = w # w에 방문
            visited[w] = True
        else:
            # 4단계: 더 이상 갈 곳이 없다면 pop
            if('스택이 비어있지 않다면'):
                v = pop()

            # 5단계: 모두 방문했으면 끝
            else:
                break
```

```py
'''
입력
7 8
인접하는 노드 정보
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v, N):
    # 방문표시, 스택
    visited = [0]*(N+1)
    stack = []

    while True:
        # 첫 방문
        if(visited[v] == 0):
            visited[v] = 1
            print(v)

        # v에 인접하고 방문 안한 w가 있으면
        for w in adj_list[v]:
            if(visited[w] == 0):
                #방문 먼저 기록
                visited[w] = 1
                stack.append(v)
                v = w
                break

        # 더 이상 갈 곳이 없는 경우
        else:
            # pop
            if(stack):
                v = stack.pop()

            # 스택이 비었으면 종료
            else:
                break

# V: E:
V, E = map(int, input().split())
graph = list(map(int, input().split()) )

#인접 리스트 초기화
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    v, w = graph[i*2], graph[i*2+1]

    # 인접하는 정보를 리스트로 만들기
    adj_list[v].append(w)
    adj_list[w].append(v)
```

# 그래프 경로
- 노드와 간선으로 이루어진 구조
- 비선형적 자료구조
- 그래프의 순회: 모든 정점을 1번씩만 방문
- 방문처리가 중요
- 저장방법: 인접행렬, 인접리스트, 간선리스트

## 인접행렬
- **통행 가능한 정보를 저장한 행렬**
- 2차원 행렬로 그래프를 저장
- 두 정점 a, b가 a > b 방향일 때
- 연결되어있다면: adj[a][b] = 1, 아니면 0

## 인접리스트
- **그래프를 그대로 받은 행렬**
- adj[1]: 1번 정점과 연결되어 있는 정점 번호 저장
- ex: **adj[1] = [2, 3, 5] >> 1번이 1-2, 1-3, 1-5 로 연결되어있다**
- 만약 무향그래프라면 반대 방향도 넣는다
- ex: adj[3] = [**1**, ...]

## 간선리스트
- [[출발점, 도착점], [출, 도], ... ]
- ex: edge_list = [[1, 2], [1, 3], [1, 5], ...]
- 그래프 탐색을 할 때는 인접행렬 또는 인접 리스트를 사용

1. 인접행렬을 만든다
  - arr[v1][v2] = 1이면, v1 > v2 노드로 이동 가능
  - 크기: (V + 1)*(V + 1) 이다 >> 1 ~ V 인덱스만 사용함
  - 무향그래프(양방향): 대칭형태
  - 유향그래프(단방향): 비대칭
  - 연결상태 확인: 인덱스만 확인하면 바로 나옴 >> 시간복잡도 O(1)

2. 인접리스트를 만든다
  - arr[v1] = [연결된 노드들]
  - 크기: (V+1) * (연결된 노드 수) >> 1 ~ v 인덱스를 사용
  - 연결상태 확인: 해당 인덱스에서 또 찾아야 함 >> 시간복잡도 O(N)