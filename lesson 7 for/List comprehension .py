# List comprehension exercise

# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.


i = tuple(a for a in range(1, 11))
j = tuple(a * a for a in i)
y = [i, j]
print(y)
