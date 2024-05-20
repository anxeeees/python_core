# When a bank has financial problems the government can return a client's deposit if it is less than 700,000. The interest rate for a particular deposit is 7.1% a year. The percentages are paid to the same deposit at the end of the year
# and a new value of the interest is calculated.

value = int(input())
year = 0

while value < 700000:
    value += value * 0.071
    year += 1

print(year)