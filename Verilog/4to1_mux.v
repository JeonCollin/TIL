/*--------------data flow---------------*/
module mux_4to1_dataflow (i0, i1, i2, i3, s0, s1, out);

input i0, i1, i2, i3, s0, s1;
output out;

// #을 이용해서 delay를 줄 수 있다.
assign #10 out = (s1 & s0) ? i3 :((s1 & ~s0) ? i2 : ((~s1 & s0) ? i1 : ((~s1 ? ~s0) ? i0 : 0)));

endmodule

/*--------------좀 더 업그레이드 된data flow---------------*/
module mux_4to1(i0, i1, i2, i3, s0, s1, out);

input i0, i1, i2, i3;
input s0, s1;

output out;

wire Y;
assign Y = {s0, s1};

assign out = (Y == 2'b00) ? i0:
             (Y == 2'b01) ? i1:
             (Y == 2'b10) ? i2:
             (Y == 2'b11) ? i3:
             1'b0 // default

endmodule


/*--------------behavioral---------------*/
module mux_4to1_behavioral (i0, i1, i2, i3, s0, s1, out);

input i0, i1, i2, i3, s0, s1;
output out;

always @(*) begin
    case ({s1, s0})
        2'b00: i0;
        2'b01: i1;
        2'b10: i2;
        2'b11: i3; 
        default: 1'b0
    endcase
end
    
endmodule
