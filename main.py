num = int(input("Enter an int: "))
digit_sum = 0
hold = num


while num > 0:
    rem = num % 10
    digit_sum = digit_sum + rem
    num = int(num/10)


print("sum of digit", hold, "is: ", digit_sum)