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

#emner = ['INFO100', 'INFO132', 'INFO282', 'ECON221']
"""
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
    start()

    
def en():

    def printfag(fag, karakterer):
        if fag in karakterer:
                print(fag, karakterer[fag])
        else: 
            print(fag)


    print('Velg fag og/eller nivå (<enter> for alle')
    faginp = input('- Fag: ').upper()
    nivå = input('- Nivå: ').upper()

    for fag in emner: 
        if nivå == '' and (faginp == '' or faginp[0] == fag[0]):
            printfag(fag, karakterer)

     
        #Her må nivå være spesifisert men faget kan være tomt 
        elif (faginp== '' or faginp[0] == fag[0]) and nivå[0] == fag[-3]:
           printfag(fag, karakterer)
     



def to():
    nyttemne = input('Nytt emne: ').upper()

    if nyttemne not in emner:
        emner.append(nyttemne)
    else:
        print('Emnet eksisterer allerede')
    


def tre():
    
    kemne = input('Emne: ').upper()
    nykarakter = input('Karakter (<enter> for å slette): ').upper()
    
    if nykarakter == '':
        del karakterer[kemne] 
    else:
        karakterer[kemne] = nykarakter

   

def fire():
    faginp = input('-fag: ').upper()
    nivå = input('-nivå: ')

    d= {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
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
        
        
    
    




