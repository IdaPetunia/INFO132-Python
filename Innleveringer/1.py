"""
målinger = [
    { 'stasjon': 'Havn', 'nedbør': 0.0, 'temp': 1.0, 'vind': 1.0, 'tid': '2021-01-15 06:00' },
    { 'stasjon': 'Topp', 'temp': 4.0, 'vind': 6.0, 'tid': '2021-01-15 12:00' },
    { 'stasjon': 'Havn', 'nedbør': 0.0, 'temp': 6.0, 'vind': 3.0, 'tid': '2021-01-15 12:00' },
    { 'stasjon': 'Torg', 'nedbør': 0.2, 'temp': 5.0, 'vind': 2.0, 'tid': '2021-01-15 14:00' },
    { 'stasjon': 'Torg', 'nedbør': 1.6, 'temp': 4.0, 'vind': 1.5, 'tid': '2021-01-15 16:00' },
    { 'stasjon': 'Havn', 'nedbør': 0.4, 'temp': 3.0, 'vind': 0.5, 'tid': '2021-01-15 18:00' },
]

torg_målinger = []

for måling in målinger:
    if måling.get('stasjon')=='Torg':
        torg_målinger.append( måling )

print( målinger[2] )

havn_målinger = [

       {'stasjon': 'Havn', 'nedbør': 0.0, 'temp': 1.0, 'vind': 1.0, 'tid': '2021-01-15 06:00'},

       {'stasjon': 'Havn', 'nedbør': 0.0, 'temp': 6.0, 'vind': 3.0, 'tid': '2021-01-15 12:00'},

       {'stasjon': 'Havn', 'nedbør': 0.4, 'temp': 3.0, 'vind': 0.5, 'tid': '2021-01-15 18:00'}

]

for måling in havn_målinger:
    r = havn_målinger.get('temp')
    resultat = r-0.8
"""  


filnavn = 'målinger.txt'
for x in open(filnavn, 'r'):
    print(x)
