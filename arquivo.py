import csv
from cliente import Cliente
# leitura e escrita no arquivi

# ler os clientes do arquivo e retorna uma lista
def lerArquivo(): #os parâmetros não existe
  lista_clientes = []
  with open('clientes.csv','r',) as file:
      reader = csv.reader(file, delimiter='\t')
      for row in reader:
          x = row[0].split(",") #separar os campos por virgula
          nome = x[0]
          idade = x[1]
          ano = x[2]
          x = Cliente(nome, idade, ano)
          lista_clientes.append(x)
      return lista_clientes


# escreve a lista de clientes em arquivo
def escreverArquivo(lista_clientes):
  with open('clientes.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerows(lista_clientes)
  return False

# imprimir a lista de objetos
def printArquivo(lista_clientes):
  for x in lista_clientes:
      x.printCadastro()
      print(lista_clientes) # imprimir uma lista cheia de coisas estranhas (objetos e suas posições na memória)