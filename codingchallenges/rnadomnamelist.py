import random

# get a random element from this list
people = ["allen", "michael", "john", "ben"]



chosen = random.choice(people)

people.remove(chosen)

print(chosen)

print(people)
