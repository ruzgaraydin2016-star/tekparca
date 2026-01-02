None

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir sakaya karsilik cevap.",
            "SHEESH":"onaylamamak.",
            "CREEPY":"korkunc.",
            "AGGRO": "agresiflesmek, sinirlenmek."
            }
print("hos geldiniz. bilmediginiz kelimeleri sorarak ne anlama geldigini ogrenebilirsiniz.")

for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
    else:
        print("boyle bir kelime bulunamadi.")
    # Kelime eşleşmiyorsa ne yapmalıyız?
