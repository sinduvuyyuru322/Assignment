#conditional statements it allows you to execute a block of code only when the 
# specific condition is TRUe if,elif,else
#if is used to exicute a block of code
#elif is used to have multiple conditional statements in b/w if and else
#else when if and elif statements are false
a = input()
b = input()
if a == "banking" or a == "BANKING" or a == "Banking":
    print("Show same opetions related to banking")
    if b == "Balance enquiry":
        print("show the 2 digit box")
    elif b == "chashwithdrow":
        print("s")
    elif b == "Mine statement":
        print("Print the statement")
    
elif a == "PINCHANGE" or a == "Pinchange" or a == "pinchange":
    print("Shoe th e pin change opetion")
elif a == "WITHDROW" or a== "withdrow" or a=="Withdrow":
    print("Amount in the account")
else:
    print("ERROR")
# iterative Statements
#For loop
#It iterates over each items of the sequence of charater dequence of number
# while Loop
# It excuite a block of code fr several time untile the condition remain False 
# (or) as long as code is True
#range: it generates a sequence of code based on it's rsnge

first_1 = input()
for each_char in range(len(first_1)):
    print(each_char)

fist_whi = int(input())
size = 0
while size < fist_whi:
    print(size+3)
    size+=1
import keyward
print(keyword.kwlist)

#trasfor statements 
# break it stopes the execution of block of code
# continue It skips the remaining statements in the current iteration and begion the next iteration
# pass It is used as a syntactic placeholder, when it executed nothing
a = int(input())
for i in range(a):

    if i==5:
        break
    elif i <5:
        print(i)
    elif i >5 and i<9:
        continue
    else:
        pass


