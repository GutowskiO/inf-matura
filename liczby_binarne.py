def wczytaj_dane_z_pliku():
    odczyt = open("liczby.txt", "r")
    liczby_binarne = odczyt.readlines()
    odczyt.close()
    for a in range(len(liczby_binarne)):
        liczby_binarne[a] = liczby_binarne[a].strip()
    return liczby_binarne

def ma_wiecej_0_niz_1(liczba):
    liczba_0 = 0
    liczba_1 = 0
    for cyfra in liczba:
        if cyfra == "0":
            liczba_0 += 1
        else:
            liczba_1 += 1
    if liczba_0 > liczba_1:
        return True
    return False
def zad_4_1(liczby_binarne):
    licznik = 0
    for liczba in liczby_binarne:
        if ma_wiecej_0_niz_1(liczba):
            licznik += 1
    zapis = open("wynik4.txt", "w")
    zapis.write("4.1\n")
    zapis.write(str(licznik))
    zapis.write("\n\n")
    zapis.close()

def podzielna_przez_2(liczba):
    if liczba[len(liczba) - 1] == "0":
        return True
    return False
def podzielna_przez_8(liczba):
    if liczba[len(liczba) - 1] == "0" and liczba[len(liczba) - 2] == "0" and liczba[len(liczba) - 3] == "0":
        return True
    return False

def zad_4_2(liczby_binarne):
    liczba_liczb_podzielnych_przez_2 = 0
    liczba_liczb_podzielnych_przez_8 = 0
    for liczba in liczby_binarne:
        if podzielna_przez_2(liczba):
            liczba_liczb_podzielnych_przez_2 += 1
            if podzielna_przez_8(liczba):
                liczba_liczb_podzielnych_przez_8 += 1
    zapis = open("wynik4.txt", "a")
    zapis.write("4.2\n")
    zapis.write("Podzielne przez 2: " + str(liczba_liczb_podzielnych_przez_2))
    zapis.write("\nPodzielne przez 8: " + str(liczba_liczb_podzielnych_przez_8))
    zapis.write("\n\n")
    zapis.close()

def jest_wieksza(liczba_1, liczba_2):
    if len(liczba_1) > len(liczba_2):
        return True
    elif len(liczba_1) == len(liczba_2):
        for a in range(len(liczba_1)):
            if liczba_1[a] > liczba_2[a]:
                return True
            if liczba_1[a] < liczba_2[a]:
                return False
    return False

def jest_mniejsza(liczba_1, liczba_2):
    if len(liczba_1) < len(liczba_2):
        return True
    elif len(liczba_1) == len(liczba_2):
        for a in range(len(liczba_1)):
            if liczba_1[a] < liczba_2[a]:
                return True
            if liczba_1[a] > liczba_2[a]:
                return False
    return False

def zad_4_3(liczby_binarne):
    numer_wiersza_z_najwieksza = 1
    numer_wiersza_z_najmniejsza = 1
    for a in range(len(liczby_binarne)):
        if jest_wieksza(liczby_binarne[a], liczby_binarne[numer_wiersza_z_najwieksza - 1]):
            numer_wiersza_z_najwieksza = a + 1
        if jest_mniejsza(liczby_binarne[a], liczby_binarne[numer_wiersza_z_najmniejsza - 1]):
            numer_wiersza_z_najmniejsza = a + 1
    zapis = open("wynik4.txt", "a")
    zapis.write("4.3\n")
    zapis.write("Numer wiersza z najwieksza liczba: " + str(numer_wiersza_z_najwieksza))
    zapis.write("\nNumer wiersza z najmniejsza liczba: " + str(numer_wiersza_z_najmniejsza))
    zapis.close()


liczby_binarne = wczytaj_dane_z_pliku()
zad_4_1(liczby_binarne)
zad_4_2(liczby_binarne)
zad_4_3(liczby_binarne)
print("Odpowiedzi zostaly zapisane do plikow")
