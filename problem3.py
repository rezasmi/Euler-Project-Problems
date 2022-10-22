def is_prime(n):
    for i in range(2,int(n**0.5)+1):  
        if n%i==0:
            return False
    return True
                
num=[]
for i in range(2,int(600851475143**0.5)+1):
    #print('i is '+str(i))
    if 600851475143%i==0 and is_prime(i):
        num.append(i)
#print(num)
print(max(num))
