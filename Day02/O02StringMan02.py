
print("find".center(40, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1: {st1}")

res = st1.find("w")
print(f"res :{res}")

res = st1.find("l")
print(f"res :{res}")

res = st1.find("l", st1.find("l") + 1)
print(f"res :{res}")

res = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"res :{res}")

print("-" * 40)
print(f"st2 :{st2}")
res1 = st2.find("fox")
print(f"res1 :{res1}")

res1 = st2.find("the")
print(f"res1 :{res1}")

res1 = st2.find("the", st2.find("the")+1)
print(f"res1 :{res1}")

print(f"replace".center(40, "-"))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")

res = st1.replace("h", 'H')
print(f"res :{res}")

res = st1.replace("l",  "L")
print(f"res :{res}")

res = st1.replace("l",  "L", 1)
print(f"res :{res}")

res = st1.replace("l",  "L", 2)
print(f"res :{res}")

res = st1.replace("l",  "L", 5)
print(f"res :{res}")

print("-" * 40)

print(f"st2 :{st2}")
res = st2.replace("brown fox", "white tiger")
print(f"res :{res}")

res = st2.replace("the", "The")
print(f"res :{res}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")
