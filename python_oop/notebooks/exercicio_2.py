"""
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
Adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
"""

class Pessoa():
    pessoas = []

    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'O nome é {self.nome}, tem {self.idade} anos e sua profissão é {self.profissao}.'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, chamo-me {self.nome} e trabalho com {self.profissao}.'
        else:
            return f'Olá, chamo-me {self.nome}!'
    
    def aniversario(self):
        self.idade += 1

#########################################################################################################

pessoa_1 = Pessoa('José Eduardo', 33, 'Engenheiro de Dados')

print('Informações iniciais:')
print(pessoa_1)

pessoa_1.aniversario()
print('\nInformações após aniversário:')
print(pessoa_1)

