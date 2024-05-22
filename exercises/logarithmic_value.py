import math
num1 = int(input())
num2 = int(input())

if num2 > 1:
    result = math.log(num1, num2)
    print(f"{math.log(num1, num2):.2f}")
else:
    result = math.log(num1)
    print(f"{math.log(num1):.2f}")


