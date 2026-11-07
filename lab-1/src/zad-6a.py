import random


def main():
    print("Kalkulator paliwa (losowa droga 20-150)")
    droga = random.randint(20, 150)

    try:
        spalenie = float(input("Podaj średnie spalenie litra na 100km: "))
        cena_paliwa_za_l = float(input("Podaj cene paliwa za l: "))
    except ValueError:
        print("\nWprowadzona wartość jest błędna!")
        return

    spalono = droga * spalenie / 100

    print("")
    print("Droga:", droga, 'km')
    print("Spalono:", round(spalono, 2), "l")
    print("Koszt:", round(spalono * cena_paliwa_za_l, 2), "PLN")


main()
