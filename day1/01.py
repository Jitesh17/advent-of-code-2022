''' Advent of Code 2022 : Day 1 Part 1'''

data = open("day1/input.txt").read().splitlines()
answer = 0
total = 0
for d in data:
    if d is '':
        if answer < total:
            answer = total
        total = 0
    else:
        total += int(d)
print(answer)
