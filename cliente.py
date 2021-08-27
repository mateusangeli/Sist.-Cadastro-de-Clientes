# classe Cliente

class Cliente:
  def __init__(self, nome, idade, ano):
      self.nome = nome
      self.idade = idade
      self.ano =  ano

  # get - pegar - obter
  def getList(self):
      return [self.nome, self.idade, self.ano]

  def printCadastro(self):
      print("Nome: ", self.nome)
      print("Idade: ", self.idade)
      print("Ano: ", self.ano)