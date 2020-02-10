print('please input the N')

n = input()

def fact(n):
    
    if n==1:
        return 1
    if n==0:
        return 1
    return fact(n-1) + fact(n-2)
    
    

print(fact(int(n)))