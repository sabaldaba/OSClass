def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

if __name__ == "__main__":
    lista = []
    branch=True
    while(branch==True):
        valor=int(input("Ingrese un valor entero:"))
        lista.append(valor)
        print("La mediana es: " + str(median(lista)))
        op=bool(input("Desea ingresar un nuevo numero: 0/1"))
