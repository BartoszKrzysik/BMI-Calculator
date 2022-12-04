def text(filepath):
    import csv

    # filepath = "pomiary2.csv"

    with open(filepath) as csvfile:
        with open("arkuszwyniki.csv", mode='w') as f:
            reader = csv.reader(csvfile, delimiter=';')
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            wiersze = list(reader)
            naglowek = wiersze.pop(0)  # pomiń naglowek
            naglowek.append("BMI")
            writer.writerow(naglowek)
            for wiersz in wiersze:
                wzrost = float(wiersz[3]) / 100
                waga = float(wiersz[4])
                BMI = round(waga / (wzrost * wzrost), 2)
                wiersz.append(str(BMI))
                writer.writerow(wiersz)
