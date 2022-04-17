`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   16:21:00 04/17/2022
// Design Name:   ring_counter
// Module Name:   /home/thahobbist/CSS451_Prac/Ring_Counter_Test.v
// Project Name:  CSS451_Prac
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: ring_counter
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Ring_Counter_Test;
	// Inputs
	reg clk;
	reg rst;

	// Outputs
	wire [2:0] out;

	// Instantiate the Unit Under Test (UUT)
	ring_counter uut (
		.clk(clk), 
		.rst(rst), 
		.out(out)
	);
	always #10 clk = ~clk;
	
	initial begin
		// Initialize Inputs
		{clk, rst} <= 0;

		$monitor("T=%0t out=%b", $time, out);
		repeat(2) @(posedge clk);
		rst<=1;
		repeat(15) @(posedge clk);
		$stop;

	end
      
endmodule

