meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XOX": "Besos y abrazos",
            "CHEVERE": "Algo genial",
            }


user = input("¿Que palabra desea consultar?").upper()

if user in meme_dict.keys():
    print(meme_dict[user])
else:
    print("La palabrabra no esta registrada")
