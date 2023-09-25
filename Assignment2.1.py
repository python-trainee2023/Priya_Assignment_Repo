# Q:2 Take input n and then display the factorial of that number

num = int(input("enter a number: "))
factorial = 1

if num < 0:
    print("The factorial doesn't exists for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1, num+1):
        factorial = factorial*i
        print("The Factorial of", num, "is", factorial)


