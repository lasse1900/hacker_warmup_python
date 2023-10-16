# Password chekker

username = input("Give username: ")
password = input("Give your password: ")

password_length = len(password)
output = '*'*password_length

print(f'{username} your password {output} is {len(password)} long')

