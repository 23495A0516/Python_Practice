"""
 Data types -> primitive, composite
 primitive ----> int 10, str "maaz", float 30.1, bool True, False
 composite ----> list [1, 2], tuple (1, 2), 
                 set {1, 2}, dict {'name':'akash'},
                 frozenset frozentset({1, 2})

- we can convert any data type into str
"""
# To check that what is it's data_type
num=(20)
print(type(num))

# int --> str
num = 30 # we know that 30 is int
num = str(30) # int 30 is converted to str
print("int->str====", num, type(num))

# int --> float
num = 30 # we know that 30 is int
num = float(30) # int 30 is converted to 30.0 let's see it by print
print("int->float====", num, type(num))

# float --> int
num = 40.99999 #float
num = int(num) #converted to int
print("float->int====", num, type(num))

#"str" --> num
num = "123" #"str"
num = int(num) #"cnvrtd to num"
print("str->int====", num, type(num))

# "str"--> float
num = "123.9" # actually it is float but it in "_____" so it is denoted as string
num = float(num) # cnvrtd to float
print("str->float====", num, type(num))

# str-->float-->int
num = "123.9" #str
num = float(num) #str->float
num = int(num) #float->int
print("str->int====", num, type(num))

# non-zeroes or non-empty -------> True
# zeroes or empty -------> False
#str-->bool
value = "temp"
value = bool(value)
print("str->bool===", value, type(value))

# composite type conversions
# list [1, 2], tuple (1, 2), set {1, 2}, dict {'name':'akash'},frozenset frozentset({1, 2})
arr = [1, 2, 3, 3]
arr_tuple = tuple(arr)
print("list->tuple====", arr_tuple, type(arr_tuple))

arr_set = set(arr)
print("list->set====", arr_set, type(arr_set))

temp = [("name","MAAZ"), ["course", "python"]]
arr_dict = dict(temp)
print("list->dict====", arr_dict, type(arr_dict))