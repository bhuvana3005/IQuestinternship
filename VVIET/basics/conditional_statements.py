''''a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
if a>b and a>c:
      print("a is greatest")
elif b>a and b>c:
         print("b is greatest")
else :
   print("c is greatest")            


a=100
b=100
c=20
if a>=b and a>=c:
        print("a is greatest")
elif b>=a and b>=c:
         print("b is greatest")
else :
    print("c is greatest")'''
    
'''for x in range(1,7,2):     
    print(x,end=" ")'''
'''
    *
    **
    ***
    ****
    *****'''
for a in range(0,5):
    for b in range(0,a+1):
        print("*",end=" ")
    print("  ")
'''
     *****
     ****
     ***
     **
     *'''
n=6
print("  ")
for x in range(1,n):
    for y in range(x-1,n-1):
        print("*",end=" ")
    print("  ")
'''
*******
 *****     
  ***
   *  '''
# pyramid star pattern
n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2*i - 1):
        print('*', end='')
    print() 
    


           
'''n = int(input("Enter length of Fibonacci series: "))
num1 = 0
num2 = 1
next_number = 0
count = 1

for count in range(n):
    print(next_number, end=" ")
    count += 1
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
print("               ")'''




num=int(input("enter a number"))
factorial=1
while(num < 0) :
    print("enter a valid number")
    num=int(input("enter a number"))
if num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)         


for x in range(8):
    if x%2==0:
        print(x*2)
        continue
    else:
        print(x)













