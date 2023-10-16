# Lists

li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a','True']

# Data Structure

amazon_cart = [
    'notebook', 
    'sunglasses',
    'toys',
    'grapes'
    ]

print(amazon_cart)
print(amazon_cart[0::2])
print(amazon_cart[2:])

print('-'*15)
amazon_cart[0] = 'laptop'
print(amazon_cart[0:3])
print(amazon_cart)

# print('-'*15)
# new_cart = amazon_cart  # OBS! Note this is a catcha
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

print('-'*15)
new_cart = amazon_cart[:]  # OBS! Note this, copy list to another
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

