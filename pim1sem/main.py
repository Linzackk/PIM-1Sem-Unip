from util.estrutura import *
from util.arquivos import *
from util.funcionalidades import *
cores = {
    "0": "\033[m",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "green": "\033[1;32m"
}

# Fazer para Rodar em um CMD (Limpando o Terminal a Cada mudança de Página)

titulo('PLATAFORMA EDUCACIONAL DIGITAL')
login = login()
if login in 'AP':
    #Começar a Contar o Inicio de Tempo.
    while True:
        if login == 'A':
            opc = ['Video-Aulas', 'Notas', 'Grade Curricular', '']
            titulo('ÁREA DO ALUNO')
            menu(opc)
            e = escolha(len(opc))
            if not e:
                break

        else:
            opc = ['Adicionar Aluno', 'Atribuir Notas', 'Horário de Aulas', 'Sair']
            titulo('ÁREA DO PROFESSOR')
            menu(opc)
            e = escolha(len(opc))
            print(e)

if login not in 'AP':
    print(f'{cores["red"]}ERRO, FUNCAO NÃO VALIDADA.{cores["0"]}')
else:
    print(f'{cores["red"]}Encerrando, volte sempre.{cores["0"]}')
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
    
