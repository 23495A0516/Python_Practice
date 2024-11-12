# General Process to print
sentence = "This is python code"
print(sentence[0] + sentence[1])
print(f"{sentence[0]}{sentence[1]}")

#Slicing( : : )
""" 
syntax --> var[start:stop:step]
syntax --> var[start:stop]
"""
print("=======positive slicing========")
print(sentence[0:4:2])
print(sentence[0:])
print(sentence[:])
print(sentence[0:len(sentence):2])

print("=======negative slicing========")
print(sentence[-4::2])
print(sentence[-1::-1])
print(sentence[-11:-5])
print(sentence[::])
print(sentence[:])