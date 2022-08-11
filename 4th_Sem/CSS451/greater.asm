.data
	m1: .asciiz "Enter a number: "
	m2: .asciiz "\nGreatest Number: "
	m3: .asciiz "\nLeast Number: "
	arr: .space 20
.text

main:
	la $t6, 999999
	la $t7, 0
	
	la $t5, 0
	la $t4, 1
while:			 
	beq $t0,20,exit
	
	li $v0,4	
	la $a0,m1
	syscall
	
	li $v0,5	
	syscall
	move $t1, $v0
	
	slt $t3, $t6, $t1
	beq $t3, $t5, gr
	
	slt $t3, $t7, $t1
	beq $t3, $t4, sm
	
gr:
	move $t6, $t1
	j end

sm:
	move $t7, $t1
	j end
	
end: 
	addi $t0, $t0,4 			
	j while		

exit:

li $v0, 4
la $a0, m3
syscall

li $v0, 1
la $a0, ($t6)
syscall

li $v0, 4
la $a0, m2
syscall

li $v0, 1
la $a0, ($t7)
syscall

li $v0,10
syscall
