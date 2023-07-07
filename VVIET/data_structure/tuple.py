'''
1.define using ()and inbuilt func"tuple"
2.can create empty list
3.access elements using index func and slicing operator
4.reverse list using -1 as step in slicing operator
5.can accept duplicate values
6.can accept different type of data in a single hence it is heterogenous
7.it is not mutable so we can store fixed objects
'''
a=(1,2,3,4,5,'abs',1)
b=tuple(range(10))#can store diff data types 
c=()
d=(1,2,3,'a')
print(a)
print(d)
print(type(a)) 
print(type(b))
print(type(c))
print(a[4])#index
print(a[1:5:2])#slicing operation
print(b[::-1])#reverse
print(len(b))#length of object
print(a.count(2))
'''iteration over tuples'''
for x in a:
    print(x)
print('  ')    
'''performing diff operation on tuples'''
a.index(4,0,5)
print(a)  
'''print even numbers in a given tuple'''

x=(1,2,3,4,5,6,7,8,9,10)
for y in range(len(x)):
    if(x[y]%2)==0:
        print(x[y])
'''z=(y for y in x if y%2==0)
print('tuple comprehension',z)''' 
 
print(10 not in a) 

    