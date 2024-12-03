import re

print("Day 3 - Exercise 1")

with open('input.txt', 'r') as file:
    memory = file.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
isGood = re.findall(pattern, memory)

result = 0

for match in isGood:
    X, Y = map(int, match)
    result = result + X * Y

print(result)