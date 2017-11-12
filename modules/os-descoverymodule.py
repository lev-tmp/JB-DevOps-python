import os
from datetime import datetime
# print(dir(os))

print(os.getcwd())

os.chdir('/Users/lev/Desktop')

# os.mkdir('os-demo-1')
# os.makedirs('os-demo-1/Sub-dir-1')
# os.removedirs('os-demo-1/Sub-dir-1')
# os.rename('python2- lev.pptx', 'python2-lev.pptx')

# print(os.stat('python2-lev.pptx').st_mtime)

# mod_time = os.stat('python2-lev.pptx').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.getcwd())
# print(os.listdir())

# for dirpath, dirname, filename in os.walk('/Users/lev/Desktop'):
#     print('Current path',dirpath)
#     print('Directories:', dirname)
#     print('Files:', filename)
#     print()

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'),'test.txt')
# print(file_path)

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# os.path.isdir() os.path.isfile()
# print(os.path.splitext('/tmp/test.txt'))

# print(dir(os.path))
print(dir(int))