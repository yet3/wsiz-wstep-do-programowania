import math


def main():
    print("Rozwiązywanie równania ax^2 + bx + c = 0")

    try:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        c = float(input("Podaj c: "))
    except ValueError:
        print("\nWprowadzona wartość jest błędna!")
        return

    print("")

    if a == 0:
        if b != 0:
            x = -c/b
            print(f"Równanie ma jedno rozwiązanie: x = {x}")
        else:
            if c == 0:
                print(
                    "Równanie ma nieskończenie wiele rozwiązań")
            else:
                print("Równanie nie posiada żadnych rozwiązań")
        return

    delta = b ** 2 - 4 * a * c

    if delta == 0:
        x = -b / (2 * a)
        print(f"Równanie ma jedno rozwiązanie: x = {x}")
    elif delta > 0:
        x_1 = (-b + math.sqrt(delta)) / (2 * a)
        x_2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Równanie ma dwa rozwiązania: x = {x_1} i x = {x_2}")
    else:
        print("Równanie nie posiada żadnych rozwiązań")


main()
