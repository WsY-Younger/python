import os
files = [x for x in os.listdir('.') if 'py' in x]
print(files)
