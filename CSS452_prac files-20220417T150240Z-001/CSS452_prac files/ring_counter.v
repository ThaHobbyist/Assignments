`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    16:17:46 04/17/2022 
// Design Name: 
// Module Name:    ring_counter 
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
module ring_counter (input clk, rst, output [2:0]out);
reg [2:0]tmp;
always @(posedge clk, posedge rst) begin
	if(rst == 1'b1) begin
		tmp = 4'b0001;
	end
	else begin
		tmp = {tmp[1:0], tmp[2]};
	end
end
assign out = tmp;
endmodule
