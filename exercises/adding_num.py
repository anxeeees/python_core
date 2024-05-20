# Carl asks you to count the sum of the first k natural numbers.
# Read k from the input, then add up numbers from 1 to k and print your answer.

counter = 0
k = int(input())

for i in range(1, k + 1):
    counter += i

print(counter)
