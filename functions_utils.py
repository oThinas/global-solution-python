import os, msvcrt

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
  
  @description: Função que aguarda o usuário pressionar qualquer tecla para continuar
"""
def pressAnyKeyToContinue():
  print('\nPressione qualquer tecla para continuar')
  msvcrt.getch()