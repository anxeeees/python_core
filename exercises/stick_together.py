#You are given a list of numbers. Print them out together.
numbers = [int(x) for x in input().split()]
# print all numbers without spaces
print(*numbers, sep="")