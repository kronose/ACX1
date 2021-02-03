from datetime import datetime as d
print("""
	WELLCOME TO	    fyedjlsfbm
     ============= KRONOSE ==============
     ============= CYPHER  ==============
   This is a simple incryption python program


	                    _                                
	     /\             | |                            
	    /  \   _ __   __| |_ __ ___                       
	   / /\ \ | '_ \ / _` | '__/ _ \                       
	  / ____ \| | | | (_| | | | (_) |                          
	 /_/    \_\_| |_|\__,_|_|  \___/                       
    """ )

def enription():

	try:
		ms=input ("write your message :")
		for i in ms:
			if not (ord(i) ==32 or i.isalpha()):
				raise ValueError				
			break
				
	except :
		print("enter only strings,space and writting sighns  ")
	while True:
		try:
			key=(input(int("enter you encryption key :")))
			
		except:
			print("enter only numeric figures")
			break

	result=
	for i in ms:
		if (ord [i]== 32):
			result +=i
		elif (i.isupper()):
			result +=chr((ord(i) + key - 65) % 26 + 65)
		else :
			result +=chr((ord(i) + key - 97) % 26 + 97)
	print(result)
'''		                        
print("""choose what you want to do
For encryption enter :1
For decryption enter :2
""")
f=input(int(>>>>))
if f == 1 :
'''
enription()
