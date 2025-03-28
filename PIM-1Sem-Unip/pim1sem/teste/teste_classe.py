class Filme:
   def __init__(self, duracao, genero, nacionalidade, ano_lancamento):
       self.duracao = duracao
       self.genero = genero
       self.nacionalidade = nacionalidade
       self.ano_lancamento = ano_lancamento

   def Informacoes(self):
           print(self.duracao, self.genero, self.nacionalidade, self.ano_lancamento)

print('Adicionando Filme')
dur = str(input('Duração: '))
gen = str(input('Genero: '))
nac = str(input('Nac: '))
ano = int(input('Ano: '))

novoFilme = Filme(dur, gen, nac, ano)
print('Adicionado novo Filme.')
print(novoFilme.Informacoes())