'''
def new(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(new(4,5,6))
'''
num_i=0
num4 = float(input("enter number one: "))
num5 = float(input("enter number two: "))
op_a = input("enter operator + or - or x or / ")

if op_a == "+":
    print(num4 + num5)
if op_a == "-":
    print(num4 - num5)
if op_a == "*":
    print(num4 * num5)
if op_a == "/":
    print(num4 / num5)