
def factorial(n): 
	
	if n == 0: 
		return 1
	return n * factorial(n-1) 

fac=int(input("Enter number : ")) 
result = factorial(fac)
print(f"Factorial of {fac} is {result}")

#factorial(fac)


