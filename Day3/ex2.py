import re

print("Day 3 - Exercise 2")

with open('input.txt', 'r') as file:
    memory = file.read()

pattern = r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
isGood = re.findall(pattern, memory)

do = False
result = 0

for match in isGood:
    instruction = match[0]
    if instruction == 'do()':
        do = True
    elif instruction == 'don\'t()':
        do = False
    elif do and instruction.startswith('mul'):
        X, Y = map(int, match[1:])
        result = result + X * Y

print(result)