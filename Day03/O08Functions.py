
def greet():
    print("Greetings Mr.Sachin, Welcome to the event....")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# city is called default argument and gname is called non default argument
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event........")



greet()
print("-" * 40)

greetGst("Rahul")
greetGst("Sachin")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
# variable length arguments
def multiplyMe(*numbers):              # numbers can accept more than one value
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(multiplyMe(1, 2, 3, 4, 5))

print("-" * 40)

def Extract_Details(**details):       # accepts data like a dictionary
    print(details)
    print(f"Name :{details['name']}")
    print(f"Age :{details['age']}")
    print("-" * 40)
    for k,v in details.items():
        print(k, "=>", v)


Extract_Details(name="Richard", age=31, dept='IT', desig='PL', salary=75000)

print("-" * 40)

def AddMe(x, y):
    return x + y

a = 14
b = 25
print(f"The sum of {a} and {b} is :{AddMe(a, b)}")

# python supports recursive calls - function calling itself

print("-" * 40)
# recursive call
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

num = 5
print(f"The fact of {num} is :{fact(num)}")

print("-" * 40)
def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")
