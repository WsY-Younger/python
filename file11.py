import pickle

d = dict(name ='bob',age ='20')

f = open('/Users/a/Desktop/wsy2/a.txt','wb')
pickle.dump(d,f)
f.close()

f = open('/Users/a/Desktop/wsy2/a.txt','rb')
d = pickle.load(f)
print(d)
f.close()