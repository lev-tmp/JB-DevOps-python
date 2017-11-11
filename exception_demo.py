

try:
    f = open('test2_.txt','r')
    # var = bad_var
except FileNotFoundError as e: # explain about general and show examples
    print(e)
except Exception as e:
    print(e)
# else:
#     pass
# finally:
#     pass