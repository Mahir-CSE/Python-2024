#Sets

#empty set
e = set()
print(type(e))

e.add(73)
print(e)

print(len(e))

s = {1, 3, 5, 7, 9, 15, 11, 16}

s.remove(11)
print(s)

s.pop()
print(s)

s.pop()
print(s)

s.pop()
print(s)

e.clear()
print(e)

a = {1, 3, 5, 7}
b = {2, 4, 6}

c = a.union(b)
print(c)

d = {2, 4, 6, 8}

e = b.intersection(d)
print(e)
