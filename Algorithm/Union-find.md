# Disjoint-sets
- 대표자를 통해 집합을 구분

## 상호배타 집합 연산
- Make-set(x): 자신을 대표자로 설정 >> x개의 집합을 생성
- Find-set(x): 대표자가 누구인가
- Union(x, y): x, y를 하나의 집합으로 묶자
```py
# 예시
'''
a b x y
make-set(x)
make-set(y)
make-set(a)
make-set(b)

union(x,y) >> x,y : x가 대표가 됨
union(a,b) >> a,b : a가 대표가 됨
find-set(y) >> x 리턴
find-set(b) >> a 리턴
union(x,a)
'''
```

## 서로소 집합
- 상호배타 집합
- disjoint set
- 교집합이 없다
- union find
- 세 가지 함수: make-set, union, find

- 집합인데 트리로 봐야한다
- 부모만 모두에 연결되어있고 나머지는 서로 연결되어있지 않다
  - union 하면서 트리 형태로 바뀐다
  - 부모가 대표임

- 서로소 집합이 아니면 트리가 아니게됨
- => 자식들 사이에 간선이 생김
- => 사이클 발생

## 서로소 집합 알고리즘
1. make-set(x): 자신이 대표자인 집합으로 만들기 >> 본인이 루트 노드인 트리 N개를 만듬
2. find(x): x 노드의 대표자를 찾는 함수(부모의 부모의... 재귀로 거슬러 올라가서 대표자를 찾는다)
3. union(x, y): x의 대표자와 y의 대표자를 찾아서, 한 대표자를 다른 대표자의 자식으로 만든다

```py
def find(a):
    global parents
    # 대표자를 찾았다
    if(parents[a] == a):
        return a

    # 대표자를 못찾았으면 부모가 대표자인지 확인
    return find(parents[a])

# comprehension
def find2(a):
    global parents
    # 대표자를 찾았다
    if(parents[a] == a):
        return a

    # path comrehension
    parents[a] = find2(parents[a])
    return parents[a]

def union(a, b):
    # 대표자를 찾는다
    aRoot = find(a)
    bRoot = find(b)
    # 한 대표자를 다른 대표자의 자식으로 만든다
    # b > a
    parents[bRoot] = aRoot



T = int(input())

for t in range(1, T+1):
    # 1~N: 노드의 번호, M: 유니온 파인드 진행 횟수
    N, M = list(map(int, input().split()))
    
    arr = list(map(int, input().split()))

    # 1. make_set
    # i번째 노드의 부모를 기록
    parents = [0]*(N+1)

    # 제일 처음에는 본인이 대표(부모)
    for i in range(1, N+1):
        parents[i] = i

    # M번의 union을 진행한다.
    for i in range(M):
        a = arr[2*i]
        b = arr[2*i + 1]

        # 두 대표자가 다른 경우에만 합칠 수 있다.
        if(find(a) != find(b)):
            union(a, b)

    # 그룹의 수를 센다
    # 대표자의 수 == 그룹의 수
    groups = set()
    for i in range(1, N+1):
        groups.add(find(i))

    # 결과 출력
    print(f'#{t}')

```