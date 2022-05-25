#global vs local variables
total=0 #Global variables
def sum(a,b=0):
    total=a+b #local variables
    return total
n=sum(5)   #positional Arguments(Need to check)
print("inside the function",n)
print("outside the function",total)

#default Arguments

#if b is not assigned we can pass default value would be zero

#if we pass default variable value it will take what we pass in function



