import pickle


f = open('/Users/a/Desktop/wsy2/a.txt','rb')
d = pickle.load(f)
print(d)
f.close()