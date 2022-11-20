"""learning what is TDD and how to work that way"""
"""The func gets string and number and returns the string after the number added to each letter (ASCII Code) """
"""The check function checks the input and if the output is right"""

def check(stringA,stringB,num):
    flag= True
    while num>=26:
        num-=26
    if len(stringA)==len(stringB):
        for i in range(0,len(stringA)):
            if isinstance(stringA[i],str) and isinstance(stringB[i],str):
                flag=True
            else:
                return False
            if (ord(stringA[i])+num)!=ord(stringB[i])and(ord(stringA[i])-26+num)!=ord(stringB[i]):
                return False
    if flag:return True
    else:return False




def func(stringA,num):
    while num>=26:
        num-=26
    stringB=''
    for i in range(0,len(stringA)):
        res=ord(stringA[i])+num
        if ((stringA[i].isupper()) and res-64>26) or (stringA[i].islower()and res-96>26):
            res=res-26
        stringB+=chr(res)
    return stringB

print(check("ABc",func("ABc",27),27))
print(func("ABc",27))