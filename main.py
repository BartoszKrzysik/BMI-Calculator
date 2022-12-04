from BMI_input import wsadzanie
from bmi_chart import chart
from BMI_text import text

wybor = input("Czy chcesz wprowadzic swoj plik .cvs? yes/no")
if wybor.lower() == "yes":
    path = input("Podaj sciezke do pliku")
    text(path)
    chart()
elif wybor.lower() == "no":
    print("wprowadz dane recznie: ")
    wsadzanie()
    chart()

