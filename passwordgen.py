import random
chars="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-={}[]:'|;\<>?|,./\""
len=int(input('Enter a length:'))
password=""

for a in range(len):
	password+=random.choice(chars)
print(password)