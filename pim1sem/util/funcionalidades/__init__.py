from util import *
from util.estrutura import *
from util.arquivos import *

cores = {
    "0": "\033[m",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "green": "\033[1;32m"
}
import json

def funcao():
    while True:
        func = str(input('Aluno ou Professor: ')).upper()[0]
        if func not in 'AP':
            print(f'{cores["red"]}ERRO, INSIRA UM VALOR VÁLIDO.{cores["0"]}')
        else:
            break
    return func

def login():
    with open('alunos.json', 'r') as file:
        try:
            alunos: dict = json.loads('\n'.join(file.readlines()))
        except JSONDecodeError:
            print(f'{cores["red"]}NÃO HÁ ALUNOS CADASTRADOS!{cores["0"]}')
    while True:
        usuario = str(input('Insira o Usuário: '))
        password = str(input('Insira a Senha: '))
        if usuario not in alunos:
            print(f'{cores["red"]}USUÁRIO NÃO ENCONTRADO NO SISTEMA.{cores["0"]}')
        else:
            log = alunos[usuario]
            if "senha" not in log:
                print(f'{cores["red"]}ERRO, SENHA NÃO CADASTRADA!{cores["0"]}')
            elif log["senha"] != password:
                print(f'{cores["red"]}SENHA INVÁLIDA.{cores["0"]}')
            else:
                print(f'{cores["green"]}Logado com Sucesso{cores["0"]}')
                break

    return usuario

def escolha(n):
    while True:
        esc = int(input('Insira Sua Escolha: '))
        if 0 > esc or esc > n - 1:
            print(f'{cores["red"]}Escolha Inválida. {cores["0"]}')
        else:
            break
    return esc





