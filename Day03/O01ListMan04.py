
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the elements of l1 into l2

l2 = l1          # shallow copy - copying the address along with the data

print(f"l2 before :{l2}")

print("-" * 40)
l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print('\n', "-" * 40, "\n")
l3 = [2, 4, 6, 8, 10]
print(f"l3 before :{l3}")

l4 = l3.copy()          # deep copy - only data is copied
print(f"l4 before :{l4}")

print("-" * 40)
l4.extend([12, 14, 16, 18])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print('\n', "-" * 40, "\n")
l5 = [11, 22, 33, 44, [1, 2, 3, 4, 5], 55]
print(f"l5 before :{l5}")

l6 = l5.copy()
print(f"l6 before :{l6}")

print("-" * 40)
l6[4].extend([6, 7, 8])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print('\n', "-" * 40, "\n")

l7 = [1, 2, 3, 4, 5, [10, 20, 30, 40, 50]]
print(f"l7 before :{l7}")

from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")
print("-" * 40)

l8[5].extend([60, 70])
l8[5].extend([80, 90])

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("sort".center(40, "-"))
l1 = [10, 5, 2, 9, 1, 8, 3, 6, 4, 7]
print(f"l1 :{l1}")

"""
sort    - sort will sort the original list
sorted  - will return a copy of sorted list
"""

Asc_res = sorted(l1)
print("Ascending  :", Asc_res)

Desc_res = sorted(l1, reverse= True)

print(f"Descending :", Desc_res)

print("-" * 40)
l1 = [10, 'zebra', 5,'apple', 2,'yellow', 9, 'blue', 1, 'white', 8, 'green', 3, 'violet',  6, 'maroon', 4, 'pink', 7, 'red', 'orange', 1080, 120, 26, 219, 20123]
print(f"l1 :{l1}")


print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 40)
res = res[0:res.index('zebra')] + sorted(res[res.index(1):])
print(f"res :{res}")

