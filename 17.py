#print the square of each value
def first_seq(f):
    return int(f)*int(f)

first = ["1","4","3","7","5","2","9","8"]
l1 = map(first_seq,first)
print(list(l1))

#print revers of the function 

seq = "Learing python is very easy"
seq_1 = seq.split()
l1 = lambda seq_1:seq_1[::-1]
k = l1(seq_1)
a = ""
for i in k:
    a+=i+" "
print(a)

#print reverse of reverse str
y = ""
for i in k:
    y+=i[::-1]+" "
print(y)


#create a dictonary where the keys are tuple representing coordinates (x,y) and the values
#are city names.write a python program to print the city name

def function(dict_1,dict_2):
    for i,j in dict_1.items():
        b = eval(i)
        if b == dict_2:
            print(j)
#{"(40.7128, -74.0060)": "New York", "(34.0522, -118.2437)": "Los Angeles"}    
dict_1 = eval(input())
dict_2 = eval(input())
function(dict_1,dict_2)

#((1,2),(3,1),(5,1))
#write a program to sort a tuple based on the second element of each tuple
sec_tup = eval(input())
lam_sec = sorted(sec_tup,key = lambda sec_tup : sec_tup[1])
print(tuple(lam_sec))


#write a python program to find the min and max elements in a tuple of integers
a = eval(input())
print(min(a))
print(max(a))

#given a tuple contaning nested tuple write a python to flatten it into a single tuple
tup = eval(input())
li = []
for i in tup:
    if str(i).isdigit():
        li.append(i)
    else:
        for j in list(i):
            li.append(j)
print(tuple(li))
    