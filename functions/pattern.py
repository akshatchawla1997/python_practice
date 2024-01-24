"""Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
        *
        **
        ***
if input is 4 then it should print

        *
        **
        ***
        ****
"""
def pattern(n=3):
    for i in range(n+1):
        print(i*"*", end="\n")

pattern()
pattern(5)