from time import time, sleep
from util.estrutura import *
from util.arquivos import *
from util.funcionalidades import *
from util import *
cores = {
    "0": "\033[m",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "green": "\033[1;32m"
}
#add_conta()
att_nota()
#ver_notas('IsaacMedeirosA')
# Fazer para Rodar em um CMD (Limpando o Terminal a Cada mudança de Página)
alunos = abrir_dados()
usuario = ''
titulo('PLATAFORMA EDUCACIONAL DIGITAL')

while True:
    usuario = login()
    if usuario in alunos:
        break
hora_login = time()
log = alunos[usuario]
    #Começar a Contar o Inicio de Tempo.
e = -1
while True:
    if log["funcao"] == 'A':
        opc = ['Video-Aulas', 'Notas', 'Grade Curricular', 'Sair']
        titulo('ÁREA DO ALUNO')
        menu(opc)
        e = escolha(len(opc))
        if e == len(opc) - 1:
            break
        elif e == 0:
            print()
            #faz abrir o arquivo das video aulas se der
        elif e == 1:
            ver_notas(usuario)
            #mostra as notas
        elif e == 2:
            print()
            #mostrar Grade Curricular


    if log["funcao"] == 'P':
        opc = ['Adicionar Aluno', 'Atribuir Notas', 'Horário de Aulas', 'Sair']
        titulo('ÁREA DO PROFESSOR')
        menu(opc)
        e = escolha(len(opc))
        if e == len(opc) - 1:
            break
        elif e == 0:
            add_conta()
        elif e == 1:
            att_nota()
        elif e == 2:
            print()
            #hr_aula()



print(f'{cores["red"]}Encerrando, volte sempre.{cores["0"]}')
hora_logoff = time()
att_hora(usuario, hora_login, hora_logoff)

    # Contar o Horario de Saída.


# Quando logado contar a hora de login
# Quando der Logout contar a hora de logout
# Tempo de uso da plataforma é o (hora de login - hora de logout)

# No login precisa de usuário e senha
# Terão Usuários: Aluno e Professor
# Certos usuarios tem acessos diferentes

# Usuário Aluno vai ter acesso a:
    # VideoAulas, Notas (1 sem, 2 sem, media), Grade (opcional)

# Usuário Professor vai ter acesso a:
    # Adicionar novos alunos.
    # Definir notas (opcional)
    
