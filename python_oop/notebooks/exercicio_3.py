""" 
1) Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

2) Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
Crie duas instâncias da classe e imprima essas instâncias.

3) Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4)Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

5) Crie uma instância da classe e imprima o valor da propriedade titular.

6)Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

7)Crie um método de classe para a conta ClienteBanco.

"""

class ContaBancaria:

    def __init__(self, titular='', saldo=0, ativo=False):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'O nome do titular é {self._titular} com saldo de {self._saldo}. O status da sua conta é {self.ativar_conta}.'

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self.ativo

    @property
    def ativar_conta(self):
        return 'ativa' if self._ativo else 'desativada'