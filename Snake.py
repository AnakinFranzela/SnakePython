import keyboard
import random
import time
import os

rows = int(input("Rows: ")) + 2
cols = int(input("Cols: ")) + 2
pointsMax = (rows - 2) * (cols - 2) * 100
points = 300
counter = 3

# Правя матрица със съотношение [rows + 2, cols + 2] с цел покрайнините да са тиренца (стената в която змията не трябва да се блъска)
    # Мился си метод как да разчертая границите на игрището

matrix = [[" " for _ in range(cols)] for _ in range(rows)] # 0 for _ in range(cols) прави list с cols брой от 0; _ е throwaway variable, защото не се нуждаем от него
# Просто стойността i която я има по принцип, не я използваме
#for row in matrix:
#    print(' '.join(map(str, row))) # map(str, row) - преобразува цифрите в string, защото само string може да се joinva

# Прави границите на игралното поле
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1:
            matrix[i][j] = "-"
        elif j == 0 or j == cols - 1:
            matrix[i][j] = "|"

#for row in matrix:
#    print(' '.join(map(str, row)))
# Трябва да е стрингов масив, за да може вътре да слагам какъвто си символ искам (за главата, тялото, плода и свободното пространство)

snake = [(rows - 2, cols - 4), (rows - 2, cols - 3), (rows - 2, cols - 2)]
direction = "LEFT"
for (r, c) in snake:
    if c == cols - 4:
        matrix[r][c] = "+"
    else:
        matrix[r][c] = ":"

for row in matrix:
    print(' '.join(map(str, row)))

def spawn_fruit(matrix, snake, rows, cols): # Метод за добавяне на храната
    while True:
        if counter != pointsMax / 100:
            r = random.randint(1, rows - 2)
            c = random.randint(1, cols - 2)
            if (r, c) not in snake:  # Проверка за това да не се появи вътре в змията
                matrix[r][c] = "@"
                return (r, c)
        else:
            break

fruit = spawn_fruit(matrix, snake, rows, cols) # Начално плодче

# Пази информацията при всяко натискане на клавиша и директно сменя direction-а
def on_key(event):
    global direction
    if event.name == 'w' and direction != 'DOWN':
        direction = 'UP'
    elif event.name == 's' and direction != 'UP':
        direction = 'DOWN'
    elif event.name == 'a' and direction != 'RIGHT':
        direction = 'LEFT'
    elif event.name == 'd' and direction != 'LEFT':
        direction = 'RIGHT'

keyboard.hook(on_key)

#def playTheGame(matrix):
while points != pointsMax:
    time.sleep(0.3)  # леко забавяне, в случая е секунда

    # След това трябва да измисля как да стане движението на змията (вероятно чрез някоя библиотека)
    # Проверка за натиснат клавиш

    # Преместване на змията
    head = snake[0]
    if direction == "UP":
        newHead = (head[0] - 1, head[1])
    elif direction == "DOWN":
        newHead = (head[0] + 1, head[1])
    elif direction == "LEFT":
        newHead = (head[0], head[1] - 1)
    elif direction == "RIGHT":
        newHead = (head[0], head[1] + 1)

    # Проверка за удар в стена
    if (newHead[0] == 0 or newHead[0] == rows - 1 or
        newHead[1] == 0 or newHead[1] == cols - 1):
        print("Змията се удари в стената! Game Over!")
        break

    # Проверка за удар в себе си
    if newHead in snake:
        print("Змията се ухапа! Game Over!")
        break

    if newHead == fruit:
        counter += 1
        points += 100
        snake.insert(0, newHead)
        fruit = spawn_fruit(matrix, snake, rows, cols) # Добавяне на плода след изяждане
    else:
        # Обновяване на тялото
        snake.insert(0, newHead)  # нова глава
        snake.pop()                # махни опашката

    os.system('cls')

    # Принтирай дъската наново
    # първо изчисти матрицата (без стените)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            matrix[i][j] = " "

    # после постави змията
    for (r, c) in snake: # Тук трябва да направя проверка, за да може края на змията (опашката) да е различна
        matrix[r][c] = "#"
    matrix[snake[0][0]][snake[0][1]] = "+"  # главата
    matrix[snake[counter - 2][0]][snake[counter - 2][1]] = ":"
    matrix[snake[counter - 1][0]][snake[counter - 1][1]] = ":"

    if counter != pointsMax / 100:
        matrix[fruit[0]][fruit[1]] = "@"

    for row in matrix:
        print(' '.join(row))

    time.sleep(0.1)

if points != pointsMax:
    print(f"Game Over! Твоят резултат е {points} от {pointsMax}")
else:
    print(f"You won! Твоят резултат е {points} от {pointsMax}")
