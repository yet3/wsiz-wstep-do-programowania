def main():
    print("Kalkulator pola i obwódu prostokąta")

    try:
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
    except ValueError:
        print("\nWprowadzona wartość jest błędna!")
        return

    p = a * b
    obw = 2 * a + 2 * b

    print("")
    print(f"Pole prostokąta to: {p}")
    print(f"Obwód prostokąta to: {obw}")


main()
