import os

# 获取到当前文件夹的路径(绝对路径)
currentPath = os.path.abspath('.')

print('Please input the string you want to search in file:')

filename = input()

def printRightFileInfolder(folder):
  # os.path.isfile 的参数必须是绝对路径，所以这里只能先用绝对路径，后面再改成相对路径
  files = [x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder,x)) and filename in x]
  for f in files:
    # 先得到绝对路径
    absolutePath = os.path.join(folder,f) 
    # 删除掉 currentPath 得到相对路径
    
    relativePath = absolutePath[len(currentPath) + 1:]
    # 打印相对路径
    print(relativePath)
    print(absolutePath)
  
  # os.path.isfile 的参数必须是绝对路径，所以这里只能先用绝对路径，后面再改成相对路径
  folders = [x for x in os.listdir(folder) if os.path.isdir(os.path.join(folder, x))]
  # 如果当前目录下没有子文件夹，函数就返回退出 
  if len(folders) == 0: 
    return
  for f in folders: 
    folderPath = os.path.join(folder, f)
    # 对于子文件夹，递归调用自身
    printRightFileInfolder(folderPath)

printRightFileInfolder(currentPath)

