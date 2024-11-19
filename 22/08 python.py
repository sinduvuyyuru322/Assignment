"""# variable is nothing but a container
#object in general anything that can be assign to a variable
a = int(input("enter the value:"))
b = int(input("enter the value:"))
c = input()
d = input()
print(a)
print(b)

#Arthemetic oparations: performs all simple mathematic operations(+,-,*,%,/,//,*)
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(a**b)
print(id(a))

#logical operater:and, or, not 
print(a==10 and b==20)
print(a==10 or b==20)
print(a!=10)

#Relational operater: <,>,<=,>=,=!
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)
print(a!=b)


#identity operater: It is comparative operater (is, isnot)

print(a is b)
print(a is not b)

#Menbership opertor: To check it present in or not (in or not in)
print(c in d)
print( c not in d)


#assignment operater: to assign the value (=)
print(a>=b)

#to fine the keywords
import keywords
print(keywords.kwlist)

#ACII values 
#to find the unicode value of a cha 
print(ord("A"))
#to find the cha with given unicode 
print(chr(120))"""

a = "sinduvuyyuru"
b = "aeiou"
for i in a:
    if i in b:
        v = a.split(i)
        print("@".join(v))
        break;
