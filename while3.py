print("napíš program, ktorý bude V CYKLE načítavať mená a "
      "vypisvať ich dĺžku dovtedy, poikiaľ ako meno nezdáte reťazec 'koniec'")

while True:
    meno = input("Zadaj meno: ")
    if meno == 'koniec':
        break
    print("Počet písmen v mene:",len(meno))

print("Koniec programu.")
