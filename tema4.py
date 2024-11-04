# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

#Interfata joc
print("Bine ai venit la jocul Spanzuratoarea!")
print("Cuvantul de ghicit: " + " ".join(progres))
print(f"Incercari ramase: {incercari_ramase}")

#Rationament
while "_" in progres and incercari_ramase > 0:
    #introducere litera
    litera = input("Introdu o litera: ").lower()

    if len(litera) != 1 or not litera.isalpha():
       print("Te rog sa introduci o litera valida.")
       continue

    if litera in litere_incercate:
       print("Incearca alta litera.")
       continue
#Evitarea duplicatelor si urmarirea progresului
    litere_incercate.append(litera)
#Verificarea literei in cuvant
    if litera in cuvant_de_ghicit:
        for idx, chr in enumerate(cuvant_de_ghicit):
            if chr == litera:
                progres[idx] = litera
        print("Bravo! Litera se afla in cuvant.")
    else:
        incercari_ramase -= 1
        print(f"Litera nu se afla in cuvant. Incercarile ramase sunt: {incercari_ramase}")
#Afisare progres si incercari ramase
    print("Cuvantul de ghicit este: " + " ".join(progres))
    print(f"Incercari ramase: {incercari_ramase}")
#Final joc
if "_" not in progres:
    print(f"Felicitari! Ai ghicit cuvantul: {cuvant_de_ghicit}!")
else:
    print(f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}.")


