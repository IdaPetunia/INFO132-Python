#oppgave 1

vokal ='aeuioyæøå'

def antallVokaler(setning):
    #etter antall vokaler til 0 i starten
    antall = ''
    for bokstav in setning:
        if bokstav not in vokal:
            continue
        if bokstav in vokal:
            #derson bokstav er en vokal blir den lagt til i antall variabelen
           antall += bokstav
           #deretter bruker jeg len funskjonen til å telle antall bokataver i antall
           resultat = len(antall)
    return resultat

print(antallVokaler('Tre små kinesere på Høybro plass.'))


#oppgave 2

TV = '''\
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''


def verv(navn):
    arbeid = []
    #splitter strengen til en liste etter linjeskift
    lines = TV.split('\n')

    #Går gjennom hver linje
     
    for n in lines:
        #skjekker om navnet er i hver linje
        if n.find(navn)>-1:
            arbeid.append(n.split(':')[0])
            #splitter linjen ved : og starten av linjen og
            #legger til i listen arbeid

    return arbeid


print(verv('Liv'))



    
    
