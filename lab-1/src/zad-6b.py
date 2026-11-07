CENA_PALIWA_ZA_L = 6.5


def main():
    print("Kalkulator paliwa")

    try:
        droga = float(input("Podaj przebytą drogę (km): "))
        spalenie = float(input("Podaj średnie spalenie litra na 100km: "))
    except ValueError:
        print("\nWprowadzona wartość jest błędna!")
        return

    spalono = droga * spalenie / 100

    print("")
    print(f"Spalono: {round(spalono, 2)} l")
    print(f"Koszt: {round(spalono * CENA_PALIWA_ZA_L, 2)} PLN")


main()
