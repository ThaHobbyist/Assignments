`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    15:20:39 04/17/2022 
// Design Name: 
// Module Name:    PIPO 
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
module PIPO(clk, rst, pi, po);
input clk, rst;
input [3:0] pi;
output [3:0]po;
reg [3:0]po;

always @(posedge clk, posedge rst)
	begin
		if(rst == 1'b1)
			po<=4'b0000;
		else
			po<=pi;
	end

endmodule
