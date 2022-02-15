#The greatest number

#Write a Python program to get the largest number from a list of random numbers with the length of 10

#Constraints: use only while loop and random module to generate numbers

# from random import sample                                     # вариант №1
#lst1 = sample(range(1, 100), 10)


#import random                                                  # вариант №2
#while True:
    #lst1 = [random.randint(1, 100) for _ in range(10)]
    #print("List of random:", lst1)
    #print("Largest number from a list:", max(lst1))

    #break
import random                                   # вариант №3
y = [random.randint(1,100)]
i=1
while i < 10:
    y += [random.randint(1,100)]
    i +=1
print("List of random:", y)
print("Largest number from a list:", max(y))
