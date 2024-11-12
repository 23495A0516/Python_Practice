# memory model
""" 
mutable ---> changeble & before and after changes, address should be same
immutable ---> unchangeble & before and after changes, address may be change
"""


name = "python"
print(f"Address Before Changes: {id(name)}")

name += "crt"
print(f"Address After Changes: {id(name)}")