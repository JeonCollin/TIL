# 검색
## 정렬되어 있지 않은 경우
### 그냥 다 검색하는 법
- 시간복잡도 O(n)
```c
for(int i = 0; i < N; i++)
{   
    //모든 요소를 다 비교한다
    if(num == numbers[i])
    {
        index = i;
        break;
    }
}
```

## 정렬되어 있는 경우
### 단순 크기비교
- 시간복잡도: O(n)
``` c
for(int i = 0; i < N; i++)
{   
    //모든 요소를 다 비교한다
    //그 요소가 있다면 리턴
    if(num == numbers[i])
    {
        index = i;
        break;
    }

    //그 요소보다 작다면 다음 숫자를 비교
    else if(num > numbers[i])
        continue;
    
    //그 요소보다 크다면 없다는 뜻이므로 검색 끝
    // >> 정렬되어있으니까
    else
        break;
}
```

### Binary search
- 이진검색을 하기 위해서는 항상 **정렬**되어 있어야 함
- 시간복잡도: O(log n)
1. 시작점 = 0, 끝점 = N-1, 중앙 = (시작 + 끝)//2
2. 지금 값이 큰 경우: 시작점=현재위치, 끝점=그대로
3. 지금 값이 작은 경우: 시작점=그대로, 끝점=현재위치
```c
int binarySearch(int arr, int N, int num)
{
    //초기 파라미터 설정
    int start = 0;
    int end = N-1;

    while(start <= end)
    {
        //중간지점 초기화: 정수 나누기로
        middle = (int) (start + end)/2

        //찾으려는 수가 더 큰 경우
        if(num > arr[middle])
            //시작점을 오른쪽으로
            start = middle+1;

        //찾으려는 수가 더 작은 경우
        else if(num < arr[middle])
            //끝 점을 왼쪽으로
            end = middle-1;

        //수를 찾았다면 끝내기
        else
            return middle;
    }
    //검색 실패
    return -1;
}
```

#### 인덱스
- 

### 선택 정렬
- 가장 작은 원소부터 앞으로 보낸다(오름차순)
- 시간복잡도: O(n^2)
1. 리스트에서 min을 찾는다
2. 맨 앞과 교환한다
3. 맨 앞 제외하고 다시 시작
```c
void selectionSort(int *myarr)
{
    for(int i = 0; i < N; i++)
    {
        //최소값 초기화
        int min = *myarr[i];
        int index = i;

        //i ~ N에서 최소값을 찾는다
        for(int j = i; j < N; j++)
        {
            if(min >= *myarr[j])
            {
                min = *myarr[j];
                index = j;
            }
        }

        //i번째와 값을 교환한다
        temp = *myarr[i];
        *myarr[i] = *myarr[index];
        *myarr[index] = temp;

        //이제 그 다음 루프에서 확인한다
    }
}
```