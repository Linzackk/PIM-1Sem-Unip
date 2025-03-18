num = 1
dicionario = {
        "IsaacMedeiros": '123'
    }
def add_pessoa(lstPessoas):
    num = 1
    nomeCompleto = str(input('Nome COMPLETO do Aluno: '))
    nomeSplit = nomeCompleto.lower().title().split()
    usuario = nomeSplit[0] + nomeSplit[-1]
    tamanho_nome = len(nomeSplit)


    cont = -1
    while usuario in lstPessoas:
        if tamanho_nome <= 3:
            if nomeSplit[1] in 'DaDeDo':
                usuario = nomeSplit[0] + nomeSplit[-1] + str(num)
                print(usuario)
            else:
                usuario = nomeSplit[0] + nomeSplit[-1] + str(num)
        else:
            while usuario in dicionario and cont > -tamanho_nome:
                if nomeSplit[cont] not in 'DaDeDo':
                    usuario = nomeSplit[0] + nomeSplit[cont]
                    cont -= 1
                else:
                    cont -= 1
        num += 1
    print(usuario)
    print(lstPessoas)
    dicionario[usuario] = '123'
    print(lstPessoas)
add_pessoa(dicionario)

