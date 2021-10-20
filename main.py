def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def gasesteNr(l,n,poz):
    '''
    determina daca număr citit de la tastatura se regaseste in lista începând de la o anumită poziție
citită de la tastatură.
    :param l: lista de nr. intregi
    :param n: nr. integ
    :param poz: nr. natural
    :return: True daca gasim nr. sau False in caz contrar
    '''
    for i in range(len(l)-1):
        if l[i] == n and i >= poz:
            return True
    return False

def TestGasesteNr():
    assert gasesteNr([2, 32, 122, 12, 1456],12,3) is True
    assert gasesteNr([2, 32, 122, 12, 1456], 12, 4) is False
    assert gasesteNr([2, 32, 122, 1456], 12, 1) is False

def sumaPare(l):
    '''
    determina suma nr. pare din lista
    :param l: lista de nr. intregi
    :return: suma nr. pare din lista
    '''
    suma = 0
    for x in l:
        if x % 2 == 0:
            suma = suma + x
    return suma

def TestSumaPare():
    assert sumaPare([2, 3, 12, 5, 9]) == 14
    assert sumaPare([1, 3, 5, 9]) == 0
    assert sumaPare([2, 4, 12, 5]) == 18



def main():
    TestGasesteNr()
    TestSumaPare()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afișați dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție citită de la tastatură. ")
        print("3. Afișați suma tuturor numerelor întregi pare din lista.")
        print("4. ")
        print("5. ")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            n = int(input("Dati nr. n: "))
            poz = int(input("Dati pozitia: "))
            if gasesteNr(l,n,poz) == True:
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            print(sumaPare(l))
        elif optiune == "4":
            pass
        elif optiune == "5":
            pass
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

if __name__ == '__main__':
    main()