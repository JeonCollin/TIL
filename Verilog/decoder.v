/*-----------always를 사용한 신박한 구조------------*/
module decoder_strange(din, dout);

// 4 to 1 decoder
input[1:0] din;
output reg[3:0] dout;
    
always @(din) begin
    // din에 따라 1을 shift 시킴
    // 0001 0010 0100 1000
    dout = {{3{1'b0}}, 1'b1} << din;
end
endmodule

/*-----------always를 사용한 일반적인 구조------------*/
module decoder(in, en, out);
// 2 to 4 decoder
// output은 4bit
input[1:0] x;
input en;

output reg[3:0] out;

always @(x or en) begin
    // 초기화: en = high
    if(enable == 1'b1)
        y = 4'b1111;
    
    // low active
    else begin
        case (x)
        2'b00: y = 4'b0001;
        2'b01: y = 4'b0010; 
        2'b10: y = 4'b0100; 
        2'b11: y = 4'b1000; 
            default: y = 4'b1111;
        endcase
    end
end
endmodule