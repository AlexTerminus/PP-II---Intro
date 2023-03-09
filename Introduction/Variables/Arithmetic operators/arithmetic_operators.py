number = 9.0        # Float number

division_result = number/2 # divide the number by two

division_remainder = number-division_result*2# get the argument of the division of the number by two

multiplication_result = division_result*2 # multiply the division result by 2

addition_result = division_remainder + multiplication_result# add the division remainder to the multiplication result

subtraction_result = number - multiplication_result# subtract the multiplication result from the initial number

floor_result = number / 2 # perform a floor division of number by 2

power_result = multiplication_result*3   # raise the multiplication result to the power of 3

print("result = " + subtraction_result+floor_result+power_result)
