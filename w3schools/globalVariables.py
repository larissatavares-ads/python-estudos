
x="awesome"

def func():
    x = "fantastic"
    print("python is " + x)

func()

print("python is " + x)


def func():
    global x
    x = "fantastic"
    print("python is " + x)

func()

print("python is " + x)