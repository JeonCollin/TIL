## 2차원 배열 접근
- 행 우선 순회
```C
for(int i = 0; i < N; i++)
{
    for(int j = 0; j <N; j++)
    {
        arr[i][j];
    }
}
```

- 열 우선 순회
```C
for(int j = 0; j < N; j++)
{
    for(int i = 0; i <N; i++)
    {
        arr[i][j];
    }
}
```

- 행에서 지그재그 순회
```C
for(int i = 0; i < N; i++)
{
    for(int j = 0; j <N; j++)
    {
        arr[i][j + (N-1 - 2*j)*(i%2)];
    }
}
```

- **델타를 이용한 2차 배열 탐색**
```C
arr[N][1]
dx[] = {0, 0, -1, 1} // + 상 하 좌 우
dy[] = {-1, 1, 0, 0}

for(int x = 0; x < N; x++)
{
    for(int y = 0; y < N; y++)

        for(int i = 1; i <= 3; i++)
        {
            testX = x + dx[mode];
            testY = y + dy[mode];
            arr[testX][testY];            
        }
}s
```

```C
arr[N][1]
dx[] = {-1, 1, -1, 1} // X 좌상 우상 좌하 우하
dy[] = {-1, -1, 1, 1}

for(int x = 0; x < N; x++)
{
    for(int y = 0; y < N; y++)

        for(int i = 1; i <= 3; i++)
        {
            testX = x + dx[mode];
            testY = y + dy[mode];
            arr[testX][testY];            
        }
}s
```
  - 배열 경계를 넘어가면 무시하는 로직
  ```C
  if(testX < 0 || testY < 0 || test X >= N || testY >= N)
    continue;
  ```
- 응용
  - 나이트 움직임 로직 >> 움직이는 거리를 변경
    ```C
    int dx[] = {-2, -1, +1, +2, +2, +1, -2, -1};
    int dy[] = {-1, -2, -2, -2, +1, +2, +1, +2}
    ```
  - 좌표 원하는 끝까지 탐색
  ```C
  for(int d = 1; d <= num; d++)
  {
      int testX = x + dx[mode]*d
      int testY = y + dy[mode]*d
  }
  ```

- 전치행렬
```C
int arr[3][3]

for(int j = 0; j < N; j++)
{
    for(int i = 0; i <N; i++)
    {
        swap(arr[i][j], ary[j][i]);
    }
}
```