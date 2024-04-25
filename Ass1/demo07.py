# def factorial(n): 
	
# 	if n == 0: 
# 		return 1
	
# 	return n * factorial(n-1) 

# for i in range(1,11):
#     print(i)
# fac=int(input(f"Enter number {i}: ")) 
# result = factorial(fac)
# print(f"Factorial of {fac} is {result}")

for num in range(1,11):
    factorial=1 #stores the calculated value init value is 1.

    for i in range(1,num+1):
        #range(1,3+1)
        #range(1,4+1)
        #range(1,5+1) like this
        
        factorial = factorial*i

    print(f"Factorial of {num} is {factorial}")

# # Loop to calculate and print factorials for 1 to 10
# for num in range(1, 11):
#   factorial = 1  # Initialize factorial for each number
#   for i in range(1, num + 1):  # Iterate from 1 to the current number (inclusive)
#     factorial *= i  # Multiply factorial by each number in the sequence
#   print(f"Factorial of {num} is {factorial}")
