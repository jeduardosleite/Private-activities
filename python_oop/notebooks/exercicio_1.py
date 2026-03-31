"""
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
"""

class Carro:

    def __init__ (self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano 
        self.cor = cor

class Restaurante:
    def __init__ (self, nome, categoria, nacionalidade, regiao_brasil, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.nacionalidade = nacionalidade
        self.regiao_brasil = regiao_brasil

    def __str__(self):
        return f'{self.nome.ljust(10)} | {self.categoria.ljust(10)} | {self.nacionalidade.ljust(10)} | {self.regiao_brasil.ljust(10)}'
    
class Cliente:
    def __init__ (self, nome, sobrenome, idade, sexo, vip=False):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.vip = False
    
    def __str__(self):
        return f'O nome do cliente é {self.nome} {self.sobrenome}, com idade de {self.idade}, sexo {self.sexo}.'

#########################################################################################################################

restaurante = Restaurante('Santa Marmita', 'Prato Feito', 'Brasileira', 'Sul')
print(restaurante)

#########################################################################################################################

cliente_1 = Cliente('Paulo', 'Koch', '34', 'Masculino')
cliente_2 = Cliente('Maria', 'Leticia', '24', 'Femenino')
cliente_3 = Cliente('Joana', 'Darc', '44', 'Femenino')
cliente_4 = Cliente('Deniz', 'Fonseca', '55', 'Masculino')
print('\n')
print(cliente_1)
print(cliente_2)
print(cliente_3)
print(cliente_4)