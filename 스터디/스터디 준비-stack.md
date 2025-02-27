 3. stack
- 선형구조
- LIFO(후입선출)
- top: 현재 자료 맨 위
- push: 저장
- pop: 반환
- isEmpty: 스택이 공백인가
- peek: top에 있는 원소 반환
1단계: push
  - top증가
  - overflow 생각
  - 그게 아니면 top에 item 저장
2단계: pop
  - underflow 생각
  - 그게 아니면 top 감소
  - 그 후 item 반환

* 재귀호출
def f(i, N, v):
   if i == N:
      return 0
   elif arr[i] == v:
      return 1
   else:
      return f(i+1, N)

* memoization
- 그냥 재귀는 stack에 많이 쌓여서 계산이 느림
- 계산하자마자 값을 메모리에 저장
- 저장된 값을 재귀함수에 다시 돌려준다
1단계: memo를 위한 배열을 할당하고 초기화
2단계: memo의 가장 초기값 설정
3단계: 재귀호출 이후에 바로 값을 저장

* DP: 크기가 작은 부분문제 해결 후 크기가 큰 문제 해결
- 결과는 테이블에 저장해서 상위 문제를 해결할 수 있다

* DFS
- 한 방향으로 깊이 가다가 더이상 갈 곳이 없으면 그 전 갈림길로 되돌아 오며 결국 모든 정점을 방문 >> 후입 선출인 stack사용