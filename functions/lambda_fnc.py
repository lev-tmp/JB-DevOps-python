# lambda expretion or lambda function
# anonymous funtion - function that don't have name bounce to it

# regular function
# def p(num):
#     return num ** 2
# print(p(4))
# print(type(p))

# lambda function general syntax :
# y = lambda x: x ** 2
# print(y(4))
# print(y)

## Why is usefull, for example :
# def h(n):
#     return lambda x: (x + n) ** 2
#
# c = h(3)
# b = h(0)
# print(c)
# print(b)
#
# print (b(2))
# print(c(2))

##
# Another example build quadratic functions
# def build_quadratic_runction(a, b, c):
#     """Returns the function f(x)=ax^2 + bx + c"""
#     return lambda x: a*x**2 + b*x + c
#
# f = build_quadratic_runction(2, 3, -5)
#
# print(f(0))
# print(f(1))
# print(f(2))
#
# print(build_quadratic_runction(3, 0, 1)(2)) # 3x^2+1 evaluated for x=2
