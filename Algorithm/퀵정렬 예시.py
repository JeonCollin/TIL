'''
 # 퀵정렬: 모든 숫자를 한 번에 정렬하는 것은 어렵다
 >> 한 숫자만 정렬된 위치에 놓는 것은 쉽다
 '''
 
 arr = [5,8,1,7,3,4,2,9]
 
 # arr의 첫 번째 원소 5
 # 만약 arr이 정렬되어 있다면 몇 번째에 있어야 하는가?
 # 정렬된 위치: 정렬되었을 때 해당 원소의 위치
 
 # 정렬된 위치를 찾을 때는
 # 왼쪽 i, 오른쪽 j 포인터 사용
 # 왼쪽에서는 기준보다 큰 것을 찾는다.
 # 오른쪽에서는 기준보다 작은 것을 찾는다.
 # 둘을 교환한다
 # [(기준점보다 작음), 기준, (기준보다 큼)]
 
 # 0번 인덱스를 기준점으로 삼는다
 pivot = arr[0]
 
 # 왼쪽 / 오른쪽
 i = 1
 j = len(arr) - 1
 
 # 크로스 전까지
 while(i < j):
     
     # 왼쪽에서는 피봇보다 큰 애들 찾아야 한다
     # 만약 피봇이 최대 숫자라면 index out of range 발생
     while(i < len(arr) and arr[i] < pivot):
         i += 1
     # while문을 빠져나오면 i는 피봇보다 큰 수를 가리킴
     
     # 오른쪽에서는 피봇보다 작은 수를 찾아야 함
     while(arr[j] > pivot):
         j -= 1
     # while문을 빠져나오면 j는 피봇보다 작은 수를 가리킴
     
     # 크로스가 발생하지 않았다면
     if(i < j):
         # swap
         arr[i], arr[j] = arr[j], arr[i]
         
 # 피봇을 정렬된 위치에 놓는다
 arr[0], arr[j] = arr[j], arr[0]

########## 예시문제 ##########

def partition(left, right):
    global mylist
    # 피봇(제일 처음 인덱스)을 기준으로
    pivot = mylist[left]

    i = left
    j = right

    # cross 전까지
    while(i < j):
        # 왼쪽에서 pivot보다 큰 수를 찾는다
        while(i <= right and mylist[i] <= pivot):
            i += 1
        # i를 찾음

        # 오른쪽에서 pivot보다 작은 수를 찾는다
        while(j >= left and mylist[j] > pivot):
            j -= 1
        # j를 찾음

        # i < j이면 스왑한다
        if(i < j):
            mylist[i], mylist[j] = mylist[j], mylist[i]

    # 전부 다 스왑했으면 피봇을 해당 인덱스로 옮기고 인덱스 리턴
    mylist[left], mylist[j] = mylist[j], mylist[left]
    return j

    

def quick_sort(left, right):

    # 현재 리스트가 2개 이상일 때
    if(left < right):
        # pivot 인덱스를 받는다
        pivot_idx = partition(left, right)
        # pivot 왼쪽 정렬
        quick_sort(left, pivot_idx-1)
        # picot 오른쪽 정렬
        quick_sort(pivot_idx+1, right)


T = int(input())

for t in range(1, T+1):

    # N개의 정수
    N = int(input())

    # 숫자 리스트
    mylist = list(map(int, input().split()))

    quick_sort(0, N-1)
    print(mylist)

    print(f'#{t} {mylist[N//2]}')
