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
def merge(left, mid, right):
    global mylist
    # 사용할 부분 복사
    L = mylist[left : mid+1]
    R = mylist[mid+1 : right+1]

    # 인덱스 초기화
    i = 0
    j = 0
    k = left

    # 배열의 범위 내에서
    while(i < mid+1 - left and j < right - mid):
        # 왼쪽이 더 작다면 왼쪽 원소를 넣는다
        if(L[i] <= R[j]):
            mylist[k] = L[i]
            i += 1
            k += 1

        # 오른쪽이 더 작다면 오른쪽 원소를 넣는다
        else:
            mylist[k] = R[j]
            j += 1
            k += 1

    # 반복문이 끝나면 아직 남은 리스트가 존재함
    # 왼쪽이 남은 경우
    while(i < mid+1 - left):
        mylist[k] = L[i]
        i += 1
        k += 1

    # 오른쪽이 남은 경우
    while(j < right - mid):
        mylist[k] = R[j]
        j += 1
        k += 1



def merge_sort(left, right):
    # 길이가 1이 될 때 까지 쪼갠다
    if(left < right):
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        # 쪼갠 놈들을 합친다
        merge(left, mid, right)



T = int(input())

for t in range(1, T+1):

    # N: 정수의 개수
    N = int(input())

    # 정수 받기
    mylist = list(map(int, input().split()))

    merge_sort(0, N-1)

    print(mylist)

    print(f'#{t} {mylist[N//2]} ')
