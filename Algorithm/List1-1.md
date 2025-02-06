# 알고리즘
- 어떤 문제를 해결하기 위한 절차나 방법
- 슈도코드나 순서도로 표현

## 시간복잡도
- 실행되는 명령문의 개수 == 연산량
- 빅 오 표기법
- 가장 큰 영향력만 표기
- O(2n^2 + 3n + 4) >> O(n^2)

#### 참고
- 어차피 내장함수는 안쓸거다
- 상남자로 성장하기 위해 C로 연습하였다.

## 정렬

### Bubble sort
- 일일이 다 정렬하는거
- 시간복잡도: O(n^2)
- N = 5라면
  1. OOOOO (맨 뒤는 최대값이 됨)
  2. OOOO
  3. OOO
  4. OO
  5. O (완성)

```c
int BubbleSort(int array, int N)
{
    //오름차순으로 정렬

    int temp;

    for(int i = N-1; i >= 0; i--)
    {
        for(int j = 0; j < i; j++)
        {
            // 왼쪽 값이 더 크다면 바꾼다.
            if(array[j] > array[j+1])
            {
                //swap j <-> j+1
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }

    return array;
}
```

### Counting sort
- 정수나 정수로 표현할 수 있는 자료형에만 가능
- 가장 큰 정수를 알아야 사용 가능
- 시간복잡도: O(n + k)
```C
int CountingSort(int data, int k)
{
    //기본 파라미터 설정
    length = strlen(data);
    int count[k+1]; //0 ~ k까지이므로
    int temp[length];

    //1단계: array를 순회하며 각 정수의 개수를 세고
    // count 리스트에 넣는다
    for(int i = 0; i < length; i++)
    {
        count[data[i]] = count[data[i]] + 1;
    }

    //2단계: count 리스트를 누적합 시킨다
    for(int i = 1; i < k+1; i++)
    {
        count[i] = count[i] + count[i-1];
    }

    //3단계: data를 뒤에서부터 순회한다.
    // 해당 data[x] 의 값을 count에서 찾는다
    // 누적에서 뺀다
    // count[y]를 인덱스로 삼아서 결과에 넣는다
    for(int x = length-1; x >= 0; x--)
    {   
        count[data[x]] = count[data[x]] - 1
        temp[count[data[x]]] = data[x];
    }

    return temp;
}
```

### 완전검색
- 모든 경우의 수 생각
- 경우의 수가 적을 때 유용
- 보통 정답 알아내는 용도
- 시간복잡도: 최악의 경우 => O(n!)
```c
void Permutation(int data)
{
    //파라미터 설정
    length = strlen(data);

    //data = {2, 7, 7}
    //1단계: 만들어야 하는 순서쌍이 (i1, i2, i3)라면
    for(int i1 = 0; i1 < length; i++)
    {
        for(int i2 = 0; i2 < length; i++)
        {
            if(i2 != i1)
            {
                if (i3 != i1 && i3 != i2)
                {
                    for(int i3 = 0; i3 < length; i++)
                    {
                        print("%d %d %d",
                        data[i1],
                        data[i2],
                        data[i3]);
                    }
                }
            }
        }
    }
}
```

### Greedy 알고리즘
- 직관적인 방법
1. 최적이라고 생각 되는 것을 코드로 구현한다
2. 다른 테스트케이스에서도 적용되는지 확인한다

#### 참고
- 입력받은 수를 count 리스트에 나눠 넣기
```c
void splitNum(int num)
{
    int count[10] = {};

    while(1)
    {
        //1단계: 1의 자리부터 뽑아낸다
        //나머지계산하면 1의 자리부터 나온다
        count[num%10] = count[num%10] + 1;

        //num이 456789라면
        //index |  0 1 2 3 4 5 6 7 8 9
        //count = {0,0,0,0,1,1,1,1,1,1}로 됨

        //2단계: 1의자리를 제거하고 한 칸씩 땡겨온다
        num = (int) num/10;

        //3단계: 끝
        if(num == 0)
            break;
    }
}
```
