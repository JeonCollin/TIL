## 문자의 표현
- ASCII 형식 >> 유니코드
- ord(): 웬만한 문자의 아스키코드를 다 알려줌

- big endian: 0000 0000 0011 0000 == 00으로 뒤에서 해석
- little endian: 0011 0000 0000 0000 == 30으로 앞에서 해석

## 문자열
### 문자열 처리
- java: hash, count, offset, value같은 것들도 메모리에 저장
- C에서 문자열 처리
```c
//문자열 == 문자들의 연결임
char arr[] = "abc"; == {"a", "b", "c", \n};
```
- java에서 문자열 처리: String 클래스 이용 - 필요한 메서드가 다 있다.
- python에서 문자열 처리: 시퀀스 자료형으로 분류됨, 불가변 객체

- C는 아스키코드로 저장한다. java는 유니코드(UTF16, 2byte)로 저장한다. 파이썬은 유니코드(UTF8)로 저장한다.

### 문자열 비교
- C: strcmp()
- java: equals()
- python: ==, is

### 문자열 <-> 정수
- C: atoi(), itoa()
- java: parse, toString()
- int(), str()
```py
#int() 만들기
def atoi(string):
    #결과 정수 초기화
    i = 0

    #string을 순회한다
    for x in s:
        #'0'으로부터 x의 상대적 위치 계산
        #그 다음 계산에서 10배로 늘려준다
        #1 >> 12 >> 123
        i = i*10 + ord(x) - ord('0')
    return i

#참고
#a가 16진수로 써져있는데 이걸 10진수로 표현
a = 'F'
int(a, 16) # 15
```

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
0 1 2 3 4 5 = j
a b a a b a
0 0 1 1 2 3 = F(j)

j에서 불일치가 발생했을 경우 인덱스를 F(j-1)로 문자열을 이동시킨다
'''
```