
def ej1(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

print(ej1(2,4))


def ej2(a):
    palabras = a.lower().split()
    return palabras[0][0] == palabras[1][0]


print(ej2('Hola HUela'))   


def lasuma20(a,b):
    return (a+b)==20 or a==20 or b==20

print(lasuma20(2,2))

#LEVEL 1---------------------------------------------------------
def ej1_lvl1(mystring):
    mystringlist=list(mystring)
    mystringlist[0]=mystringlist[0].upper()
    mystringlist[3]=mystringlist[3].upper()
    return ''.join(mystringlist)

print(ej1_lvl1('macdonald'))


def ej2_lvl1(mystring=''):
    mylista=mystring.split()
    mylista.reverse()
    #usando join convierto la lista en un string de salida
    print(' '.join(mylista))
    
ej2_lvl1('Hola mi nombre es Yoda')

def ej3_lvl1(n):
    n=abs(n)
    return (100+10 >=n>=100-10 or 200+10 >= n >= 200-10)

ej3_lvl1(209)


#LEVEL 2____________________________

def ej1_lvl2(*args):
    i=0
    args=list(args[0])
    while i < len(args):
        if args[i] == 3:
            if args[i+1] == 3:
                return True
        i+=1
    else:
        return False

print(ej1_lvl2([2,3,8,5,1]))

def ej2_lvl2(text):
    text=list(text)
    texto = ''
    for x in text:
        texto += x+x+x

    return texto

print(ej2_lvl2("Hola"))


def ej3_lvl2(a,b,c):
    if 21 >= a+b+c:
        return a+b+c
    elif a+b+c > 21 and a == 11 or b== 11 or c == 11:
        return a+b+c - 10
    elif a+b+c > 21 and a != 11 or b!= 11 or c != 11:
        return 'BUST'

print(ej3_lvl2(9,9,9))


def ej4_lvl2(arr):
    result, i=0,0
    ban = False
    while len(arr) > i:
        if arr[i] == 6:
            ban=True
            i+=1
            continue
        elif arr[i] == 9 and ban:
            i+=1
            ban = False
            continue
        elif ban == False:
            result += arr[i]
        i+=1
    
    return result
       
print(ej4_lvl2([2,1,6,9,11]))
