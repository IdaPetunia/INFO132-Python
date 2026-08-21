#oppgave1

print('Ida\nLeivdal\nØvreberg')
print('Ida')
print('Leivdal')
print('Øvrebreg')


#oppgave2

print('****    ***           *')
print(' *      *   *        * *')
print(' *      *    *      *   *')
print(' *      *    *     * * * *')
print(' *      *    *    *       *')
print(' *      *   *    *         *')
print('****    ***     *           *')




#oppgave 3 a)


#hvis man her taster inn 250 så får man det oppgaveteksten ber om
kroner = bool(input('skriv inn kroner:'))
# eventuelt: kroner =250

dollar = kroner/8.60
dollar1 = ('%.2f' % (dollar))
euro = kroner/9.30
euro1 = ('%.2f' % (euro))

print(kroner, 'kroner tilsvarer', euro1, 'Euro og', dollar1, 'Dollar')


#oppgave 3 b)
kroner = int(input('skriv inn kroner:'))

dollar = kroner/8.60
dollar1 = ('%5.2f' % (dollar))
euro = kroner/9.30
euro1 = ('%5.2f' % (euro))

print(kroner,'kroner tilsvarer',euro1, '\N{euro sign} og',dollar1,'\N{dollar sign}')
