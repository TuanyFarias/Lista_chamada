from sklearn.preprocessing import LabelEncoder
from sqlalchemy import create_engine
import pandas as pd
from datetime import date
import locale


# Tratamento de dados
usuario = 'root'
senha = 'cabracega321'
host = 'localhost'
banco = 'alunos'
banco2 = 'calendario'

engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}')
engine2 = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco2}')

df_chamada = pd.read_sql('SELECT * FROM alunos_dados', con=engine)
df_chamada.drop(labels= ['Idade', 'Email'], axis=1, inplace=True)
print(df_chamada)
df_chamada.to_sql('chamada', con=engine, index=False, if_exists='replace')


df_cronograma = pd.read_sql('SELECT * FROM calendario', con=engine)
df_cronograma['calendario'] = pd.to_datetime(df_cronograma['Data_mes'], dayfirst=True, errors='coerce')
print (df_cronograma.head())

label_enconder = LabelEncoder()
df_chamada['Numero'] = label_enconder.fit_transform(df_chamada['id']) + 1
df_chamada.drop(labels= ['id'], axis = 1, inplace=True)
print(df_chamada)


# Reconhecimento e registro do dia de hoje
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
except:
    locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')

hoje = date.today()
dia_semana = hoje.strftime('%A').lower()
dia_semana = dia_semana.capitalize()

df_alunos = pd.read_sql("SELECT Nome FROM alunos_dados", con=engine)
query_aulas = f"SELECT * FROM aulas WHERE dia_da_semana = '{dia_semana}'"
df_aulas_dia = pd.read_sql(query_aulas, con=engine)

if df_aulas_dia.empty:
   print(f" Nenhuma aula cadastrada para {dia_semana}.")

print(f"Aulas de hoje ({dia_semana}):")
print(df_aulas_dia)

# Input dos alunos faltantes
entrada = input("Digite os nomes dos alunos que faltaram separados por vírgula: ")
faltaram_hoje = [nome.strip() for nome in entrada.split(',') if nome.strip()]
presencas_gerais = []

# função de faltas/presenças
for col in df_aulas_dia.columns:
    if col.startswith('aula') and pd.notna(df_aulas_dia.iloc[0][col]):
        materia = df_aulas_dia.iloc[0][col]
        for _, row in df_alunos.iterrows():
            aluno = row['Nome']
            estado = 'F' if aluno in faltaram_hoje else 'P'
            presencas_gerais.append({
                'aluno_nome': aluno,
                'data_mes': hoje,
                'aulas': materia,
                'estado': estado
            })

df_presencas = pd.DataFrame(presencas_gerais)

#Printa o nome e as aulas que os alunos faltaram
df_presencas.to_sql('presencas', con=engine, index=False, if_exists='append')
print(f"✅ Presenças registradas para {dia_semana}, {hoje.strftime('%d/%m/%Y')}.")
print(f" Os alunos {faltaram_hoje} perderam as seguintes aulas:\n {df_aulas_dia.head(1)}")
