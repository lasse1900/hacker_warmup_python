# List methods

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_lists_methods.asp
# Python reference w3 schools, https://www.w3schools.com/python/python_reference.asp
# Keywords : https://www.w3schools.com/python/python_ref_keywords.asp

basket = ['a','x','b','c','d','e','d']

print(basket.index('d'))

# print(basket.index('d', 0, 4))

print('d' in basket)
print('x' in basket)

print('i' in 'my name: Lauri')

print(basket.count('d'))

# basket.sort()
print(basket)

print(sorted(basket)) # OBS , makes a new copy and sorts it, so using this have to be taken in a variable if needed
print(basket)

print('-'*15)
new_basket = basket[:] # OR copy() as below
new_basket = basket.copy()
new_basket.sort() # in place
print(basket)

print('-'*15)
print(basket.sort()) # in place
print(basket)

print('-'*15)

basket.sort()
basket.reverse() # in place
print(basket)