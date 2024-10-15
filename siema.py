# podział paczek
def podzialpaczek(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"waga paczki przekracza maksymalną wagę")

    wagi_sorted = sorted(wagi, reverse=True)
    kursy = []

    for waga in wagi_sorted:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy

wagi = [10, 15, 5, 10, 20, 7, 8]
max_waga = 25
liczba_kursów, kursy = podzialpaczek(wagi, max_waga)
print(f"Liczba kursów: {liczba_kursów}")
for i, kurs in enumerate(kursy, 1):
    print(f"Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg")
