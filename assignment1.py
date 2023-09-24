input1 = input("Enter the list of multiple values separated by spaces: ")
input_list = input1.split(" ")

int_list=[]
string_list=[]
float_list=[]

for value in input_list:
    try:
        int_value = int(value)
        int_list.append(int_value)
    except ValueError:
        try:
            float_value = float(value)
            float_list.append(float_value)
        except ValueError:
            string_list.append(value)

print("Integer list is: ", int_list)
print("string list is: ", string_list)
print("Float list is: ", float_list)