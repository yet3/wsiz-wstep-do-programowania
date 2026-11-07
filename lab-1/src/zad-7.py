def main():
    print("Rozwiązywanie równania ax + b = 0")

    try:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
    except ValueError:
        print("\nWprowadzona wartość jest błędna!")
        return

    print("")
    if a != 0:
        x = -b/a
        print(f"Równanie ma jedno rozwiązanie: x = {x}")
    else:
        if b == 0:
            print(
                "Równanie ma nieskończenie wiele rozwiązań")
        else:
            print("Równanie nie posiada żadnych rozwiązań")


main()
