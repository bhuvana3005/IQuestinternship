'''
data structure:
1.lists:[]
2.tuples:() even if we don't use brackets it is considered as tuple
3.sets:{elements}
4.dictionaries:{key:value}
'''
a=[]
b=()
c={1,2,3}
d={1:1, 2:b}
e=1,2,3
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("    ")
print("next topic")
print("   ")
'''define a list
1.define using []and inbuilt func"list"
2.can create empty list
3.access elements using index func and slicing operator
4.reverse list using -1 as step in slicing operator
5.can accept duplicate values
6.can accept different type of data in a single hence it is heterogenous
7.it is mutable so we can't store fixed objects '''

a=[1,2,3,1,1,'abc',4]

b=[]
c=list(range(6))
e=[7,5,4,3,3,4,3]
print(a)
print(b)
print(c)
print(a[0])#index
print(c[0:4:2])#slicing operator
print(c[::-1])#reverse list
a[2]='bbb'
print(a)
print(len(a))
print(a.count(1))

'''iterate over list'''
for x in a:
    print(x)
'''performing some function or operation on lists''' 
a.append(500)#adding the value to the end of the list 
print(a) 
a.append(c)#adding entire list to  end of the list
print(a) 
a.insert(4,400)#inserting a value to list
print(a)
a.insert(5,b)#inserting object to certain index
print(a)
d=c.copy()#copying one object to another
print(d)
print(a[10])
a.extend(c)#adds all elements of c to a seperate elements
print(a)
print(a[12])
a.pop(5)
print(a)
e.sort()
print(e)
a.pop()
print(a)
a.reverse()
print(a)
e.remove(7)
print(e)


print('******************************')
x=[1,2,3,4,5,6,7,8,9,10]
for y in range(len(x)):
    if(x[y]%2)==0:
        b.append(x[y])
print('normal comprehension',b) 
p=[y for y in x if y%2==0]
print('list comprehension:',p)  