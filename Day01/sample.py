
#! c:\python\bin

print("Hello World \n" * 5)

print("-" * 40)

def fun():
    # this is a commment
	"""
		function fun will take two arguments

		fun will return the sum of these two arguments
	"""
	print("hello world")

fun()
print(fun.__doc__)

print("-" * 40)
help(fun)

print("-" * 40)

print("Hello World")
print("Hello World")
print("Hello World")

"""
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
"""

print("-" * 40)

def fun1():

    print("hello world")
    print("funtion fun code")

    for i in range(1, 15):      # generate numbers from 1 to <15

        print("for loop code")

        if i % 2 == 0:
            print("if condition code")
            print(i)

fun1()

