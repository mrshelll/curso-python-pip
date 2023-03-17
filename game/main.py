import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ').lower()

  if not user_option in options:
    print('Esa opción no es válida!')
    return None, None
    
  computer_option = random.choice(options)
  
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gana!')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gana!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gana!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gana!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gana!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gana!')
      computer_wins += 1
  return user_wins, computer_wins

def winner(user_wins, computer_wins):
  game_over = False
  if computer_wins == 2:
    print('El ganador es la computadora!')
    game_over = True
  if user_wins == 2:
    print('El ganador es el usuario!')
    game_over = True
  return game_over

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('Computer wins => ', computer_wins)
    print('User wins => ', user_wins)
    
    rounds += 1
  
    user_option, computer_option  = choose_options()

    if  user_option == None and computer_option == None:
      print('\n')
      continue;
    
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    print('\n')

    game_over = winner(user_wins, computer_wins)

    if game_over:
      break;

run_game()