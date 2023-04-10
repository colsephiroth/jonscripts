#! /usr/bin/env python3
import itertools

people = ["burke", "cole", "craig", "evan", "jax", "zane", "reuben", "levi", "ryan", "martai"]

for e in itertools.combinations(people, 2):
    print(f"{e[0]}, {e[1]}")
