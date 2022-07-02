primes = []
num = 600851475143 
while True:
    for i in range(2, num+1):
        if num % i == 0:
            num //= i
            print(num)
            primes.append(i)
            break
    if num == 1:
        break

print(primes)
