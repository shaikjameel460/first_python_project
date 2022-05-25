#write a program that asks user to enter dish name and it should print which cuisine is that dish

indian=["samosa","Daal"]
chinese=["fried rice","Egg roll"]
italian=["pizza","pasta",'risotto']

dish=input("enter a dish name :")


if dish in indian:
    print("the dish is indian")
elif dish in chinese:
    print("the dish is chinese")
elif dish in italian:
    print("the dish is italian")
else:
    print("Based on little knowledge i have no idea which cuisine is ", dish)


