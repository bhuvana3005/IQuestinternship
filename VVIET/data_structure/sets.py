'''
1.define using {}and inbuilt func"set"
2.can create empty list
3.can't access elements using index func and slicing operator
4.can't reverse list using -1 as step in slicing operator
5.can't accept duplicate values
6.can accept different type of data in a single hence it is heterogenous
7.it is not mutable so we can store fixed objects
'''
a={1,2,3,4,5,'abs',1}
b=set(range(10))
c={}
d={1,2,3,'a'}
print(a)
print(d)
print(c)
print(type(a)) 
print(type(b))
print(type(c))
#print(a[4])#index
#print(a[1:5:2])#slicing operation
#print(b[::-1])#reverse
print(len(b))#length of object
#a.index(0)
#print(a)
'''iteration over sets'''
for x in a:
    print(x)
print('  ')    
'''performing diff operation on sets'''
  
'''print even numbers in a given sets'''

''''x={1,2,3,4,5,6,7,8,9,10}
for y in range(len(x)):
    if(x[y]%2)==0:
        print(x[y])'''

