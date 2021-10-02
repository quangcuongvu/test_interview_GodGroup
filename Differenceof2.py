list_number=[1, 2, 3, 4] 
list_number1=[4, 1, 2, 3]
list_number2=[1, 23, 3, 4, 7]
list_number3=[4, 3, 1, 5, 6]
def twos_difference(lst): 
    results=[]
    for i in lst:
        if i +2 in lst:
            results.append((i,i+2))
    results=sorted(results,key=lambda x:x[0])
    return results

print(twos_difference(list_number))
print(twos_difference(list_number1))
print(twos_difference(list_number2))
print(twos_difference(list_number3))
