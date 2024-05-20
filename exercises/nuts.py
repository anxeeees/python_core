#Some squirrels found some nuts and decided to divide them equally.
# You will get the number of squirrels and the number of nuts as input on separate lines. Find out how many nuts will be left after each of the squirrels takes an equal number of nuts.
# Print the result.

sq = int(input())
nuts = int(input())
result = nuts % sq
print(result)
