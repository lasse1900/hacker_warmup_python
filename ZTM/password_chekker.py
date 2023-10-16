# Password chekker

username = input("Give username: ")
password = input("Give your password: ")

password_marks = []
string = " "
ret = string.join(password_marks)   

for i in range(len(password)):
    password_marks.append("*")

ret = string.join(password_marks)    
output = ''.join(ret.split())    

print(f'Password {output} is {len(password)} long')

