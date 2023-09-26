# take the input for the start and stop value for a range. Then get the sum of odd and even numbers
# within that range using function or lambda and display that.

from functools import reduce

num = input("Enter two starting and ending numbers")
start, end = num.split(",")
value = range(int(start), int(end))

even_list = list(filter(lambda x: x % 2 == 0, value))
odd_list = list(filter(lambda x: x % 2 != 0, value))

# even_list_sum = reduce(lambda a, b: a+b, even_list)
# odd_list_sum = reduce(lambda a, b: a+b, odd_list)


even_list_sum = 0
for item in even_list:
    even_list_sum += item

odd_list_sum = 0
for item in odd_list:
    odd_list_sum += item

print("The sum of even number in the list is: ", even_list_sum)
print("The sum of odd number in the list is: ", odd_list_sum)

# new_list = [1,2,3,4,5,6]
# first, second, *rest = new_list
# print(first, second, rest)


