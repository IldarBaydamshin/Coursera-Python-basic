v = int(input())
t = int(input())
ring = 109
iterations = (v * t) // ring
position = v * t - ring * iterations
print(position)
