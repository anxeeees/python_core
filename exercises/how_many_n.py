# Write a program that reads numbers until 55

number = 0
sum = 0
counter = -1

while number != 55:
    number = int(input())
    counter += 1
    sum += number
print(counter)
print(sum)
print(sum/counter)
