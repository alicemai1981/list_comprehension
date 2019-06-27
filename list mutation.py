#use += operator to add element to list
alist =['a', 'b', 'c', 'd']
print(id(alist))
alist +=['e']
print(id(alist))
print(alist)
# use + to add element to list
blist =['a', 'b', 'c', 'd']
print(id((blist)))
blist = blist +['e']
print(id(blist))
print(blist)



