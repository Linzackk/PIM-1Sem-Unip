menu_aluno = ['Video-Aulas', 'Notas', 'Grade Curricular', 'Alterar Senha', 'Sair']
menu_prof = ['Atribuir Notas', 'Horário de Aulas', 'Alterar Senha', 'Sair']
menu_adm = ['Adicionar Conta', 'Alterar Senhas', 'Sair'] #outras configs

def linha(tam):
    print('-' * (tam + 4))

def titulo(msg=''):
    linha(len(msg))
    print(msg.center(len(msg)))
    linha(len(msg))

def menu(lst):
    cont = 0
    linha(26)
    for c in lst:
        print(f'[ {cont} ] - {c}')
        cont += 1
    linha(26)

