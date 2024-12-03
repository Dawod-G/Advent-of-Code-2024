import re

print("Day 3 - Exercise 1")

with open('input.txt', 'r') as file:
    memory = file.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
isGood = re.findall(pattern, memory)

result = 0

for match in isGood:
    num1, num2 = map(int, match)
    result = result + num1 * num2

print(result)