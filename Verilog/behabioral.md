## Initial block
- 처음 한 번만 실행
- 같은 initial block에선 누적됨
```v
initial begin
#5 a = 1'b1; // 5초 후
#10 b = 1'b0; // 실제로는 30초 후
end

// 다른 block
initial begin
#7 a = 1'b0; // 7초 후
#13 b = 1'b1 // 20초 후
end
```

## Always block
- 끝나기 전까지 반복하는 루프
- 응용하면 클락신호 생성 가능
```v
reg clk;

initial clk = 1'b0;
always #5 clk = ~ clk; // 주기가 10ns
```
- initial과 always는 서로 다른 block에 있어야 한다

## Assignment types
- Procedural: 반드시 reg 사용, always나 initial
- Continuous: 반드시 wire 사용, assign

### Blocking assignment
- = 사용
- 차례대로 업데이트
```v
reg x, y, z;

initial begin
x = #5 1'b0; // 5ns에 0됨
y = #3 1'b0; // 8ns에 0됨
z = #6 1'b0; // 14ns에 0됨
end
```

### Nonblocking assignments
- <= 사용
- 동시에 업데이트
- **Flip Flop 구현에 사용**
```v
reg x, y, z;

initial begin
x = #5 1'b0; // 5ns에 0됨
y = #3 1'b0; // 3ns에 0됨
z = #6 1'b0; // 6ns에 0됨
end
```

#### 회로에서 초기화
- flip flop을 사용한 초기화
```v
// 전형적인 형태
always @(posedge clk or negedge reset) begin

//초기화
if(reset == 0) begin

end
    
// 데이터 부여
else begin
q[0] <= din;
...
q[3] <= q[2];
end
end
```
**Filp Flop 하나 당 always문 하나 작성할 것**
**하나의 출력은 하나의 always에서 할 것**

## selection construct
- **부족한 조건문은 latch를 만들어낸다**
  - input에 해당하는 값이 없으면 이전 상태를 유지하기 위해 latch가 생성된다
- 모든 케이스를 적어줘야 한다. Default까지
```v
if(a >= b)
a = b // 이대로 끝내면 latch 생성

// else를 넣어줘야 wire로 합성된다
else:
b = a
```

### Case문
- 예시를 바로 보자
```v
always @(i0, i1, i2, i3, s) begin
// select의 경우에 따라 다르다
case(s) // sensitivity 리스트
2'b00: out = i0;
2'b01: out = i1;
2'b10: out = i2;
2'b11: out = i3;
default out = 1'b0
end
```

## Loop
- while(condition) begin ~~ end
- for(i = 0; i < N; i++) begin ~~ end
- repeat(몇 번) begin ~~ end
- forever begin ~~$finish end: finish만나면 끝난다