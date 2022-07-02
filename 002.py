fibonacci_seq = [1, 2]
next_term = 0
while True:
    next_term = fibonacci_seq[-1] + fibonacci_seq[-2]
    if next_term > 4000000:
        break
    fibonacci_seq.append(next_term)

sum = 0
for term in fibonacci_seq:
    if term % 2 == 0:
        sum += term  

print(sum)

