#to create tuple 
tuple_1 = ()
print(type(tuple_1))
tuple_2 = (1,)
print(type(tuple_2))


#To unpack the tuple
# variables in left side should be equal to the values 
tuple_one = (20,"sindu",5.0,True)
(t1,t2,t3,t4) = tuple_one
print(t1)


#add an element to the tuple 
add_t =tuple(input())
list_1 = list(add_t)
list_1.append(input())
print(tuple(list_1))


#most frequent element 
tuple_ele = input()
print(tuple_ele.count(input()))

#tuple into a string 
tuple_str = tuple(input())
print(tuple_str)
str = ""
for item in tuple_str:
    str+=item
print(str)
