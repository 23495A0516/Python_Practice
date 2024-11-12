# Examples
def details(a, b, name, age, city="ong"):
    print(a, b, name, age, city)
details(10, 20, age=123, name="steeve")

print("============================")

def addition(*args):
    print(sum(args))
addition(10, 20, 30, 40)
addition(10, 20)
addition(10, 20, 30, 40, 50)

print("============================")

def addition(n1, n2, *remaining):
    return n1 + n2 + sum(remaining)
addition(10, 20, 30, 40, 50, 60)