from BMI_input import wsadzanie
from bmi_chart import chart
from BMI_text import text
from BMI_dodatkowe import wypisz

wybor = input("Czy chcesz wprowadzic swoj plik .cvs? yes/no ")
if wybor.lower() == "yes":
    path = input("Podaj sciezke do pliku")
    text(path)
    chart()
elif wybor.lower() == "no":
    print("wprowadz dane recznie: ")
    wsadzanie()
    chart()
wybor2 = input("Czy chcesz wypisac osoby powyzej pewnego BMI? yes/no ")
if wybor2.lower() == "yes":
    limit = float(input("Podaj wartosc BMI \n"))
    wypisz(limit)
