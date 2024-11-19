"""def function(dict_in,dict_prise):

    n = int(input())
    for i in range(n):
        function_1(dict_in)
    count = 0

    for i,j in dict_in.items():
        for a,b in dict_prise.items():
            if i == a:
                count+=int(j)*int(b) 
    return count
def function_1(dict_in):
    dict_in[input()] = input()


dict_in = eval(input())
dict_prise = eval(input())
a = function(dict_in,dict_prise)
print(a)



def function(seq_1):
    import random
    num = random.randint(1,100)
    if int(seq_1) == num:
        print("congragulations")
    elif int(seq_1) < num:
        print("Your number is less than given guess")
    elif int(seq_1) > num:
        print("Your number is greater than guess")

seq = input()
function(seq)"""
a = {2,3,4}
print(max(a))