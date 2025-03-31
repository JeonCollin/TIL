module encoder_4to2(in, en, y);

input[3:0] in;
input en;

output reg[1:0] y;

always @(in, en) begin
    // case문 사용
    if(en == 1):
        y = 2'b11;

    else:
        case (in)
        4'b0001: y = 2'b00;
        4'b0010: y = 2'b01;
        4'b0100: y = 2'b10;
        4'b1000: y = 2'b11;
            default: y = 2'b11;
        endcase

    // 혹은 if/else문 사용
    if(en == 1):
        y = 2'b11;

    else:
        if(x == 4'b0001) y = 2'b00; else
        if(x == 4'b0010) y = 2'b01; else
        if(x == 4'b0100) y = 2'b10; else
        if(x == 4'b1000) y = 2'b11; else
            y = 2'b11;

    // 혹은 우선순위사용
    if(en == 1):
        y = 2'b11;

    else:
        case (in)
        4'b1xxx: y = 2'b11;
        4'b01xx: y = 2'b10;
        4'b001x: y = 2'b01;
        4'b0001: y = 2'b00;
            default: y = 2'b11;
        endcase

        // 위 코드랑 같다
        for(i = m-1; i >= 0; i--) begin
            if(in[i] == 1)
                y = i;
        end
end
    
endmodule