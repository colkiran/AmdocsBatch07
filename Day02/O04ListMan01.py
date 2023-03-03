
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.6, 9.3, 10+5j, 10-5j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 =  list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.6, 9.3, 10+5j, 10-5j, True, False]
print(f"l2 :{l2}")
# memory allocation

print(f"l2[0] :{id(l2[0])}")
print(f"l2[1] :{id(l2[1])}")
print(f"l2[2] :{id(l2[2])}")
print(f"l2[3] :{id(l2[3])}")

print("-" * 40)
# create
l1 = list(range(1, 6))
print(f"l1 :{l1}")

print("-" * 40)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")

# iterate
for i in l1:
    print(i, end=" ")
print()

print("-" * 40)
# modify

#replace
l1[2] = 300
l1[0] = 11

# insert
l1[4] = 500

print(f"l1 :{l1}")          # we cannot insert a new value into the list

print("-" * 40)
# delete
del l1[2]
del l1[3]

print(f"l1 :{l1}")

print("-" * 40)
print(dir(l1))

