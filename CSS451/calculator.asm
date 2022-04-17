.data 
	m1: .asciiz
	m2: .asciiz
	m3: .asciiz
	m4: .asciiz
	
.text
main: 
	#Menu
	li $v0, 4
	la $a0, ml
	syscall
	li $v0, 5
	syscall
	move $t0, $v0
	
	# Input 1
	li $v0, 4
	la $a0, m2
	syscall
	li $v0, 5
	syscall
	move $t2,$v0
	
	#Input 2
	li $v0,4
	la $a0,m3
	syscall
	li $v0,5
	syscall
	move $t3,$v0
	
