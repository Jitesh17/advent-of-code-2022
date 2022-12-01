''' Advent of Code 2022 : Day 1 Part 2'''

data = open("day1/input.txt").read().splitlines()
total = 0
total_calories_list = []
for d in data:
    if d == '':
        total_calories_list.append(total)
        total = 0
    else:
        total += int(d)

answer = sum(sorted(total_calories_list)[-3:])

print(answer)
