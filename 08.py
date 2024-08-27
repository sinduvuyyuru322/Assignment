#string is as sequence of charectors enclosed with single quotes or double quotes
#string slicing :To get a part of string using
#index gives the location of given cha
first_ind = input()
print(first_ind[2])

#str_var[startindex:endindex]
#extendedslicing : str_var[startindex:endindex:step]
print(first_ind[1:5])
print(first_ind[0:len(first_ind):1])

# mathamatical operator
#concationation : Add one str to another str
#reptation : we can print any number of times we want by reptation
send_ind  = input()
concat = first_ind +send_ind
reptate_1 = first_ind *5
reptate_2 = send_ind *5
print(concat)
print(reptate_1)
print(reptate_2)
print(reptate_1 +" " +reptate_2)

#str methods 
#find() we get the index of value
# if given valur or char is not found it display the -1 as output 
#rfind() from the right side 
#lfind for the left side 
#index() it also gives index as result 
#if the give char or value is not found it display the exception error

print(first_ind.rfind("s"))
print(first_ind.find("s"))

print(send_ind.index("s"))
print(send_ind.rindex("s"))

#count() To count how many number of times the given input is presented
#strip() Removes the unwanted spaces (start and end) and also removes the given value at start and end
#split() It return the seperation of given value

print(first_ind.count("p"))
print(send_ind.count("a"))

print(first_ind.split())
print(send_ind.split("a"))

print(first_ind.strip())
print(send_ind.strip("a"))

len_1 = len(first_ind)
for i in range(len_1):
    if first_ind[i] == "s":
        a = first_ind[:i+1]
        print(a+"prameela")
    elif i==3:
        a = first_ind.split(first_ind[i])
        print(a)
    else:
        a = first_ind.count("d")
        print(a)



