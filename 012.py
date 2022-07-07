import math

def find_triangle_number(num):
    triangle_num = 0
    while num > 0:
        triangle_num += num
        num -= 1
    return triangle_num


def find_divisors(num):
    num_of_divisors = 1
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            num_of_divisors += 2

    return num_of_divisors


num = 1
while True:
    triangle_num = find_triangle_number(num) 
    num_of_divisors = find_divisors(triangle_num)
    print(triangle_num, num_of_divisors)
    if num_of_divisors > 500:
        print('\nAnswer:')
        print(triangle_num)
        quit()
    num += 1
