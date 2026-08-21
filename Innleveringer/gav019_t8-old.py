#oppgave 1
#a


eksamen = {
 'INFO100': 'C', 'INFO104': 'B', 'INFO116': 'E',
 'INFO180': 'A', 'INFO201': 'F', 'INFO280': 'C',
 'GEO101': 'D', 'GEO110': 'B', 'ADM101': 'A',
 'ECON100': 'B', 'ECON201': 'C', 'GEO210': 'C',
 'FAIL101': 'F'
}

def karakterfrekvens():
    counter = dict()
    keys = list(eksamen.keys())
    for karakter in keys:
        x= eksamen[karakter]#karakter.get(karakter)+1
        counter[x] = counter.get(x, 0)+1

    print(counter)

karakterfrekvens()

# b)


def histogram():
    counter = dict()
    keys = list(eksamen.keys())
    for karakter in keys:
        x= eksamen[karakter]
        counter[x] = counter.get(x, 0)+1
    liste = list(counter.keys())
    for i in sorted(liste):
        nr = counter.get(i)
        if nr >=1:
            print(i, ':', nr*'*')
   

histogram()


#oppgave 2
#a)

engelske_siffer = {
 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}



def skriv_sortert():
    liste = list(engelske_siffer.keys())
    sortert = sorted(liste)
    print(sortert)
    for i in sortert:
        tall = engelske_siffer.get(i)
        print(i,':',tall)

skriv_sortert()

#b)

def invers(inv):
    global invers_dict
    invers_dict = {}

    for k, v in engelske_siffer.items():
        invers_dict[v] = k
    print(invers_dict)


inv = invers(engelske_siffer)

del engelske_siffer

#c)

def skriv_invers_sortert(ftg):
    #inv = invers_dict
    liste = list((ftg.keys()))
    print(liste)
    for i in liste:
        nr = ftg.get(i)
        print(i, ':', nr)

    

skriv_invers_sortert(inv)


