from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):   # __init__ é um método construtor. Será sempre chamado quando for criada a instância
        self._nome = nome.title()           # self quer dizer: esse atributo pertence a ESTE objeto // title deixa a primeira letra maiúscula
        self._categoria = categoria.title()
        self._ativo = False                # colocando o _ativo, estamos protegendo o atributo e controlando o acesso
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'NOME DO RESTAURANTE'.ljust(20)} | {'CATEGORIA'.ljust(20)} | {'AVALIAÇÃO'.ljust(25)} | {'STATUS'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')


    @property   # Transforma método em atributo
    def ativo(self):
        return 'Ok' if self._ativo else 'x'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 >= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:  # Se não tiver avaliação, retorna zero
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)   # pega a soma das notas
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media