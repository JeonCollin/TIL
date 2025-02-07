# 2차원 배열
## 입력받기
- 공백 없이 들어올 경우
```py
'''
3
123
456
789
'''
N = int(input())

mylist = [list(map(int, input())) for _ in range(N)]
```

- 공백 있게 들어올 경우
```py
'''
3
1 2 3
4 5 6
7 8 9
'''
N = int(input())

mylist = [list(map(int, input().split())) for _ in range(N)]
```

- 주의사항: 얕은 복사 문제
```py
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr = [[0]*4]*3 #이런 식으로 2차원을 생성하면

#의도한 바는 하나만 바꾸는 거지만
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
arr[2][1] = 1

'''
실제로는 얕은복사가 일어난다
[[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
'''
```

## 배열 순회
- 행 우선 순회(좌 >> 우)
```py
for row in range(N):
    for col in range(M):
        array[row][col]
```

- 열 우선순회(위 >> 아래)
```py
for col in range(M):
    for row in range(N):
        array[row][col]
```

- 지그재그 순회(좌 >> 우, 우 >> 좌 ...)
```py
for row in range(N):
    for col in range(M):
        array[row][col + (M - 1 - 2*col)*(i%2)]
```

- 델타: 방향벡터
```py
#북 북동 동 동남 남 남서 서 북서 현재위치
drow = [-1, -1, 0, 1, 1,  1,  0, -1, 0]
dcol = [ 0,  1, 1, 1, 0, -1, -1, -1, 0]

#응용하면 나이트의 움직임도 구현할 수 있다
drow = [-2, -1, 1, 2,  2,  1, -1, -2]
dcol = [ 1,  2, 2, 1, -1, -2, -2, -1]

#실제 사용
for row in range(N):
    for col in range(M):

        #방향벡터 적용, V는 벡터 인덱스
        for i in range(V)

            #num은 탐색해야하는 크기
            for mul in range(num)

                #행렬 범위를 벗어나지 않는지 확인
                if(0<= R < N and 0 <= C < M):
                    R = row + drow*mul
                    C = col + dcol*mul
                    array[R][C]
```

- 전치행렬(행과 열을 바꾸면 된다)
```py
for row in range(N):
    for col in range(row):
        temp = array[row][col]
        array[row][col] = array[col][row]
        array[col][row] = temp
```

# 부분집합
- 다른 배열을 만들어서 해당 인덱스의 원소를 포함시킬건지, 안시킬건지 결정한다
- 가장 단순한 방법
```py
#아래 배열에서 부분집합을 생성하려면
arr = [1, 2, 3]

#노가다 방법
bit = [0, 0, 0]
subset = []

#0 아니면 1이니까
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k

            #b번째 인덱스가 1이라면 해당 부분이 부분집합에 들어간다.
            for b in range(3):
                if bit[b] == 1:
                    subset += arr[b]
'''
[0, 0, 0] >> []
[0, 0, 1] >> [3]
...
[1, 1, 1] >> [1, 2, 3]
'''
```

- 비트연산을 이용한 방법
  - &: 비트단위로 AND
  - |: 비트단위로 OR
  - <<: shift == 곱하기 2
  - \>>: shift == 나누기 2
- 1 << n: 2의 n승
- i & (1 << j): i의 j번째 비트가 1인지 아닌지 검사
```py
arr = [3, 6, 7, 1, 5, 4]

#원소의 갯수
n = len(arr)

# 1 << n: 부분집합의 갯수
for i in range(1 << n):
#i = 1001011이라고 가정

    # 원소의 수 만큼 비교
    for j in range(n):

        # i의 j번 비트가 1인 경우
        if i & (1 << j):
        #i = 1001011
        #j = 0001000
        #위와 같은 경우에는 0,1,3,6 선택함
            #j 선택
            print(arr[j])
```