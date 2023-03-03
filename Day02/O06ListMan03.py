
print("count".center(40, "-"))
l1 = [1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")

print("remove".center(40, "-"))
l1 = [1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(f"l1 :{l1}")

print("-" * 40)
l1.remove(3)
l1.remove(3)
l1.remove(3)
# l1.remove(3)

print(f"l1 :{l1}")
for i in range(0,l1.count(1)):
    l1.remove(1)

print(f"l1: {l1}")

print("clear".center(40, "-"))
l1 = list(range(1, 11))

print(f"l1 :{l1}")

l1.clear()

print(f"l1 :{l1}")

print("index".center(40, "-"))

l1 = [1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(f"l1 :{l1}")

print("-" * 40)
print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3)+1))
print("3 :", l1.index(3, l1.index(3, l1.index(3)+1)+1))

print("reverse".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

"""
reverse and reversed are the same except that
reverse will reverse the original list
reversed will reverse a copy of the list and returns it
"""

res = list(reversed(l1))
print(f"res :{res}")

