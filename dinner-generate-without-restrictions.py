#! /usr/bin/env python3
import random

l1 = [ "burke", "cole", "craig", "evan", "jax", "zane", "reuben", "levi", "ryan", "martai" ]
l2 = [ "burke", "cole", "craig", "evan", "jax", "zane", "reuben", "levi", "ryan", "martai" ]

rotation = []

length = len(l1)

# exhuastively iterate over every combination, there's almost certainly a better way
for i in range(length):
    for n in range(length):

        # makes sure it doesn't pair the person with themselves
        if l1[n] != l2[n]:

            # puts the names in the pair in alphabetical order ('<' and '>' compares strings by ascii code)
            # which is necessary for easy deduplication since the nested loop makes hella duplicate pairs
            if l1[n] < l2[n]:
                rotation.append((l1[n], l2[n]))
            else:
                rotation.append((l2[n], l1[n]))

    # rotates the list so that it doesn't just keep creating the same pairs
    # first iteration: [ 1, 2, 3 ] -> [ 3, 1, 2 ]
    # second iteration: [ 3, 1, 2 ] -> [ 2, 3, 1 ]
    l2 = l2[1:] + l2[:1]

# deduplicate pairs by converting the list to a set (sets by definition can't contain duplicate values)
rotation = set(rotation)

# loop through rotation and print out pairs via nice f-string syntax
for e in rotation:
    print(f"{e[0]}, {e[1]}")
