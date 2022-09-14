import random as rd

person_names = str(input("Digite o nome das pessoas separados por vírgula: "))

def choice_random_person(person_names):
    names = person_names.split(", ")
    print(f'O(a) {rd.choice(names)} vai pagar a conta hoje!')

choice_random_person(person_names)