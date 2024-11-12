"""-functions
  -return functions
  -not return functions
  -parameterized functions
  	-positional
	-keyword
	-default
	-*args
	-**kwargs(variable keyword arguments)
	-passing parameter by unpacking"""
# --> To re-use the code
# --> syntax: 
# 	def functionName(parameters):
# 		pass
# --> function will get execute, only when it's called
# --> if control finds return in function, it will get out of that entire function 
# non-return function & parameterized function
def welcome(name, bank):
    print(f"Hello {name}, Happy {bank} Banking")

welcome("Nick", "Paypal")
welcome("Rasool", "Hdfc")
welcome("Akash", "CANARA")
welcome("Anil", "ICICI")

print("-----------------------------------")

# return function & parameterized function
def welcome(name, bank):
   return f"Hello {name}, Happy {bank} Banking"

print(welcome("Dhanjay", "Paypal"))
print(welcome("Mouneesh", "Hdfc"))
print(welcome("Swaroop", "CANARA"))
print(welcome("Varma", "ICICI"))

print("-----------------------------------")

# non-parametrized function & return function
def oneToFive():
  for i in range(1, 6):
    print(i)
  return "done"

print(oneToFive())

print("-----------------------------------")

# non-parametrized function & non-return function
def oneToFive():
  for i in range(1, 6):
    print(i)

oneToFive() 

print("-----------------------------------")