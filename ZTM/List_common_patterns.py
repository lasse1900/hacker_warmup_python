# List methods

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_lists_methods.asp
# Python reference w3 schools, https://www.w3schools.com/python/python_reference.asp
# Keywords : https://www.w3schools.com/python/python_ref_keywords.asp

basket = ['a','x','b','c','d','e','d']

basket.sort()
basket.reverse()
print('-'*15)
print(len(basket))
print('-'*15)
print(basket[::-1])
print('-'*15)
print(basket)

print(list(range(1,100)))
print('-'*15)
print(list(range(101)))
print('*'*15)

sentence = ' '
new_sentence = sentence.join(['Hi','my', 'name', 'is', 'Jojo!'])
print(new_sentence)

new_sentence = sentence.join(['Hello, how are you doing?'])
print(new_sentence)