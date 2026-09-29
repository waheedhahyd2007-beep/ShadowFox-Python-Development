def format_number(number, format_specifier):
    return format(number, format_specifier)

result = format_number(145, "o")

print("Formatted result:", result)
print("Representation used: Octal (Base 8)")
print("--------------------------------------------------")
pi = 3.14
radius = 84

area = pi * radius ** 2
water_per_square_meter = 1.4

total_water = area * water_per_square_meter

print("Pond area:", area, "square meters")
print("Total water:", int(total_water), "liters")
print("--------------------------------------------------")
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print("Distance:", distance, "meters")
print("Time:", time_seconds, "seconds")
print("Speed:", round(speed), "m/s")
