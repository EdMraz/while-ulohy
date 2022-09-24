print("načítavaj čísla dovtedy, pokiaľ nenačítaš číslo väčšie ako 100. Ak sa to stane, "
      "program skončí a vypíše celkový počet načítaných čísel")

x = 0
vstup = 0

while vstup <= 100:
    vstup = int(input("Zadaj číslo: "))
    x+=1
print("Počet načítaných čísel:",x)
