text = "Câteva sute de mineri protestează la Palatul Victoria, din cauza noii legi a pensiilor."
lungime=len(text)
mijloc=lungime//2
prima_jumatate = text[:mijloc]
a_doua_jumatate = text[mijloc:]

# 1
prima_jumatate = prima_jumatate.upper()
prima_jumatate = prima_jumatate.strip()

#2
a_doua_jumatate = a_doua_jumatate[::-1]
a_doua_jumatate = a_doua_jumatate.capitalize()
a_doua_jumatate  = a_doua_jumatate.replace(".","").replace(",","").replace("!","".replace("?",""))
# print(elimina_caracterele_de_punctuatie)
print(prima_jumatate + a_doua_jumatate)




