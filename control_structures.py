"""
control structures
  -conditional structures
	-if-else
	-multiple if
	-nested if-else
  -looping statements
	-for loop
	-for-else loop
	-while loop
	-while-else loop
  -unconditional statements
	-break
	-continue
	-pass
"""

print("(((((((((((((((((for loop)))))))))))))))))")
# looping statment[[[[[["(for i in range(0,10,1):)"]]]]]]
for india in range(0,10,1):#instead of (i) in range we can take any variable which is used to print it by calling the variable
    print(india)
    
   # "muhammad_maaz" is a string
name="muhammad_maaz"
for india in range(0,13,1):
    print(name[india])
    
    
#(((((((((((((((((for-else loop)))))))))))))))))
"""
take 5 inputs from user
after each input, print if input length is below or equal to 100, else print invalid
"""
for i in range(5):
    data=int(input("Enter Number: "))
    if data <= 100:
        print("Valid Input")
else:
    print("Invalid")
    
    
print("((((((((((((((((((While loop))))))))))))))))))")    
name = "python"
current = 0
while current < len(name):
    print(name[current], current)
    current += 1
# name = "python"
# current = len(name)-1
# while current >= 0:
#     print(name[current], current)
#     current -= 1


#(((((((((((((((((((While-else loop)))))))))))))))))))  
start = 0
while start < 5:
    data=int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
    start += 1
else:
    print("No Negative num Entered")  
  
