# Tuple
a = (1, 2, 3, 4, 5, 2, 9)
print(a)
print(type(a))

b = ()
c = (1,)

print(b)
print(type(b))
print(c)
print(type(c))

# methods of tuple
print(a.count(2))
print(a.index(2))
print(a * 2) #repeat the tuple twice
print( 2 in a)
print( 45 in a)
print(len(a))

# unpacking a tuple
r = (1, 2, 3)
m,n,o = r
print(m,n,o)