def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total
tom_exp_list=[2100,3400,4500]
john_exp_list=[200,500,700]
toms_total=calculate_total(tom_exp_list)
john_total=calculate_total(john_exp_list)
print("tom's total expenses :",toms_total)
print("john's total expenses ",john_total)