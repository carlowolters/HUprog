getallenrij= [2, 4, 6, 8, 10, 9, 7]
zoekgetal = eval(input('voer een getal in:'))
gevonden='false'
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = 'true'
print(gevonden)

