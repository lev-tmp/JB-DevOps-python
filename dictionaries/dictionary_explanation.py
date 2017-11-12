# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type;
# strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
# You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# 1 Initialization , key, value. access
# student = {'name': 'Jhon', 'age':'25', 'courses':['Math', 'CompSci']} # key can be int , string all immutable types !
# print(student['name'])
# print(student['courses'])
#
# print(student.get('phone', 'Not Found'))

# 2 add key value
# student = {'name': 'Jhon', 'age':'25', 'courses':['Math', 'CompSci']} # key can be int , string all immutable types !
# student['phone'] = '555-55556'
# print(student)
# student['name'] = 'Janet'
# print(student)

# 3 dictionary update
# student = {'name': 'Jhon', 'age':'25', 'courses':['Math', 'CompSci']} # key can be int , string all immutable types !
# print(student)
# student.update({'name': 'Jane', 'age':23, 'phone': '555-55556'})
# print(student)

# 4 dictionary del method
# student = {'name': 'Jhon', 'age':'25', 'courses':['Math', 'CompSci']} # key can be int , string all immutable types !
# print(student)

# with del
# del student['age']
# print(student)

# with pop
# age = student.pop('age')
# print(age)
# print(student)


# walking through dic
# student = {'name': 'Jhon', 'age':'25', 'courses':['Math', 'CompSci']} # key can be int , string all immutable types !
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# walking throught key
# for key in student:
#     print(key)

# walking both key, values
# for key, value in student.items():
#     print(key,value)

