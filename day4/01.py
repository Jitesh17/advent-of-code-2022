''' Advent of Code 2022 : Day 4 Part 1'''

s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
data = s.split('\n')
# print(data)
data = open("day4/input.txt").read().splitlines()
answer = 0
total = 0

for d in data:
    [[e11, e12], [e21, e22]] = [map(int, e.split('-')) for e in d.split(',')]

    if (e11 <= e21 and e12 >= e22) or (e11 >= e21 and e12 <= e22):
        total += 1
    # print(d, e11, e12, e21, e22, total)

print(total)
# 471
