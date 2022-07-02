import math
import logging

# My old code which I found.

def input_valid_num():
    num_of_p = -1
    valid = False
    while valid is False:
        try:
            num_of_p = int(input("Enter the number of primes you want to know: "))
            valid = True
            if num_of_p < 0: 
                print("The number should be natural!")
                valid = False
        except ValueError:
            print("n is not an integer!")
    return num_of_p


def is_prime(num):
    check_before = int(math.sqrt(num))
    for factor in primes:
        if factor >= check_before + 1:
            return True
        if num % factor == 0:
            return False
    return True


def find_primes(num_of_p):
    global primes
    primes = []
    cnt = 0
    cur = 2
    while cnt != num_of_p:
        if is_prime(cur):
            primes.append(cur)
            cnt += 1
        cur += 1


def main():
    num_of_primes = input_valid_num()
    find_primes(num_of_primes)
    print(primes)


if __name__ == '__main__':
    # Logging
    lvl = logging.DEBUG 
    fmt = '%(lineno)s: [%(levelname)s] %(msg)s'
    logging.basicConfig(level = lvl, format = fmt)

    main()
