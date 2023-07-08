def upper1(x):
    s1=""
    for y in x:
        if ord(x)>=97 and ord(x)<=122:
            s1+=chr(ord(x)-32)
        else: 
            s1+=x
    return s1

def lower1(x):
    s1=""
    for y in x:
        if ord(x)>=65 and ord(x)<=90:
            s1+=chr(ord(x)+32)
        else: 
            
            
            s1+=x
    return s1

def isupper1(x):
    for y in x:
        if ord(y)>=97 and ord(y)<=122:
            return False
        else: 
            continue
    return True
    
    def islower1(x):
    for y in x:
        if ord(y)>=65 and ord(y)<=90:
            return False
        else: 
            continue
    return True

def isalpha1(x):
    for y in x:
        if ord(y)>=65 and ord(y)<=122:
            return True
        else:
            return False
        
        def isdigit1(x):
    for y in x:
        if ord(y)>=48 and ord(y)<=57:
            return True
        else:
            return False
        
        def isalnum1(x):
    for y in x:
        if ord(y)>=48 and ord(y)<=122:
            return True
        else:
            return False
        
        def swapcase1(x):
    s1=""
    for y in x:
        if ord(y)>=65 and ord(y)<=90:
            s1+=chr(ord(y)+32)
        elif ord(y)>=97 and ord(y)<=122:
            s1+=chr(ord(y)-32)
        else:
            s1+=y
    return s1       

def capitalize1(st):
    s=""
    for x in range(len(st)):
        if x==0:
            if ord(st[0])<=122 and ord(st[0])>=97:
                s+=chr(ord(st[0])-32)
            else:
                s+=st[x]
        else:
            if st[x-1]==" ":
                if ord(st[x])<=122 and ord(st[x])>=97:
                    s+=chr(ord(st[x])-32)
                    continue
                else:
                    s+=st[x]
                    continue
            elif ord(st[x])>=65 and ord(st[x])<=90:
                s+=chr(ord(st[x])+32)
            else:
                s+=st[x]
    return s

def title1(input_str):
    result = ""
    capitalize1 = True

    for char in input_str:
        if ord(char) >= 97 and ord(char) <= 122:
            if capitalize1:
                char = chr(ord(char) - 32)
                capitalize1 = False
        elif char in [" ", "-", "_"]:
            capitalize1 = True
        result += char

    return result

