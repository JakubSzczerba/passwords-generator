# Very simple password generator

import random
password = []
print('')
print('PASSWORD GNERTATOR ')
print('')
print('l -> low\nm -> medium\ns -> strong')
print('')
x = input('Your choice: ')
low = 'abcdefghijklmnoprstwuyz'
medium = 'abc1def2gh3ijkl4mn5oprs6t7wu8y9z' 
strong = 'abc1def2gh3ijkl4ABCDE!@#$%^&*(FGHIJ)+_-KLMNOPRSTWUmn5oprs6t7wu8y9zYZ'


if x == 'l':
    password = random.sample(low, k=6)  
    print(''.join(password))    

elif x == 'm':
    password = random.sample(medium, k=9)
    print(''.join(password))

elif x == 's':
    password = random.sample(strong, k=16)
    print(''.join(password))
else:
    exit()




