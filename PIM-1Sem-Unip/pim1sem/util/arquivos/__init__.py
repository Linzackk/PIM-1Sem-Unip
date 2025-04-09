from json import JSONDecodeError
import json
import pim1sem.util.estrutura as est

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

def verify_user(nomeCompleto, usuario, funcao):
    with open('alunos.json', 'r') as file:
        try:
            lstPessoas = json.loads('\n'.join(file.readlines()))
        except JSONDecodeError:
            lstPessoas = {}

    usuario = usuario.lower()
    print(nomeCompleto)
    nomeSplit = nomeCompleto.lower().split()
    print(nomeSplit)
    funcao = funcao.lower()
    cont = -1
    num = 1
    tamanho_nome = len(nomeSplit)

    while usuario in lstPessoas:
        if tamanho_nome <= 3:
            if nomeSplit[1] in 'dadedo':
                usuario = nomeSplit[0] + nomeSplit[-1] + str(num) + funcao
        else:
            while usuario in lstPessoas and cont > -tamanho_nome:
                if nomeSplit[cont] not in 'dadedo':
                    usuario = nomeSplit[0] + nomeSplit[cont] + funcao
            cont -= 1
        num += 1
    print(usuario)
    return usuario.lower()

def add_conta():
     with open('alunos.json', 'r') as file:
         try:
            dict_db = json.loads('\n'.join(file.readlines()))
         except JSONDecodeError:
            dict_db = {}
     est.titulo('REGISTRO DE CONTAS')
     nomeCompleto = str(input('Nome COMPLETO: ')).title()
     nomeSplit = nomeCompleto.lower().title().split()
     job = str(input('Função: ')).upper()[0:2]  # Aluno ou Professor (pega apenas a primeira letra) > Adicinar depois ADM para adicionar alunos, mexer em grades, aulas etc.
     if job == 'AL':
        curso = str(input('Curso: '))
     else:
        curso = ''
     # Categorias de cada aluno
     senha = '123' # Senha da conta, padrão para todos > Adicionar uma criptografia básica para a senha > Fazer uma configuração para trocar a senha
     tempo_uso = 0 # Tempo total do uso do usuário na plataforma (contabilizado do Login até o Logoff) > contabilizar também na interrupção do sistema
     sessoes = 0 # Quantidade de sessões logadas na plataforma
     tempo_medio_uso = 0 # Tempo médio do uso (Tempo total / Sessões)
     semestre1 = [0,0,0] # Notas NP1, NP2 e Média no 1° Semestre
     semestre2 = [0,0,0] # Notas NP1, NP2 e Média no 2° Semestre
     usuario = nomeSplit[0] + nomeSplit[-1] + job # Usuário do Aluno (pode-se mudar por um RA usando alguma criptografia ou alguma base (hexadecimal?)
     usuario = verify_user(nomeCompleto,usuario, job) # Verifica se o Usuário já existe.
     dict_db[usuario] = {
         "senha": senha,
         "funcao": job,
         "curso": curso,
         "nomeCompleto": nomeCompleto,
         "tempoUso": tempo_uso,
         "tempoMedio": tempo_medio_uso,
         "sessoes": sessoes,
         "semestre1": semestre1,
         "semestre2": semestre2,
     }
     login = json.dumps(dict_db,indent=4)

     with open('alunos.json', 'w') as file:
         file.write(login)
         print(f'Salvo com Sucesso!')

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
        print(f'V')

def alterar_senha(lst, usuario):
    log = lst[usuario]
    password = ''
    print(f'Caso não lembre sua senha, informe o Admistrativo.')
    while password != log["senha"]:
        password = str(input('Insira a Senha atual: (Digite SAIR para voltar) ')).strip()
        if password == 'SAIR':
            break
        elif password != log["senha"]:
            print('Senha Inválida.')
        else:
            nova_senha = str(input('Nova senha: '))
            print(f'Sua nova senha será: "{nova_senha}"')
            log["senha"] = nova_senha
            print(log["senha"])
            novo = json.dumps(lst, indent=4)
            with open('alunos.json', 'w') as subs:
                subs.write(novo)
                print(f'V')
            est.linha(16)
            input('Insira qualquer coisa para sair...')
            break

