def iseven(n):
    if n%2==0:
        return True
    else:
        return False
a=1
b=2
sum = 0
while (a<4*10**6):
    if iseven(a):
        sum=sum+a
    c=a+b
    a=b
    b=c

print(sum)
    
