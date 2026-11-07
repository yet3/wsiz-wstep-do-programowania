# 1)
print(type(1 + 2))
# <class 'int'> (liczba całkowita)
# wynik: 3
# operator: + (dodawanie)

# 2)
print(type(1 + 4.5))
# <class 'float'> (liczba zmiennoprzecinkowa)
# wynik: 5.5
# operator: + (dodawanie; dodanie int do float daje float)

# 3)
print(type(3 / 2))
# <class 'float'> (liczba zmiennoprzecinkowa)
# wynik: 1.5
# operator: / (dzielenie zmiennoprzecinkowe)

# 4)
print(type(4 / 2))
# <class 'float'> (liczba zmiennoprzecinkowa)
# wynik: 2.0
# operator: / (dzielenie zmiennoprzecinkowe)

# 5)
print(type(3 // 2))
# <class 'int'> (liczba całkowita)
# wynik: 1
# operator: // (dzielenie całkowite)

# 6)
print(type(-3 // 2))
# <class 'int'> (liczba całkowita)
# wynik: -2
# operator: // (dzielenie całkowite)

# 7)
print(type(11 % 2))
# <class 'int'> (liczba całkowita)
# wynik: 1
# operator: % (reszta z dzielenia)

# 8)
print(type(2 ** 10))
# <class 'int'> (liczba całkowita)
# wynik: 1024
# operator: ** (potęgowanie)

# 9)
print(type(8 ** (1/3)))
# <class 'float'> (liczba zmiennoprzecinkowa)
# wynik: 2.0
# operator: ** (potęgowanie)


# 1)
print(int(3.0))
# wynik: 3
# działanie: konwersja liczby zmiennoprzecinkowej na całkowitą

# 2)
print(float(3))
# wynik: 3.0
# działanie: konwersja liczby całkowitej na zmiennoprzecinkową

# 3)
print(float("3"))
# wynik: 3.0
# działanie: konwersja tekstu na liczbę

# 4)
print(str(12.4))
# wynik: "12.4"
# działanie: konwersja liczby na tekst

# 5)
print(bool(0))
# wynik: False
# działanie: konwersja liczby na wartość logiczną (0 -> False)
