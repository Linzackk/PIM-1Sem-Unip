from util.arquivos import *
from util.estrutura import *
from util.estrutura import *
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

def ver_notas(usuario):
    from util.arquivos import abrir_dados
    from util.estrutura import menu
    from util.estrutura import titulo

    dados = abrir_dados()
    aluno = dados[usuario]
    semestres = ['1° Semestre', '2° Semestre']
    menu(semestres)
    esc = escolha(len(semestres))
    if esc == 0:
        titulo('1° SEMESTRE')
        print(f'Np1: {aluno["semestre1"][0]}\n'
              f'Np2: {aluno["semestre1"][1]}\n'
              f'Média: {aluno["semestre1"][2]}')
    elif esc == 1:
        titulo('2° Semestre')
        print(f'Np1: {aluno["semestre2"][0]}\n'
              f'Np2: {aluno["semestre2"][1]}\n'
              f'Média: {aluno["semestre2"][2]}\n')

def att_nota():
    from util.arquivos import abrir_dados
    from util.estrutura import menu
    from util.estrutura import titulo

    def atualizador(dados_alunos, sem="",prova=1, usuario=''):
        dados_aluno = dados_alunos[usuario]
        nota_semestre = dados_aluno[sem]

        nota = escolha(11)
        nota_semestre[prova - 1] = nota

        np1 = nota_semestre[0]
        np2 = nota_semestre[1]
        nota_semestre[2] = (np1 + np2) / 2

        dados_aluno[sem] = nota_semestre
        novos_dados = json.dumps(dados_alunos, indent=4)

        with open('alunos.json', 'w') as subs:
             subs.write(novos_dados)
             print(f'{cores["green"]}V{cores["0"]}')

    dados = abrir_dados()
    usuario = ''
    semestres = ['1° Semestre', '2° Semestre']
    notas = ['Np 1', 'Np 2']
    while usuario not in dados:
        usuario = str(input('Usuário do Aluno: '))
    dados_aluno = dados[usuario]
    menu(semestres)
    sem = escolha(len(semestres))
    if sem == 0:
        titulo('1° SEMESTRE')
        menu(notas)
        provas = escolha(len(notas))
        if provas == 0:
            atualizador(dados, "semestre1",1, usuario)
        elif provas == 1:
            atualizador(dados, "semestre1", 2, usuario)
    elif sem == 1:
        titulo('2° SEMESTRE')
        menu(notas)
        provas = escolha(len(notas))
        if provas == 0:
            atualizador(dados, "semestre2", 1, usuario)
        elif provas == 1:
            atualizador(dados, "semestre2", 2, usuario)
