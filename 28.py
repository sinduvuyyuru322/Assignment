#count the occurence of the char 
str_n = input()
str_c = input()
print(str_n.count(str_c))

# two str are anagram are not 
ana_1 = input()
ana_2 = input()
str = 0
if len(ana_1) == len(ana_2):
    for i in ana_1:
        if i in ana_2:
            str=str+1
        else:
            print("Not a anagram")
            break;
    if str == len(ana_1):
        print("Is a anagram")
else:
    print("Not a anagram")


# palindrome or not
pal_1 = input()
pal_2 = pal_1[::-1]
if pal_1 == pal_2:
    print("Is a palindrome")
else:
    print("NOt a palindrome")

#relace str space with given char
str_1 = input().split()
a = "a".join(str_1)
print(a)

# using replace 
rep_1 = input()
rep_old = input()
rep_new = input()
print(rep_1.replace(rep_old,rep_new))

#lower to upper 
a = input()
print(a.upper())

#lower case vowel to upper case
lower_vowel = input()
vowel_a = "aeiou"
b = lower_vowel
for i in vowel_a:
    if i in lower_vowel:
        c= b.replace(i,i.upper())
        b = c
print(b)

#seperste the char
sep_1 = input()
print(a.split())

#remove the blank spaces
blank_1 = input()
print(blank_1.strip())

#concatenate two str
con_1 = input()
con_2 = input()
print(con_2.join(con_1))

#concatenate two str with out join()
a = con_1+con_2
print(a)

#remove the repeated char from str

repchar_str = input()
a = ""
for i in repchar_str:
    if i not in a:
        a+=i 
print(a)

#check given is vowel or not
vowel_1 = input()
b = "aeiou"
c = "AEIOU"
if (vowel_1 in b) or (vowel_1 in c):
    print("Vowel")
else:
    print("Consonant")


#check isdigit
isdigit_1 = input()
if a.isdigit():
    print("Is digit")
else:
    print("Not is digit")

#delete vowels in a string

del_vol = input()
a = "AEIOU"
b = "aeiou"
empty = ""
for i in del_vol:
    if (i in a) or (i in b):
        pass;
    else:
        empty+=i 
print(empty)

#count the occurrence of vowels and con
con_vow = input()
a = "aeiou"
b = "AEIOU"
empty = ""
count = 0
sum = 0
for i in con_vow:
    if (i in a) and (i not in empty):
        count_vo = con_vow.count(i)
        empty+=i
        count+=count_vo
    elif (i not in a) and (i not in empty) and (i != " "):
        sum_con = con_vow.count(i)
        empty+=i
        sum+=sum_con
print("sum of vowels:"+" "+str(count))
print("sum of consonants:"+" "+str(sum))

#highest frequence cha of a str 
high_fre = input()
fre_char = input()
print(high_fre.count(fre_char))

#replace first occurrence of vawel with "-"
first_vowel = input()
a = "aeiou"
b = "AEIOU"
for s in range(len(first_vowel)):
    if (first_vowel[s] in a) or (first_vowel[s] in b):
        c_index = first_vowel[:s+1]
        rep_1 = c_index.replace(first_vowel[s],"-")
        print(rep_1+first_vowel[s+1:])
        break;



#using isdigit() method 
a= input()
if a.isdigit():
    print("It is is digit")
else:
    print("Not is digit")

#sum of integers in str 
a= input()
sum = 0
for i in a:
    sum+=int(i)
print(sum)

#non repeating cha 
non_rep =  input()
for i in non_rep:
    a = non_rep.count(i)
    if a > 1:
        pass;
    else:
        print(i)


# to find given char is digt or not
a = input()
if a.isdigit():
    print("It is digit")
else:
    print("It is not a digit")

#count the alphabets digits special cha
a = input()
b =0
c = 0
d =0
f = "@","!","#","$","%","^","&","*","?","/"
for i in a:
    if i.isdigit():
        b+=1
    elif i in f:
        c+=1

    else:
        d+=0
print(b)
print(c)
print(d)




        





