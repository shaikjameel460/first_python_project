text="ice cream"
print(text)
a=text[0]
print(a)
# if we want to replace character in string not possible
# strings are immutable in python
#print(text[0]='g')

#to get substring in string[indexing]
b=text[0:3]
print(b)
c=text[4:9]
print(c)
d=text[:3]
print(d)
e=text[4:]
print(e)

#single quotes/double quotes
x="hello"
y='hello'
#z='let's learn the python' # throws error bcoz quote ended at lets so use double quotation

z="let's learn the python"
print(z)


#u can use triple quotes when string need to go to new line

address='''1 purplestreet
newyork
dawakhana'''
print(address)


#Concatinating strings
s1="hello"
s2="world"
s3=s1+' '+s2
print(s3)

#Now join string with numbers it will throw error python doesn't know to club

place="total states in USA"
num=25
#print(place+num) # it throws error cannot

#important function str() very imp and used in anycase in python

s=str(num)
print(s)
print(place+s)
