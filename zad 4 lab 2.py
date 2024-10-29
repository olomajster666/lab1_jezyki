import numpy as np
from functools import reduce

def wczytaj_macierze():
    """Funkcja wczytująca macierze od użytkownika i zwracająca listę macierzy."""
    macierze = []
    while True:
        rozmiar = input("Podaj rozmiar macierzy (np. 2x2, 3x3) lub 'stop' aby zakończyć: ")
        if rozmiar.lower() == 'stop':
            break
        try:
            wiersze, kolumny = map(int, rozmiar.split('x'))
            print(f"Wprowadz macierz {wiersze}x{kolumny}:")
            macierz = []
            for i in range(wiersze):
                wiersz = list(map(float, input(f"Wiersz {i+1}: ").split()))
                if len(wiersz) != kolumny:
                    raise ValueError("Nieprawidłowa liczba kolumn w wierszu.")
                macierz.append(wiersz)
            macierze.append(np.array(macierz))
        except ValueError as e:
            print("Błąd:", e)
    return macierze

def wczytaj_operacje():
    """Funkcja wczytująca operację jako wyrażenie od użytkownika."""
    operacja = input("Podaj operację (użyj 'a' i 'b' dla macierzy): ")
    return lambda a, b: eval(operacja)

def wykonaj_operacje_na_macierzach(macierze, operacja):
    """Funkcja łącząca macierze za pomocą operacji przy użyciu reduce()."""
    wynik = reduce(operacja, macierze)
    return wynik

def main():
    macierze = wczytaj_macierze()
    if not macierze:
        print("Brak macierzy do połączenia.")
        return
    print("Dostępne operacje: a + b, a - b, a * b (mnożenie elementów), np.dot(a, b) (mnożenie macierzy)")
    operacja = wczytaj_operacje()
    try:
        wynik = wykonaj_operacje_na_macierzach(macierze, operacja)
        print("Wynik operacji na macierzach:")
        print(wynik)
    except Exception as e:
        print("Błąd podczas wykonywania operacji:", e)

if __name__ == "__main__":
    main()
