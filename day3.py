def print_treasure_chest_and_messages():
    treasure_chest = ("""
                                _.--.
                            _.-'_:-'||
                        _.-'_.-::::'||
                   _.-:'_.-::::::'  ||
                 .'`-.-:::::::'     ||
                /.'`;|:::::::'      ||_
               ||   ||::::::'     _.;._'-._
               ||   ||:::::'  _.-!oo @.!-._'-.
               \'.  ||:::::.-!()oo @!()@.-'_.|
                '.'-;|:.-'.&$@.& ()$%-'o.'U||
                  `>'-.!@%()@'@_%-'_.-o _.|'||
                   ||-._'-.@.-'_.-' _.-o  |'||
                   ||=[ '-._.-U/.-'    o |'||
                   || '-.]=|| |'|      o  |'||
                   ||      || |'|        _| ';
                   ||      || |'|    _.-'_.-'
                   |'-._   || |'|_.-'_.-'
                    '-._'-.|| |' `_.-'
                        '-.||_/.-'
    """)

    print(treasure_chest)
    print("Bem-vindo a ilha do tesouro.")
    print("A sua missão é encontrar o tesouro.")


def choice_first_path():
    while (True):
        path_choice = str(
            input("Você está prestes a cruzar uma estrada. Para onde seja ir? Escreva direita ou esquerda ")).upper()
        if len(path_choice) == 0:
            print("Escolha errada, tente novamente...")
        elif path_choice == 'DIREITA' or path_choice == 'ESQUERDA':
            break

def choice_second_path():
    while(True):
       second_choice = str(input("Você chegou a um lago. Tem uma ilha no meio do lago. Escreva 'espere' para esperar um bote. Digite 'nadar' para nadar até lá ")).upper()
       if len(second_choice) == 0:
           print("Escolha errada, tente novamente...")
       elif second_choice == 'ESPERE' or second_choice == 'NADAR':
           break


def choice_third_path():
    while(True):
        third_choice = str(input("Você chegou a ilha ileso(a). Tem uma casa com 3 portas. Uma 'vermelha', uma 'amarela' e outra 'azul'. Qual cor você escolhe? ")).upper()
        if len(third_choice) == 0:
            print("Escolha errada, tente novamente...")
        elif third_choice == 'AMARELA' or third_choice == 'VERMELHA' or third_choice == 'AZUL':
            break
    return third_choice


def final_choice_red_color():
    fire_ascii = ("""
    
        ⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
    
    """)
    print(fire_ascii)
    print("É um quarto pegando fogo. Game Over!")



def final_choice_yellow_color():
    treasure_chest = ("""
                                    _.--.
                                _.-'_:-'||
                            _.-'_.-::::'||
                       _.-:'_.-::::::'  ||
                     .'`-.-:::::::'     ||
                    /.'`;|:::::::'      ||_
                   ||   ||::::::'     _.;._'-._
                   ||   ||:::::'  _.-!oo @.!-._'-.
                   \'.  ||:::::.-!()oo @!()@.-'_.|
                    '.'-;|:.-'.&$@.& ()$%-'o.'U||
                      `>'-.!@%()@'@_%-'_.-o _.|'||
                       ||-._'-.@.-'_.-' _.-o  |'||
                       ||=[ '-._.-U/.-'    o |'||
                       || '-.]=|| |'|      o  |'||
                       ||      || |'|        _| ';
                       ||      || |'|    _.-'_.-'
                       |'-._   || |'|_.-'_.-'
                        '-._'-.|| |' `_.-'
                            '-.||_/.-'
        """)

    print(treasure_chest)
    print("Você encontrou o báu de tesouros, parabéns!")


def final_choice_blue_color():
 beasts = """
                _.------.                        .----.__
           /         \_.       ._           /---.__  
          |  O    O   |___  //|          /       `\ |
          |  .vvvvv.  | )   `(/ |         | o     o  \|
          /  |     |  |/      \ |  /|   ./| .vvvvv.  |
         /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | 
       ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/
      /   / |         \        /  | | ~   \          |  
      \  /  |        / \ Y   /'   | \     |          |   ~
       `'   |  _     |  `._/' |   |  \     7        /
         _.-'-' `-'-'|  |`-._/   /    \ _ /    .    |
    __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_
 --'                  \  \ |   /    |  |              `-
                       uU UU/     |  /   :F_P:
 """
 print(beasts)
 print("Você entrou em um quarto cheio de bestas. Game Over!")


def main():
    print_treasure_chest_and_messages()
    choice_first_path()
    choice_second_path()
    choice = choice_third_path()
    if(choice.upper() == "VERMELHA"):
        final_choice_red_color()
    elif (choice.upper() == "AMARELA"):
        final_choice_yellow_color()
    else:
        final_choice_blue_color()

main()

