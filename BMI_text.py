def text(filepath):
    import csv #importuje bibliotekę do obsługi plików CSV


    with open(filepath) as csvfile:
        with open("arkuszwyniki.csv", mode='w') as f:
            reader = csv.reader(csvfile, delimiter=';') #komenda do zczytywania
            writer = csv.writer(f, delimiter=',', lineterminator='\n') #komenda do zapisywania
            wiersze = list(reader)
            naglowek = wiersze.pop(0)  # pomiń naglowek
            naglowek.append("BMI")
            writer.writerow(naglowek)
            for wiersz in wiersze:
                wzrost = float(wiersz[3]) / 100
                waga = float(wiersz[4])
                BMI = round(waga / (wzrost * wzrost), 2) #obliczanie BMI
                wiersz.append(str(BMI))
                writer.writerow(wiersz)
