# Type conversion

# name = 'Andrei Neagoie'
# age = 50
# relationship_status = 'single'

# relationship_status ='it\'s complicated'
# print(relationship_status)
import datetime
current_year = datetime.datetime.now().year

birth_year = input("What year you were born? ")

# current_year = 2023
age = int(current_year) - int(birth_year)
# print(f"You were born year {birth_year}. Your current age is {current_year} - {birth_year}")
# print(f"You were born year {birth_year}. Your current age is {age}")
print(f"You were born year {birth_year}. Your current age is {int(current_year) - int(birth_year)}")

print(f"You were born year {birth_year}. Your current age is {current_year - int(birth_year)}")

print("You were born year {}. Your current age is {}".format(birth_year, age ))
