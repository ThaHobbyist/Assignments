.data
	m1: .asciiz "\nType of Input"
	m2: .asciiz "\n1. Cube"
	m3: .asciiz "\n2. Rectangular prism"
	m4: .asciiz "\nEnter Choice: "
	m5: .asciiz "\nEnter Value: "
	m6: .asciiz "\nEnter Length: "
	m7: .asciiz "\nEnter Width: "
	m8: .asciiz "\nEnter Height: "
	m9: .asciiz "\nVolume: "

.text
main: 
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 4
	la $a0, m3
	syscall
	
	li $v0, 4
	la $a0, m4
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	la $t3, 1
	la $t4, 2
	
	beq $t0, $t3, cube
	beq $t0, $t4, rec
	
cube:
	li $v0, 4
	la $a0, m5
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	mul $t1, $t0, $t0
	li $v0, 4
	la $a0, m9
	syscall
	
	li $v0, 1
	move $a0, $t1
	syscall
	
	li $v0, 10
	syscall
rec:
	li $v0, 4
	la $a0, m6
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	li $v0, 4
	la $a0, m7
	syscall
	
	li $v0, 5
	syscall
	move $t1, $v0
	
	li $v0, 4
	la $a0, m8
	syscall
	
	li $v0, 5
	syscall
	move $t2, $v0

	mul $t3, $t0, $t1
	mul $t3, $t3, $t2
	
	li $v0, 4
	la $a0, m9
	syscall
	
	li $v0, 1
	move $a0, $t3
	syscall
	
	li $v0, 10
	syscall