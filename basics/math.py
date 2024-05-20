print(((3 + 5) // 2 * 2 ** 3) % 7)
#(8) / 2 = 4
#4 * ( 2 * 2 *2) = 32
# 32 / 7 = 4, rest = 4

##Write a program that takes a single integer number n and then performs the following operations in the following order:
#adds n to itself

#multiplies the result by n

#subtracts n from the result

#exactly divides the result by n (that means, you need to carry out integer division).

n = int(input())
result = n + n
#print(result)
result2 = result *n
#print(result2)
result3 = result2 - n
#print(result3)
result4 = result3 // n
print(result4)
#print("The result is " + str(result4) + "")