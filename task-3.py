""" 
TASK: Take email as an input from user, than can contain 
      lower, upper, numbers and domains like @gmail.com, @hotmail.com, @yahoo.com
    After separating the domain,
      print the domainless lowercase name and count the number of vowels in the email.

      Your code should work for all the mails, irrespective of the domain.
      NOTE: No invalid email should be taken

Sample Input1:
  NIck@gmail.com
Sample Output1:
  nick ---- 1

Sample Input2:
  coDEwala@yahoo.com
Sample Output2:
  codewala ---- 4

Sample Input3:
  SteeveRogers123@hotmail.com
Sample Output3:
  steeverogers123 ---- 5

"""
print()
email=input("Enter Email: ").lower()
#SteeveRogers123@hotmail.com
ind=email.find("@")
vowels="aeiou"
domainless=email[0:ind]
cnt=0
for v in range(5):
    letter=vowels[v]
    cnt+=domainless.count(letter)
print(domainless,cnt)