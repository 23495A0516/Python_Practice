""" 
TASK: Get the username from the user and generate the userid
For Memory Issues, Limit the userid to length 10 with following conditions
  - if the length of userid is less than 10, then cover it with 0 at prefix
  - if length of userid exceeds 10, then remove the extra characters

For the security reasons, we had to mask the user id with following:
  replace the last two characters with 'X'
Print the userid along with masked userid

Sample Input1:
  nick
Sample Output1:
  000000nick ---- 000000niXX

Sample Input2:
  codewala
Sample Output2:
  00codewala ---- 00codewaXX

Sample Input3:
  SteeveRogers
Sample Output3:
  SteeveRoge ---- SteeveRoXX

"""
print()
name = "steeverogers"
n = (10 - len(name))
userid = (n*"0") + name
masked = userid[:8]+"XX"
# print(userid, userid[:8]+"XX")
print(f"{userid} ---- {masked}")

name = "steeverogers"
userid = ((10 - len(name))*"0") + name
print(f"{userid} ---- {userid[:8]+"XX"}")





