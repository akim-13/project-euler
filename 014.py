max_chain_len = -1
starting_num = -1
for i in range(2, 1000000):
    print(i)
    n = i 
    chain_len = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        n = int(n)
        chain_len += 1

    if chain_len > max_chain_len:
        max_chain_len = chain_len
        starting_num = i

print(starting_num)
