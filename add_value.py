# add 5 to each item in numbs and numbs 2

numbs = [5,4,6,7,10]
numbs = [i+5 for i in numbs]
print(numbs)


numbs2 = [1,2,3,4,5]
print(id(numbs2))
for i,s in enumerate(numbs2):
    numbs2[i]=s+5  # the loop variable in for loop is a copy of the element.
    # enumerate return index & value of an  iteratable , numbs2[i] allows accessing the element in numbs2
print(id(numbs2))
print(numbs2)
