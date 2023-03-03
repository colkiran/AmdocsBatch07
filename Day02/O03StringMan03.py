
# maketrans and translate
st = 'hello world'
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'
# the lenght of a and b should be the same

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("split".center(40, "-"))
st = "this is a sample string"
print(f"st :{st}")

# convert string into a list
resLst = st.split()
print(f"resLst :{resLst}")

# convert list into a string
res = " ".join(resLst)
print(f"res :{res}")

print("format".center(40, "-"))

# c style - printf
format = "Welcome %s, what a %s player"
print(format)

values = ("Sachin", "class")            # tuple
print(values)
print(format, values)
print(format % values)

print("-" * 40)
print("Welcome %s, what a %s player" % ("Sachin", "class"))
print("Welcome %s, with a rating of %d what a %s player" % ("Sachin", 4, "class"))
print("Welcome %s, with a rating of %d what a %s player" % ("Sachin", 4.672345, "class"))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Sachin", 4.672345, "class"))

print("-" * 40)
# interpolation
from math import pi, e
print(f"PI = {pi} and Euler's constant :{e}")
print(f"PI = {pi} and Euler's constant :{e}")

print("-" * 40)
# format from python strings
print("Welcome {},what a {} player".format("Sachin", "class"))
print("Welcome {}, with a rating of {} what a {} player".format("Sachin", 4, "class"))
print("Welcome {0}, with a rating of {1} what a {2} player for {3}".format("Sachin", 4, "class", "India"))
print("Welcome {2}, with a rating of {3} what a {0} player for {1}".format("Sachin", 4, "class", "India"))
print("Welcome {pname}, with a rating of {rat} what a {adj} player for {cty}".format(pname= "Sachin", rat=4, adj="class", cty="India"))

print("Welcome {pname}, with a rating of {rat} what a {adj} player for {cty}".format(pname= "Sachin", rat=4.78390, adj="class", cty="India"))

print("Welcome {pname}, with a rating of {rat:.3f} what a {adj} player for {cty}".format(pname= "Sachin", rat=4.78390, adj="class", cty="India"))

print("Welcome {0}, with a rating of {1:.3f} what a {adj} player for {cty}".format("Sachin", 4.78390, adj="class", cty="India"))

print("-" * 40)
# conversion
print("{val} {val} {val}".format(val="A"))
print("{val!r} {val!a} {val!s}".format(val="A"))

print("-" * 40)
print("{val} {val} {val}".format(val=36))
print("{val:b} {val:f} {val}".format(val=36))
print("{val:10} {val:f} {val:b}".format(val=36))
print("{val:5} {val:f} {val:b}".format(val=36))
print("{val:5} {val:f} {val:b}".format(val=363454545233))

print("-" * 40)
print("{val:15} world".format(val=36))
print("{val:15} world".format(val="Hello"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
print("{val:10.2}".format(val = pi))
print("{val:10.3}".format(val = pi))
print("{val:10.4}".format(val = pi))
print("{val:10.5}".format(val = pi))

print("-" * 40)
print("{val:^15} Tendulkar".format(val="Sachin"))       # center align
print("{val:>15} Tendulkar".format(val="Sachin"))       # right align
print("{val:<15} Tendulkar".format(val="Sachin"))       # left align

print("-" * 40)
print("{val:-^15} Tendulkar".format(val="Sachin"))       # center align
print("{val:*>15} Tendulkar".format(val="Sachin"))       # right align
print("{val:#<15} Tendulkar".format(val="Sachin"))       # left align

print("-" * 40)
print("{val:015}".format(val=50))       # left align




