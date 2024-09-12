#given a tuple containing nested tuple,write a python program to flatten it into a single tuple
tuple_1 = eval(input())
lis = []
for i in tuple_1:
    if str(i).isdigit():
        lis.append(i)
    else:
        a_list = list(i)
        for i in a_list:
            lis.append(i)
print(lis)
    
#write a python program to sort a tuple based on the second element of each tuple 
first_in = eval(input())
li = []
for i in first_in:
    li.append(i[1])
a = sorted(li)
empty_lis = []
for i in a:
    for j in first_in:
        list_j = list(j)
        if list_j[1] == i:
            if j not in empty_lis:
                empty_lis.append(j)
print(tuple(empty_lis))

