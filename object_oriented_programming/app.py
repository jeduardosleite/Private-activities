from modelos.restaurante import Restaurante   # importando a classe Restaurante criada anteriormente

res_praca = Restaurante('Praca', 'Gourmet')
res_praca.receber_avaliacao('Gui', 10)
res_praca.receber_avaliacao('Lais', 8)
res_praca.receber_avaliacao('José', 2)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()