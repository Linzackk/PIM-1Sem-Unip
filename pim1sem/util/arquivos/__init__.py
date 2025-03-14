from json import JSONDecodeError
from util.estrutura import *
from util.funcionalidades import *
from util import *
cores = {
    "0": "\033[m",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "green": "\033[1;32m"
}
import json
try:
    a = open('alunos.json', 'r')
except FileNotFoundError:
    a = open('alunos.json', 'x')
finally:
    a.close()

def add_conta():
     with open('alunos.json', 'r') as file:
         try:
            dict_db = json.loads('\n'.join(file.readlines()))
         except JSONDecodeError:
            dict_db = {}
     nomeCompleto = str(input('Nome COMPLETO do Aluno: '))
     nomeSplit = nomeCompleto.lower().title().split()
     job = funcao()
     senha = '123'
     tempo_uso = 0
     tempo_medio_uso = 0
     sessoes = 0
     nota1 = 0
     nota2 = 0
     media = 0

     usuario = nomeSplit[0] + nomeSplit[-1] + job
     dict_db[usuario] = {
         "senha": senha,
         "funcao": job,
         "nomeCompleto": nomeCompleto,
         "tempoUso": tempo_uso,
         "tempoMedio": tempo_medio_uso,
         "sessoes": sessoes,
         "notaSemestre1": nota1,
         "notaSemestre2": nota2,
         "media": media
     }
     login = json.dumps(dict_db)
     with open('alunos.json', 'w') as file:
        file.write(login)
        print(f'{cores["green"]}Salvo com Sucesso!{cores["0"]}')



