import math
angle_in_deg = int(input())
angle_radians = math.radians(angle_in_deg)
result = 1/math.tan(angle_radians)
print(f"{result:.10f}")
