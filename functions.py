
#Function is a block of code that performs a specific task

# ex:-Dish Washer
#
# Dirty dishes(i/p)
# return value(o/p)
#
# Function:wash_dishes
# 1.Add water/detergent
# 2.wash dishes
# 3.Dry them

#functions make ur code more modular and readable

#problem:you are given two lists of numbers and you need to find total of each of these list

#without function
#tom_exp_list=[2100,3400,4500]
#john_exp_list=[200,500,700]

#total=0
#for item in tom_exp_list:
 #   total=total+item
#print("Tom's total expense: ",total)

#for item in john_exp_list:
 #   total=total+item
#print("johns total expense: ",total)

#above code is using same code for multiple times if u have 100 expns list then its difficult so we use in function,we can encapsulate in function
#with function

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


