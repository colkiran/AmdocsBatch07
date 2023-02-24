
"""
for loop is similar to foreach loop

foreach loop will relies on a collection (objects)

collection - range(1, 10)

range(1, 10)    - starts from 1 to < 10

range(1, 20, 2) - odd numbers = 1, 3, 5, 7....19

range(10, 0, -1) - 10, 9, 8....1

 - continue - to skip the iteration

 - break - to stop the iteration

 - else - will execute after the for loop

"""

for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(1, 25):
    # if i > 20:
    #     break
    if i % 2 == 1:
        continue
    print(i, end=" ")
else:
    print("\nCompleted the iteration")
print()

# best example for else - find the prime numbers








