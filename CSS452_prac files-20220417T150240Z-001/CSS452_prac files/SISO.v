`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:43:35 04/17/2022 
// Design Name: 
// Module Name:    SISO 
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
module SISO(clk, rst, si, so);
input si;
input clk, rst;
output so;
reg so;
always @(posedge clk, posedge rst)
	begin
		if(rst==1'b1)
			so<=1'b0;
		else
			so <= si;
	end
	
endmodule