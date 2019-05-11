from bs4 import BeautifulSoup
import urllib.request
# -*- coding: utf-8 -*-
import xlwt

# kodowanie arkusza
book = xlwt.Workbook(encoding="utf-8")


owoce = book.add_sheet("Owoce")
warzywa = book.add_sheet("Warzywa")
salatki = book.add_sheet("Salatki")
ziola = book.add_sheet("zioła")
grzyby = book.add_sheet("grzyby")
orzechy_ziarniste = book.add_sheet("orzechy i ziarnista")
owoce_suszone = book.add_sheet("owoce suszone")

arkusz = [owoce,warzywa,salatki,ziola, grzyby,orzechy_ziarniste, owoce_suszone ]
lista = []
cena_laczna = []
ilosc =[]
waga = []
t = []
zakres = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
lista_zmiennych =[]
adres = ['https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/owoce/all?page=','https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/warzywa/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/salatki/all?page=','https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/ziola/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/grzyby/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/orzechy-i-ziarniste/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/owoce-warzywa/owoce-suszone-i-bakalie-na-wage/all?page=']

for c in range(len(adres)):
    try:
        for a in range(len(zakres)):
            url = str(adres[c])+str(zakres[a])
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            table = soup.find_all('a',{'class': 'product-tile--title product-tile--browsable'})
            table2 = soup.find_all('span',{'class':'value'})
            table3 = soup.find_all('span', {'class': 'weight'})

            for i in range(len(table)):

                k = str(table[i])

                if 'a class="product-tile--title product-tile--browsable"' in k:
                    produkt = k.split()

                    k1 = k[102:]
                    k2 = k1.replace("</a>",'')

                    lista.append(k2)

            for e in range(len(table2)):
                f = str(table2[e])

                if 'span class="value" data-auto="price-value"' in f:
                    cena = f.split()

                    f1 = f[44:]
                    f1 = f1.replace('</span>','')
                    cena_laczna.append(f1)

            for gh in range(len(table3)):
                gj = str(table3[gh])
                if '<span class="weight">' in gj:
                    zmienna = gj.split()
                    zmienna = zmienna[1][16:18]
                    lista_zmiennych.append(zmienna)
                    print(zmienna)

    except (urllib.error.HTTPError):
        pass

    waga = cena_laczna[1::2]
    ilosc = cena_laczna[::2]
    k = arkusz[c]
    pozycja =len(lista)
    for j in range(len(lista)):
        x = j + 1
        k.write(j + 1, 0, lista[j])
        k.write(j+1,1,ilosc[j])
        if "sz" in lista_zmiennych:
            k.write(j + 1, 2, 'szt')
        else:
            k.write(j + 1, 2, 'kg')

        if ilosc[j] != waga[j]:
            k.write(j + 1+pozycja, 0, lista[j])

            k.write(j + 1+pozycja, 1, waga[j])
            k.write(j + 1 + pozycja, 2, lista_zmiennych[j])

    for d in range(len(lista)):
        lista.pop()
        ilosc.pop()
        waga.pop()
    for g in range(len(cena_laczna)):
        cena_laczna.pop()
    print("usuniete "+str(c))
    k.write(0, 0, "nazwa")
    k.write(0, 1, "cena")
    k.write(0, 2, "jednostka")


book.save("tesco_warzywa_owoce.xls")

