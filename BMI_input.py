List = []

no_osob = int(input("Wpisz liczbe osob"))
a = float(2)

for i in range(no_osob):
    wzrost = "Wzrost="
    waga = "Waga="
    cale = "Cale="
    funty = "Funty="
    bmi = "BMI="
    metrical_input = input(
        "Czy chcesz korzystac z jednostek metrycznych? yes/no")
    if metrical_input.lower() == "yes":
        name = input("Wpisz nazwe/imie osoby (Wazne aby sie nie duplikowala z "
                     "poprzednimi)")
        imie = name
        name = []
        name.append(imie)
        height = float(input("Wpisz wzrost w centymetrach"))
        height = height / 100
        wzrost = wzrost + str(height)
        name.append(wzrost)
        weight = float(input("Wpisz wage w kilogramach"))
        waga = waga + str(weight)
        name.append(waga)
        List.append(name)
        BMI = weight / height ** a
        bmi = bmi + str(BMI)
        name.append(bmi)
    elif metrical_input.lower() == "no":
        name = input("Wpisz nazwe/imie osoby (Wazne aby sie nie duplikowala z "
                     "poprzednimi)")
        imie = name
        name = []
        name.append(imie)
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
print(List)
import json
with open('Wyniki.txt', 'w') as f:
    f.write(json.dumps(List))