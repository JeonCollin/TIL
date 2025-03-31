// 4bit compartor
module four_bit_comparator(iagtb, iaeqb, ialtb, a, b, oagtb, oaeqb, oaltb);

input[3:0] a, b;
input iagtb, iaeqb, ialtb;

output oagtb, oaeqb, oaltb;

assign oagtb = (a > b)||((a == b)&&(iagtb == 1)); // 원래 a가 b보다 크거나, 같았다면 그 밑의 비트가 컸다
assign oaeqb = (a == b)&&(iaeqb == 1); // 현재, 아래 비트도 같아야 한다
assign oaltb = (a < b)||((a == b)&&(ialtb == 1)); // 원래 b가 a보다 크거나, 같았다면 그 밑의 비트가 컸다
    
endmodule

// 4bit를 연결해서 만든 12bit compartor
module compartor_12bit(iagtb, iaeqb, ialtb, a, b, oagtb, oaeqb, oaltb);

input[11:0] a, b;
input iagtb, iaeqb, ialtb;

output oagtb, oaeqb, oaltb;

// glue logic
// 각각의 eq, gt, lt 판단 비트를 wire로 연결해준다
wire ~~;

// gate modeling으로 연결
four_bit_comparator bit11_8(~~);
four_bit_comparator bit7_4(~~);
four_bit_comparator bit3_0(~~);
    
endmodule