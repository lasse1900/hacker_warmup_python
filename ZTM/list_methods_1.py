# List methods

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_lists_methods.asp

basket = [1,2,3,4,5]
print(len(basket))

# adding
basket.append(100)
print(basket)
new_list = basket.append(101) # OBS, modifies list on place
print(new_list)
print('-'*15)
new_list = basket
print(basket)
print(new_list)

basket.insert(2, 50)
print(basket)
print(new_list)

basket.extend([25, 26])
print(basket)
print(new_list)

# removing
basket.pop()
print(basket)
basket.pop(0) # index we remove
print(basket)

basket.remove(4) # value we remove
print(basket)

new_list = basket.remove(100) # work in place
print(new_list)

new_list = basket.pop(2) # returns what it removes (from index 2)
print(new_list)

new_list = basket.clear() # clears the list
print(basket)