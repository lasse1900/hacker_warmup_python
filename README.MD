
# https://www.youtube.com/results?search_query=python+string+interview+questions+
# https://www.youtube.com/watch?v=wwtzs7vTG50&list=PLZ7s-Z1aAtmJqtN1A3ydeMk0JoD3Lvt9g
# https://www.youtube.com/watch?v=j5pBNieB1rs

# https://www.youtube.com/watch?v=z3BRVQeyXAQ&list=PLd3UqWTnYXOnvJnzMN9nayiKmo5aT9Xzv
# Reverse a string


Slice operator:
---------------
string = "Hello World!"
print(string[::-1])

&[begin:end:step]
begin index to end-1 index

# Python  Built-im methods, String methods, List methods
# Built-in https://docs.python.org/3/library/functions.html
# String    https://www.w3schools.com/python/python_ref_string.asp
# List      https://www.w3schools.com/python/python_lists_methods.asp


s = input("Enter a string to be reversed: ")
r = reversed(s)
for char in r:
    print(char, end = "")
print('\n----------------')

s = input("Enter a string to be reversed: ")
r = reversed(s)
output = ''.join(r)
print(output)

