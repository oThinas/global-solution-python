from functions_utils import *

""" 
  @description: Dicionário que armazena os usuários registrados. A chave é o login e os valores são name (nome), email, password (senha) e amountOfPointsCreated (quantos pontos criou esse usuário criou).
  @exemple: {
    users: {
      "thinas": {
        "name": "Thiago Martins Prado",
        "email": "thinas@example.com",
        "password": "Thinas123@",
        "amountOfPointsCreated": 3
      },
      "tata": {
        "name": "Taís Barcelos",
        "email": "tatabarcelos@example.com",
        "password": "Tata3123!",
        "amountOfPointsCreated": 0
      }
    }
  }
"""
users = {}

""" 
  @description: Dicionário que armazena os pontos registrados. A chave é o endereço e os valores são amountKidsBikes (quantidade de bike tamanho infantil) e amountOfAdultsBikes (quantidade de bikes tamanho adulto) e ownerLogin (login do usuário que criou o ponto).
  @exemple: {
    users: {
      "Rua Clélia, 500": {
        "amountKidsBikes": 3,
        "amountOfAdultsBikes": 2
      }
      "Avenida Paulista, 1000": {
        "amountKidsBikes": 0,
        "amountOfAdultsBikes": 1
      }
    }
  }
"""
points = {}


""" 
  ? status: Should be tested
  
  @description: Função que inicializa o menu MVP. Deve ser chamado no início do programa e após a escolha do usuário, ser mandado para a função handleMvpMenu()
  @return: userInput (string) - Opção escolhida pelo usuário
  @see: handleMvpMenu()
"""
def initializeMvpMenu():
  while True:
    clearConsole()
    print('________ Menu MVP ________')
    print('\n1 - Criar conta')
    print('2 - Login')
    print('3 - Listar pontos de bike')
    print('4 - Cadastrar ponto de bike')
    print('5 - Voltar para o Menu principal')
    
    userInput = input('\n\nDigite a opção desejada: ')
    if userInput in ['1', '2', '3', '4', '5']:
      return userInput
    
"""
  ? status: Should be tested

  @description: Trata o retorno do método initializeMvpMenu() e chama a opção que o usuário escolheu.
  @see: initializeMvpMenu()
"""
def handleHomeMenu():
  while True:
    clearConsole()
    userInput = initializeMvpMenu()
    if userInput == '1':
      createUser() # ? TEST
    elif userInput == '2':
      login() # ? TEST
    elif userInput == '3':
      showBikePoints() # ? TEST
    elif userInput == '4':
      createBikePoint() # ? TEST
    elif userInput == '5':
      break # * DONE
    else:
      print('Opção inválida!')
  