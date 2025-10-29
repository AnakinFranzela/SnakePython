import keyboard
import random

rows = int(input("Rows: ")) + 2
cols = int(input("Cols: ")) + 2

# Правя матрица със съотношение [rows + 2, cols + 2] с цел покрайнините да са тиренца (стената в която змията не трябва да се блъска)
    # Мился си метод как да разчертая границите на игрището

matrix = [[" " for _ in range(cols)] for _ in range(rows)] # 0 for _ in range(cols) прави list с cols брой от 0; _ е throwaway variable, защото не се нуждаем от него
# Просто стойността i която я има по принцип, не я използваме
for row in matrix:
    print(' '.join(map(str, row))) # map(str, row) - преобразува цифрите в string, защото само string може да се joinva

# Прави границите на игралното поле
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1:
            matrix[i][j] = "-"
        elif j == 0 or j == cols - 1:
            matrix[i][j] = "|"

for row in matrix:
    print(' '.join(map(str, row)))
# Трябва да е стрингов масив, за да може вътре да слагам какъвто си символ искам (за главата, тялото, плода и свободното пространство)

snake = [(rows - 2, cols - 4), (rows - 2, cols - 3), (rows - 2, cols - 2)]
direction = "LEFT"
for (r, c) in snake:
    if c == cols - 4:
        matrix[r][c] = "+"
    else:
        matrix[r][c] = "#"

for row in matrix:
    print(' '.join(map(str, row)))


#def playTheGame(matrix):

# След това трябва да измисля как да стане движението на змията (вероятно чрез някоя библиотека)

