print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")

try:
    vastus = input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
    
    if vastus == "1":
        pikkus = int(input("Sisesta oma pikkus (cm): "))
        mass = float(input("Sisesta oma kaal (kg): "))
        indeks = mass / (0.01 * pikkus) ** 2
        print(nimi + "! Sinu keha indeks on:", indeks)

        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Alakaal")
        elif 19 <= indeks < 25:
            print("Normaalkaal")
        elif 25 <= indeks < 30:
            print("Ülekaal")
        elif 30 <= indeks < 35:
            print("Rasvumine")
        elif 35 <= indeks < 40:
            print("Tugev rasvumine")
        elif indeks >= 40:
            print("Tervisele ohtlik rasvumine")
    else:
        print("Kahju! See on väga kasulik info!")
        print("")
    
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

except ValueError:
    print("Vale sisend! Palun sisesta sobivad väärtused.")
