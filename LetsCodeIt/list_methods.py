# List methods

cars = ['bwm', 'honda','toyota']

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(0,"Opel")
print(cars)

x = cars.index('Benz')
print(x)

y = cars.pop()
print(y)
print(cars)

slicing = cars[1:]
print(slicing)

print('-'*15)
cars = ['bwm', 'honda','toyota',"audi"]
print(cars)
print(cars)
print('-'*15)
# sorted_cars = cars[:]
sorted_cars = cars.copy()
sorted_cars.sort()
print(sorted_cars)
print(cars)


l=[1, 2, 3, 3, 2, 1]
print(l[-2:])
print(l[4:6])