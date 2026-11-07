def main():
    print("Przeliczenia")

    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
    except ValueError:
        print("\nWprowadzona wartość jest błędna!")
        return

    print("")
    print(f"Dodawanie: {a + b}")
    print(f"Odejmowanie: {a - b}")
    print(f"Mnożenie: {a * b}")
    if b != 0:
        print(f"Dzielenie: {a / b}")
    else:
        print("Dzielenie: Nie można dzielić przez 0")
    print(f"Potęgowanie: {a ** b}")


main()
