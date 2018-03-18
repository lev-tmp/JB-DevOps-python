# Object Identity: is
# Operation: and or not


# General explanation
# if True:
#     print('Conditional was True')

# 1 with var
# language = 'Python'
# if language == 'Python':
#     print('Conditional was True')

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is              # if the value have same id, same object in memory

## 2 else statement

# language = 'Python'
#
# if language == 'Python':
#     print('Conditional was True')
# else:
#     print('No match')

## 3 elif
language = 'Python'

if language == 'Python':
    print('language is python')
elif language == 'Java':
    print('language is java')
else:
    print('No match')

## 4 and , or , not operation

# user = 'Admin'
# logged_in = True

# if user == 'Admin' and logged_in:
#     print('Admin page')
# else:
#     print('Bad Creds')

# not examle
# if not logged_in:
#     print('Please Log in')
# else:
#     print('Welcome')

## 5 is operation
# object id explanation
# a = [1,2,3]
# b = [1,2,3]
#
# print(a == b)
# print (a is b)
#
# print(id(a))
# print(id(b))

## True and False values
# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# condition = False
#
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')








