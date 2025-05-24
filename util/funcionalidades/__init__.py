import json
import util.arquivos as arq
import util.estrutura as est

def funcao():
    """
    Verifica se a função é Aluno, Professor ou Administrativo
    :return: Retorna a abreviação em 2 letras da função caso seja validada.
    """
    while True:
        func = str(input('Aluno ou Professor: ')).upper()[0:1]
        if func != 'AL' or func != 'PR' or 'AD':
            print(f'ERRO, INSIRA UM VALOR VÁLIDO.')
        else:
            break
    return func

def login():
    """
    Menu onde o login acontece, recebe o usuário e senha e valida com as informações contidas no Banco de dados "alunos.json"
    :return: O usuario caso ele exista no sistema.
    """
    with open('usuarios.json', 'r') as file:
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
    """
    Cria uma interação junto com a função menu para validar apenas valores presentes no menu
    :param n: quantidade de valores máximo
    :return: o numero caso seja válido
    """
    valido = False
    while not valido:
        esc = input('Insira sua Escolha: ').strip()
        if esc.isdigit() != True or esc.count('.') > 0:
            valido = False
        elif int(esc) > (n - 1) or int(esc) < 0:
            valido = False
        else:
            valido = True
            return int(esc)

def ver_notas(usuario):
    """
    Abre um menu interativo com as notas do primeiro e segundo semestre de um ano de um aluno.
    :param usuario: usuario a verificar as notas
    :return: uma print com as notas Np1, Np2 e média do semestre.
    """
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
    """
    Atualiza a nota de uma conta referente a: 1° ou 2° semestre e NP1 ou NP2
    :return: none
    """
    def atualizador(dados_alunos, sem="",prova=1, usuario=''):
        """
        Função que atualiza as notas.
        :param dados_alunos: banco de dados
        :param sem: semestre referente
        :param prova: np1 ou np2
        :param usuario: usuario do aluno
        :return: none
        """
        def valor_nota():
            while True:
                valor = input('Nota: ').strip()
                if ',' in valor:
                    valor = valor.replace(',', '.')
                if valor.replace('.', '').isdigit() and valor.count('.') <= 1:
                    return float(valor)
                else:
                    print('Nota inválida.')
        dados_aluno = dados_alunos[usuario]
        nota_semestre = dados_aluno[sem]

        nota = valor_nota()
        nota_semestre[prova - 1] = nota

        np1 = nota_semestre[0]
        np2 = nota_semestre[1]
        nota_semestre[2] = (np1 + np2) / 2

        dados_aluno[sem] = nota_semestre
        novos_dados = json.dumps(dados_alunos, indent=4)

        with open('usuarios.json', 'w') as subs:
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
    """
    Função usada para ver a grade de um aluno. Os cursos e a grade curricular do semestre é anotado.
    :param curso: Curso do Aluno
    :return: print de todas as matérias do semestre
    """
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