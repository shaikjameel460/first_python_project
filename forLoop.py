#problem

#store monthly expenses in a list and find out total expenses for all months

exp=[2340,2500,2100,3100,1800,1600,2900]

#traditional approach
# total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]+exp[5]+exp[6]
# print(total)

#doing same thing using for loop

total=0

for item in exp:
    total= total+item
print(total)



