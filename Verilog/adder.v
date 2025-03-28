module half_adder (x, y, s, c);
input x, y;
output s, c;

// gate level
xor xor1(s, x, y);
and and1(c, x, y);
    
endmodule


// half adder를 이용한 full adder
module full_adder (x, y, cin, s, cout);
input x, y, cin;
output s, cout;

wire s1, c1, c2;

half_adder ha1(x, y, s1, c1);
half_adder ha2(.x(cin), .y(s1), .s(s), .c(c2));
or(cout, c1, c2);
    
endmodule

// 그냥 full adder 자체를 설계
module full_adder2 (x, y, cin, s, cout);

input x, y, cin;
output s, cout;

wire s1, c1, c2, c3;

xor xor1(s1, x, y);
and and1(c1, x, y);
and and2(c2, x, cin);
and and3(c3, y, cin);

xor xor2(s, s1, cin);
or or1(cout, c1, c2, c3);
endmodule

// full adder를 이용한 4비트 에더
module four_bit_adder (x, y, cin, sum, cout);
input[3:0] x, y;
input cin;

output[3:0] sum;
output cout;

// glue logic: 4bit full_adder 사이에 cout을 대체해줌
wire c1, c2, c3;

full_adder fa1(.x(x[0]), .y(y[0]), .cin(cin), .s(s[0]), .cout(c1));
full_adder fa1(.x(x[1]), .y(y[1]), .cin(c1),  .s(s[1]), .cout(c2));
full_adder fa1(.x(x[2]), .y(y[2]), .cin(c2),  .s(s[2]), .cout(c3));
full_adder fa1(.x(x[3]), .y(y[3]), .cin(c3),  .s(s[3]), .cout(cout));
    
endmodule