#The math quiz program
#Write a program that asks the answer for a mathematical expression,
#checks whether the user is right or wrong, and then responds with a message accordingly.

m = 2 + 2 * 2
while True:
    if int(input("Напишите чему равно выражение 2 + 2 * 2 = ")) == m:
        print("Это правильный ответ, ты молодец")
        break
    else:
        print("Подумай")
