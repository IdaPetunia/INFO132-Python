#hoved 2

import json
#bruker json for å lese inn til fil 

#her er karakterfortegnelsen i fil
f= open('karakterer.txt')
data = f.read()

karakterer = json.loads(data)

#emner listen i fil
e = open('emner.txt')
data2 = e.read()
  
emner = json.loads(data2)

  

#Innholdet i filene----- 
"""
emner = ['INFO100', 'INFO132', 'INFO282', 'ECON221']

karakterer={
    
        'INFO100': 'C',
        'INFO132': 'A',
        'INFO110': 'E',
        
        'INFO282': 'B',
        'GEO221': 'A',
        'INFO226': 'F',
}
"""
#--------------------------




def start():
    meny = """------------------------
1 Emneliste
2 Legg til emne
3 Sett karakter
4 Karaktersnitt
5 Avslutt
6 Lagre
------------------------"""
    print(meny)

    while True: 
        handling = int(input('Velg handling (0 for meny) > '))

        if handling == 0:
            null()

        elif handling == 1:
            en()

        elif handling == 2:
            to()
    
        elif handling == 3:
            tre()

        elif handling ==4:
            fire()


        elif handling ==5:
            fem()
            break
        elif handling == 6:
            seks()
        

def null():
    print(meny)


def en():
    print('Velg fag og/eller nivå (<enter> for alle')
    faginp = input('- Fag: ').upper()
    nivå = input('- Nivå: ')

    
    # Denne skjekker om nivå er speisfisert. Dersom det ikke er
    # skjekker den om faget er spesifisert, begge kan være tomme
    for fag, karakter in karakterer.items():
        if nivå == '' and (faginp == '' or faginp[0] == fag[0]):
                print(fag, karakter)

        #Her må nivå være spesifisert men faget kan være tomt 
        elif (faginp== '' or faginp[0] == fag[0]) and nivå[0] == fag[-3]:
                print(fag,karakter)
        

def to():
    nyttemne = input('Nytt emne: ').upper()
    #legger nytt fag til i fortegnelse, uten karakter
    karakterer.setdefault(nyttemne)
    karakterer[nyttemne] = 'not_set'
    #legger fag til i listen
    emner.append(nyttemne)

def tre():
    
    kemne = input('Emne: ').upper()
    nykarakter = input('Karakter (<enter> for å slette): ').upper()
    #dersom enter trykkes, vil karakteren til emne få verdien 'not_set'(0)
    if nykarakter == '':
        karakterer[kemne] = 'not_set'
    else:
        karakterer[kemne] = nykarakter

   

def fire():
    faginp = input('-fag: ').upper()
    nivå = input('-nivå: ')

    #for å regne ut snittet gjøres karakterene om til tall-
    #ingen karakter blir regnet som 0 og drar snittet ned
    d= {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2, 'F': 1, 'not_set': 0}
    teller = 0
    antall = 0

  
    for fag, v in karakterer.items():
        if nivå == '' and (faginp == '' or faginp[0] == fag[0]):
                 teller += d.get(v)
                 antall += 1
                
        elif (faginp== '' or faginp[0] == fag[0]) and nivå[0] == fag[-3]:
                 teller += d.get(v)
                 antall += 1

    #her regnets snittet:             
    snitt = round(teller/antall)
    print(teller, antall)
    for key, value in d.items():
        if snitt == value:
            print(key)
              


def fem():
    lagre = input('vil du lagre endringene? (j/n): ')
    if lagre == 'j':
        seks()
    else: 
        print('Takk for nå')
    

def seks():
    filnavn1 = 'karakterer.txt'
    filnavn2 ='emner.txt'
    lagre_karakter = open(filnavn1, 'w')

    jsondata = json.dumps(karakterer)
    lagre_karakter.write(jsondata)
    lagre_karakter.close()
    

    lagre_emne = open(filnavn2, 'w')
    sortemner = sorted(emner)

    jsondata = json.dumps(sortemner)
    lagre_emne.write(jsondata)

    lagre_emne.close()
    
    

start()
        
        
    
    




