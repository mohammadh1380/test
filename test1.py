import random
import pygame
import stddraw

#get information from user for sing up

user_name=input('enter your name:')
if len(user_name)<=5:
    print('no pass')
else:
    print('pass')
    password=input('enter your passwors:')
    if len(password)<=7:
        print('no pass')
    else:
        print('pass')
        confirm_passwors=input('enter your password again:')
        if confirm_passwors==password:
            print('pass')
        else:
            print('no math')

#play game with user

for i in range(21):
    Random_number=random.random(0,100000)
    guss_user=int(input('enter yor guss:'))
    if guss_user<Random_number:
        print('guss low')
    elif guss_user>Random_number:
        print('guss high')
    else:
        stddraw.text(0.5,0.5,'you win')
stddraw.show()




