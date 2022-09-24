print("načítavaj čísla dovtedy, pokiaľ ich súčet nepresiahne hodnotu 100. Program vypíše hodnotu tohto súčtu a aj počet čísel")

x = 0
y = 0
vstup = 0

while x <= 100:
    vstup = int(input("Zadaj číslo: "))
    x+=vstup
    y+=1
print("Súčet načítaných čísel je:",x,"a počet načítaných čísel:",y)
