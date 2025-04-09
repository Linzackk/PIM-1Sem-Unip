import json
import util.estrutura.estrutura as est
import util.arquivos.arquivos as arq


def funcao():
    while True:
        func = str(input('Aluno ou Professor: ')).upper()[0]
        if func != 'AL' or func != 'PR' or 'AD':
            print(f'ERRO, INSIRA UM VALOR VÁLIDO.')
        else:
            break
    return func

def login():
    with open('alunos.json', 'r') as file:
        try:
            alunos: dict = json.loads('\n'.join(file.readlines()))
        except JSONDecodeError:
            print(f'NÃO HÁ ALUNOS CADASTRADOS!')
    while True:
        usuario = str(input('Insira o Usuário: ')).strip().lower()
        password = str(input('Insira a Senha: ')).strip()
        if usuario not in alunos:
            print(f'USUÁRIO NÃO ENCONTRADO NO SISTEMA.')
        else:
            log = alunos[usuario]
            if "senha" not in log:
                print(f'ERRO, SENHA NÃO CADASTRADA!')
            elif log["senha"] != password:
                print(f'SENHA INVÁLIDA.')
            else:
                print(f'Logado com Sucesso')
                break

    return usuario

def escolha(n):
    while True:
        esc = int(input('Insira Sua Escolha: '))
        if 0 > esc or esc > n - 1:
            print(f'Escolha Inválida.')
        else:
            break
    return esc

def ver_notas(usuario):
    dados = arq.abrir_dados()
    aluno = dados[usuario]
    semestres = ['1° Semestre', '2° Semestre']
    est.menu(semestres)
    esc = escolha(len(semestres))
    if esc == 0:
        est.titulo('1° SEMESTRE')
        print(f'Np1: {aluno["semestre1"][0]}\n'
              f'Np2: {aluno["semestre1"][1]}\n'
              f'Média: {aluno["semestre1"][2]}')
    elif esc == 1:
        est.titulo('2° Semestre')
        print(f'Np1: {aluno["semestre2"][0]}\n'
              f'Np2: {aluno["semestre2"][1]}\n'
              f'Média: {aluno["semestre2"][2]}\n')
    input('Insira qualquer coisa para continuar...')

def att_nota():
    def atualizador(dados_alunos, sem="",prova=1, usuario=''):
        dados_aluno = dados_alunos[usuario]
        nota_semestre = dados_aluno[sem]

        print('Nota: ')
        nota = escolha(11)
        nota_semestre[prova - 1] = nota

        np1 = nota_semestre[0]
        np2 = nota_semestre[1]
        nota_semestre[2] = (np1 + np2) / 2

        dados_aluno[sem] = nota_semestre
        novos_dados = json.dumps(dados_alunos, indent=4)

        with open('alunos.json', 'w') as subs:
             subs.write(novos_dados)

    dados = arq.abrir_dados()
    usuario = ''
    semestres = ['1° Semestre', '2° Semestre']
    notas = ['Np 1', 'Np 2']
    while usuario not in dados:
        usuario = str(input('Usuário do Aluno: '))
    dados_aluno = dados[usuario]
    est.menu(semestres)
    sem = escolha(len(semestres))
    if sem == 0:
        est.titulo('1° SEMESTRE')
        est.menu(notas)
        provas = escolha(len(notas))
        if provas == 0:
            atualizador(dados, "semestre1",1, usuario)
        elif provas == 1:
            atualizador(dados, "semestre1", 2, usuario)
    elif sem == 1:
        est.titulo('2° SEMESTRE')
        est.menu(notas)
        provas = escolha(len(notas))
        if provas == 0:
            atualizador(dados, "semestre2", 1, usuario)
        elif provas == 1:
            atualizador(dados, "semestre2", 2, usuario)

def ver_grade(curso=''):
    cursos = {
        "ADS": ["Cibersegurança",
        "Direitos Humanos",
        "Ética, Cidadania e Sustentabilidade",
        "Infraestrutura Computacional",
        "Lei Geral de Proteção de Dados",
        "Matemática e Estatísica",
        "Pensamento Lógico Computacional com Python",
        "Tecnologia da Informação e Comunicação"
        ]
        #Adicionar outros cursos pra melhor interação
    }
    if curso == '':
        print('Você não tem uma grade Curricular')
    elif curso in cursos:
        materias = cursos[curso]
        est.titulo(f'GRADE CURRICULAR DO CURSO {curso.upper()}')
        for c in materias:
            print(c)
    est.linha(29)
    input('Insira qualquer coisa para continuar...')
