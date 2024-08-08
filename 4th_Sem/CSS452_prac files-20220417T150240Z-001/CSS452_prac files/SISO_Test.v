`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   15:41:24 04/17/2022
// Design Name:   SISO
// Module Name:   /home/thahobbist/CSS451_Prac/SISO_Test.v
// Project Name:  CSS451_Prac
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: SISO
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module SISO_Test;

	// Inputs
	reg clk;
	reg rst;
	reg si;

	// Outputs
	wire so;

	// Instantiate the Unit Under Test (UUT)
	SISO uut (
		.clk(clk), 
		.rst(rst), 
		.si(si), 
		.so(so)
	);
	initial
	clk = 1'b1;
	always #10 clk = ~clk;
	initial begin
		// Initialize Inputs
		si = 1'b0; rst = 1'b1;

		// Wait 100 ns for global reset to finish
		#100 rst = 1'b0;
		#100 si = 1'b1;
		#100 rst = 1'b1;
		#100 rst = 1'b0;
        
		// Add stimulus here

	end
      
endmodule

