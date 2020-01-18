h = int(input())
a = int(input())
b = int(input())
day_minus_night = a - b
number_of_days = ((h - a) + day_minus_night - 1) // day_minus_night + 1
print(number_of_days)
