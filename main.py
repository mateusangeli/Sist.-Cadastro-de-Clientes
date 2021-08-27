import time
import os
import arquivo as a
from cliente import Cliente

## --------- FUNÇÕES -------------##
# inserir novo cliente
def inserirCliente():
  nome = input("Digite nome:")
  idade = input("Digite a idade:")
  ano = input("Digite o ano de cadastro:")
  lista_clientes.append(Cliente(nome, idade, ano).getList())



## ----------- INÍCIO ------------##

# Variáveis globais
lista_clientes = a.lerArquivo()



# Início do programa (Menu)
#inserirCliente()
#a.escreverArquivo(lista_clientes)
a.printArquivo(lista_clientes)




'''
def menu():
  while(True):
    print("++++ Seja bem vindo +++++")
    print("+++++ Marcos Produtos Alimentícios LTDA +++++")
    print("1 - Acessar a lista de clientes")
    print("2 - Manual de instruções")
    print("3 - FAQ")
    print("4 - Criadores")
    print("5 - Finalizar o programa")


    opc = int(input("Selecione a opção: "))
    if opc > 5 or opc < 1:
      print("Opção inválida, tente novamente!")
    if opc == 1:
      a.printArquivo(lista_clientes)
      os.system('clear')
      print("1 - Adicionar um novo cliente")
      print("2 - Excluir um cliente")
      print("3 - Ferramenta de pesquisa")
      opcao = input("Escolha a opção: ")
      if opcao == 1:
        
      

      
    if opc == 2:
      os.system('clear')
      print("++++ Manual de instruções ++++")
      
    if opc == 3:
      os.system('clear')
      print("++++ FAQ ++++")

    if opc == 4:
      os.system('clear')
      print("~~~ Desenvolvido por Wallace Cardoso e Mateus de Angeli ~~~ ")
      time.sleep(0.5)
      break

    if opc == 5:
      time.sleep(0.5)
      os.system('clear')
      print(" ~~~ Sistema finalizado, muito obrigado!! ~~~ ")
      break'''



# a sua regra de negócio (lógica do programa)