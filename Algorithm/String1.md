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