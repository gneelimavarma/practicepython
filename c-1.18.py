##Demonstrate how to use Python’s list comprehension syntax to produce
##the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

result = [m*(m-1) for m in range(1,11)]
print(result)
