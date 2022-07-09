one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4

ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8

twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6

hundred = 7
thousand = 8

_and = 3

singles = one + two + three + four + five + six + seven + eight + nine
eleven_to_nineteen = eleven + twelve + thirteen + fourteen + fifteen + sixteen + seventeen + eighteen + nineteen
tens = twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety

# 1-9
singles_one_to_hundred = singles*9
singles_one_to_thousand = singles_one_to_hundred*10
singles_in_hundreds = singles*100
## One is 1000
all_singles = singles_one_to_thousand + singles_in_hundreds + one

# 11-19
all_eleven_to_nineteen = eleven_to_nineteen*10

# 20-99
tens_under_hundred = tens*10 + ten
all_tens = tens_under_hundred*10

# 100-999
one_to_two_hundred = hundred*100
all_hundreds = one_to_two_hundred*9

# and
ands_from_one_to_two_hundred = _and*99
all_ands = ands_from_one_to_two_hundred*9

print(all_singles + all_eleven_to_nineteen + all_tens + all_hundreds + thousand + all_ands)
