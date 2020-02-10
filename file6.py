import os
import sys

sys.setrecursionlimit(1000000)
# # 获取到当前文件夹的路径
# currentPath = os.path.abspath('.')

# print('current path is %s' % currentPath)

# # 根据当前文件夹的路径生成新文件夹的路径

# createdPath = os.path.join(currentPath, 'abTest')

# print('The new path is %s' % createdPath)

# # 根据生成的文件夹的路径，创建新的文件夹

# os.mkdir(createdPath)

# nowname = os.path.join(currentPath, 'cdTest')

# os.rename(createdPath, nowname)

# print('Create new path successful')

# names = os.listdir('.')
# print(names)

def printRightFileInfolder(folder):
  files = [x for x in os.listdir(folder) if os.path.isfile(x) and 'a' in x]
  for f in files:
    print('%s/%s' % (folder, f))
  folders = [x for x in os.listdir(folder) if os.path.isdir(x)]
  if（len(folders) == 0):
    return
  for f in folders: 
    printRightFileInfolder(f)

printRightFileInfolder('.')