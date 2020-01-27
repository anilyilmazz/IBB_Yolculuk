import json
import requests
import matplotlib.pyplot as plt

data = requests.get('https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=c2c6cec1-ceb5-4fab-8d87-c5d900a99809')

jsondata = json.loads(data.content)

karayoluList = []
denizyoluList = []
raylisistemList = []

for i in jsondata['result']['records']:
    if 'Karayolu' in i['Yolculuk Turu']:
        karayoluList.append(i)
    elif 'Deniz' in i['Yolculuk Turu']:
        denizyoluList.append(i)
    elif 'Raylı' in i['Yolculuk Turu']:
        raylisistemList.append(i)

plt.plot([i['Yil'] for i in karayoluList], [i['Yolcu Sayisi (Kisi/Gun)'] for i in karayoluList],label= 'Kara Yolları',color = 'black')
plt.plot([i['Yil'] for i in denizyoluList], [i['Yolcu Sayisi (Kisi/Gun)'] for i in denizyoluList], label='Deniz Yolları',color = 'blue')
plt.plot([i['Yil'] for i in raylisistemList], [i['Yolcu Sayisi (Kisi/Gun)'] for i in raylisistemList], label='Raylı Sistem',color = 'brown')

plt.xlabel('Yıllar')
plt.ylabel('Yolcu Sayısı')
plt.title('Yolcu Sayıları')
plt.ticklabel_format(style ='plain')
plt.legend(loc='best')
plt.show()
