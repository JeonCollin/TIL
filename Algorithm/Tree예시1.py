'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(n):
    # 완전이진트리 전위 순회
    # if(T != 0):
    if(n != 0):
        print(n) # visit(T)
        pre_order(n*2) # pre_order(left[T])
        pre_order(n*2+1) # pre_order(right[T])

        
## 순회법 셋 다 방법은 똑같은데, 순서만 다르다
def pre_order(T):
    # 전위 순회법: 현재 > 왼 > 오
    # 현재 노드에 자식이 존재한다면
    if (T != 0):
        # 현재 노드를 출력
        print(T)
        # 왼쪽 자식으로 이동
        pre_order(left[T])
        # 오른쪽 자식으로 이동
        pre_order(right[T])


def in_order(T):
    # 중위 순회법: 왼 > 현재 > 오
    # 현재 노드에 자식이 존재한다면
    if (T != 0):
        # 왼쪽 자식으로 이동
        pre_order(left[T])
        # 현재 노드를 출력
        print(T)
        # 오른쪽 자식으로 이동
        pre_order(right[T])


def post_order(T):
    # 후위 순회법: 왼 > 오 > 현재
    # 현재 노드에 자식이 존재한다면
    if (T != 0):
        # 왼쪽 자식으로 이동
        pre_order(left[T])
        # 오른쪽 자식으로 이동
        pre_order(right[T])
        # 현재 노드를 출력
        print(T)
    

# 총 노드 수
N = int(input())
# 간선 수
E = N - 1
# 간선 정보 받음
arr = list(map(int, input().split()))

# 부모가 인덱스. 왼쪽/오른쪽 자식을 저장
left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(E):
    # 시작(부모): 1 1 2
    #  끝(자식) : 2 3 4
    p = arr[i*2]
    c = arr[i*2 + 1]

    # 왼쪽 자식 먼저 채운다
    if(left[p] == 0):
        left[p] = c

    # 왼쪽 자식이 있다면 오른쪽에 채운다
    else:
        right[p] = c

# 자식이 인덱스. 부모를 저장
par = [0] * (N + 1)
root = 1

for i in range(E):

    p = arr[i*2]
    c = arr[i*2 + 1]

    par[c] = p


print(left)
print(right)
pre_order(3)
post_order(1)