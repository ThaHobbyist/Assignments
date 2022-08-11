`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:49:52 04/17/2022 
// Design Name: 
// Module Name:    SIPO 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module SIPO(input si, clk, rst, output [3:0]PO);
reg [3:0] tmp;

always @(posedge clk, posedge rst)
	begin
		if(rst == 1'b1) begin
			tmp<=4'b0000;
		end else begin 
			tmp<=tmp<<1'b1;
			tmp[0]<=si;
		end
	end
assign PO = tmp;
endmodule
