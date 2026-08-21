#oppgave 1
#a)
x=9
y=66
(x!=7 and y<=50 )
#evalueres til false
(x>7 or 50<y)and(x>y or y<100)
#evalueres til true

#b)

x=9
y=66

(x!=7 and y<=50)
(not x!=7) and (not y<=50)

(x>7 or 50<y) and (x>y or y<100)
(x>7 or 50<y) or not(x>y or y<100)

    
#oppgave 2

alder= int(input('Oppgi alder:'))
lengde= int(input('Hvor lenge ha du bodd i Tulleby?:'))


if alder>=30 and lengde>=9:
    print('Du kan bli ordfører eller sitte i bystyret.')

elif 25<=alder and 5<=lengde:
    print('Du kan sitte i bystyret.')

    if alder<=30 and lengde>=9:
        print('prøv igjen om', 30-alder, 'år for å bli ordfører')

    if alder>=30 and lengde<9:
        print('Prøv igjen om', 9-lengde,'år for å bli ordfører')

elif 25>alder:
    print('du er ikke kvalifisert enda, prøv igjen om',25-alder,'år')
elif 5>lengde:
    print('du er ikke kvalifisert enda, prøv igjen om',5-lengde,'år')


    
#oppgave 3

x=int(input('Tall: '))
if 10>x and x>5:
   print('6, 7, 8, eller 9')
elif x>=10:
   print('minst 10')
else:
   print('maks 5')


