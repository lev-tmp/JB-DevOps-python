## General explanation
# https://docs.python.org/3/library/exceptions.html
# log module short explanation and example (import logging)
# https://docs.python.org/3/library/logging.html#logging.Logger.error

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

## Let's try to open file

# f = open('test.txt ','r')

## Let's handle this with general exception
try:
    f = open('test.txt','r')
except Exception:
    print("Sorry this file isn't exist!")

## Let's handle it with specific exeption
# try:
#     f = open('test.txt ','r')
# except FileNotFoundError:
#     print("Sorry this file isn't exist!")

## Let's add more code , with differnt broken line
# try:
#     f = open('test.txt','r') # file open fixed
#     var = bad_var # bad varibale
# except FileNotFoundError: # add and show as e, print(e)
#     print("Sorry this file isn't exist!")
# except Exception: # add and show as e, print(e)
#     print("Something went wrong!")
    # print(e)

## Else block
# try:
#     f = open('test.txt','r')
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()

## Finally block
# try:
#     f = open('test.txt','r')
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing Finally...!")

## Log module

# import logging
#
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
#
# try:
#     f = open('test.txt','r')
# except Exception as e:
#     logging.error(e)
# else:
#     print(f.read())
#     logging.info("end file {} manipulation".format(f.name))
#     f.close()
# finally:
#     logging.info("from finally block of exception")