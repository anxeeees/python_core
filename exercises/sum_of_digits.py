# make a program to sum from number 476 to 4 + 7 + 6

number = int(input("Enter a number: "))
first_digit = number % 10  # 6
second_digit = number // 10 % 10 # 7
third_digit = number // 100 % 10
print(first_digit + second_digit + third_digit)
