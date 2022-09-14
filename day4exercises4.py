
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
board = [row1,row2,row3]

def draw_board():
    print("\t\t1\t2\t3")
    print(f'*1 {board[0]}\n*2 {board[1]}\n*3 {board[2]}')

def ask_user_where_to_place_treasure():
    user_choice = str(input("Onde você deseja colocar o tesouro? exemplo: 32 "))
    sep_user_choice = list(map(str,user_choice))
    return sep_user_choice

def mark_x_in_user_choice(choice):
    first_choice = int(choice[0]) - 1
    second_choice = int(choice[1]) -1
    board[first_choice][second_choice] = "X"

def main():
    draw_board()
    choice = ask_user_where_to_place_treasure()
    mark_x_in_user_choice(choice)
    draw_board()

main()

