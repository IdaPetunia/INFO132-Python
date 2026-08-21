#Oppgave 1

import math

#man kan skrive inn ønsket radiusverdi
#float gjør at desimaltall er akseptert
r = float(input('Radius:'))
#siden jeg importerte math vet programmet verdien til math.pi
#da kan man skrive formelen for arealet til en sirkel med variablene
a = math.pi*r**2
print('arealet til en sirkel med radius',r, 'er %5.3f' % (a))


#oppgave 2

import random
setning= str(input('skriv setning: '))
antall=int(len(setning))
gjett=int(input('Gjett lengden på setningen: '))
print('That`s', antall==gjett,'!')

#oppgave 3
#importerer funksjoner fra biblioteket random
import random

tall= int(input('Gi meg et tall:'))
#spør om et random tall fra 1-9
tall2 = random.randint(1,9)
tall1=str(tall)+str(tall2)
konvertering=int(tall1)

#programmet printer ut tallene 
print(tall1,'/',tall, '= %.2f'%(konvertering/tall2))
