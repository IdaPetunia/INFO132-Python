#oppgave 1

#def fak(n):
def fak(n, total=1):
    while True:
        if n == 1:
            #når n bare er en så skal bare tallet vi har fått bli returnert
            return total
        #Dersom n er noe annet enn 1 vil programmet utføre fakultetfunksjonen slik:
        n, total = n - 1, total * n

def fak1(n):
    fact = 1
    for num in range(2, n + 1):
        #tallet blir ganget med fact og lagt til i vriabelen
        fact *= num
    return fact


#oppgave 2

class Monark:
    kongerekke = []


    def __init__(self, nasjon, navn, år):
        self.nasjon = nasjon
        self.navn = navn
        self.år = år
        self.etterfølger = None

        Monark.kongerekke.append(self)
  
    #oppgave a
    def skrivkongerekke():
         for konge in Monark.kongerekke:
             print(konge.navn,'av', konge.nasjon, 'tiltro i', konge.år)

    #oppgave b
             #det er her vi setter funksjonen hvor man kan legge til en etterfølger 
    def sett_etterfølger(self, nestekonge):
        self.etterfølger = nestekonge
        
            
    #her blir det skrevet ut som i oppgave a, med etterfølger
    def skriv(self):
        if self.etterfølger:
            print( self.navn, 'av', self.nasjon,'tiltro i', self.år, 'etterfølger', self.etterfølger.navn)
       #dersom det ikke er noen etterfølger, altså verdien None, blir den skrevet ut uten. 
        else:
            print( self.navn, 'av', self.nasjon,'tiltro i', self.år)


           
haakon = Monark('Norge', 'Kong Haakon VII', 1905)
olav= Monark('Norge','Kong Olav V', 1957)
harald = Monark('Norge', 'Kong Harald V', 1991)

Monark.skrivkongerekke()

haakon.sett_etterfølger(olav)
olav.sett_etterfølger(harald)

Monark.skriv(haakon)
Monark.skriv(olav)
Monark.skriv(harald)     

    

        
    
