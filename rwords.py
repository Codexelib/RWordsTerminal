RWords_surum = 'terminal beta 1.0'

import random
import sys
import os

# Renkler
class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    RED = '\u001b[31m'
    ACIKMAVI = '\u001b[32;1m'

# Temizleme
os.system('clear')

# Menu
print(bcolors.ACIKMAVI + """

  ██████╗ ██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗
  ██╔══██╗██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝
  ██████╔╝██║ █╗ ██║██║   ██║██████╔╝██║  ██║███████╗
  ██╔══██╗██║███╗██║██║   ██║██╔══██╗██║  ██║╚════██║
  ██║  ██║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████║
  ╚═╝  ╚═╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
""" + bcolors.ENDC + '				created by coderman \n')
print(bcolors.ACIKMAVI + '[1]' + bcolors.ENDC + ' Calismayi Baslat \n' + bcolors.ACIKMAVI + '[2]' +
bcolors.ENDC + ' Kelime Ekle \n' + bcolors.ACIKMAVI + '[B]' + bcolors.ENDC + ' Bilgi \n' + bcolors.ACIKMAVI +
'[Q]' + bcolors.ENDC + ' Cikis')

# Dosyalar
kelimeDosya = open('kelimeler','r+')
anlamDosya = open('anlamlar','r+')

# Degiskenler
kelimeler = []
anlamlar = []
indexler = []
eksikler = []
ilk = True

# Dosya Okuma
kelimeSatirlar = kelimeDosya.read().splitlines()
anlamSatirlar = anlamDosya.read().splitlines()

for kelime in kelimeSatirlar:
	kelimeler.append(kelime)
for anlam in anlamSatirlar:
	anlamlar.append(anlam)

# Liste Index Hesaplama
for i in range(0,len(kelimeler)):
	indexler.append(i)

# Calisma Fonksiyonu
def Calisma(indexListe):
	while True:
		if bool(indexListe) == False:
			print(bcolors.ACIKMAVI + 'Calisma bitti ! \n' + bcolors.ENDC)
			break
		rastgeleIndex = random.choice(indexListe)
		soru = input(kelimeler[rastgeleIndex] + ' = ')
		if soru == anlamlar[rastgeleIndex]:
			indexListe.remove(rastgeleIndex)
		else:
			indexListe.remove(rastgeleIndex)
			if ilk == True:
				eksikler.append(rastgeleIndex)
			print(bcolors.RED + 'Dogru Cevap : ' + anlamlar[rastgeleIndex] + bcolors.ENDC)

# Menu Secimleri
while True:
	menuSecim = input(bcolors.WARNING + ' \nSeciminiz : ' + bcolors.ENDC)

	# Calismayi Baslat
	if menuSecim == '1':
		Calisma(indexler)
		ilk = False
		if bool(eksikler) == True:
			Calisma(eksikler)

	# Kelime Ekle 
	elif menuSecim == '2':
		while True:
			yeniKelime = input('Yeni Kelime : ')
			yeniAnlam = input('Yeni Anlam : ')
			kelimeDosya.write(yeniKelime + '\n')
			anlamDosya.write(yeniAnlam + '\n')
			cikisOnay = input(bcolors.ACIKMAVI + '\nCikmak icin C ye basiniz . \n' + bcolors.ENDC)
			if cikisOnay == 'C':
				break

	# Bilgi
	elif menuSecim == 'B':
		print(RWords_surum)

	# Cikis
	elif menuSecim == 'Q':
		sys.exit()
