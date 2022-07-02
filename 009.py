import math
for a in range(1, 9999):
    for b in range(1, 9999):
        sum_of_sq = a**2 + b**2
        c = math.sqrt(sum_of_sq) 
        if c.is_integer() and a+b+c == 1000:
            print(a, b, c)
            print(a*b*c)
            quit()
