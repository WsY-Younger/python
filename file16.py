

import json

dic = {
  'name': 'John',
   'age': '20'
}

string = json.dumps(dic)

print(string)

with open('c.txt', 'w') as f:
    f.write(string)
print('Write over')