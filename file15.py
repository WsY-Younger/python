
import os

# 获取到当前文件夹的路径(绝对路径)

print('Please input the string you want to save:')

n = input()

import json
def write(data, path):
  resultBytes = json.dumps(data)
  print('Start writing...') 
  with open(path, 'wb') as f:
    f.write(resultBytes)
  print('Write over')

def read(path): 
  print('Start reading...')
  with open(path, 'rb') as f: 
    text = json.load(f)
    print(text)
  print('Reading over')


write(n, 'c.txt')
print('-----------')
read('c.txt')