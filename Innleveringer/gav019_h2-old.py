#hoved 2


# importing the module
import json

f= open('karakterer.txt')
data = f.read()
  
karakterer = json.loads(data)

e = open('emner.txt','r')
data2 = e.read()
  
emner = json.loads(data2)

  

emner = ['INFO100', 'INFO132', 'INFO282', 'ECON221']

"""
karakterer={
    
        'INFO100': 'C',
        'INFO132': 'A',
        'INFO110': 'E',
        
        'INFO282': 'B',
        'ECON221': 'D',
        'INFO226': 'F',
}
"""





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

    

    for fag, karakter in karakterer.items():
        if nivå == '' and (faginp == '' or faginp[0] == fag[0]):
                print(fag, karakter)
                
        elif (faginp== '' or faginp[0] == fag[0]) and nivå[0] == fag[-3]:
                print(fag,karakter)
        

def to():
    nyttemne = input('Nytt emne: ').upper()
    karakterer.setdefault(nyttemne)
    karakterer[nyttemne] = 'not_set'
    emner.append(nyttemne)

def tre():
    #karakterer[ input('Emne: ')] = input('Karakter (<enter> for å slette): ')

    kemne = input('Emne: ').upper()
    nykarakter = input('Karakter (<enter> for å slette): ').upper()
    if nykarakter == '':
        karakterer[kemne] = 'not_set'
    else:
        karakterer[kemne] = nykarakter

   

def fire():
    faginp = input('-fag: ').upper()
    nivå = input('-nivå: ')

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
        
        
    
    




