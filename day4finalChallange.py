import day4finalBib as imgs
import random as rd

def ask_user():
    while(True):
        usr_choice = int(input("Qual você escolhe? Digite '0' para Pedra. '1' para Papel ou '2' para Tesoura "))
        if usr_choice<0 or usr_choice>2:
            print("Escolha inválida, tente novamente....")
        else:
            break
    print("Você escolheu: ")
    print(imgs.hand_signs[usr_choice])
    return usr_choice



def computer_rnd_choice():
    computer_number_choice = rd.SystemRandom().randint(0,2)
    print("Computador escolheu: ")
    print(imgs.hand_signs[computer_number_choice])
    return computer_number_choice

def win_or_lose(computer_choice,human_choice):
    if computer_choice == 0 and human_choice == 1:
        print("Você venceu!")
    elif computer_choice == 1 and human_choice == 2:
        print("Você venceu!")
    elif computer_choice == 2 and human_choice == 0:
        print("Você venceu!")
    elif computer_choice == human_choice:
        print("EMPATE!")
    else:
        print("Você PERDEU!")

def main():
    human = ask_user()
    computer = computer_rnd_choice()
    win_or_lose(computer, human)

main()

