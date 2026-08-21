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
        x= eksamen[karakter]
        counter[x] = counter.get(x, 0)+1
    print(counter)

    return counter

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
    invers_dict = {}

    for k, v in engelske_siffer.items():
        invers_dict[v] = k
    return invers_dict

print(invers(engelske_siffer))

del engelske_siffer

invers = {'nine': 9, 'five': 5, 'one': 1, 'zero': 0, 'three': 3, 'seven': 7,
'four': 4, 'six': 6, 'eight': 8, 'two': 2}

#c)

def skriv_invers_sortert(fortegnelse):
  
    liste = list(invers.values())
    sortert = sorted(liste)
    print(sortert)
    for i in sortert:
        for key, value in invers.items():
            if i == value:
                print(key,':',i)
    

skriv_invers_sortert(invers)


