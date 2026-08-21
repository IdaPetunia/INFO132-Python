from random import *
import sys
import json



hjerte = f'\u2665'
kløver = f'\u2663'
ruter= f'\u2666'
spar = f'\u2660'


stokk =[]

for i in range(7, 15):
    if i== 12:
        i='J'
    elif i == 13:
        i ='Q'
    elif i ==14:
        i ='K'
    stokk.append(hjerte+str(i))
    stokk.append(kløver+str(i))
    stokk.append(ruter+str(i))
    stokk.append(spar+str(i))



  

def har_vunnet():
    global bunker

    for elem in bunker:
        if len(elem)>0:
            return False

    print('-------GRATULERER du VANT!!-------')
    return True

def har_tapt():
    global bunker
    aktiveKort=[]
    
    for elem in bunker:
        if len(elem) == 0:
           continue 
        kortverdi =elem[0][1:]
        #print(liste1)
        if kortverdi in aktiveKort:
            return False
        else:
            aktiveKort.append(kortverdi)

    print('--------Du TAPTE :-(---------')
    return True
        


def del_ut(split):
    shuffle(split)

    lengde = len(split)
    split=[split[kort:kort +4]for kort in range(0,lengde,4)]
        
    return split
bunker = del_ut(stokk)

def ta_vekk(x1,x2):
    global bunker
    global bokstaver

    

        
    for nummer, char in enumerate(bokstaver):
        if x1 == char:
            bunkenA = bunker[nummer]
            
        if x2 == char:
            bunkenB = bunker[nummer]
            
    if len(bunkenA) == 0 or len(bunkenB) == 0:
         print('en av korbunkene er allerede tom -prøv igjen')
    elif bunkenA[0][1:] == bunkenB[0][1:] and x1 != x2:        
        bunkenA.pop(0)
        bunkenB.pop(0)
    else:
        print('kortene matcher ikke')
        
    if har_vunnet() or har_tapt():
        startigjen_meny()
    else:
        vis_kort()


def vis_kort():
    global bunker
    global bokstaver
    
    bokstaver = list('ABCDEFGH')
    navn = zip(bokstaver, bunker)
    listen = list(navn)
    #print(listen)



    print('\nBunke\tKort\tAntallIgjen')
    for char, bunken in listen:
        bokstav = char[0]
        if len(bunken) == 0:
           print(bokstav, '\t', 'TOM', '\t',len(bunken),'\n')    
        else:
            print(bokstav, '\t', bunken[0], '\t',len(bunken),'\n')

    print('+for å lagre og avslutte skriv <Q>\n')   

    bruker = input('Velg to bunker (like kort): ').upper()

    if bruker == 'Q':
        lagring()

    elif len(bruker) != 2 and len(bruker) not in bokstaver:
        print('\nugyldig input -prøv igjen!')
        vis_kort()
    else:
        elem = list(bruker)
        x = elem[0]
        y= elem[-1]

        ta_vekk(x,y)
       
def fortsett():
    global bunker

    print('henter lagret spill...')

    try:
        f= open('lagretkabal.txt')
        data = f.read()
        bunker = json.loads(data)
        vis_kort()
    except FileNotFoundError:
        print('\nIngen lagret spill - velg nytt spill eller avslutt')
        print()

        startigjen_meny()
        
    



def lagring():
    print('lagrer spill og avslutter..\nPå gjensyn :-)')
    global bunker
    filnavn ='lagretkabal.txt'
    jsondata = json.dumps(bunker)
    
    lagre_bunker = open(filnavn, 'w')
    lagre_bunker.write(jsondata)
    lagre_bunker.close()

def startigjen_meny():

    print("""-----------------
1. start nytt spill
2. exit
-----------------""")
    valg = int(input('hva vil du gjøre nå? '))

    if valg == 1:
        global bunker
        
        bunker = del_ut(stokk)
        vis_kort()
    elif valg == 2:
        print('bye')
        sys.exit() 



def meny():
    print("""-----------------
1. start nytt spill
2. fortsett gammelt spill
3. lagre
-----------------""")

    bruker = int(input('velg: '))
    print()

    if bruker == 1:
        global bunker
        vis_kort()
        bunker = del_ut(stokk)
        
        

    elif bruker == 2:
         fortsett()
         

    elif bruker == 3:
         lagring()
         sys.exit()

   
meny()
    
        

