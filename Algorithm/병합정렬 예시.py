'''
# 병합정렬
핵심 아이디어: 정렬되어 있는 두 개의 배열을 합쳐서
정렬된 배열을 만드는 것은 빠르게 할 수 있다.

L = [2, 2, 3, 5, 5] i
R = [1, 3, 3, 4, 6] j

i와 j를 비교
더 작거나 같은쪽을 넣고
인덱스 + 1

arr = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

# 병합하기 로직
i, j, k = 0으로 놓고 출발
i: L 배열의 가장 작은 원소를 가리킴
j: R배열을 가리키는 포인터
l: 합칠 배열의 원소를 가리키는 포인터

# i번째와 j번째를 비교해서 둘 중 작은 값을 적는다
i번째가 작다 >> i번째를 arr 배열에 쓰고 i+=1, k+=1
j번째가 작다 >> j번째를 arr 배열에 쓰고 j+=1, k+=1
'''

i = 0
j = 0
k = 0

L = [2, 2, 3, 5, 5]
R = [1, 3, 3, 4, 6]

arr = [0]*10

while(i < len(L) and j < len(R)):
    # 왼쪽 배열의 수가 더 작다면
    if(L[i] <= R[j]):
        # 왼쪽 원소를 넣는다
        arr[k] = L[i]
        k += 1
        i += 1
        
    # 오른쪽 배열의 수가 더 작다면
    else:
        # 오른쪽 원소를 넣는다
        arr[k] = R[j]
        k += 1
        j += 1
        
# while문 끝남
# 둘 중 하나는 원소가 남아있을거다
# 나머지 값은 순서대로 집어넣으면 된다

# i가 남아있다면
while(i < len(L)):
    arr[k] = L[i]
    k += 1
    i += 1
    
# j가 남아있다면
while(j < len(R)):
    arr[k] = R[j]
    k += 1
    j += 1
    
# 정렬 끝

########## 예시 문제 ##########
# 주어진 배열 arr에서 left ~ right 구간만 정렬된 배열로 만든다
# L: left ~ mid-1 // R: mid ~ right
# L R을 합치면ㄴ서 arr에 덮어쓴다.
def merge(left, mid, right):
    global arr
    
    # 내가 사용할 부분 복사 떠오기
    L = arr[left:mid]
    R = arr[mid:right]
    
    i = 0
    j = 0
    k = left
    
    # i, j가 배열의 범위에 있다면
    while(i < mid - left and j < right - mid):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            k += 1
            i += 1
            
        else:
            arr[k] = R[j]
            k += 1
            j += 1
    
    # L, R 중 남은 배열 소진
    while(i < mid - left):
        arr[k] = L[i]
        k += 1
        i += 1
    
    # j가 남아있다면
    while(j < right - mid):
        arr[k] = R[j]
        k += 1
        j += 1

def merge_sort(left, right):
    # 1단계: 길이가 1일 때 까지 쪼갠다
    print(left, right)
    if(left < right):
        mid = (left + right)//2
        merge_sort(left, mid-1)
        merge_sort(mid, right)
        
    # 2단계: 쪼개진 배열을 합친다
    merge()


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 보통은 폐구간이 낫다
    cnt = 0
    merge_sort(0, N-1)