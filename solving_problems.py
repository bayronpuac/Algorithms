# Write a function power() given value a and exponent b will compute a^b 
# It would be silly to have the functuon say return a^b, we won't learn anything

def power(value, exponent):
    #What is 2 ^ 3?
    #2 * 2 * 2

    # if exponent == 1:
    #     return value
    # if exponent == 2:
    #     return value * value
    # if exponent == 3:
    #     return value * value * value

    if exponent < 0:
        exponent *= -1
        value = 1 / value


    if exponent == 0:
        return 1
    
    return value * power(value, exponent - 1 )

print(power(4, 2))