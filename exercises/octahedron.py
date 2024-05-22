import math
edge_length = int(input())

area = 2 * math.sqrt(3) * edge_length ** 2

volume = (math.sqrt(2) / 3) * edge_length ** 3

print(f"{area:.2f} {volume:.2f}")