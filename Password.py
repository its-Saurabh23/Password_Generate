import random
import array as arr


max_len = 12

digit = ['0','1','2','3','4','5','6','7','8','9']
lowercase_character = ['a','b''c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_charater = ['A','B''C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols =['@','~','#','$','%','&','*'<',','?',"/"]

combine_list = digit + lowercase_character +uppercase_charater + symbols 

rand_digit = random.choice(digit)
rand_lower = random.choice(lowercase_character)
rand_upper = random .choice(uppercase_charater)
rand_symbol = random.choice(symbols)

password = rand_digit + rand_lower + rand_upper + rand_symbol

#print(password)

for x in range(max_len - 4):
    password = password + random.choice(combine_list)
    password_list = arr.array('u',password)
    random.shuffle(password_list)
    
new_password =""
for x in password_list:
    new_password = new_password + x
    
print("The Generated password is: " + new_password)