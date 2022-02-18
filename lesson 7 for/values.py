
# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys and the number of occurrences as values.


R = {}
n = int(input("The number of occurrences:"))
for k in range(n):                      # range(1,10)
    kl = input("Unique Words:")
    R[kl] = k + 1
print(R)
