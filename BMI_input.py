import csv
# import bibliotek

def wsadzanie():
    List = []
    # lista z osobami
    no_osob = int(input("Wpisz liczbe osob: "))
    a = float(2)
    # no osbo, liczba osob i wykonan w petli
    for i in range(no_osob):
        # zmienne do zapisu w listach
        metrical_input = input(
            "Czy chcesz korzystac z jednostek metrycznych? yes/no ")
        # z jakich jednostek korzystać
        if metrical_input.lower() == "yes":
            name = input("Wpisz imie osoby (Wazne aby sie nie duplikowala z "
                         "poprzednimi): ")
            imie = name
            name = []
            name.append(imie)
            # name jako nazwa listy + imię w arg0
            nazwisko = input("Wpisz nazwisko: ")
            name.append(nazwisko)
            # nazwisko jako kolejny argument
            plec = input("Wpisz plec K/M ")
            name.append(plec)
            # kolejny argument plec
            height = float(input("Wpisz wzrost w centymetrach: "))
            height = height / 100
            wzrost = str(height)
            # wzrost w m, można zapisać jako czysta liczba
            name.append(wzrost)
            weight = float(input("Wpisz wage w kilogramach: "))
            waga = str(weight)
            # analogicznie jak wyżej
            name.append(waga)
            List.append(name)
            BMI = weight / height ** a
            # wzór na BMI
            bmi = str(BMI)
            name.append(bmi)
            # analogicznie do wzrostu
        elif metrical_input.lower() == "no":
            # przy jednostkach imperialnych analogicznie do metrycznych
            name = input("Wpisz imie osoby (Wazne aby sie nie duplikowala z "
                         "poprzednimi): ")
            imie = name
            name = []
            name.append(imie)
            nazwisko = input("Wpisz nazwisko: ")
            name.append(nazwisko)
            # nazwisko jako kolejny argument
            plec = input("Wpisz plec K/M ")
            name.append(plec)
            # kolejny argument plec
            print("Wpisz wzrost")
            h_ft = float(input("Wpisz ilosc stop: "))
            h_inch = float(input("Wpisz ilosc cali: "))
            h_inch = 12 * h_ft + h_inch
            cale = str(h_inch)
            name.append(cale)
            height = h_inch * 2.54
            height = height / 100
            w_lb = float(input("Wpisz wage ciala w funtach: "))
            funty = str(w_lb)
            name.append(funty)
            weight = w_lb * 0.45359237
            BMI = weight / height ** a
            bmi = str(BMI)
            name.append(bmi)
            List.append(name)
    Details = ['Imie', 'Nazwisko', 'Plec', 'Wzrost', 'Waga', 'BMI']
    rows = List
    with open('arkuszwyniki.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(Details)
        write.writerows(rows)
    # zapisanie danych w csv
