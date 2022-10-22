def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#print(isprime(11))
sum=2
for m in range(3,2*10**6,2):
    if isprime(m):
        sum+=m
        
print(sum) 