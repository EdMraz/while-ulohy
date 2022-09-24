print("napíš program, ktorý bude V CYKLE načítavať mená a "
      "vypisvať ich dĺžku dovtedy, poikiaľ ako meno nezdáte reťazec 'koniec'")

i = True

while i:
    meno = input("Zadaj meno: ")
    if meno != 'koniec':
        print("Počet písmen v mene:",len(meno))
    elif meno == 'koniec':
            i = False

print("Koniec programu.")
