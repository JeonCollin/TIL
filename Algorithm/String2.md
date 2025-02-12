## 패턴매칭
### 고지식한 알고리즘
- 일일이 다 매칭해본다
- 시간복잡도: O(NM)
```c
int brute_matching(char in, char comp, int inlen, int complen)
{
    //기준 문자열 순회
    for(int i = 0; i < inlen; i++)
    {
        //문자열이 동일한지 확인하는 파라미터
        int success = 0;

        //비교 문자열을 순회
        for(int j = 0; j < complen; j++)
        {
            //둘이 다르면 끊고 처음부터 다시 비교한다
            //단, 비교하는 문자는 옆에서 다시 시작
            if(in[i+j] != comp[j])
                break;
            success++;
        }

        //break 없이 성공적으로 비교가 되었다면 리턴
        if(success == complen)
            return 0;
    }
}
```

### KMP 알고리즘
- 텍스트 비교를 진행했으니까 정보가 있을거임
- 아예 불일치한 부분은 스킵함
- 어느 정도 일치한 부분으로 이동하여 다시 비교
- 시간복잡도: O(M+N)
- 매칭이 실패했을 경우 돌아갈 곳을 계산한다
```py
'''
실패함수: 접두사와 접미사가 같은 최대 문자열 길이
 0 1 2 3 4 5 6 7 8 = j
 a b c d a b c e f 
-1 0 0 0 0 1 2 3 0 0 = 패턴 매칭에 실패했을 때 돌아갈 인덱스
처음 -1과 마지막 0: 처음에 실패했으면 한 칸 당기고
마지막에 찾았으면 그 다음에 또 찾아야겠지

예를 들어 e에서 실팼으면 3이니까 j = 3인 d를 현재 자리로 가져온다
'''

def kmp(t, p):
    N = len(t) #기준문자열
    M = len(p) #찾아야하는 문자열: a b c d a b c e f
    lps = [0] * (M+1)

    j = 0 # 일치한 개수 == 비교할 패턴 위치
    
    #첫 번째 칸은 -1 고정
    lps[0] = -1

    #
    for i in range(1, M):
        lps[i] = j #p[i] 이전에 일치한 개수

        #접두사/접미사가 같은 부분 만큼 증가시킨다
        if p[i] == p[j]:
            j += 1

        else:
            j = 0

    #마지막 칸은 j 고정
    lps[M] = j

    i = 0 #비교할 텍스트 위치
    j = 0 #비교할 패턴 위치

    while i < N and j <= M:
        if i == -1 or t[i] == p[j]:
            i += 1
            j += 1

        else:
            i = lps[j]

        if j == M:
            index = i-M
            j = lps[j]
```

### 보이어 무어 알고리즘
- 패턴의 끝 부분이 일치하는지 확인한다
- 일치하지 않으면 점프
- 점프를 위해 skip 배열 사용
- skip배열: (찾아야 하는 패턴 기준) length - index - 1
- 패턴에 없는 모든 문자: length
- 시간복잡도: 보통 O(n)보다 작다
