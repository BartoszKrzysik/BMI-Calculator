List = []
#lista z osobami
no_osob = int(input("Wpisz liczbe osob"))
a = float(2)
#no osbo, liczba osob i wykonan w petli
for i in range(no_osob):
    wzrost = "Wzrost="
    waga = "Waga="
    cale = "Cale="
    funty = "Funty="
    bmi = "BMI="
    #zmienne do zapisu w listach
    metrical_input = input(
        "Czy chcesz korzystac z jednostek metrycznych? yes/no")
    #z jakich jednostek korzystać
    if metrical_input.lower() == "yes":
        name = input("Wpisz nazwe/imie osoby (Wazne aby sie nie duplikowala z "
                     "poprzednimi)")
        imie = name
        name = []
        name.append(imie)
        #name jako nazwa listy + imię w arg0
        nazwisko = input("Wpisz nazwisko")
        name.append(nazwisko)
        #nazwisko jako kolejny argument
        plec = input("Wpisz plec K/M")
        name.append(plec)
        #kolejny argument plec
        height = float(input("Wpisz wzrost w centymetrach"))
        height = height / 100
        wzrost = wzrost + str(height)
        #wzrost w m, można zapisać jako czysta liczba
        name.append(wzrost)
        weight = float(input("Wpisz wage w kilogramach"))
        waga = waga + str(weight)
        #analogicznie jak wyżej
        name.append(waga)
        List.append(name)
        BMI = weight / height ** a
        #wzór na BMI
        bmi = bmi + str(BMI)
        name.append(bmi)
        #analogicznie do wzrostu
    elif metrical_input.lower() == "no":
        #przy jednostkach imperialnych analogicznie do metrycznych
        name = input("Wpisz nazwe/imie osoby (Wazne aby sie nie duplikowala z "
                     "poprzednimi)")
        imie = name
        name = []
        name.append(imie)
        nazwisko = input("Wpisz nazwisko")
        name.append(nazwisko)
        #nazwisko jako kolejny argument
        plec = input("Wpisz plec K/M")
        name.append(plec)
        #kolejny argument plec
        print("Wpisz wzrost")
        h_ft = float(input("Wpisz ilosc stop"))
        h_inch = float(input("Wpisz ilosc cali"))
        h_inch = 12 * h_ft + h_inch
        cale = cale + str(h_inch)
        name.append(cale)
        height = h_inch * 2.54
        height = height / 100
        wzrost = wzrost + str(height)
        name.append(wzrost)
        w_lb = float(input("Wpisz wage ciala w funtach"))
        funty = funty + str(w_lb)
        name.append(funty)
        weight = w_lb * 0.45359237
        waga = waga + str(weight)
        name.append(waga)
        BMI = weight / height ** a
        bmi = bmi + str(BMI)
        name.append(bmi)
        List.append(name)
import json
with open('Wyniki.txt', 'w') as f:
    f.write(json.dumps(List))
#zapisanie danych w txt
