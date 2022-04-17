`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   15:59:21 04/17/2022
// Design Name:   Adder
// Module Name:   /home/thahobbist/CSS451_Prac/Adder_Test.v
// Project Name:  CSS451_Prac
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Adder
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Adder_Test;

	// Inputs
	reg [3:0] s1;
	reg [3:0] s2;
	reg c;

	// Outputs
	wire [3:0] sum;
	wire carry;

	// Instantiate the Unit Under Test (UUT)
	Adder uut (
		.s1(s1), 
		.s2(s2), 
		.c(c), 
		.sum(sum), 
		.carry(carry)
	);

	initial begin
		// Initialize Inputs
		s1 = 0;
		s2 = 0;
		c = 0;

		// Wait 100 ns for global reset to finish
		#100 s1=1; s2=3; c=0;
		#100 s1=3; s2=2; c=1;
        
		// Add stimulus here

	end
	initial 
	#400 $stop;
endmodule

