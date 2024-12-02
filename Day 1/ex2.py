print("Day 1 - Exercise 2")

left_values = []
right_values = []

with open('input.txt', 'r') as input:
    for line in input:
        left, right = map(int, line.split())
        left_values.append(left)
        right_values.append(right)

similarity_score = []
total_similarity_score = 0

for i in range(len(left_values)):
    value = 0
    for j in range(len(right_values)):
        if left_values[i] == right_values[j]:
            value = value + 1
    similarity_score.append(value * left_values[i])

for i in range(len(similarity_score)):
    total_similarity_score = total_similarity_score + similarity_score[i]

print("Similarity_score:", total_similarity_score)