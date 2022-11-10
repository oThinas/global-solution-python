# Utils Functions
import os, msvcrt, re

""" 
  * status: DONE

  @description: Função que limpa o console
"""
def clearConsole():
  os.system('cls' if os.name == 'nt' else 'clear')
  
""" 
  * status: DONE
  
  @description: Função que verifica se a tecla pressionada foi ESC
  @param keyPressed (string) - Tecla pressionada
  @return (boolean) - True se a tecla pressionada foi ESC, False caso contrário
"""
def checkEscapeKey(keyPressed):
  if keyPressed == b'\x1b': # ESC key
    return True
  return False

""" 
  * status: DONE
  
  @description: Função que lista os meses de referência cadastrados de forma simples
  @param data: Dicionário com os dados dos meses de referência
"""
def listMonths(data):
  print('Meses de referência cadastrados:\n')
  for monthYearReference in data:
    print(monthYearReference)

""" 
  * status: DONE
  
  @description: Função que aguarda o usuário pressionar qualquer tecla para continuar
"""
def pressAnyKeyToContinue():
  print('\nPressione qualquer tecla para continuar')
  msvcrt.getch()

""" 
  @description: Dicionário que armazena o mês-ano como chave e o valor como um dicionário com os dados numberOfInhabitants (total de habitantes) e numberOfDeaths (total de óbitos) do mês
  @example: {
    data: {
      "01-2020": {
        "numberOfInhabitants": 1000,
        "numberOfDeaths": 200
      },
      "02-2020": {
        "numberOfInhabitants": 1000,
        "numberOfDeaths": 100
      }
    }
  }
"""
# data = {}
data = {
  "01-2020": {
    "numberOfInhabitants": 1000,
    "numberOfDeaths": 2
  },
  "02-2020": {
    "numberOfInhabitants": 1000,
    "numberOfDeaths": 2
  }
}


""" 
  * status: DONE
  
  @description: Inicializa o Menu Principal. Deve ser chamado no início do programa e após a escolha do usuário, ser mandado para a função handleHomeMenu()
  @see: handleHomeMenu()
"""
def initizalizeHomeMenu():
  while True:
    clearConsole()
    print('________ Menu Principal ________')
    print('\n1 - Cadastrar mês de referência')
    print('2 - Exibir dados do mês de referência')
    print('3 - Relatório comparativo - Referência de 2019')
    print('4 - Listar todos os meses cadastrados')
    print('5 - Menu MVP')
    print('6 - Sair')
    
    userInput = input('\n\nDigite a opção desejada: ')
    if userInput in ['1', '2', '3', '4', '5', '6']:
      return userInput
  
    

"""
  ? status: Should be tested

  @description: Trata o retorno do método initizalizeHomeMenu() e chama a opção que o usuário escolheu.
  @see: initizalizeHomeMenu()
"""
def handleHomeMenu():
  while True:
    clearConsole()
    userInput = initizalizeHomeMenu()
    if userInput == '1':
      registerMonth(data) # ? TEST
    elif userInput == '2':
      showDataInMonth(data) # ? TEST
    elif userInput == '3':
      compareMonths(data) # ? TEST
    elif userInput == '4':
      listMonthsScreen(data) # ? TEST
    elif userInput == '5':
      initializeMvpMenu() # TODO
    elif userInput == '6':
      print('Saindo...') # * DONE
      break
    else:
      print('Opção inválida')
  
"""
  ? status: Should be tested

  @description: Insere um registro no dicionário de dados
  @params: data (dict) - Dicionário de dados
  @return: data (dict) - Dicionário de dados com novos dados inseridos
"""    
def registerMonth(data):
  clearConsole()
  print('________ Cadastrar mês de referência ________')
  print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
  
  if not checkEscapeKey(msvcrt.getch()):
    while True:
      monthYearReference = input('Digite o mês e ano de referência (MM-AAAA): ')
      if monthYearReference in data:
        print('Mês já cadastrado')
      elif len(monthYearReference) != 7 or not re.search('[0-9]+-[1-9][0-9]+', monthYearReference):
        print('Formato inválido. Valor correto (MM-AAAA)')
      else:
        break
    
    while True:
      numberOfInhabitants = input('Digite o número de habitantes: ')
      if numberOfInhabitants.isnumeric():
        break
      else:
        print('Valor inválido. Valor correto (número inteiro)')
        
    while True:
      numberOfDeaths = input('Digite o número de óbitos: ')
      if numberOfDeaths.isnumeric():
        break
      else:
        print('Valor inválido. Valor correto (número inteiro)')
    
    data[monthYearReference] = {
      "numberOfInhabitants": numberOfInhabitants,
      "numberOfDeaths": numberOfDeaths
    }
    print('Mês cadastrado com sucesso')
    pressAnyKeyToContinue()
  
  return data

""" 
  ? status: Should be tested

  @description: Função que exibe o os dados de referência de um mês-ano determinado pelo usuário
  @params: data (dict) - Dicionário de dados
"""
def showDataInMonth(data):
  clearConsole()
  print('________ Exibir dados do mês de referência ________')
  print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
  
  if not checkEscapeKey(msvcrt.getch()):
    listMonths(data)
    print('-' * 50)
    while True:
      monthYearReference = input('\nDigite o mês e ano de referência (MM-AAAA): ')
      if monthYearReference in data:
        break
      elif len(monthYearReference) != 7 or not re.search('[0-9]+-[1-9][0-9]+', monthYearReference):
        print('Formato inválido. Valor correto (MM-AAAA)')
      else:
        print('Mês não cadastrado')
    
    print('Registro encontrado')
    print('Mês de referência:', monthYearReference)
    print('Total de habitantes:', data[monthYearReference]['numberOfInhabitants'])
    print('Total de óbitos:', data[monthYearReference]['numberOfDeaths'])
    pressAnyKeyToContinue()
  
""" 
  ? status: Should be tested
  
  @description: Função que exibe o os dados de referência de um mês-ano determinado pelo usuário
  @params: data (dict) - Dicionário de dados
  @see: texto de referência - "3.6 Até 2020, reduzir pela metade as mortes e os ferimentos globais por acidentes em estradas. No Brasil, em 2015 ocorreu 19 mortes de trânsito para cada 100 mil habitantes. Em 2019, a taxa reduziu para 15 mortes para cada 100 mil habitantes, mas ainda longe da meta da ODS."

"""
def compareMonths(data):
  clearConsole()
  print('________ Relatório comparativo - Referência de 2019 ________')
  print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar\n')
  
  if not checkEscapeKey(msvcrt.getch()):
    listMonths(data)
    print('-' * 50)
    
    while True:
      yearReference = input('Digite o ano de referência (AAAA): ')
      if len(yearReference) != 4 or not re.search('[1-9][0-9]+', yearReference):
        print('Formato inválido. Valor correto (AAAA)')
      else:
        yearExists = False
        for monthYearReference in data:
          if monthYearReference[3:] == yearReference:
            yearExists = True
            break
        if yearExists:
          break
        else:
          print('Nenhum mês com esse ano foi cadastrado')
    
    sumOfInhabitantsInYear = 0
    sumOfDeathsInYear = 0
    for monthYearReference in data:
      if monthYearReference[3:] == yearReference:
        sumOfInhabitantsInYear += int(data[monthYearReference]['numberOfInhabitants'])
        sumOfDeathsInYear += int(data[monthYearReference]['numberOfDeaths'])
        
    taxPer100KInhabitantsInYear = (sumOfDeathsInYear * 100000) / sumOfInhabitantsInYear
    comparativeDeathTax = (taxPer100KInhabitantsInYear * 100) / 15
    if comparativeDeathTax > 100:
      comparativeDeathTax -= 100
    elif comparativeDeathTax < 100:
      comparativeDeathTax -= 100
    
    print(f'Total de habitantes em {yearReference}: {sumOfInhabitantsInYear}')
    print(f'Total de óbitos em {yearReference}: {sumOfDeathsInYear}')
    print(f'Taxa de óbitos por 100 mil habitantes em {yearReference}: {taxPer100KInhabitantsInYear: .2f}')
    print(f'Taxa de óbitos por 100 mil habitantes em 2019: 15')
    print(f'Taxa de óbitos por 100 mil habitantes em {yearReference} em relação a 2019: ' + 
          f'{"+" if taxPer100KInhabitantsInYear > 15 else "-"}{round(comparativeDeathTax, 2)}%')
    pressAnyKeyToContinue()
    
""" 
  ? status: Should be tested
  
  @description: Função que monta a tela de listagem de meses cadastrados. Utiliza a função listMonths() para obter os meses cadastrados
  @params: data (dict) - Dicionário de dados
  @see: listMonths
"""
def listMonthsScreen(data):
  clearConsole()
  print('________ Listar mês de referência ________')
  print('Pressione ESC para voltar ao menu principal e qualquer outra tecla para continuar')
  
  if not checkEscapeKey(msvcrt.getch()):
    listMonths(data)
    print('-' * 50)
    pressAnyKeyToContinue()