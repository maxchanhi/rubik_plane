def print_matrix(matrix):
        for row in matrix:
            print(row)
        print()

def vertical(col):
    temp_1 = plane[0][col]
    temp_2 = plane[1][col]
    temp_3 = plane[2][col]
    plane[0][col] = temp_3
    plane[1][col] = temp_1
    plane[2][col] = temp_2
    return plane

def move_down(col): #if col = 0
    vertical(col)
    return plane

def move_up(col): 
    for i in range(2):
        vertical(col)
    return plane

def horizontal(row): #0
    temp_1 = plane[row][0]
    temp_2 = plane[row][1]
    temp_3 = plane[row][2]
    plane[row][0] = temp_3
    plane[row][1] = temp_1
    plane[row][2] = temp_2
    return plane

def move_left(row):
    for i in range(2):
        horizontal(row)
    return plane

def move_right(row):
    horizontal(row)
    return plane
import random

def com_input(c, p):
    command = ["u", "d", "l", "r"][c]
    position = [0, 1, 2][p]
    return [command, position]

def shuffle():
    difficulty=input("Choose your difficulty level: [1, 2, 3]")
    user_input = []
    try:
        if difficulty == "1":
            for j in range(2):
                user_input.append(com_input(random.randint(0, 3), random.randint(0, 2)))
            #print(user_input)
        elif difficulty == "2":
            for j in range(10):
                user_input.append(com_input(random.randint(0, 3), random.randint(0, 2)))
        elif difficulty == "3":
            for j in range(15):
                user_input.append(com_input(random.randint(0, 3), random.randint(0, 2)))
        for i in range(len(user_input)):
            command = user_input[i][0]
            position = int(user_input[i][1])
            plane = moving(command, position)
        if plane == [[1,2,3],[4,5,6],[7,8,9]]:
            shuffle()
        else:
            pass
        return plane
    except:
        print("Invalid input")
        return shuffle()

def moving(command, position):
    if command == "u":
        plane = move_up(position)
    elif command == "d":
        plane = move_down(position)
    elif command == "l":
        plane = move_left(position)
    elif command == "r":
        plane = move_right(position)
    return plane

def main(plane):
    print_matrix(plane)
    step = 0
    while True:
        user_input = input("Enter a command: [u, d, l, r] and a position, q for quit: ")
        if user_input == "q":
            break
        elif len(user_input) != 2 or user_input[0] not in "udlr" or user_input[1] not in "012":
            print("Invalid command")
            continue
        command = user_input[0]
        position = int(user_input[1])
        if command == "u":
            plane = move_up(position)
            step += 1 
        elif command == "d":
            plane = move_down(position)
            step += 1 
        elif command == "l":
            plane = move_left(position)
            step += 1 
        elif command == "r":
            plane = move_right(position)
            step += 1 
        else:
            print("Invalid command")
            continue
        print_matrix(plane)
        if plane == [[1,2,3],[4,5,6],[7,8,9]]:
            print("You win!","\nNumber of steps:",step)
            break
if __name__ == "__main__":
    plane=[[1,2,3],[4,5,6],[7,8,9]]
    plane = shuffle()
    main(plane)
