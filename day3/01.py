''' Advent of Code 2022 : Day 3 Part 1'''
import string
priority_list = string.ascii_lowercase + string.ascii_uppercase

s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
data = s.split('\n')

data = open("day3/input.txt").read().splitlines()
answer = 0
total = 0


def common_string(l1, l2):
    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                return i1


for l in data:
    len_l = len(l)
    l1 = l[:len_l//2]
    l2 = l[len_l//2:]
    print(l1, l2)
    match = common_string(l1, l2)
    total += priority_list.index(match)+1


print(total)
