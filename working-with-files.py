import os
from subprocess import call

print(os.getcwd())

# cmd = ["man", "man"]
# call(cmd)

# f = open('test.txt','r')
# f.close()

# print(f.name)
# print(f.mode)
# with open('test.txt','r') as f:

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # f.seek(0)
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)


    # f_contents = f.readlines()

    # f_contents = f.readline()
    # print(f_contents, end='')
    #
    # f_contents = f.readline()
    # print(f_contents, end='')

    # for line in f:
    #     print(line, end='')

with open('screen.png','rb') as rf:
    with open('screen_copy.png','wb') as wf:
        for line in rf:
            wf.write(line)
    # pass for only cration file analogy to touch
    # f.write('Test')
    # f.seek(0) not many uses on w mode show
    # f.write('Test')

