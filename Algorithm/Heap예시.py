def enqueue(item):
    # heap에 원소 삽입
    global last

    # heap의 끝에 item 저장
    last += 1
    heap[last] = item

    # 자식과 부모의 키값 비교를 위해
    c = last
    # 부모의 정점 번호 계산
    p = c//2

    # 부모가 있고, 부모 < 자식 (최대 힙 위반)
    while(p != 0 and heap[p] < heap[c]):
        heap[p], heap[c] = heap[c], heap[p]
        # 현재 부모를 자식으로 하고
        # 다시 그 위의 부모와 비교해야 함
        c = p
        p = c//2


def dequeue():
    # heap에 원소 삭제
    global last
    # 가장 큰(작은) 값 반환
    temp = heap[1]
    # 마지막 원소를 루트에 넣는다
    heap[1] = heap[last]
    # 원소들을 한 칸 당김
    last -= 1

    # 부모노드와 자식노드 비교 시작
    p = 1
    c = p*2

    # 자식이 하나라도 있는 경우
    while(c <= last):
        # 근데 오른쪽 자식이 있고, 오른쪽 자식이 더 크다면
        if(c+1 <= last and heap[c] < heap[c+1]):
            # 비교 대상을 오른쪽 자식으로 정한다
            c += 1
        # 자식이 더 크다면
        if(heap[p] < heap[c]):
            # 부모와 교환
            heap[p], heap[c] = heap[c], heap[p]
            # 자식을 새로운 부모로
            p = c
            # 그 아래 자식과 다시 비교
            c = p*2

            # 자식이 없다면 끝난다

    # 최대값 반환
    return temp


# 힙 생성
heap = [0]*100
last = 0

enqueue(2)
enqueue(5)
enqueue(7)
enqueue(3)
enqueue(4)
enqueue(6)
print(heap[:10])
'''
# 2 삽입
2

# 5 삽입
2
5

# 부모가 더 커서 바꾼다(2 <-> 5)
5
2

# 7 삽입
 5
2 7

# 부모가 더 커서 바꾼다(7 <-> 5)
 7
2 5

# 3 삽입
  7
 2 5
3

# 부모가 더 커서 바꾼다(3 <-> 2)
  7
 3 5
2

# 4 삽입
  7
 3 5
2 4

# 부모가 더 커서 바꾼다(3 <-> 4)
  7
 4 5
2 3

# 6 삽입
   7
 4   5
2 3 6

# 부모가 더 커서 바꾼다(5 <-> 6)
   7
 4   6
2 3 5
'''

print(dequeue())
'''
# 7을 빼냈다

 4   6
2 3 5

# 가장 마지막 원소를 루트에 넣는다
   5
 4   6
2 3

# 아래 자식과 비교한다
# 4는 괜찮은데 6이 부모보다 더 커서 바꿔야 한다
# 5 <-> 6
   6
 4   5
2 3
'''
print(heap[:10])