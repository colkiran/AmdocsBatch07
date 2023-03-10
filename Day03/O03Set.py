

s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9.2, 10.5, 11.3, 12.9, True, False, 15+2j, 15-2j}
print(f"s2 :{s2}")

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s1 = {1, 2, 3}
print(f"s1 :{s1}")

# add values into a set - add, update
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(5)
s1.add(3)
print(f"s1 :{s1}")

# update
s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([8, 9, 10])
s1.update([4, 5, 6])
print(f"s1 :{s1}")

print("-" * 40)
for i in s1:
    print(i, end=" ")
print()

# remove values from a set - pop, remove, discard
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print("-" * 40)

s1.remove(8)
s1.remove(4)
# s1.remove(1)
print(f"s1 :{s1}")

print("-" * 40)
s1.discard(6)
s1.discard(10)
s1.discard(1)
print(f"s1 :{s1}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 40)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 40)
print(f"A symmetric difference A :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 40)
# frozen sets -> immutable
x = frozenset([1, 2, 3, 4, 5])
print(f"x :{x}")
print(type(x))
