# wersja 1.0
wiek = input("Podaj wiek: ")
płeć = input("Wybierz płeć. Wpisz K dla płci żeńskiej, M dla męskiej oraz X jeśli nie chcesz podawać.")

if płeć == "K" or płeć == "M" or płeć =="X":
    pass
else:
    exit("Podaj oznaczenie płci jako K, M lub X.")

if wiek.isdigit() == False:
    exit("Wiek musi być liczbą całkowitą")
wiek = int(wiek)

if wiek >= 18 and wiek <= 40:
    print("Witaj w naszym sklepie")

elif wiek >= 40 and wiek <= 100:
    print("Witaj w naszym sklepie")
    print("W Twoim wieku alkohol jest niewskazany")

else:
    print("Jesteś za małody. Zapraszamy na Disney.com")

if wiek >= 30 and płeć == "K":
    print("GRATULACJE!!! WYGRAŁA PANI DARMOWY APEROL SPRITZ! DOBREJ ZABAWY")




