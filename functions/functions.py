
## 1 basic function definition, empty function

# def hello_func():
#     pass
#
# print(hello_func())

## 2 function defenition
# def hello_func():
#     print('hello function!')
#
# hello_func()
# hello_func()
# hello_func()
# hello_func()
# hello_func()

## 3 return of function and method on return
# def hello_func():
#     return 'hello function!'
# print(hello_func())
# print(hello_func().upper())

## function arguments, to show : error when without argument, default value argument, couple arguments
# def hello_func(greeting):
#     return '{} function!'.format(greeting)
#
# print(hello_func())

#####
# DRY principle keep your code clean without repeats. Don't repeat yourself !
# Concentred on input and return value of functions
#####

# Advanced topic, function with args and kwargs
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# student_info('Math', 'Art', name='Jhon', age=22)
#
# courses = ['Math', 'Art']
# info = {'name':'Jhon', 'age':22}
#
# student_info(courses, info)
# student_info(*courses, **info)