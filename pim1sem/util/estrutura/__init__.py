menu_aluno = ['Video-Aulas', 'Notas', 'Grade Curricular', 'Alterar Senha', 'Sair']
menu_prof = ['Atribuir Notas', 'Horário de Aulas', 'Alterar Senha', 'Sair']
menu_adm = ['Adicionar Conta', 'Alterar Senhas', 'Sair'] #outras configs

def linha(tam):
    """
    Cria uma string com '-' do tamanho requisitado
    :param tam: Tamanho do Texto para formatação.
    :return: A linha com o Tamanho requisitado + 4 algarismos '-'.
    """
    print('-' * (tam + 4))

def titulo(msg=''):
    """
    Cria uma mensagem formatada com Linha em Cima, Mensagem Centralizada, Linha em Baixo.
    :param msg: Mensagem a ser escrita formatada.
    :return: Uma print da mensagem.
    """
    linha(len(msg))
    print(msg.center(len(msg)))
    linha(len(msg))

def menu(lst):
    """
    Cria um menu com numero e os itens de uma lista
    :param lst: A lista com as opções para a lista
    :return: Um print formatado com número referente a opção e a opção
    """
    cont = 0
    linha(26)
    for c in lst:
        print(f'[ {cont} ] - {c}')
        cont += 1
    linha(26)
