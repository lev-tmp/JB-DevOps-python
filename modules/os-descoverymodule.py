import os
from datetime import datetime
# print(dir(os))

print(os.getcwd())
os.chdir('/Users/lev/Desktop')
print(os.getcwd())

## directories :
# print(os.listdir())
# os.mkdir('os-demo-1')
# os.makedirs('os-demo-1/Sub-dir-1')
# os.removedirs('os-demo-1/Sub-dir-1')
# os.rename('python2- lev.pptx', 'python2-lev.pptx')

## files stats
# print(os.stat('python2-lev.pptx'))
# print(os.stat('python2-lev.pptx').st_size)
# print(os.stat('python2-lev.pptx').st_mtime)
# mod_time = os.stat('python2-lev.pptx').st_mtime
# print(datetime.fromtimestamp(mod_time))
# mod_time = os.stat('python2-lev.pptx').st_mtime
# print(datetime.fromtimestamp(mod_time))


## Walking throught directories and files :
# for dirpath, dirname, filename in os.walk('/Users/lev/Desktop'):
#     print('Current path',dirpath)
#     print('Directories:', dirname)
#     print('Files:', filename)
#     print()

## Access to env variebles :
# print(os.environ.get('HOME'))

# path to file withou join
# file_path = os.environ.get('HOME') + 'test.txt'
# print(file_path)

# path to file with join
# file_path = os.path.join(os.environ.get('HOME'),'test.txt')
# print(file_path)

## some usefull os.path :
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.isdir('/Users'))
# os.path.isfile()
# split file and extention :
# print(os.path.splitext('/tmp/test.txt'))
