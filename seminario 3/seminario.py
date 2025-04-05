
#Lista
array=[20,18,1,6,9,17,13,5,4,2,11]


def quick_sort(contenedor,menor,mayor):
    if menor<mayor:
        va=particion(contenedor,menor,mayor)
        quick_sort(contenedor,menor,va-1)
        quick_sort(contenedor,va+1,mayor)

def particion(va,menor,mayor):
    p=va[mayor]
    i=menor-1
    for a in range (menor,mayor):
        if va[a]<=p:
            i+=1
            va[i],va[a]=va[a],va[i]
    va[i+1],va[mayor]=va[mayor],va[i+1]
    return i+1


quick_sort(array,0,(len(array)-1))
print (array)