// mux가 input을 선택한다면
// demux는 input을 받을 output을 선택한다

module demux_4to1(in, s, out0, out1, out2, out3);

input [3:0] in;
input [1:0] s;

output [3:0] out0, out1, out2, out3;

always @(in, s) begin
    if(s == 2'b00) out0 = in; else out0 = 4'b0000; 
    if(s == 2'b01) out1 = in; else out1 = 4'b0000; 
    if(s == 2'b10) out2 = in; else out2 = 4'b0000; 
    if(s == 2'b11) out3 = in; else out3 = 4'b0000; 
    
end
    
endmodule