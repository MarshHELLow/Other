user_input = "_________"
lst = list(user_input)

board = [
    [lst[0], lst[1], lst[2]],
    [lst[3], lst[4], lst[5]],
    [lst[6], lst[7], lst[8]]
]


def grid():
    print("---------")
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print("---------")


def line():
    global move
    row1 = [board[0][0], board[0][1], board[0][2]]
    row2 = [board[1][0], board[1][1], board[1][2]]
    row3 = [board[2][0], board[2][1], board[2][2]]
    column1 = [board[0][0], board[1][0], board[2][0]]
    column2 = [board[0][1], board[1][1], board[2][1]]
    column3 = [board[0][2], board[1][2], board[2][2]]
    dia1 = [board[0][0], board[1][1], board[2][2]]
    dia2 = [board[0][2], board[1][1], board[2][0]]
    win_line = [row1, row2, row3, column1, column2, column3, dia1, dia2]
    win_list = [a[0] for a in win_line if a[0] == a[1] == a[2]]
    if win_list == ["X"]:
        print("X wins")
        exit()
    elif win_list == ["O"]:
        print("O wins")
        exit()
    elif move > 9:
        print("Draw")
        exit()


grid()
move = 1
while True:
    player_turn = input("Enter the coordinates: ")
    n = [y for y in player_turn.split() if y.isalpha()]
    if len(n) > 0:
        print("You should enter numbers!")
    else:
        row, col = player_turn.split()
        row, col = int(row), int(col)
        if row > 3 or col > 3:
            print("Coordinates should be from 1 to 3!")
        elif board[row - 1][col - 1] == " ":
            if move % 2 == 1:
                board[row - 1][col - 1] = "X"
                move += 1
                grid()
                line()
            elif move % 2 == 0:
                board[row - 1][col - 1] = "O"
                move += 1
                grid()
                line()
        else:
            print("This cell is occupied! Choose another one!")
