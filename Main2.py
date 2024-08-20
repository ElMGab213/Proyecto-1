meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREPPY": "Aterrador o siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "XD": "Se responde cuando hay algo gracioso"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print([meme_dict])
else:
   print ("Perdon, no se encontro tu palabra")
