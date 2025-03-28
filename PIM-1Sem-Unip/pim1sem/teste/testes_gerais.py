negativos = 0
positivos = 0
e = 0
while e != 999:
    e = int(input('[ 999 ] - Parar \nInsira um Valor Real: '))
    if e == 999:
        break
    elif e < 0:
        negativos += 1
    elif e >= 0:
        positivos += 1
print(f'Foram Inseridos {negativos} números negativos e {positivos} números positivos')
