
## Links
[Interview questions google search](https://www.youtube.com/results?search_query=python+string+interview+questions+)

[Interview questions - Python](https://www.youtube.com/watch?v=wwtzs7vTG50&list=PLZ7s-Z1aAtmJqtN1A3ydeMk0JoD3Lvt9g)

[Interview questions - Strings](https://www.youtube.com/watch?v=j5pBNieB1rs)

[Interview questions - Strings 2](https://www.youtube.com/watch?v=z3BRVQeyXAQ&list=PLd3UqWTnYXOnvJnzMN9nayiKmo5aT9Xzv&index=1)

### Reverse a string

Slice operator:
---------------
string = "Hello World!"
print(string[::-1])

- &[begin:end:step]
- begin index to end-1 index

Python  Built-im methods, String methods, List methods

[Built-in](https://docs.python.org/3/library/functions.html)

[String methods](https://www.w3schools.com/python/python_ref_string.asp)

[List methods](https://www.w3schools.com/python/python_lists_methods.asp)


s = input("Enter a string to be reversed: ")
r = reversed(s)
for char in r:
    print(char, end = "")
print('\n----------------')

s = input("Enter a string to be reversed: ")
r = reversed(s)
output = ''.join(r)
print(output)

