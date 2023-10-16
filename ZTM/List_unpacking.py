# List unpacking

basket = [1,2,3]

a,b,c = [1,2,3]

print(a)
print(b)
print(c)
print('-'*15)

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)
