def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3 :
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3

num1 = 1
num2 = 3
num3 = -1
max_num = find_max_number(num1, num2, num3)
print("The maximum number is:", max_num)
