""" 
operators
  Arithematic ---> +, -, *, /, //, %, **
  Short hand assignment ---> +=, -=, *=, /=, //=, %=, **=
  Relational ---> <=, >=, ==, !=
  Logical    ----> and, or
  MemberShip ----> in, not in
  Identity   ----> is, is not (based on id)
"""
  #-------------------Arithematic ---> +, -, *, /, //, %, **---------------------------------#
a = 10
b = 3
# Addition
print(a + b)  # Output: 13
# Subtraction
print(a - b)  # Output: 7
# Multiplication
print(a * b)  # Output: 30
# Division (float result)
print(a / b)  # Output: 3.3333333333333335
# Floor Division (integer result)
print(a // b)  # Output: 3
# Modulus (remainder)
print(a % b)  # Output: 1
# Exponentiation (power)
print(a ** b)  # Output: 1000

#---------------------Short hand assignment ---> +=, -=, *=, /=, //=, %=, **=--------------------#
num = 10
# Add and assign
num += 2  # num = num + 2
print(num)  # Output: 12
# Subtract and assign
num -= 2  # num = num - 2
print(num)  # Output: 10
# Multiply and assign
num *= 2  # num = num * 2
print(num)  # Output: 20
# Divide and assign
num /= 2  # num = num / 2
print(num)  # Output: 10.0
# Floor divide and assign
num //= 2  # num = num // 2
print(num)  # Output: 5.0
# Modulus and assign
num %= 2  # num = num % 2
print(num)  # Output: 1.0
# Exponentiate and assign
num **= 3  # num = num ** 3
print(num)  # Output: 1.0

#--------------------  Relational ---> <=, >=, ==, !=------------------------------------------#
a = 5
b = 10
# Less than or equal to
print(a <= b)  # Output: True
# Greater than or equal to
print(b >= a)  # Output: True
# Equal to
print(a == 5)  # Output: True
# Not equal to
print(a != b)  # Output: True


#--------------------Logical ----> and, or------------------------------------------------------#
# should be greater than 20 and even number
num = 4
print((num>20) and (num%2==0))
print((num>20) or (num%2==0))

#-------------------MemberShip ----> in, not in-------------------------------------------------#
print("code" in "codewala") # is in it and we say 'in'-->True
print("code" in "Codewala") # is not in it but we say 'in'-->False
print("Code" not in "Codewala") # is in it but we say 'not in' -->False

#--------------------Identity ----> is, is not (based on id)-------------------------------------#
a = -3
b = -3
#--------------------object pooling range (-6, +256)---------------------------------------------#
print(a==b)
print(a is b)

