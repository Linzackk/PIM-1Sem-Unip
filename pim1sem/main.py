from time import time, sleep
import os

import util.estrutura as est
import util.funcionalidades as fun
import util.arquivos as arq

# Fazer para Rodar em um CMD (Limpando o Terminal a Cada mudança de Página)
alunos = arq.abrir_dados()
while True:
    usuario = ''
    est.titulo('PLATAFORMA EDUCACIONAL DIGITAL')

    while True:
        usuario = fun.login()
        if usuario in alunos:
            break
    os.system('cls')

    #Começar a Contar o Inicio de Tempo.
    hora_login = time()
    log = alunos[usuario]

    e = -1
    if log["funcao"] == 'AL': # Menu Alunos
        while e != len(est.menu_aluno) - 1:
            est.titulo('ÁREA DO ALUNO')
            est.menu(est.menu_aluno)
            e = fun.escolha(len(est.menu_aluno))
            if e == 0:
                print()
                #faz abrir o arquivo das video aulas se der
            elif e == 1:
                fun.ver_notas(usuario)
                #mostra as notas
                os.system('cls')
            elif e == 2:
                fun.ver_grade(log["curso"])
                #mostrar Grade Curricular
                os.system('cls')
            elif e == 3:
                arq.alterar_senha(alunos, usuario)
                os.system('cls')

    elif log["funcao"] == 'PR': # Menu Professor
        while e != len(est.menu_prof) - 1:
            est.titulo('ÁREA DO PROFESSOR')
            est.menu(est.menu_prof)
            e = fun.escolha(len(est.menu_prof))
            if e == 0:
                fun.att_nota()
                os.system('cls')
            elif e == 1:
                print()
                #hr_aula()
                os.system('cls')
            elif e == 2:
                arq.alterar_senha(alunos, usuario)
                os.system('cls')

    elif log["funcao"] == 'AD': # Menu Admistrativo
        while e != len(est.menu_adm) - 1:
            est.titulo('ADMINISTRAÇÃO')
            est.menu(est.menu_adm)
            e = fun.escolha(len(est.menu_adm))
            if e == 0:
                arq.add_conta()
                os.system('cls')

    print(f'Deslogando..')
    hora_logoff = time()
    arq.att_hora(usuario, hora_login, hora_logoff)
