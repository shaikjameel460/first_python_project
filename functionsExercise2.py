#Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
#rectangle area=length*width
#If no shape is supplied then it should take triangle as a default shape

def calculate_area_shapetype(dimension1,dimension2, shape="triangle"):
    if shape=="triangle":
         area=dimension1*dimension2
    else:
        area = (1/2) * dimension1 * dimension2
    return  area



#area =calculate_area_shapetype(2,4,)
#print("area of triangle is:",area)
area=calculate_area_shapetype(4,6,shape="rectangle")
print("area of triangle is:",area)