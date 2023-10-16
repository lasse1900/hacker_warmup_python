# Accessing characters in a string

a = "1abc2abc3abc4abc"
print(a.replace('abc','ABC'))

print(a.replace('abc','ABC',1))

# Sub-Strings

sub = a[1]

print('-'*15)
print(sub)

# Start index is inclusive, end index is exclusive
sub = a[0:3]
print(sub)

sub = a[0:6:2]
print(sub)
