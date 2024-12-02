print("Day 1 - Exercise 1")

left_values = []
right_values = []

with open('input.txt', 'r') as input:
    for line in input:
        left, right = map(int, line.split())
        left_values.append(left)
        right_values.append(right)

left_values.sort()
right_values.sort()

distance = []
total_distance = 0

for i in range(len(left_values)):
    distance.append(abs(left_values[i] - right_values[i]))

for i in range(len(distance)):
    total_distance = total_distance + distance[i]

print("Total distance:", total_distance)