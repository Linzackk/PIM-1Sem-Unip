from json import JSONDecodeError
from operator import index

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

def abrir_dados():
    with open('alunos.json', 'r') as file:
        lstPessoas = json.loads('\n'.join(file.readlines()))
    return lstPessoas

def verify_user(nomeSplit, usuario, funcao):
    with open('alunos.json', 'r') as file:
        try:
            lstPessoas = json.loads('\n'.join(file.readlines()))
        except JSONDecodeError:
            lstPessoas = {}
    cont = -1
    num = 1
    tamanho_nome = len(nomeSplit)
    while usuario in lstPessoas:
        if tamanho_nome <= 3:
            if nomeSplit[1] in 'DaDeDo':
                usuario = nomeSplit[0] + nomeSplit[-1] + str(num) + funcao
            else:
                usuario = nomeSplit[0] + nomeSplit[-1] + str(num) + funcao
        else:
            while usuario in lstPessoas and cont > -tamanho_nome:
                if nomeSplit[cont] not in 'DaDeDo':
                    usuario = nomeSplit[0] + nomeSplit[cont] + funcao
                    cont -= 1
                else:
                    cont -= 1
        num += 1
    return usuario

def add_conta():
     with open('alunos.json', 'r') as file:
         try:
            dict_db = json.loads('\n'.join(file.readlines()))
         except JSONDecodeError:
            dict_db = {}
     nomeCompleto = str(input('Nome COMPLETO do Aluno: '))
     nomeSplit = nomeCompleto.lower().title().split()
     job = str(input('Função: ')).upper()[0]
     senha = '123'
     tempo_uso = 0
     tempo_medio_uso = 0
     sessoes = 0
     nota1 = 0
     nota2 = 0
     media = 0
     usuario = nomeSplit[0] + nomeSplit[-1] + job
     usuario = verify_user(nomeSplit,usuario, job)
     dict_db[usuario] = {
         "senha": senha,
         "funcao": job,
         "nomeCompleto": nomeCompleto,
         "tempoUso": tempo_uso,
         "tempoMedio": tempo_medio_uso,
         "sessoes": sessoes,
         "semestre1": [0,0,0],
         "semestre2": [0,0,0],
         "media": media
     }
     login = json.dumps(dict_db,indent=4)

     with open('alunos.json', 'w') as file:
         file.write(login)
         print(f'{cores["green"]}Salvo com Sucesso!{cores["0"]}')

def att_hora(usuario, hrI, hrF):
    alunos = {}
    with open('alunos.json', 'r') as file:
        alunos = json.loads('\n'.join(file.readlines()))
    hr_total = abs(int(hrI - hrF))
    log = alunos[usuario]
    log["tempoUso"] += hr_total
    log["sessoes"] += 1
    log["tempoMedio"] = log["tempoUso"] / log["sessoes"]
    novo = json.dumps(alunos,indent=4)
    with open('alunos.json','w') as subs:
        subs.write(novo)
        print(f'{cores["green"]}V{cores["0"]}')

#def att_nota():

#def hr_aula():
