import pandas as pd


dados = {"Nome": ["Wendel", "Paulo", "Mikaias", "Gersoney", "Fernando"],
        "idade": [20, 20, 21, 25, 23],
        "cidade" : ["Camaçari", "Feira de santana", "Berimbal", "Catu de Abrante", "Jauá"]
        }
df = pd.DataFrame(dados)
#print(df)

for dado in df.values:
        #print(dado)
        print(dado[0], dado[1], dado[2]) 