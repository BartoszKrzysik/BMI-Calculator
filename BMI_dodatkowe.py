def wypisz(limit):
    import csv

    with open('arkuszwyniki.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    dlugosc = len(data)
    i = 1
    while i < dlugosc:
        if float(data[i][5]) >= limit:
            print(data[i][0], data[i][1], "ma bmi wieksze niz", limit, "wynoszace:",data[i][5] ,"\n")

        i = i + 1
