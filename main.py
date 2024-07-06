maze_width = 10
maze_height = 10

maze = [['.' for _ in range(maze_width)] for _ in range(maze_height)]

start_pos = (0, 0)
end_pos = (maze_height - 1, maze_width - 1)

player_pos = list(start_pos)

maze[end_pos[0]][end_pos[1]] = 'E'

def print_maze():
    temp_maze = [row.copy() for row in maze]
    temp_maze[player_pos[0]][player_pos[1]] = 'X'
    for row in temp_maze:
        print(' '.join(row))
    print()


def move_player(direction):
    global player_pos

    new_pos = player_pos.copy()

    if direction == 'w' and player_pos[0] > 0:
        new_pos[0] -= 1
    elif direction == 's' and player_pos[0] < maze_height - 1:
        new_pos[0] += 1
    elif direction == 'a' and player_pos[1] > 0:
        new_pos[1] -= 1
    elif direction == 'd' and player_pos[1] < maze_width - 1:
        new_pos[1] += 1

    player_pos = new_pos


def game_loop():
    while True:
        print_maze()
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            move_player(move)
        else:
            print("Invalid move. Please enter 'w', 'a', 's', or 'd'.")

game_loop()