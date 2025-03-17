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


########## 예시 문제 ##########
def partition(left, right):
    global arr
    
    # 해당 구간에서 가장 왼쪽에 있는 것이 기준
    pivot = arr[left]
    i = left
    j = right
    
    while(i < j):
        while(i < right and arr[i] <= pivot):
            i += 1
            
        while(arr[j] > pivot):
            j -= 1
            
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
            
    # 정렬된위치에 놓기
    arr[j], arr[left] = arr[left], arr[j]

def quick_sort(left, right):
    
    # 구간의 길이가 2 이상이라면
    if(left < right):
        # 가장 왼쪽을 pivot으로 삼고
        # pivot을 정렬된 위치에 놓고, pivot_idx를 반환
        pivot_idx = partition(left, right)
        
        quick_sort(left, pivot_idx-1)
        quick_sort(pivot_idx+1, right)
        
        
T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    arr = list(map(int, input().split()))
    
    quick_sort(0, N-1)
    
    print(arr)