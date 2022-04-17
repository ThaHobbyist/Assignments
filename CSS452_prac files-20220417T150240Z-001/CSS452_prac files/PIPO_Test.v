`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   15:36:35 04/17/2022
// Design Name:   PIPO
// Module Name:   /home/thahobbist/CSS451_Prac/PIPO_Test.v
// Project Name:  CSS451_Prac
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: PIPO
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module PIPO_Test;

	// Inputs
	reg clk;
	reg rst;
	reg [3:0] pi;

	// Outputs
	wire [3:0] po;

	// Instantiate the Unit Under Test (UUT)
	PIPO uut (
		.clk(clk), 
		.rst(rst), 
		.pi(pi), 
		.po(po)
	);
	initial
	clk=1'b1;
	always #10 clk = ~clk;
	initial begin
		// Initialize Inputs
		pi=4'b1101; rst=1'b1;

		// Wait 100 ns for global reset to finish
		#100 rst=1'b0;
		#100 pi=4'b1000;
		#100 rst=1'b1;
		#100 rst=1'b0;
        
		// Add stimulus here

	end
      
endmodule

