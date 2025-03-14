from util.arquivos import *
from util.funcionalidades import *
cores = {
    "0": "\033[m",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m"
}

def titulo(msg=''):
    tam = len(msg) + 4
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)

def menu(lst):
    cont = 0
    for c in lst:
        print(f'{cores["yellow"]}[ {cont} ] {cores["0"]}- {cores["blue"]}{c}{cores["0"]}')
        cont += 1
