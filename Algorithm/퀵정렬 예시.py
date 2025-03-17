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
