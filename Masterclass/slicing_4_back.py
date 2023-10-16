
letters = "abcdefghijklmnopqrstuvxyz"
# letters = ""
#          1234567890123456789012345

backwards = letters[25::-1]
print(backwards)

print(letters[::-1])
print('-'*15)

# qpo
print(letters[16:13:-1])

# edcba
print(letters[4::-1])

# last 8 chars
# print(letters[:17:-1] + letters[17])

print(letters[:-9:-1]) # reversed order

print(letters[-4:])
print(letters[-1:])

print(letters[:1])
print(letters[0]) # if string is empty causes error

