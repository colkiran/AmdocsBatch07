
print("arithmetic".center(40, "-"))
print(f"Add : 10 + 3 = {10 + 3}")
print(f"Sub : 10 - 3 = {10 - 3}")
print(f"Mul : 10 * 3 = {10 * 3}")
print(f"Div : 10 / 3 = {10 / 3}")
print(f"Flr_div : 10 // 3 = {10 // 3}")
print(f"Mod : 10 % 3 = {10 % 3}")
print(f"Exp : 10 ** 3 = {10 ** 3}")

print("Augmentor".center(40, "-"))
# =, +=, -=, /=, *=

x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("comparison".center(40, "-"))
# ==, >, >=, <, <=, !=
a = 10
b = 15
print(f"a == b :{a == b}")
print(f"a > b  :{a > b}")
print(f"a != b :{a != b}")
print(f"a < b  :{a < b}")

print("logical".center(40, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
#or
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
# not
print(f"not(1 == 1 and 2 == 2) :{not(1 == 1 and 2 == 2)}")
print(f"not(1 == 1 and 2 == 1) :{not(1 == 1 and 2 == 1)}")

print("-" * 40)
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print("Bitwise".center(40, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"5 >> 1 :{5 >> 1}")
print(f"16 >> 1 :{16 >> 1}")


print("ternery".center(40, "-"))
age = 18
print("Eligible" if age >= 18 else "Not Eligible")
