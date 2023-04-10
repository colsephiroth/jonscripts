#! /usr/bin/env python3
import math
import random
import datetime as dt

# check to see if they went in the last 4 weeks
def too_soon(rotation, person, distance):
    toosoon = False

    for r in rotation[-distance:]:
        if person == r[1] or person == r[2]:
            toosoon = True

    return toosoon

# figure out if they are available for the week we are trying to match for
def not_available(gone, date, person):
    notavailable = False

    for e in gone:
        if date == e[0] and person == e[1]:
            notavailable = True

    return notavailable

def get_predetermined(predetermined, date):
    for e in predetermined:
        if e[0] == date:
            return e[1]

def is_retreat(retreats, date):
    return date in retreats

cole = "Cole"
evan = "Evan"
craig = "Craig"
jax = "Jax"
zane = "Zane"
burke = "Burke"
reuben = "Reuben"
levi = "Levi"
ryan = "Ryan"
alan = "Alan"
drew = "Drew"
martai = "MarTai"

rpeople = [ cole, evan, craig, jax, zane, burke, reuben, levi, ryan, martai ]

# weeks
distance = 3

# people that aren't allowed to serve together
restricted = {
        zane: { cole },
        reuben: { craig, burke, ryan },
        levi: { evan },
        ryan: { zane, drew },
        evan: { alan },
        craig: { martai },
        }

for k, v in restricted.copy().items():
    for p in v:
        if p not in restricted:
            restricted[p] = set()
        restricted[p].add(k)

# last four serving pairs
rotation = [
        (dt.datetime(2022, 7, 8), zane, evan),
        (dt.datetime(2022, 7, 15), "", ""),
        (dt.datetime(2022, 7, 22), alan, cole),
        (dt.datetime(2022, 7, 29), craig, burke),
        ]

# people that are unavailable on certain dates go here
gone = [
        ]

# people that have to serve on certain dates go here
predetermined = [
        ]

# whole homechurch/cell retreats
retreats = [
        (dt.datetime(2022, 5, 13)),
        (dt.datetime(2022, 5, 20))
        ]

iterations = int(input("iterations: "))
people = rpeople.copy()
random.shuffle(people)
leftovers = []

for i in range(iterations):
    print(f"starting iteration {i+1}")

    while len(people) != 0:
        date = rotation[-1][0] + dt.timedelta(days=7)

        if is_retreat(retreats, date):
            rotation.append((date, "", ""))
            continue


        p1 = get_predetermined(predetermined, date)

        if p1 is None:
            p1 = people.pop()
        else:
            rotation = [p for p in rotation if p is not p1]

        p2 = None

        print(f"trying to match {p1}")

        if not_available(gone, date, p1):
            print(f"{p1} is not available on {date.strftime('%Y-%m-%d')}")
            continue

        if too_soon(rotation, p1, distance):
            print(f"{p1} served too recently")
            people.insert(0, p1)
            continue

        for p in people:
            allowed = True

            # make sure they aren't matched with a restricted person
            if p1 in restricted:
                for b in restricted[p1]:
                    if p == b:
                        print(f"{p1} can't be matched with {p}")
                        allowed = False
                        break

            for r in reversed(rotation):
                if (p1 == r[1] and p == r[2]) or (p1 == r[2] and p == [1]):
                    print(f"{p1} and {p} served together last")
                    allowed = False
                    break

            if not_available(gone, date, p):
                print(f"{p} is not available on {date.strftime('%Y-%m-%d')}")
                people.remove(p)
                continue

            if too_soon(rotation, p, distance):
                print(f"{p} served too recently")
                allowed = False

            if allowed:
                p2 = p
                people.remove(p)
                break

        if p2 is not None:
            print(f"matched {p1} with {p2} for {date.strftime('%Y-%m-%d')}")
            rotation.append((date, p1, p2))
        else:
            print(f"{p1} has no suitable matches")
            leftovers.append(p1)

    people = rpeople.copy()
    for p in leftovers:
        people.remove(p)
    people.extend(leftovers)
    leftovers = []

print("")
for r in rotation[::-1]:
    print(r[0].strftime("%Y-%m-%d") + f", {r[1]}/{r[2]}")
