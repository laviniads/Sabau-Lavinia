meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

#comenzi
for student in studenti:
    if not comenzi or not tavi:
        break

    comanda = comenzi.pop(0)
    tava = tavi.pop()
    istoric_comenzi.append(comanda)

    print(f"{student} a comandat {comanda}.")

#inventar
#numararea comenzilor
numar_comenzi = {produs: 0 for produs in ["papanasi", "ceafa", "guias"]}
for comanda in istoric_comenzi:
    numar_comenzi[comanda] +=1

#afisarea stocurilor
print(f"S-au comandat {numar_comenzi['guias']} guias, {numar_comenzi['ceafa']} ceafa, {numar_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
#verificarea stocurilor
print(f"Mai este ceafa: {numar_comenzi['ceafa']<3}.")
print(f"Mai sunt papanasi: {numar_comenzi['papanasi'] <10}.")
print(f"Mai sunt guias: {numar_comenzi['guias'] <6}.")

#finante
total_venit = sum([pret[1] for pret in preturi if pret[0] in istoric_comenzi])
print(f"Cantina a incasat: {total_venit} lei.")

produse_pret_cel_mult_7_lei = [pret for pret in preturi if pret[1] <=7]
print(f"Produse care costa cel mult 7 lei: {produse_pret_cel_mult_7_lei}.")