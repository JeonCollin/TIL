# Data flow modeling
## Delay 부여
- '#'을 사용해서 딜레이를 줄 수 있다

```verilog
wire in1, in2, out;
assign #10 out = in1 & in2;

wire #10 out;
assign out = in1 & in2;
```

## Operand
### constant
- integer: 4'sb1001 (4비트, signed, 이진수, 1001)
- real: decimal(1.5), scientific(15E12) 
- stirng: ASCILL code

###  variable
- reg[0:7] : msb=0, lsb=7
- reg[7:0] : msb=7, lsb=0
- 데이터 저장 용도
- vector, bit extension

```verilog
input[3:0] a
input[2:0] b

assign c = a[3:2] // a의 3,2 비트를 부여 >> 2bit
assign d = {a[2:1], b[1:0]} // a의 2,1 과 b의 1,0을 부여 >> 4bit
```

- dimension을 적용할 수 있다
```verilog
wire[7:0] x[3:0]; // x의 비트가 4개인데, 각각의 비트는 8비트임
// (8bit) (8bit) (8bit) (8bit)

reg[31:0] y[15:0]
// (32bit) (32bit) ... 총 16개

reg[7:0] z[3:0][3:0] // 2차원 array의 각각의 칸이 8bit
/*
(8bit) (8bit) (8bit) (8bit)
(8bit) (8bit) (8bit) (8bit)
(8bit) (8bit) (8bit) (8bit)
(8bit) (8bit) (8bit) (8bit)
*/
z[3][1][1:0] // row,col과 같다
```

## Operators
### bitwise 연산
- 각 비트마다 대응시켜서 연산
- ~: not >> ~ 4'b1010 >> 4'b0101
- &: and 
- |: or
- ^: xor

### Arithmetic 연산
- +: 더하기
- -: 빼기
- *: 곱하기
- /: 나누기
- **: 지수
- %: 나머지

### Concatenation, Replication
- {,}: 결합
- {정수{}} >> nest할 때는 이 형태로({{4{1'b1}}}) 써야 에러가 안난다
- 예시: {1'b1, {4{1'b0}}, 2'b10} >> 7'b1000010

### Reduction operators
- 제일 왼쪽에 적는다
- 오른쪽에서 왼쪽으로 해당 연산을 진행한다
- (~)&: and 혹은 nand, (~)|: or 혹은 nor, (~)^: xor 혹은 xnor
```verilog
x = 4'b1010
& x // 1 & 0 & 1 & 0 == 0
| x // 1 | 0 | 1 | 0 == 1
^ x // 1 ^ 0 ^ 1 ^ 0 == 0

// xor은 parity bit 활용으로 사용할 수 있다.
input[8:0] = x

assign one = |x // 하나라도 1이 있는 지 확인
assign zero = &x // 하나라도 0이 있는 지 확인
assign op = ^x // 1의 개수가 홀수면 1
```

### Logical operators
- !: not인데 bool의 not >> ~는 반전시키는 not
- &&: and인데 bool의 and
- ||: or인데 bool의 or
- **0이면 False이고 그 외 나머지 모두는 True임**

### Realational operators
- 부등식, 관계식
- <=, >=, >, <
- ==, !=: 비트에 x나 z가 있으면 x를 리턴(return 0, 1, x)
- ===, !==: 비트에 x나 z가 있는데, 둘 다 동일한 생김새인지 확인(return 0, 1)
```v
X = 4'b1010
Y = 4'b1101
Z = 4'b1xxz
M = 4'b1xxz

X == Y // True
X == Z // False
M == Z // x (생김새는 같지만 비트가 뭔지를 모름)
M === Z // True (생김새가 똑같아서)
```

### Shift operators
- logical shift: 그냥 shift. 곱하기2 또는 나누기 2
  - <<: 뒷자리는 0으로 채운다
  - ,>>: 앞자리는 0으로 채운다(MSB == 0)

- arithmetic shift: 부호에 따라 다른 shift
  - <<<: 뒷자리는 0으로 채운다
  - ,>>>: 앞자리는 부호로 채운다(MSB == 1, 0)

### Conditional operators
- assign문에서 사용
- assign out = selection(조건문) ? in1(참이면) : in2(거짓이면);