from random import randint

def getRandom(k, n, lista):
    x = []
    for i in range(0,n-k):
        ran = randint(0, n-1)
        while(ran in lista or ran in x):
            ran = randint(0, n-1)
        x.append(ran)
    return x

if __name__=="__main__":
    n = 10
    k = 6
    lista = []
    lista.append(0)
    lista.append(1)
    lista.append(3)
    lista.append(5)
    lista.append(7)
    lista.append(9)

    newList = getRandom(k,n, lista)
    print(lista)
    print (newList)
