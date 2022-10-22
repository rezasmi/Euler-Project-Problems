def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

seen = 0
n = 1
while seen < 10001:
    n += 1
    if is_prime(n):
        seen += 1

print(n)