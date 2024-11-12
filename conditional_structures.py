"""control structures
  -conditional structures
	-if-else
	-multiple if
	-nested if-else"""
 
""" 
take 5 inputs from user
after each input, print if input length is below or equal to 5, else print invalid
"""
for num in range(1, 6):
    name = input(f"Enter Input-{num} :")
    if len(name) <= 5:
        print(f"Output: {name}")
    else:
        break
"""--------------------------------------------------"""    
for i in range(5):
    data = int(input("Enter Number: "))
    if data <= 100:
        print("Valid Input")
else:
    print("Invalid")
"""-----------------------------------------------------"""
