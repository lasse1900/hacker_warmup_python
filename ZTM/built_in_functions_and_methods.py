# Built-in functions and methods

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp

greet = 'Hello there'

print(len(greet))

print(greet[0:])
print(greet[0:len(greet)])

quote = 'to be or not to be'

clause = quote.upper()
print(clause)

print(quote.find('be'))
print("-"*15)

print(quote.replace('be', 'me'))
print(quote)

print("-"*15)
quote_2 = quote.replace('be', 'me')
print(quote_2)
print("-"*15)


