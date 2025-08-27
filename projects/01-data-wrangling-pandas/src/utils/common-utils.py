

def fun():
    print("Welcome to GFG")

fun()

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(20)

# Variable length non-keywords argument
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Variable length keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

# Adding Docstring to the function
def evenOdd(x):
    """Function to check if the number is even or odd"""

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

print(evenOdd.__doc__)

# Anonymous Functions in Python
def cube(x): return x*x*x   # without lambda

cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))