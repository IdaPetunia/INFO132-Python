#oppgave 1

tlf = open('telefon.txt','a')

print('Legg til navn og nummer, avslutt med <enter>.')

while True:
    
    ny = input('Navn og nummer: ')
    if ny == '':
        break
    else :
        tlf.write('\n')
        tlf.write(ny)
tlf.close()


#oppgave 2
import os


filnavn = 'telefon.txt'
nyefilnavn = 'nye-'+filnavn
orgfil = open(filnavn)
nyfil = open(nyefilnavn,'w')

navn = input('Navn: ')

for linje in orgfil:
    if linje.startswith(navn):
        gammelnr = linje[len(navn)+1:-1]
        print('Gammelt telefonnummer: ',gammelnr)
        
        nyttnr= input('Nytt nummer: ')
        nyfil.write(navn+' '+nyttnr+'\n')
        
    else:
        nyfil.write(linje)
orgfil.close()
nyfil.close()

os.remove(filnavn)
os.rename(nyefilnavn, filnavn)


     



#oppgave 3


def fjernVokaler(fil):
    innfil = open(fil,'r',encoding='utf-8')
    utfil = open(fil+'uten vokaler','w')

    for linje in innfil:
        for char in linje:
            if char not in 'aeiouyæøå':
                utfil.write(char)

    utfil.close()
    innfil.close()


fn = 'tre-små-kinesere.txt'
fjernVokaler(fn)
            

    
