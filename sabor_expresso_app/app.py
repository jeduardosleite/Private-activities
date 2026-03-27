import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

restaurantes = [{"nome":"Praça Café", "categoria":"cafe", "ativo":False},
                {"nome":"Ze do Lanche", "categoria":"Delivery", "ativo":True},
                {"nome":"Pizzaiolo", "categoria":"Lanche", "ativo":True},
                {"nome":"iTruck", "categoria":"Lanche", "ativo":True},
                {"nome":"Bistrô 99", "categoria":"cafe", "ativo":False}
]

def exibir_nome():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
def voltar_ao_menu():
    input("\nTecle ENTER para voltar ao menu principal ")
    main()

def subtitulo(texto):   
    """ Essa função personaliza o subtitulo """
    os.system("cls")
    linha = "#" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcoes():
    print("1: Cadastrar restaurante")
    print("2: Listar restaurante")
    print("3: Alterar status do restaurante")
    print("4: Sair\n")

def finalizar_app():
    subtitulo("Finalizar app")

def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu()

def cadastrar_restaurante():
    """ Essa opção cadastra um novo restaurante """
    subtitulo("Cadastrar novo restaurante")
    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Insira a categoria do {nome_restaurante}: ")
    dados_do_restaurante = {"nome":nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante {nome_restaurante} foi cadastrado com sucesso! ")
    
    voltar_ao_menu()

def listar_restaurantes():
    """ Essa função lista os restaurantes já cadastrados """
    subtitulo("Listando restaurantes")

    print(f'{'NOME'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'STATUS'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        if restaurante["ativo"] == True:
            ativo = "Ativo"
        else:
            ativo = "Inativo"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu()

def alternar_status():
    """ Essa função altera o status do restaurante """
    subtitulo("Alterando o status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que você deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('\nO restaurante não foi encontrado.')

    voltar_ao_menu()

def escolha_opcao():
    """ Essa função faz o usuário escolher a opção do menu """
    try:
        opcao_escolhida = int(input("Escolha uma opção: \n"))
        print(f"\nVocê escolheu a opção {opcao_escolhida}.")

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """  """
    os.system("cls")
    exibir_nome()
    opcoes()
    escolha_opcao()

if __name__ == "__main__":
    main()