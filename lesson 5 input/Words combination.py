#Words combination

#reate a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
#that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
#Tips: Use random module to get random char from string)

import random
text = input("Введите слово:")
a = 1
while a < 6:
   a = a + 1
   print("".join(random.sample(text,len(text))), end=" ")