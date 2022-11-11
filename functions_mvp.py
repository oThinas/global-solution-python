# Utils Functions for MVP
from functions_utils import *

""" 
  * status: DONE
  
  @description: Função que verifica se existe algum número na string
  @param string (string) - String a ser verificada
  @return (boolean) - True se existir algum número na string, False caso contrário
"""
def findNumber(string):
  for char in string:
    if char.isdigit():
      return True
  return False

""" 
  * status: DONE
  
  @description: Função que verifica se cada palavra de uma string começa com letra maiúscula
  @param string (string) - String a ser verificada
  @return (boolean) - True se cada palavra da string começar com letra maiúscula, False caso contrário
"""
def findCapitalInFistLetterOfEachWord(string):
  for letter in string.split():
    if not letter[0].isupper():
      return False
  return True

""" 
  * status: DONE
  
  @description: Função que verifica se a primeira letra de uma string é maiúscula
  @param string (string) - String a ser verificada
  @return (boolean) - True se a string começar com letra maiúscula, False caso contrário
"""
def findCapitalInFirstLetter(string):
  if not string[0].isupper():
    return False
  return True

""" 
  * status: DONE
  
  @description: Função que verifica se existe alguma letra maiúscula na string
  @param string (string) - String a ser verificada
  @return (boolean) - True se existir alguma letra maiúscula na string, False caso contrário
"""
def findAnyLetterCapitalized(string):
  for letter in string:
    if letter.isupper():
      return True
  return False

""" 
  * status: DONE
  
  @description: Função que verifica se existe um caracter especial na string
  @param string (string) - String a ser verificada
  @return (boolean) - True se existir algum caracter especial na string, False caso contrário
"""
def findSpecialCharacters(string):
  for char in string:
    if not char.isalnum():
      return True
  return False

""" 
  * status: DONE
  
  @description: Função que verifica se o login é válido
  @param users (dict) - Dicionário com os usuários cadastrados
  @param login (string) - Login a ser verificado
  @return (boolean) - True se o login for válido, False caso contrário
"""
def verifyValidLogin(users, login):
  isLoginValid = False
  if login in users:
    print('Login já cadastrado. Tente novamente.\n')
  elif len(login) < 3:
    print('Login deve ter no mínimo 3 caracteres. Tente novamente.\n')
  else:
    isLoginValid = True
  return isLoginValid

""" 
  * status: DONE
  
  @description: Função que verifica se o nome é válido
  @param users (dict) - Dicionário com os usuários cadastrados
  @param name (string) - Nome a ser verificado
  @return (boolean) - True se o nome for válido, False caso contrário
"""
def verifyValidName(users, name):
  isNameValid = False
  if findNumber(name):
    print('Nome não pode conter números. Tente novamente.\n')
  elif not name:
    print('Nome não pode ser vazio. Tente novamente.\n')
  elif not findCapitalInFistLetterOfEachWord(name):
    print('A primeira letra de cada nome/sobrenome deve ser maiúscula. Tente novamente.\n')
  elif len(name.split()) < 2:
    print('Nome deve conter nome e sobrenome. Tente novamente.\n')
  else:
    existNameInAnotherUser = False
    for login in users:
      if users[login]['name'] == name:
        existNameInAnotherUser = True
        break
    if existNameInAnotherUser:
      print('Nome já cadastrado em outro usuário. Tente novamente.\n')
    else:
      isNameValid = True
  return isNameValid

""" 
  * status: DONE
  
  @description: Função que verifica se o email é válido
  @param users (dict) - Dicionário com os usuários cadastrados
  @param email (string) - Email a ser verificado
  @return (boolean) - True se o email for válido, False caso contrário
"""
def verifyValidEmail(user, email):
  isEmailValid = False
  if not email:
    print('Email não pode ser vazio. Tente novamente.\n')
  elif not any(email.endswith(suffix) for suffix in ['.com', '.com.br']):
    print('Email deve terminar com ".com" ou com ".com.br". Tente novamente.\n')
  elif not email.count('.') == 1:
    print('Email deve conter apenas um ponto. Tente novamente.\n')
  elif not email.count('@') == 1:
    print('Email deve conter um "@". Tente novamente.\n')
  elif len(email.split('@')[0]) < 3:
    print('Email deve conter no mínimo 3 caracteres antes do "@". Tente novamente.\n')
  elif email[email.index('@') + 1:email.index('.')] == '':
    print('Email deve conter no mínimo 1 caracteres entre o "@" e o ".". Tente novamente.\n')
  else:
    existEmailInAnotherUser = False
    for login in users:
      if users[login]['email'] == email:
        existEmailInAnotherUser = True
        break
    if existEmailInAnotherUser:
      print('Email já cadastrado em outro usuário. Tente novamente.\n')
    else:
      isEmailValid = True
  return isEmailValid

""" 
  * status: DONE
  
  @description: Função que verifica se a senha é válida
  @param password (string) - Senha a ser verificada
  @return (boolean) - True se a senha for válida, False caso contrário
"""
def verifyValidPassword(password):
  isPasswordValid = False
  if not password:
    print('Senha não pode ser vazia. Tente novamente.\n')
  elif len(password) < 6:
    print('Senha deve ter no mínimo 6 caracteres. Tente novamente.\n')
  elif not findAnyLetterCapitalized(password):
    print('Senha deve conter pelo menos uma letra maiúscula. Tente novamente.\n')
  elif not findNumber(password):
    print('Senha deve conter pelo menos um número. Tente novamente.\n')
  elif not findSpecialCharacters(password):
    print('Senha deve conter pelo menos um caracter especial. Tente novamente.\n')
  else:
    isPasswordValid = True
  return isPasswordValid

""" 
  * status: DONE
  
  @description: Função que verifica se o endereco é válido
  @param points (dict) - Dicionário com os pontos de bike cadastrados
  @param address (string) - Endereço a ser verificado
  @return (boolean) - True se o endereço for válido, False caso contrário
"""
def verifyValidAddress(points, address):
  isAddressValid = False
  addressTypes = [
    'Aeroporto', 'Alameda', 'Área', 'Avenida', 'Campo', 'Chácara', 'Colônia', 'Condomínio', 'Conjunto', 'Distrito', 'Esplanada', 'Estação', 'Estrada',
    'Favela', 'Fazenda', 'Feira', 'Jardim', 'Ladeira', 'Lago', 'Lagoa', 'Largo', 'Loteamento', 'Morro', 'Núcleo', 'Parque', 'Passarela', 'Pátio',
    'Praça', 'Quadra', 'Recanto', 'Residencial', 'Rodovia', 'Rua', 'Setor', 'Sítio', 'Travessa', 'Trecho', 'Trevo', 'Vale', 'Vereda', 'Via',
    'Viaduto', 'Viela', 'Vila'
  ]
  if not address:
    print('Endereço não pode ser vazio. Tente novamente.\n')
  elif address in points:
    print('Endereço já cadastrado. Tente novamente.\n')
  elif not findNumber(address):
    print('Endereço deve conter pelo menos um número. Tente novamente.\n')
  elif not findCapitalInFirstLetter(address):
    print('A primeira letra do logradouro deve ser maiúscula. Tente novamente.\n')
  elif len(address.split()) < 3:
    print('Endereço deve conter logradouro, nome do logradouro e número. Tente novamente.\n')
  elif not findCapitalInFirstLetter(address.split(' ')[1]):
    print('A primeira letra do endereço deve ser maiúscula. Tente novamente.\n')
  elif not any(address.startswith(suffix) for suffix in addressTypes):
    print('Endereço deve começar com o logradouro. Tente novamente.\n')
  else:
    isAddressValid = True
  return isAddressValid

""" 
  * status: DONE
  
  @description: Função que verifica se existe um usuário logado
  @param users (dict) - Dicionário com os usuários cadastrados
  @return (boolean) - True se existir um usuário logado, False caso contrário
"""
def verifyUserLogged(userSession):
  if not userSession:
    return False
  return True

""" 
  * status: DONE
  
  @description: Função que lista os pontos de bike
  @param points (dict) - Dicionário com os pontos de bike
"""
def listBikePoints(points):
  print('Pontos de bike disponíveis:\n')
  if not points:
    print('Não há pontos de bike cadastrados.')
    print('-' * 50)
  else:
    for point in points:
      print(f'Endereço: {point}')
      print(f'Quantidade de bicicletas infantis: {points[point]["amountKidsBikes"]}')
      print(f'Quantidade de bicicletas adultas: {points[point]["amountAdultsBikes"]}')
      print('-' * 50)
      print('\n')

""" 
  @description: Dicionário que armazena os usuários registrados. A chave é o login e os valores são name (nome), email, password (senha) e amountOfPointsCreated (quantos pontos criou esse usuário criou).
  @exemple: {
    users: {
      "thinas": {
        "login": "thinas",
        "name": "Thiago Martins Prado",
        "email": "thinas@example.com",
        "password": "Thinas123@",
        "amountOfPointsCreated": 3
      },
      "tata": {
        "login": "tata",
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
        "amountAdultsBikes": 2
      }
      "Avenida Paulista, 1000": {
        "amountKidsBikes": 0,
        "amountAdultsBikes": 1
      }
    }
  }
"""
points = {}

""" 
  * status: DONE
  
  @description: Função que inicializa o menu MVP. Deve ser chamado no início do programa e após a escolha do usuário, ser mandado para a função handleMvpMenu()
  @return: userInput (string) - Opção escolhida pelo usuário
  @see: handleMvpMenu()
"""
def initializeMvpMenu(userSession):
  while True:
    clearConsole()
    print('________ Menu MVP ________')
    print(f'\nLogado como: {userSession["login"]}. Pontos criados: {userSession["amountOfPointsCreated"]}') if userSession else print('')
    print('1 - Criar conta')
    print('2 - Login')
    print('3 - Listar pontos de bike')
    print('4 - Cadastrar ponto de bike')
    print('5 - Voltar para o Menu principal')
    
    userInput = input('\n\nDigite a opção desejada: ')
    if userInput in ['1', '2', '3', '4', '5']:
      return userInput
    
"""
  * status: DONE
  
  @description: Trata o retorno do método initializeMvpMenu() e chama a opção que o usuário escolheu.
  @see: initializeMvpMenu()
"""
def handleMvpMenu():
  
  """ 
    @description: Variável que armazena o login do usuário que está logado no sistema.
    @default: None
    @exemple: "thinas"
  """
  userSession = None
  
  while True:
    clearConsole()
    userInput = initializeMvpMenu(userSession)
    if userInput == '1':
      registerUser(users) # * DONE
    elif userInput == '2':
      userSession = handleLogin(users) # * DONE
    elif userInput == '3':
      listBikePointsScreen(points, userSession) # * DONE
    elif userInput == '4':
      createBikePoint(points, users, userSession) # * DONE
    elif userInput == '5':
      break # * DONE
    else:
      print('Opção inválida!')

""" 
  * status: DONE
  
  @description: Função que registra um novo usuário no dicionário users. Chama diversas funções para verificar se os dados são válidos.
  @param users (dict) - Dicionário com os usuários cadastrados
  @return: users (dict) - Dicionário com o novo usuário cadastrado
  @see: verifyValidLogin(), verifyValidName(), verifyValidEmail(), verifyValidPassword()
"""
def registerUser(users):
  clearConsole()
  print('________ Registre-se ________')
  print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
  
  if not checkEscapeKey(msvcrt.getch()):
    while True:
      login = input('Login: ')
      if not verifyValidLogin(users, login):
        continue
      else:
        break
      
    while True:
      name = input('Nome: ')
      if not verifyValidName(users, name):
        continue
      else:
        break
    
    while True:
      email = input('Email: ')
      if not verifyValidEmail(users, email):
        continue
      else:
        break
    
    while True:
      password = input('Senha: ')
      if not verifyValidPassword(password):
        continue
      else:
        break
    
    users[login] = {
      "login": login,
      "name": name,
      "email": email,
      "password": password,
      "amountOfPointsCreated": 0
    }
    print('Usuário criado com sucesso!')
    pressAnyKeyToContinue()
  return users

""" 
  * status: DONE
  
  @description: Função que tenta fazer login. Verifica se o login já existe no dicionário users.
  @param users (dict) - Dicionário com os usuários cadastrados
  @return: userSession (dict) - Dicionário do usuário que está logado no sistema
"""
def handleLogin(users):
  while True:
    clearConsole()
    print('________ Logar-se ________')
    print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
    
    if not checkEscapeKey(msvcrt.getch()):
        login = input('Login: ')
        password = input('Senha: ')
        
        if login not in users:
          print('Login não encontrado. Tente novamente.')
          pressAnyKeyToContinue()
        else:
          for user in users:
            if user == login and users[user]['password'] == password:
              print('Login realizado com sucesso!')
              pressAnyKeyToContinue()
              return users[user]
    else:
      break
            
""" 
  * status: DONE
  
  @description: Função que monta a tela de listagem de pontos de bike cadastrados. Utiliza a função listBikePoints() para obter os meses cadastrados
  @params: points (dict) - Dicionário com os pontos de bike cadastrados
  @see: listBikePoints()
"""
def listBikePointsScreen(points, userSession):
  clearConsole()
  if not verifyUserLogged(userSession):
    print('Você precisa estar logado para acessar essa funcionalidade.')
    pressAnyKeyToContinue()
  else:
    print('________ Pontos de bike ________')
    print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
    
    if not checkEscapeKey(msvcrt.getch()):
      listBikePoints(points)
      pressAnyKeyToContinue()
      
def createBikePoint(points, users, userSession):
  clearConsole()
  if not verifyUserLogged(userSession):
    print('Você precisa estar logado para acessar essa funcionalidade.')
    pressAnyKeyToContinue()
  else:
    print('________ Cadastrar ponto de bike ________')
    print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
    
    if not checkEscapeKey(msvcrt.getch()):
      listBikePoints(points)
      while True:
        address = input('Endereço: ')
        if not verifyValidAddress(points, address):
          continue
        else:
          break
      
      while True:
        amountKidsBikes = input('Digite o número de bikes tamanho infantil: ')
        if amountKidsBikes.isnumeric():
          break
        else:
          print('Valor inválido. Valor correto (número inteiro). Tente novamente.\n')
          
      while True:
        amountAdultsBikes = input('Digite o número de bikes tamanho adulto: ')
        if amountAdultsBikes.isnumeric():
          break
        else:
          print('Valor inválido. Valor correto (número inteiro). Tenten novamente.\n')
      
      points[address] = {
        "amountKidsBikes": amountKidsBikes,
        "amountAdultsBikes": amountAdultsBikes
      }
      userSession['amountOfPointsCreated'] += 1
      print('Ponto de bike cadastrado com sucesso!')
      pressAnyKeyToContinue()
  return points