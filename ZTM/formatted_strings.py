# Formatted strings

name = 'Johnny'
age = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old' + '.')

print(f"Hi {name}. You are {age} years old.")

print("Hi {}. You are {} years old.".format(name, age))

print("Hi {}. You are {} years old.".format('August', 75))
