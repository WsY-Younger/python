import os

# 获取到当前文件夹的路径
currentPath = os.path.abspath('.')

print('current path is %s' % currentPath)

# 根据当前文件夹的路径生成新文件夹的路径

createdPath = os.path.join(currentPath, 'abTest')

print('The new path is %s' % createdPath)

# 根据生成的文件夹的路径，创建新的文件夹

os.mkdir(createdPath)

print('Create new path successful')