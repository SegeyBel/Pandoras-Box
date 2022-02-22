#The Guessing Game.
#Write a program that generates a random number
#between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.



import random
n=random.randint(1, 10)
while True:
    text = input("Введите число или стоп для выхода: ")
    if text == 'стоп':
        break
    elif int(text) == n:
        print("Победа")
        break
    else:
        print("Попробуйте еще")