målinger = [

    { 'stasjon': 'Havn', 'nedbør': 0.0, 'temp': 1.0, 'vind': 1.0, 'tid': '2021-01-15 06:00' },
    { 'stasjon': 'Topp', 'temp': 4.0, 'vind': 6.0, 'tid': '2021-01-15 12:00' },
    { 'stasjon': 'Havn', 'nedbør': 0.0, 'temp': 6.0, 'vind': 3.0, 'tid': '2021-01-15 12:00' },
    { 'stasjon': 'Torg', 'nedbør': 0.2, 'temp': 5.0, 'vind': 2.0, 'tid': '2021-01-15 14:00' },
    { 'stasjon': 'Torg', 'nedbør': 1.6, 'temp': 4.0, 'vind': 1.5, 'tid': '2021-01-15 16:00' },
    { 'stasjon': 'Havn', 'nedbør': 0.4, 'temp': 3.0, 'vind': 0.5, 'tid': '2021-01-15 18:00' },
]

vind_målinger = [       
måling.get('vind')for måling in målinger

]
print( vind_målinger )

vind_målinger = [1.0, 6.0, 3.0, 2.0, 1.5, 0.5]
min_vind, maks_vind =  min(vind_målinger), max(vind_målinger)
 
print(min_vind, maks_vind)

print('xxx %.5f yyy' % 2.71828)


nedbør_målinger = []
for måling in målinger:
 if 'nedbør' in måling:
    nedbør_målinger.append(måling['nedbør'])
    print( nedbør_målinger )

havn_målinger = [
    måling for måling in målinger if måling['stasjon'] == 'Havn'
]
print( havn_målinger )

for måling in havn_målinger:
    havn_målinger[måling]= havn_målinger[måling] - 0,8
print( havn_målinger )

temp
