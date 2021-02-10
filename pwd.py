
from sys import exit 
from getpass import getpass as g
 
def pwd():
	print("your pawd will be automatically encrypted and will not show on the screan ")	 
	p=g("enter your pwd :")

	r=g("retype :")
	h=1
	m=4
	s=3
	if p ==r:
		print(" You soccessfully updated your password")
		exit()
	while p != r and h < m:
		print("your first and retry pwd is not thesame !!!!")
		print("you are left with ",s,"tryal")
		s=s-1
		r=g("retry :")
		h+=1
		if p == r:
			print(" You soccessfully updated your password")
			exit()
			#break
			
		elif s==0 :
			print("You tried so many times account blocked !!! Thief !!!")
			import b_pwd
		
pwd()
