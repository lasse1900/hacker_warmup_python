
for i in range(1,13):
    # print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3)) # formatting with with 2,3 and 4

print('-'*15)

for i in range(1, 13):
    # print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3)) # center
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print('='*15)
print("Pi is approximately {0:<72.50f}".format(22 / 7)) # left align (center ^)
print("Pi is approximately {0:^72.50f}".format(22 / 7)) # left align (center ^)
print("Pi is approximately {0:<72.54f}".format(22 / 7))
print('-'*15)
print("Pi is approximately {0:<72.2f}".format(22 / 7))
print('-'*15)

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
