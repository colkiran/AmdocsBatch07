
# functions that can add values into the list - append, extend, insert

print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(f"l1[8] :{l1[8]}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(40, "-"))
l2 = list(range(2, 11, 2))
print(f"l2 :{l2}")

l2.extend(list(range(12, 19, 2)))
print(f"l2 :{l2}")

l2.extend([20, 22, 24])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

l1.insert(100, 18)      # adds this to the end of the list

print(f"l1 :{l1}")

# delete elements from a list - pop, remove, clear

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

# res = l1.pop(10)
# print(f"res :{res}")

print(f"l1 :{l1}")

