""" 
employee_db = [
        (1234, 'John', 'Physics', 23000),
        (1235, 'Nick', 'Maths', 13000),
        (1236, 'Samantha', 'Maths', 40000), 
        (1237, 'Amanda', 'Chemistry', 25000), 
        (1238, 'Vicky', 'Maths', 10000), 
    ]
print least salaried employee
print highest salaried employee
print Maths employees
sorting based on employees salaries
Print employees whose name starts with A
Print employees whose salary is in range of 20000 to 30000 (inclusive).
print even id Employees
----------MORE TASKS---------
count number of maths employees
count number of vowels in each employee name
reverse the characters in subjects and print only subjects
print the (name in lowercase, subject in uppercase)
Generate user id for each user by concatenating name and id (eg:- Nick_1235)
"""
employee_db = [
        (1234, 'Shizuka', 'Physics', 23000),
        (1235, 'Nobita', 'Maths', 13000),
        (1236, 'Rafi', 'Maths', 40000), 
        (1237, 'Saadh', 'Chemistry', 25000), 
        (1238, 'Maaz', 'Maths', 10000), 
    ]

# Least salaried employee
minimum_sal = float("inf")
employee_name = ""

for data in range(len(employee_db)):
    name, salary = employee_db[data][1], employee_db[data][3]
    if salary < minimum_sal:
        minimum_sal = salary
        employee_name = name
print(f"[QUERY-1]-->{minimum_sal, employee_name}")
# ----------------------------------------------------------

# Highest salaried employee
maximum_sal = float("-inf")
employee_name = ""

for data in range(len(employee_db)):
    name, salary = employee_db[data][1], employee_db[data][3]
    if salary > maximum_sal:
        maximum_sal = salary
        employee_name = name
print(f"[QUERY-2]-->{maximum_sal, employee_name}")

# -------------------------------------------------------------

# Maths employees
maths_employees = []
for data in range(len(employee_db)):
    name, subject = employee_db[data][1], employee_db[data][2]
    if subject == "Maths":
        maths_employees.append((name, subject))
print(f"[QUERY-3]--->{maths_employees}")

# -----------------------------------------------------------------

# Print employees whose name starts with A
employees = []
for data in range(len(employee_db)):
    name = employee_db[data][1]
    if name[0] == "A":
        employees.append(name)
print(f"[QUERY-4]--->{employees}")

# ------------------------------------------------------------------

# Print employees whose salary is in range of 20000 to 30000 (inclusive).
employees = []
for data in range(len(employee_db)):
    name, salary = employee_db[data][1], employee_db[data][3]
    if (salary >= 20000) and (salary <= 30000):
        employees.append((name, salary))
print(f"[QUERY-5]--->{employees}")

# ----------------------------------------------------------------------

# print even id Employees
employees = []
for data in range(len(employee_db)):
    _id, name = employee_db[data][0], employee_db[data][1]
    if _id % 2 == 0:
        employees.append((_id, name))
print(f"[QUERY-6]--->{employees}")

# ----------------------------------------------------------------------

# Count number of Maths employees
maths_employees_cnt = 0 
for data in range(len(employee_db)):
    name, subject = employee_db[data][1], employee_db[data][2]
    if subject == "Maths":
        maths_employees_cnt += 1
print(f"[QUERY-7]---> {maths_employees_cnt}")

print()
# ----------------------------------------------------------------------

# Count number of vowels in each employee name
vowels = "aeiou"
for data in range(len(employee_db)):
    employee_name = employee_db[data][1].lower()
    employee_vowel_cnt = 0
    for letter in range(len(employee_name)):
        if employee_name[letter] in vowels:
            employee_vowel_cnt += 1
    print(f"{employee_name}--{employee_vowel_cnt}")

print()
# ----------------------------------------------------------------------

#    reverse the characters in subjects

for data in range(len(employee_db)):
    subject = employee_db[data][2]
    print(subject[::-1])

print()
# ----------------------------------------------------------------------

#print the (name in lowercase, subject in uppercase)

for data in range(len(employee_db)):
    name, subject = employee_db[data][1].lower(), employee_db[data][2].upper()
    print(name, subject)


# ----------------------------------------------------------------------

# Generate user id for each user by concatenating name and id (eg:- Asma_1235)
print(f"")
for data in range(len(employee_db)):
    id, name = employee_db[data][0], employee_db[data][1]
    name += "_"
    name += str(id)
    print(name)
