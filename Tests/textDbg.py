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