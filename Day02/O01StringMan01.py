
st1 = "hello world"
print(f"st1 :{st1}")
print(type(st1))

print("-" * 40)
print(f"st1[0]  :{st1[0]}")          # strings are stored like a list(array)
# strings are immutable
# st1[0] = "H"
print(f"st1[6]  :{st1[6]}")
print(f"st1[10] :{st1[10]}")

print("-" * 40)
# slicing
print(f"st1[0:5]  :{st1[0:5]}")
print(f"st1[6:11] :{st1[6:11]}")
print(f"st1[0:11] :{st1[0:11]}")
print(f"st1[0:]   :{st1[0:]}")
print(f"st1[:11]  :{st1[:11]}")
print(f"st1[:]    :{st1[:]}")

print("-" * 40)
# reverse indexing
print(f"st1[-1]  :{st1[-1]}")
print(f"st1[-7]  :{st1[-7]}")
print(f"st1[-11] :{st1[-11]}")

print("-" * 40)
# slicing
print(f"st1[-1:-6:-1]  :{st1[-1:-6:-1]}")
print(f"st1[-7:-12:-1] :{st1[-7:-12:-1]}")
print(f"st1[-1:-12:-1] :{st1[-1:-12:-1]}")
print(f"st1[-1::-1]    :{st1[-1::-1]}")
print(f"st1[:-12:-1]   :{st1[:-12:-1]}")
print(f"st1[::-1]      :{st1[::-1]}")

print("-" * 40)
# using indexes find if the given string is a palindrome
st2 = "malayalam"
print(f"Palindorme {st2}" if st2 == st2[::-1] else f"Not a Palindrome {st2}")

print("-" * 40)
print(dir(st1))

print("find".center(40, "-"))

"""
find - 5 chars
40 - 5 => 35
35 / 2 => 17, 18
"""