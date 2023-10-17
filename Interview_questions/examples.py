
# https://www.youtube.com/watch?v=j5pBNieB1rs
# 4

string = "GHI"
for char in string:
    print(char, end ="")


print('\n----------------')

for i in range(len(string)):
    print(string[i], end="")

print('\n')
print('-'*15, ' Ex 5')
# 5 write a function that takes two strings and returns True if they are reverses of each other


def reverses(a,b):
    if(a == b[::-1]):
        return True
    return False

print(reverses("ABC","CBA"))


def reverses_2(string_1,string_2):
    # print(len(string_2),'\n')
    for i in range(len(string_1)):
        i_2 = len(string_2)-i-1
        # print(i_2)
        if string_1[i] != string_2[i_2]:
            return False
    return True

print(reverses_2("ABCD","DCBA"))
print('-'*15, ' Ex 6')

# 6 int1 = 1232 > int2 = 201

def larger_than(number_1, number_2):
    if len(number_1) > len(number_2):
        return True
    elif len(number_1) < len(number_2):
        return False
    for i in range(len(number_1)):
        if number_1[i] == number_2[i]:
            continue
        elif number_1[i] > number_2[i]:
            return True
        else:
            return False
    return False
        
print(larger_than("1231", "201"))

# https://www.youtube.com/watch?v=z3BRVQeyXAQ&list=PLd3UqWTnYXOnvJnzMN9nayiKmo5aT9Xzv
# Slice operator:
# ---------------
##########################################################################################################
# Q1 Reverse a string using slicing

string = "Hello World!"
print(string[::-1])

# &[begin:end:step]
# begin index to end-1 index

print(string[::1])
##########################################################################################################
# Q2 Reverse a string using reversed method

s = input("Enter a string to be reversed: ")
r = reversed(s)
for char in r:
    print(char, end = "")
print('\n----------------')

s = input("Enter a string to be reversed: ")
r = reversed(s)
output = ''.join(r)
print(output)


# Python  Built-im methods, String methods, List methods
# Built-in https://docs.python.org/3/library/functions.html
# String    https://www.w3schools.com/python/python_ref_string.asp
# List      https://www.w3schools.com/python/python_lists_methods.asp
##########################################################################################################
# Q3 Reverse a string using while loop
s = input("Enter a string to be reversed: ")
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
##########################################################################################################
# Q4 reverse order of words of a given string

s = input("Enter a string to reverse order of words in given string: ")
l = s.split()
l1=l[::-1]
output = ' '.join(l1)
print(output)
##########################################################################################################
# Q5 write a program to reverse internal content of each word

s = input("Enter a string to reverse words in: ")
l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
output = ' '.join(l1)
print(output)
##########################################################################################################
# Q6 write a program to reverse internal content of every second word in a string

s = "one two three four five six"
print(s)
l = s.split()
l1 = []
i = 0
while i < len(l):
    if i%2 == 0:
       l1.append(l[i]) 
    else:
        l1.append(l[i][::-1])
    i+=1
output = ' '.join(l1)
print(output)
##########################################################################################################
# Q7 write a program to print the chars present at even and odd index separately for the give string

s = input("Enter a string: ")
print('Chars at even index')
i=0
while i < len(s):
    if s[i % 2 == 0]:
        print(s[i], end="")
    i+=2
print('\n')

i=1
print('Chars at odd index')
while i < len(s):
    if s[i % 2 != 0]:
        print(s[i], end="")
    i+=2

##########################################################################################################
# Q8 merge chars of two strings into a single string by taking chars alternatively
# string being of same length
s1 = "RAVI"
s2 = "TEJA"
output = ''
i,j = 0,0
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)

print('-'*15)
# different lengths
s1 = "RAVI"
s2 = "TEJAKIRAN"
output = ''
i,j = 0,0
while i<len(s1) or j<len(s2):
    if i < len(s1):
        output=output+s1[i]
        i=i+1
    if j < len(s2):
        output=output+s2[j]
        j=j+1
print(output)

##########################################################################################################
# Q9 sort chars of the string, first alphabet symbols follewed by digits
# input: B4A1D3
# output: ABD134

s = "B4A1D3"
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output=''.join(sorted(alphabets)+sorted(digits))
print(output)

# alternative
s = "B4A1D3"
alphabets=''
digits=''
for ch in s:
    if ch.isalpha():
        alphabets+=ch
    else:
        digits+=ch
output=''
for ch in sorted(alphabets):
    output=output+ch
for ch in sorted(digits):
    output=output+ch
print(output)

# Q10 program for the requirement 
##########################################################################################################
# input: a4b3c2
# output: aaabbbcc

s=input("Enter some string where alphabet symbol should be followed by digit: ")
output =''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(output)

s=input("Enter some string where alphabet symbol should be followed by digit (ver 2): ")
output =''
for ch in s:
    if ch.isalpha():
        x=ch
    elif ch.isdigit():
        d=int(ch)
        output=output+x*d
print(output)

s = input("Enter some string where alphabet symbol should be followed by a digit (which may be e.g. 12) : ")
output = ''

i = 0  # Initialize an index to iterate over the string

while i < len(s):
    if s[i].isalpha():
        x = s[i]
        i += 1  # Move to the next character

        # Check for consecutive digits and accumulate them
        num_str = ''
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1

        if num_str:
            d = int(num_str)
            output += x * d
        else:
            output += x
    else:
        i += 1  # Move to the next character

print(output)

# s = input("Enter some string where alphabet symbol should be followed by a digit: ")
s = 'aaaabbbccz'
output = ''
previous=s[0]
c=1
i=0
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1:
        output=output+str(c)+previous
    i=i+1
print(output)

###########################################################################################################
# Q12 program with following requirement, input: a4k3b2, output: aeknbd
# ord() finds the unicode value for the given char e.g. print(ord('a')) #97
# to find the corresponding char for the gien unicode value e.g. print(ch(97)) # a

s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
        output=output+ch
    else:
        d=int(ch)
        newc=chr(ord(x)+d)
        output=output+newc
print(output)
