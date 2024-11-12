# *args
def numbers(a, *args):
    print(f"Numbers are {a}, {args}")

print(numbers(10, 20, 30, 40))
numbers(30, 40)

# **kwargs(variable keyword arguments)

"""
ORDER:
   positional, Default
  	    *args, **kwargs
"""

def details(**kwargs):
    print(kwargs)

details(age=15, name="gayathri", brother="vidhya")

print("--------------------------------------------")

def details(a, **kwargs):
    print(kwargs)

details(100, age=15, name="latha", brother="maaz") 

print("--------------------------------------------")

def details(a, *args, **kwargs):
    print(a, args, kwargs)

details(100, 200, 300, 400, city="newJersey", age=15, name="asma", brother="rayyan") 
print("==================")

# passing parameters by unpacking
clrs = ("red", "blue", "green")

def colors(c1, c2, c3):
    print(f"Colors are {c1}, {c2}, {c3}")

colors(clrs[0], clrs[1], clrs[2])
colors(clrs[0], clrs[2], clrs[1])
colors(*clrs)