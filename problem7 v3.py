def is_prime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True

count=0     

for i in range(2, 100000000):
    if is_prime(i)==True: 
        print (i) 
        count+=1
    elif count==10001:
        break 
    
print(count)


