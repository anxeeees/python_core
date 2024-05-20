
b_price = 202
t_price = 118
ic_price = 2250
mc_price = 1680
d_price = 1075
p_price = 80

income = b_price + t_price + ic_price + mc_price + d_price + p_price

print("Earned amount:")
print("Bubblegum: $" + str(b_price))
print("Toffee: $" + str(t_price))
print("Ice cream: $" + str(ic_price))
print("Milk chocolate: $"+str(mc_price))
print("Doughnut: $" + str(d_price))
print("Pancake: $" + str(p_price))

print("Income: $" + str(float(income)))

print("Staff expenses:")
staff_expenses = input()

print("Other expenses:")
other_expenses = input()

print("Net income: $" + str(int(income) - int(other_expenses) - int(staff_expenses)))