print("napíš program, ktorý bude načítavať čísla dovtedy pokiiaľ nezadáte nulu. "
      "Na záver program vypíše aritmetický priemer týchto čísel. Nulu do priemeru nezahrňte")

i = True
counter = 0
a = 0

while i:
    num = int(input("Zadaj číslo: "))
    if num != 0:
        a += num
        counter += 1
    else:
        i = False

print("Aritmetický priemer zadaných čísel je:", a/counter)
