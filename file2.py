import os

# 获取到当前文件夹的路径
currentPath = os.path.abspath('.')

# 根据当前文件夹的路径生成新文件夹的路径

createdPath = os.path.join(currentPath, 'abTest')
os.rmdir(createdPath)