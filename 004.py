list = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i*j
        reverse = int(str(product)[::-1])
        if product == reverse:
            list.append(product)
list.sort()
print(list[-1])
