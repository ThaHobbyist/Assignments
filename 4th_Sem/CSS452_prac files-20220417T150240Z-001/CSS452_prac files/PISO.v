`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    15:25:11 04/17/2022 
// Design Name: 
// Module Name:    PISO 
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
module PISO(clk, rst, pi, so);
input clk, rst;
input [3:0]pi;
output so;
reg so;
reg [3:0]tmp;

always @(posedge clk, posedge rst)
	begin 
		if(rst==1'b1) begin
			so<=1'b0;
			tmp<=pi;
		end else begin
			so <= tmp[0];
			tmp <= tmp>>1'b1;
		end
	end

endmodule
