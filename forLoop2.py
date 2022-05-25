#print 1 to 10 using range

for i in range(1,11):
    print(i)

#now monthly expense another exercis
#In our monthly expense example,print month number and expense and then in the end print total expense

exp=[2340,2500,2100,3100,1800,1600,2900]
total=0
#for i in range(len(exp)):
for i in range(0,7):
    print('Month: ',(i+1),'Expense: ',exp[i])
    total=total+exp[i]
    print(total)



#Problem:Search for lost car key in home and when found stop searching

Key_location="chair"
locations=["garage","living room","chair","closet"]

for i in locations:
    if i==Key_location:
        print("key is found in",i)
        break
    else:
        print("Key is not found in ",i)


#Print square of numbers between 1 to 5 except even numbers

for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)

#while statement

i=1
while i<=5:
    print(i)
    i=i+1

