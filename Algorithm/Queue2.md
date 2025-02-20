# BFS(너비 우선 탐색)
- 인접한 정점들을 먼저 모두 차례대로 방문한다
- 선입선출 형태의 큐를 활용한다
```
 / - B-(E,F)
A - C
 \ - D-(G,H,I)

- 저런 식으로 연결되어 있다면 탐색 순서는
- Queue: 앞으로 방문할 장소를 저장
A >> BCD >> CDEF >> DEF >> EFGHI >> FGHI
>> GHI >> HI >> I
```
1. 초기상태: visitied, Queue 생성, 시작점 enqueue
2. 

```py
# queue를 생성해놓았다고 가정
def BFS(adj_arr, start):
    # 방문 리스트 생성
    # 숫자가 0부터 시작이라고 가정
    visited = [0]*(n)
    # 현재 위치 enqueue
    enqueue(start)
    # 시작점 방문 기록
    visited[start] == 1

    # 큐에 원소가 있는 동안
    while True:

        # 큐의 첫 번째 원소 반환(처음은 시작점)
        node = dequeue()

        # 방문한 곳인지 확인할 필요가 없음
        # 되돌아오는게 아니라 주변 탐색 후 방문하기 때문

        # 방문한 곳에 인접한 모든 곳을 enqueue
        for i in range(len(adj_arr[node])):
            # 방문하지 않은 곳이라면
            if(visited[adj_arr[node][i]] == 0):
                # queue에 저장
                enqueue(adj_arr[node][i])
                # n으로부터 1만큼 이동
                # 왜 그렇게 하나?
                # 방문 순서를 기록할려고
                visited[adj_arr[node][i]] = visited[node] + 1

        # 큐에 원소가 없다면 끝
        if(isEmpty() == True):
            return
```
- DFS와 BFS의 차이점
  - DFS
    - 노드가 지금 당장 연결된 쪽으로 움직인다
    - 직렬적으로 움직이게 됨

  - BFS
    - 지금 노드와 연결된 모든 노드를 살핀다
    - 병렬적으로 움직이게 됨
    - 최단거리 구할 때 유리
    - 출발점이 2개 이상인 경우에도 유리
