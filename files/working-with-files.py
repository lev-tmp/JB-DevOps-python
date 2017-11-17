import os
# from subprocess import call

# print(os.getcwd())

## First option to work with file,
# not the best one !
# open file r - read, a - append, w - write to file , r+ - both read/write
# need close() expression, files descriptor etc.
# f = open('test.txt','r')
# print(f.name)
# print(f.mode)
# f.close()

## Context manager explanation auto close
# with open('test.txt','r') as f:
#     pass
# print(f.closed)
# print(f.read())

## read and print whole file :
# with open('test.txt','r') as f:
#     f_contents = f.read()
#     print(f_contents)

## read and print line by line file:
# with open('test.txt','r') as f:
#     f_contents = f.readlines()
#     print(f_contents)

## read and print single line, first one every time we call function readline will read next line (copy and show)
# with open('test.txt','r') as f:
    # f_contents = f.readline()
    # print(f_contents) # add end=''
    # f_contents = f.readline()
    # print(f_contents)

## Read extreamly long file: if we read at once, we can run out of memory
# with open('test.txt','r') as f:
#     for line in f:
#         print(line, end='')

## More control for reading , explanation of read buffer
# with open('test.txt','r') as f:
    # f_contents = f.read()
    # f_contents = f.read(100) # copy and explain
    # print(f_contents, end='')

## More contreol for big files with while and EOF condition in while loop, also f.tell() and f.seek()
# with open('test.txt','r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents)
    # print(f.tell()) # tell curent position in the file  ,show f.seek(0)
    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read) # without it infinite loop, by the end of the file it will return epmty string
                                          # and hit our while conditional

## Write to file, w flag.. let's create new file (use a flag to append)
# with open('test2.txt', 'w') as f:
#     f.write('Test') # double it and show f.seek() not common usefull in write mode (show with one letter R)

## Copy file or work with both read/write
# with open('test.txt', 'r') as rf, open('text_copy.txt', 'w') as wf: # in one line

# with open('test.txt', 'r') as rf:
#     with open('text_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)





