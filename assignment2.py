# Q:1  Fibonacci: A program that takes an input of how many terms to be displayed for the
# fibonacci sequence and then displays the total fibonacci sequence upto the number of terms specified.


nterms = int(input("Enter the number of terms for Fibonacci sequence: "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibancci sequence upto", nterms, "is :")
    print(n1)
else:
    print("Fibanacci sequence is: ")
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1


