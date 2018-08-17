print("***********************LIST*******************************")
#1
n=int(input("enter no.of elements you want to insert in list "))
l1=[ ]#create empty list
for i in range (n):
            b=input()
            l1.append(b)
print('list1 =' ,l1)

#2
#Add the given list to above created list: ['google','apple','facebook','microsoft','tesla'] 
l2= ['google','apple','facebook','microsoft','tesla']
l1.extend(l2)
print('new list1  =' ,l1)

#3
l3=['red','orange','green','blue','red','white','red','pink','green']
print('list3 =', l3)
c=l3.count('red')
print("count of 'red' is ",c)

#4
l4=[4,56,24,11,89,123,54,76,32]
print('list4 =',l4)
l4.sort()
print('Sorted list4 =',l4)

#5
A=[4,12,56,90]
B=[5,18,80]
C=[ ]
C=A+B
C.sort()#merge A and B to new list C
print('Sorted list C after merging list A and list B =',C)

#6
#cout even and odd numbers in list
l8=[34,45,12,17,99,567,80,77,89,80,43]
o=0#counts odd numbers
e=0#counts even numbers
for i in range (len(l8)):
    if(l8[i]%2==0):
        e+=1
    elif(l8[i]%2!=0):
            o+=1
print('no.of even numbers in list  = ', e)
print('no.of odd numbers in list  = ', o)

print("***********************TUPLES*******************************")

#1
t1 = ('B',9,'p',67,'w')
print('tuple = ',tuple(t1))
# Reversed the tuple
Rt1 = reversed(t1)
print('reversed tuple =', tuple(Rt1))

#2
t2=(1,5,2,9,6,7)
print(tuple(t2))
print('largest element in tuple = ',max(t2))
print('Smalest element in tuple = ',min(t2))

print("***********************STRINGS*******************************")

#1
s1="Learning Python"
Us1=s1.upper()
print(Us1)

#2
s2='123454'
print(s2.isdigit())
s2='123ABC'
print(s2.isdigit())

#3
s3="Hello World"
Rs3=s3.replace('World','Asmita')
print(Rs3)

    


            





