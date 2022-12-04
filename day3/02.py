''' Advent of Code 2022 : Day 3 Part 1'''
import string
import pyperclip


priority_list = string.ascii_lowercase + string.ascii_uppercase

# print(priority_list)
s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
data = s.split('\n')
# print(data)
data = open("day3/input.txt").read().splitlines()
answer = 0
total = 0


def common_string(l1, l2):
    common = ''
    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                common += i1
    return common


common = priority_list
len_data2 = len(data)
for i, l in enumerate(data):
    if i % 3 == 0:
        common = priority_list
    common = common_string(common, data[i])
    if i % 3 == 2:
        total += priority_list.index(common[0])+1
print(total)
# 2697

pyperclip.copy(total)