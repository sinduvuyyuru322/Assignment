#write a python program to add a key to a dictionary?

new_dict = dict()
new_dict[input()] = input()
print(new_dict)


#Write a python program to check wether the given value is present in the given dictionary are not?

sec_dict = eval(input())
values_in = sec_dict.values()
a = input()
if a in values_in:
    print("Is present")
else:
    print("Not present")


#write a python script to print a dict where the keys are thers num b/w 1 and 15 and the values are the
#square of the key?

empty_dict = dict()
for i in range(1,15+1):
    empty_dict[i] = i*i 
print(empty_dict)

#write a python program to create a dict from the string?
str_a = input()
s = ""
dict_a = {}
for i in str_a:
    if i not in s:
        count_b = str_a.count(i)
        dict_a[i] = count_b 
        s+=i
print(dict_a)


#write a python program to combine two dict by adding values of comman keys?

dict_1 = eval(input())
dict_2 = eval(input())
dict_key1 = dict_1.keys()
dict_keys2 = dict_2.keys()
for i in dict_key1:
    if i in dict_keys2:
        print(dict_1[i]+dict_2[i])

#write a python program to merge two python dict?

dict_1.update(dict_2)
print(dict_1)

#write a python program to sort dict by keys or values?
sort_dict = eval(input())
get_items = sort_dict.items()
print(dict(sorted(get_items)))


