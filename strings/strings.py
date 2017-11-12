# Strings explanation ,  Text Processing Services
# https://docs.python.org/3/library/string.html

# 1) First print
# print("Hello World")

# 2 with variable
# message = "Hello World"
# print(message)

# 3 double with single quotes
# message = "Hello guy's havn't beer yet"
# print(message)

# 4 len of string
# message = "Hello World"
# print(len(message))

# 5 Access to char and slicing
# message = "Hello World"
# print(message[0])
# print(message[0:5])
# print(message[:5])
# print(message[6:])
# print(message[3:7])

# 6 string methods:
# message = "Hello World"
# print(message.lower())
# print(message.upper())
# print(message.count("Hello"))
# print(message.count("l"))
# print(message.find("World"))
# print(message.find("Universe"))


# 7 String methods :
# message = "Hello World"
# message.replace('World','Universe')
# print(message)
# new_message = message.replace('World','Universe')
# print(new_message)
# message = message.replace('World','Universe')
# print(message)

# 8 string concatenation
# greeting = "Hello"
# name = "Lev"
# message = greeting + name
# print(message)
# message = '{}, {}. Welcome!'.format(greeting, name)
# print(message)

# 9 new f format , > 3.6
# str = "Hello World"
# name = "Lev"
# age = 39
#
# f_str = f'Hello my name is {name}, and my age is {age}'
# print(f_str)

# 10 dir,  help explanation
# message = "Hello World"
# print(dir(message))
# print(help(str))
# print(help(str.upper))