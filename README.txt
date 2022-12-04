# BMI-Calculator


Współczynnik powstały przez podzielenie masy ciała podanej w kilogramach przez kwadrat wysokości podanej w metrach. Klasyfikacja (zakres wartości) wskaźnika BMI została opracowana wyłącznie dla dorosłych i nie może być stosowana u dzieci. Dla oceny prawidłowego rozwoju dziecka wykorzystuje się siatki centylowe, które powinny być dostosowane dla danej populacji.
 
Oznaczanie wskaźnika masy ciała ma znaczenie w ocenie zagrożenia chorobami związanymi z nadwagą i otyłością, np. cukrzycą, chorobą niedokrwienną serca, miażdżycą. Przyjmuje się, że wyższe wartość BMI wiążą się ze zwiększonym ryzykiem dla zdrowia i życia[4].

Zakresy BMI:

poniżej 16 - wygłodzenie
16 - 16.99 - wychudzenie
17 - 18.49 - niedowagę
18.5 - 24.99 - wagę prawidłową
25.0 - 29.9 - nadwagę
30.0 - 34.99 - I stopień otyłości
35.0 - 39.99 - II stopień otyłości
powyżej 40.0 - otyłość skrajną



Bartosz Krzysik
Jakub Kochana
Hubert Gołda
Grzegorz Kawecki


import csv

filepath = "C:\\Users\\huber\\OneDrive\\Documents\\_Studia\\I semestr\\Podstawy Informatyki\\pomiary2.csv"

with open(filepath) as csvfile:
    with open("arkuszwyniki.csv", mode='w') as f:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';', lineterminator = '\n')
        wiersze = list(reader)
        naglowek = wiersze.pop(0) # pomiń naglowek
        naglowek.append("BMI")
        writer.writerow(naglowek)
        for wiersz in wiersze:
            wzrost = float(wiersz[3]) / 100
            waga = float(wiersz[4])
            BMI = round(waga / (wzrost * wzrost),2)
            wierszwynikowy = wiersz.append(str(BMI))
            writer.writerow(wiersz)

