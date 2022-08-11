.data 
	m1: .asciiz "Enter a number: "
	m2: .asciiz "\nAscending Order: "
	m3: .asciiz "\nDescending Order: "
.text
main: 
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0

	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 5
	syscall
	move $t1, $v0

	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 5
	syscall
	move $t2, $v0
	
	blt $t0, $t1, p1
	j p2
	
p1:
	blt $t0, $t2, p11
	j p12
p2:
	blt $t1, $t2, p21
	j p22	
p21:
	blt $t0, $t2, p211
	j p212
p11:
	blt $t1, $t2, p111
	j p112
p111:
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 1
	la $a0, ($t0)
	syscall
	la $a0, ($t1)
	syscall
	la $a0, ($t2)
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 1
	la $a0, ($t2)
	syscall
	la $a0, ($t1)
	syscall
	la $a0, ($t0)
	syscall
	
	li $v0, 10
	syscall
p112:
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 1
	la $a0, ($t0)
	syscall
	la $a0, ($t2)
	syscall
	la $a0, ($t1)
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 1
	la $a0, ($t1)
	syscall
	la $a0, ($t2)
	syscall
	la $a0, ($t0)
	syscall
	
	li $v0, 10
	syscall
p12:
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 1
	la $a0, ($t2)
	syscall
	la $a0, ($t0)
	syscall
	la $a0, ($t1)
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 1
	la $a0, ($t1)
	syscall
	la $a0, ($t0)
	syscall
	la $a0, ($t2)
	syscall
	
	li $v0, 10
	syscall
p211:
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 1
	la $a0, ($t1)
	syscall
	la $a0, ($t0)
	syscall
	la $a0, ($t2)
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 1
	la $a0, ($t2)
	syscall
	la $a0, ($t0)
	syscall
	la $a0, ($t1)
	syscall
	
	li $v0, 10
	syscall
p212: 
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 1
	la $a0, ($t1)
	syscall
	la $a0, ($t2)
	syscall
	la $a0, ($t0)
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 1
	la $a0, ($t0)
	syscall
	la $a0, ($t2)
	syscall
	la $a0, ($t1)
	syscall
	
	li $v0, 10
	syscall
p22: 
	li $v0, 4
	la $a0, m1
	syscall
	
	li $v0, 1
	la $a0, ($t2)
	syscall
	la $a0, ($t1)
	syscall
	la $a0, ($t0)
	syscall
	
	li $v0, 4
	la $a0, m2
	syscall
	
	li $v0, 1
	la $a0, ($t0)
	syscall
	la $a0, ($t1)
	syscall
	la $a0, ($t2)
	syscall
	
	li $v0, 10
	syscall
exit:
