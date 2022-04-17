`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   15:29:45 04/17/2022
// Design Name:   PISO
// Module Name:   /home/thahobbist/CSS451_Prac/PISO_Test.v
// Project Name:  CSS451_Prac
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: PISO
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module PISO_Test;

	// Inputs
	reg clk;
	reg rst;
	reg [3:0] pi;

	// Outputs
	wire so;

	// Instantiate the Unit Under Test (UUT)
	PISO uut (
		.clk(clk), 
		.rst(rst), 
		.pi(pi), 
		.so(so)
	);
	
	initial
	clk = 1'b1;
	always #10 clk = ~clk;
	initial begin
		// Initialize Inputs
		rst=1'b1; pi=4'b1101;
		#300 rst=1'b0;
		#200 rst=1'b1;
		#200 rst=1'b0;

		// Wait 100 ns for global reset to finish
        
		// Add stimulus here

	end
   
endmodule

