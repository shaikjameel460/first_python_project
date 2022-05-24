# we all go to grocery story,we make list

item1 = "bread"
item2 = "jam"
item3 = "Apple"
item4 = "Brinjal"

# above we are creating lot of variables for different items,to solve this we create a list

items = ["bread", "Jam", "Apple", "Brinjal"]
print(items)
x = items[0]
print(x)
# now i want to change my item and insted of jam i need pasta,now i do my modify my list

items[0] = 'Pasta'
print(items)

# Now how to do acess range of elements

range = items[0:2]

print(range)

z = items[-1]
print(z)

# now need to add more items we use append function

items.append("butter")
print(items)

# now butter needs to be added after Pasta

items.insert(1,"butter")
print(items)

mylist=["Perfume","Brush","Paste"]
mywifelist=["Shampoo","saop","facial cream"]
Itemslist=mylist+mywifelist
print(Itemslist)
print(len(mylist))

#if you have long list and u don't need to read long list we have "in" Operator

x="Brush" in mylist
print(x)
