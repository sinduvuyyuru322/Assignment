#write a program which will find all numbers which are divisable by 7 but not a mutiple of 5,between 2000 and 3200.
#the numbers obtained should be printed in a comma-seperated 
first_value = 2000
sec_val = 3200 
for each in range(first_value,sec_val+1):
    if each % 7 == 0 and each%5 != 0:
        print(each,end=",")


#with a given integral number n, write to generate a dictionary that contain(i,i*i) such that is an integral number b/w
#1,n.and then the program should print the dict.
dic_item = int(input())
dec_dict = {}
for item in range(1,dic_item+1):
    dec_dict[item] = (item*item)
print(dec_dict)


#write a program which accepts a sequence of comma-seperated numbers from console and generate a list and tuple which contains every number
a = input().split(",")
list = []
for i in a:
    list.append(i)
print(list)
print(tuple(list))


#write a program that accept a comma seperated sequence of words as input and print the words in a commaseperated
#sequence after sorting them alphabetically,
word = input().split(",")
print(sorted(word))



#write a program that accept the sentence and calculate the numbers and digits.
str_num = input()
letter = 0
number=0
for each in str_num:
    if each.isalpha():
        letter+=1

    elif each.isdigit():
        number+=1 
print("LETTER" +" "+str(letter))
print("DIGIT" +" "+str(number))


#write a program that accepts a sentence and calculate the number of uppercase and lowercase letters.

uc_lc = input()
upper = 0
lower = 0
for each in uc_lc:
    if each.isupper():
        upper+=1 
    elif each.islower():
        lower+=1 
print("UPPERCASE" +" "+ str(upper))
print("LOWERCASE" +" "+ str(lower))


#write a program that computes the next amount of the bank account based a transaction log from consoleinput
#the tansaction log format is shown as following:D 300 w200 

a = input().split()
count = 0
for i in range(len(a)):
    if a[i] == "D":
        count+=int(a[i+1])
    elif a[i] == "W":
        count-=int(a[i+1])
print(count)
