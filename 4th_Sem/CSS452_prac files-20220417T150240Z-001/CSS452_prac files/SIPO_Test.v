`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   15:44:09 04/17/2022
// Design Name:   SIPO
// Module Name:   /home/thahobbist/CSS451_Prac/SIPO_Test.v
// Project Name:  CSS451_Prac
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: SIPO
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module SIPO_Test;

	// Inputs
	reg si;
	reg clk;
	reg rst;

	// Outputs
	wire [3:0] PO;

	// Instantiate the Unit Under Test (UUT)
	SIPO uut (
		.si(si), 
		.clk(clk), 
		.rst(rst), 
		.PO(PO)
	);
	initial
	clk = 1'b0;
	always #10 clk = ~clk;
	initial begin
		// Initialize Inputs
		rst = 1'b1; si = 1'b1;

		// Wait 100 ns for global reset to finish
		#500 rst=1'b0;
		#100 si=1'b0;
		#100 si=1'b1;
        
		// Add stimulus here

	end
      
endmodule

