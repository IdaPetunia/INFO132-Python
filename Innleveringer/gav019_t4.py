
#oppgave 1
def siste(sekvens):
    return sekvens[-1]

print(siste([1,2,3]))
print(siste('python'))
print(siste(range(90,100)))
 

#oppgave 2

def skriv_sekvens(sekvens):
    linje=''
    for elem in sekvens:
        linje += str(elem)+' '
    print(linje)

skriv_sekvens('Python')
skriv_sekvens([1,2,3,4,5])
skriv_sekvens(range(90,100))


   
#oppgave 3

def renteutvikling():
    
    startb = int(input('Startbeløp: '))
    renteb = int(input('Rentesats (%): '))
    ønsketb = int(input('Ønsket beløp: '))
    år = 0
    
    while True:
        if startb<ønsketb:
            år += 1
            nyttb = round(startb+(renteb/100*startb),2)
            startb=nyttb
        if nyttb>ønsketb:
            print('år', år, ':', nyttb)
            break
        print('år', år, ':', nyttb)


#oppgave 4
        
print(' |', 1, 2, 3, 4, 5, 6, 7, 8, 9, sep='   ')

print('-+-----------------------------------------')
sidetabell= 0
for y in range(1, 10):
    sidetabell += 1
    print(sidetabell, end='|')
    for x in range(1, 10):
        z = x * y
        if z < 10: blank = '  '       # 2 blanks
        else:
            if z < 100: blank  = ' '  # 1 blank
        print(blank, z, end = '') 
    print()


        
    
        
    
