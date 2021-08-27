# pesquisa na lista de clientes e retorna o objeto cliente
def pesquisa(lista_clientes):
  nomes = ["Marcos Silva", "Luiz Ferrareis", "Pedro Magnelo", "Mateus de Angeli"]
  ## não pode ter input dentro dos métodos ##
  letra = input("Digite a primeira letra do nome: ")
  for i in range (0,len(nomes)):
    nome_pessoa = nomes[i].lower()
    if cliente.nome[0] == letra:
      print(nome_pessoa)
      
      return cliente # se encontrar 
  
  

  return None # se não encontrar - nulo/null/vazio