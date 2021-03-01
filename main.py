import pandas as pd
import glob

# Dez_20 = pd.read_csv('//10.1.17.4/Setores/Trade de Marketing/Inteligencia/BANCO_DE_DADOS/RODRIGO/ANS/2020/12/ben202012_AC.csv', sep=';')
# TODO Find path '//10.1.17.4/Setores/Trade de Marketing/Inteligencia/BANCO_DE_DADOS/RODRIGO/ANS/2020/12/ben202012_AC.csv'

path = '//10.1.17.4/Setores/Trade de Marketing/Inteligencia/BANCO_DE_DADOS/RODRIGO/ANS/2020/12/ben202012_AC.csv'
filenames = glob.glob(path + '/*.csv')

Dez_20 = pd.DataFrame()
df = pd.DataFrame()

for filename in filenames:
    df = pd.read_csv(filename, sep=';')
    Dez_20 = Dez_20.append(df)


if __name__ == '__main__':
    print(Dez_20)
