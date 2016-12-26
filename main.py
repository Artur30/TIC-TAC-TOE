# Игра крестики-нолики
# Глобальные константы:
NumSquares = 9
Empty = " "
Tie = "Ничья"

# Выводит на экран инструкцию для игрока. 
def displayInstruction():
    print("""
          Добро пожаловать на игру кретики-нолики.
          Чтобы сделать ход выберите цифру от 1 до 8.
          Числа соответствуют полям доски, как показано ниже.

          |  0  |  1  |  2  |
          -------------------
          |  3  |  4  |  5  |
          -------------------
          |  6  |  7  |  8  |
          """)
    print("\n")


# Задает вопрос ответом на который может быть "Да" или "Нет".
# Принимает текст вопроса.
# Возвращает "yes" или "nn".
def askYesNo(question):
    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()
    return response


# Просит ввести число из указанного диапазона.
# Принимает текст вопроса, нижнюю и верхнюю границы диапазона
# Возвращает целое число не меньше low и не больше height.
def askNumber(question, low, height):
    response = None
    while response not in range(low, height):
        response = int(input(question))
    return response



# Определяет принадлежность первого хода человеку или компьютеру.
# Возвращает типы фишек соответственно компьютера или человека. 
def pieces():
    goFirst = askYesNo("Хочешь ходить первым? (yes/no) ")
    if goFirst == "yes":
        print("Ну ладно. Ходи первый.")
        human = "X"
        computer = 0
    else:
        print("Ха! Я хожу первый")
        human = 0
        computer = "X"
    return computer, human



# Создает пустую игровую доску.
# Возвращает эту доску.
def newBoard():
    board = []
    for square in range(NumSquares):
        board.append(Empty)
    return board

# Отображает игровую доску на экране.
# Принимает эту доску.
def displayBoard(board):
    print("\n\t |" ,  board[0],  "|" ,  board[1],  "|" ,  board[2],  "|")
    print("\t ------------- ")
    print("\t |",  board[3],  "|" ,  board[4],  "|" ,  board[5],  "|")
    print("\t ------------- ")
    print("\t |" ,  board[6],  "|" ,  board[7],  "|" ,  board[8],  "|")


# Создает список доступных ходов.
# Принимает доску.
# Возвращает список доступных ходов.
def legalMoves(board):
    moves = []
    for square in range(NumSquares):
        if board[square] == Empty:
            moves.append(square)
    return moves



# Определяет победителя игры.
# Принимает доску.
# Возвращает тип фишек победителя:"Ничья" или None
def winner(board):
    waysToWin = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6))
    for row in waysToWin:
        if board[row[0]] == board[row[1]] == board[row[2]] != Empty:
            winner = board[row[0]]
            return winner
        if Empty not in board:
            return Tie
    return None


# Узнает, какой ход желает сделать игрок.
# Принимает доску и тип фишек человека.
# Возвращает ход человека
def humanMove(board, human):
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = askNumber("Давай выбирай, пока я не передумал. Поле от 0 до 8: ", 0, NumSquares)

        if move not in legal:
            print("Ну ты и дурак! Это поле уже занято.\n")
    print("Ладно...")
    return move



# Рассчитывает ход компьютера.
# Принимает доску, тип фишек компьютера и тип фишек человека
# Возвращает ход компьютера
def computerMove(board, computer, human):
    board = board[:]    # Копия доски
    bestMoves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")

    for move in legalMoves(board):
        board[move] = computer
        # Если следующим ходом может победить компьютер, выберем этот ход
        if winner(board) == computer:
            print(move)
            return move

        # Выполнив проверку, отменим внесенные изменения
        board[move] = Empty

    for move in legalMoves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = Empty

    # Если следующим ходом ни одна сторона не может победить,
    # выберем лучшее из доступных полей
    for move in bestMoves:
        if move in legalMoves(board):
            print(move)
            return move


# Осуществляет переход к следующему ходу.
# Принмает тип фишек.
# Возвращает тип фишек.
def nextTurn(turn):
    if turn == "X":
        return 0
    else:
        return "X"


# Поздравляет победителя или констатирует ничью.
# Принимает тип фишек победителя, тип фишек компьютера и тип фишек человека.
def congratWinner(theWinner, computer, human):
    if theWinner != Tie:
        print("Три", theWinner, "в ряд!\n")
    else:
        print("Ничья!")

    if theWinner == computer:
        print("Ха-ха-ха. Лошпед ты. Иди учись!\n")
    elif theWinner == human:
        print("Тебе просто повезло.\n")
    elif theWinner == Tie:
        print("В следующий раз тебе не повезет.\n")

# Главная функция
def main():
    displayInstruction()
    computer, human = pieces()
    turn = "X"
    board = newBoard()
    displayBoard(board)
    while not winner(board):
        if turn == human:
            move = humanMove(board, human)
            board[move] = human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)
    theWinner = winner(board)
    congratWinner(theWinner, computer, human)


# Запуск программы
main()
input("Нажмите Enter чтобы выйти")











