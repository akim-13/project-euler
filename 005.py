primes_mult = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

ans = primes_mult * 2 * 2 * 2 * 3

for i in range(2, 21):
    print(f'{ans} % {i} == {ans % i}. Remainder is zero: {ans % i == 0}')

print()
print(ans)
