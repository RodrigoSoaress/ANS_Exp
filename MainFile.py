import pandas as pd
import glob
from pathlib import Path

# Importação dos arquivos da ANS - Maquina do Escritório
# Paths - 1 Rede 2 Local
# glob_path = Path("//10.1.17.4/Setores/Trade de Marketing/Inteligencia/BANCO_DE_DADOS/RODRIGO/ANS/2020/12/")
glob_path = Path("D:/Arquivos/2020/12")

file_list = [str(pp) for pp in glob_path.glob("**\*.csv")]
Dez_20 = pd.DataFrame()
df = pd.DataFrame()

for filename in file_list:
    df = pd.read_csv(filename, sep=';')
    df = df.drop(columns=['DT_CARGA'])
    Dez_20 = Dez_20.append(df, ignore_index=True)

if __name__ == '__main__':
    # remember defining a var to receive the info
    print(Dez_20.describe(include='all'))
