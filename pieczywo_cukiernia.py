from bs4 import BeautifulSoup
import urllib.request
# -*- coding: utf-8 -*-
import xlwt

# kodowanie arkusza
book = xlwt.Workbook(encoding="utf-8")


owoce = book.add_sheet("chleb")
warzywa = book.add_sheet("chleb_pakowany")
salatki = book.add_sheet("Bułki")
ziola = book.add_sheet("przekaski_slone")
grzyby = book.add_sheet("slodkie_wypieki")
orzechy_ziarniste = book.add_sheet("ciasta_i_desery")
owoce_suszone = book.add_sheet("Tosty_i_pieczywo_do_odpieku")
pieczywo_bezglutenowe = book.add_sheet("Pieczywo bezglutenowe")

arkusz = [owoce,warzywa,salatki,ziola, grzyby,orzechy_ziarniste, owoce_suszone,pieczywo_bezglutenowe]
lista = []
cena_laczna = []
ilosc =[]
waga = []
lista_zmiennych =[]
zakres = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

adres = ['https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/chleb/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/chleb-pakowany/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/bulki/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/slone-przekaski/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/slodkie-wypieki/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/ciasta-i-desery/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/tosty-i-pieczywo-do-odpieku/all?page=',
         'https://ezakupy.tesco.pl/groceries/pl-PL/shop/pieczywo-cukiernia/pieczywo-bezglutenowe/all?page=']

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


    except (urllib.error.HTTPError):
        pass

    waga = cena_laczna[1::2]
    ilosc = cena_laczna[::2]
    k = arkusz[c]
    pozycja =len(lista)
    for j in range(len(lista)):
        x = j + 1
        k.write(j + 1, 0, lista[j])
        k.write(j+1,1,waga[j])
        if ("sz" in lista_zmiennych[j]):
            k.write(j + 1, 2, 'szt')
        elif ("kg" in lista_zmiennych[j]):
            k.write(j + 1, 2, 'kg')
        elif ("l" in lista_zmiennych[j]):
            k.write(j + 1, 2, 'l')
        elif ("m" in lista_zmiennych[j]):
            k.write(j + 1, 2, 'm')

    for d in range(len(lista)):
        lista.pop()
        ilosc.pop()
        waga.pop()
    print(len(lista_zmiennych))
    print(len(cena_laczna))
    for g in range(len(cena_laczna)):
        cena_laczna.pop()
    for t in range(len(lista_zmiennych)):
        lista_zmiennych.pop()
    print("usuniete "+str(c))
    k.write(0, 0, "nazwa")
    k.write(0, 1, "cena")
    k.write(0, 2, "jednostka")

book.save("Pieczywo_Cukiernia.xls")

