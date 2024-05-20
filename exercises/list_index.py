# Read input list of integers
nums = list(map(int, input().split()))

# Read the index
index = int(input())

# Print the integer at the specified index

if index > len(nums):
    print("Index out of range")
else:
    print(nums[index])
# Start your code below