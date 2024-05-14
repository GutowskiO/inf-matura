def wczytaj_dane_z_pliku(nazwa_pliku):
    odczyt = open(nazwa_pliku, "r")
    liczby = odczyt.readlines()
    for a in range(len(liczby)):
        liczby[a] = liczby[a].strip()
    odczyt.close()
    return liczby

def oblicz_sume_cyfr_z_pozycji_parzystych(liczba):
    suma = 0
    for a in range(len(liczba)):
        if a % 2 == 0:
            suma += int(liczba[len(liczba) - 1 - a])
    return suma

def oblicz_sume_cyfr_z_pozycji_nieparzystych(liczba):
    suma = 0
    for a in range(len(liczba)):
        if a % 2 != 0:
            suma += int(liczba[len(liczba) - 1 - a])
    return suma

def zad_6_1(liczby):
    kody1 = open("kody1.txt", "w")
    for a in range(len(liczby)):
        suma_cyfr_z_parzystych = oblicz_sume_cyfr_z_pozycji_parzystych(liczby[a])
        suma_cyfr_z_nieparzystych = oblicz_sume_cyfr_z_pozycji_nieparzystych(liczby[a])
        kody1.write(str(suma_cyfr_z_parzystych) + " " + str(suma_cyfr_z_nieparzystych) + "\n")
    kody1.close()

def znajdz_cyfre_kontrolna(liczba):
    suma_cyfr_z_parzystych_przez_3 = oblicz_sume_cyfr_z_pozycji_parzystych(liczba) * 3
    suma_cyfr_z_nieparzystych = oblicz_sume_cyfr_z_pozycji_nieparzystych(liczba)
    suma_sum = suma_cyfr_z_parzystych_przez_3 + suma_cyfr_z_nieparzystych

    reszta_z_dzielenia_przez_10 = suma_sum % 10
    odjety_wynik_od_10 = 10 - reszta_z_dzielenia_przez_10
    cyfra_kontrolna = odjety_wynik_od_10 % 10

    return cyfra_kontrolna

def zad_6_2(liczby):
    kody2 = open("kody2.txt", "w")
    for a in range(len(liczby)):
        cyfra_kontrolna = znajdz_cyfre_kontrolna(liczby[a])
        kody2.write(str(cyfra_kontrolna) + " " + liczby[a] + "\n")

def znajdz_kod_kreskowy_danej_cyfry(cyfra):
    kody_cyfr = wczytaj_dane_z_pliku("cyfra_kodkreskowy.txt")
    for linia in kody_cyfr:
        if linia[0] == str(cyfra):
            linia = linia[1 : :].strip()
            return linia

def znajdz_kod_w_systemie_SC25(liczba):
    kod_w_systemie_SC25 = "11011010"
    for cyfra in liczba:
        kod_kreskowy_danej_cyfry = znajdz_kod_kreskowy_danej_cyfry(cyfra)
        kod_w_systemie_SC25 += kod_kreskowy_danej_cyfry
    kod_w_systemie_SC25 += znajdz_kod_kreskowy_danej_cyfry(znajdz_cyfre_kontrolna(liczba))
    kod_w_systemie_SC25 += "11010110"
    return kod_w_systemie_SC25

def zad_6_3(liczby):
    kody3 = open("kody3.txt", "w")
    for a in range(len(liczby)):
        kod_w_systemie_SC25 = znajdz_kod_w_systemie_SC25(liczby[a])
        kody3.write(kod_w_systemie_SC25 + "\n")
    kody3.close()

liczby = wczytaj_dane_z_pliku("kody.txt")
zad_6_1(liczby)
zad_6_2(liczby)
zad_6_3(liczby)
print("Wszystko zadzialalo")