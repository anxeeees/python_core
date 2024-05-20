duration_days = int(input())
total_food = int(input())
flight = int(input())
night_cost = int(input())

print((duration_days * total_food) + (flight * 2) + (duration_days-1) * night_cost)