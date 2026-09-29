from functools import reduce
a = ["Geeks", "for", "Geeks"]
r = reduce(lambda x, y: x + " " + y, a)
print(r)