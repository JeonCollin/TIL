 1. list1-2
- bubble sort
1단계: 정렬하려는 구간을 정한다
2단계: 비교하는 인덱스를 정한다
3단계: 비교하고 바꾼다

시간복잡도: n^2

- 카운팅정렬
1단계: 0~k 범위에서 정수 각각의 개수를 세고 count 리스트에 기록한다
2단계: count list를 누적합 시킨다 >> 이게 정렬된 리스트의 인덱스가 됨
3단계: 누적합이 해당 정수의 인덱스가 되고, 하나씩 까면서 새로운 리스트 인덱스 자리에 넣음

시간복잡도: n+k


- 완전검색(순열): 모든 경우의 수를 다 살펴봄
1단계: (a, b, c, d, ...) 원하는 순서쌍의 순서대로 루프를 돌린다
2단계: 중복이 있다면 해당 루프에 조건을 걸어준다

- greedy 알고리즘
1단계: 부분집합의 최적해를 구함
2단계: 실행시켜본다
3단계: 다른 부분집합도 괜찮은지 점검

2. list2
- 행 순회
- 열 순회
- 지그재그 순회
1단계: 행 순회를 만든다
2단계: 번갈아가며 반대로 순회하게한다
>> 짝수때에는 뒤에서 시작하게

- 델타: 방향벡터 리스트
1단계: 이동하려는 좌표에 해당하는 x를 생각한다
2단계: 같은 단계에서 y좌표도 생각한다

- 부분집합(조합)
1단계: 원래 집합 크기만큼 for문을 돌린다
2단계: 비트로 생각하면 0,1이다
3단계: 0101 이면, 1인 부분만 선택하면 부분집합이 된다.

- 검색
- 순차검색
1단계: 그냥 다 검색한다

시간복잡도: n

- binary search
1단계: 기본파라미터(start, point, end)부터 시작
2단계: 지금 값보다 큰 경우와 작은 경우를 고려하여 파라미터 수정
>> 지금보다 크면 start, point를 옮겨야함
>> 지금보다 작다면 end, point를 옮겨야함
3단계: 찾았다면 끝

시간복잡도: log n
- hash: 1

- 선택정렬
1단계: 지금 리스트에서 최솟값을 찾는다
2단계: 앞의 값과 교환한다
3단계: 앞을 제외한 리스트에서 최솟값을 찾는다
4단계: 다시 앞의 값과 교환한다
5단계: 반복하다가 끝남