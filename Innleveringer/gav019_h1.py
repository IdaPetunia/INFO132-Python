#oppgave 1

import math
"""
#måte 1 - krever ett argument dersom input ikke blir brukt
def pi(d):
    #tror pi kan ha flere enn 15 desimaler, men vises ikke i "runner"
    if d>0 and d<15:
        print(round(math.pi,d))
    elif d>15:
        print('For mange desimaler.')
        print(math.pi)

#------- start -------
        
input_from_user= input('Hvor mange desimaler: ')
try:
    no_decimals=int(input_from_user)
    pi(no_decimals)
#med ingen input verdi
except:
    pi(2)



"""
    

#måte 2- slik som i oppgaveeksempelet


def pi(d='2'):
    if d=='2':
        pi=round(math.pi, 2)
    elif d>0 and d<15:
        pi=round(math.pi,d)
    elif d>15:
        print('For mange desimaler.')
        pi=(math.pi)
    return pi



#oppgave 2


def temperaturKonvertering(temperatur, typetemperatur='C'):
    #gjør om fra celcius til fahrenheit
    if typetemperatur=='C':
        temp=(temperatur*9/5)+32
    else:
        temp= (temperatur-32)*5/9
    return temp





#Oppgave 3

#3abc

#-----globale variabler---
saldo=500
rentesats=0.01
historie=[]
line='------------------'
#---------------------------



def velg():
    global saldo
    print(line)
    print('1 - vis saldo\n2 - innskudd\n3 - uttak\n4 - renteoppgjør\n5 - siste endringer')
    print(line)
    
    handling = int(input('Velg handling: '))
    if handling==1:
        print('saldo:', saldo)
        
    elif handling==2:
        input_ins= int(input('Beløp: '))
        innskudd(input_ins)
            
    elif handling==3:
        input_utk= int(input('Beløp: '))
        uttak(input_utk)
            
    elif handling==4:
        renteoppgjør()

    elif handling==5:
        siste_endringer()
    
   
        
       

#innskudd
def innskudd(ins):
    global saldo
    global historie
    saldo = ins+saldo
    historie+=['innskudd ' + str(ins)]
    if saldo>=1000000:
        global rentesats
        rentesats=0.02
        return print('Gratulerer, du har fått bonusrente')

#uttak
def uttak(utk):
    global saldo
    global historie

    if (saldo-utk)<0:
        print('overtrekk')
        return

    if saldo> 1000000 and saldo-utk < 1000000:
        global rentesats
        rentesats=0.01
        print('du har nå ordinær rente')

    historie+=['uttak ' + str(utk)]
    saldo = saldo -utk

#rentesatsen blir satt
def beregn_rente():
    global rente
    global saldo
    global rentesats
    if saldo>1000000:
        rentesats=0.02*saldo
    elif saldo<1000000:
        rentesats=0.01*saldo

#legger til renten
def renteoppgjør():
    beregn_rente()
    global saldo
    global historie
    global rentesats
    saldo=rentesats+saldo
    historie+=['rente ' + str(rentesats)]


def siste_endringer():
    for val in historie[-3:]:
        print(val)
    


#oppgave 4

import random

def tre_tilfeldige():
    nr1= random.randint(1, 9)
    nr2= random.randint(1, 9)
    nr3= random.randint(1, 9)
    rekkefølge=[nr1, nr2, nr3]
    rekkefølge.sort()
    tall= [str(integer) for integer in rekkefølge]
    print(tall)
    sammen="".join(tall)
    print(sammen)


tre_tilfeldige()


    
    

    
    

    










