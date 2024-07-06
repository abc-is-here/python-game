import random

maze_width = 10
maze_height = 10

maze = [['.' for _ in range(maze_width)] for _ in range(maze_height)]

start_pos = (0, 0)
end_pos = (maze_height - 1, maze_width - 1)

player_pos = list(start_pos)

maze[end_pos[0]][end_pos[1]] = 'E'

num_portals = 3
num_traps = 3

def place_item(item_list, symbol, count):
    while len(item_list) < count:
        pos = (random.randint(0, maze_height - 1), random.randint(0, maze_width - 1))
        if pos not in item_list and pos != start_pos and pos != end_pos:
            item_list.append(pos)
            maze[pos[0]][pos[1]] = symbol

portals = []
traps = []

place_item(portals, 'P', num_portals)
place_item(traps, 'T', num_traps)

key_pos = None
while key_pos is None:
    pos = (random.randint(0, maze_height - 1), random.randint(0, maze_width - 1))
    if pos != start_pos and pos != end_pos:
        key_pos = pos
        maze[pos[0]][pos[1]] = 'K'

has_key = False

def print_maze():
    temp_maze = [row.copy() for row in maze]
    temp_maze[player_pos[0]][player_pos[1]] = 'X'
    for row in temp_maze:
        print(' '.join(row))
    print()

def print_inventory():
    print("Inventory: " + ("Key" if has_key else "No key"))

def move_player(direction):
    global player_pos

    new_pos = player_pos.copy()

    if direction == 'w' and player_pos[0] > 0:  # Up
        new_pos[0] -= 1
    elif direction == 's' and player_pos[0] < maze_height - 1:  # Down
        new_pos[0] += 1
    elif direction == 'a' and player_pos[1] > 0:  # Left
        new_pos[1] -= 1
    elif direction == 'd' and player_pos[1] < maze_width - 1:  # Right
        new_pos[1] += 1

    player_pos = new_pos

    check_position()

def check_position():
    global player_pos, has_key, key_pos

    if tuple(player_pos) in portals:
        print("You found a portal! Teleporting...")
        player_pos = list(random.choice(portals))

    elif tuple(player_pos) in traps:
        print("You hit a trap! Back to start...")
        player_pos = list(start_pos)

    elif tuple(player_pos) == end_pos:
        if has_key:
            print("Congratulations! You reached the exit with the key!")
            exit()
        else:
            print("You need the key to exit!")

    elif tuple(player_pos) == key_pos:
        print("You found the key!")
        has_key = True
        key_pos = None

def game_loop():
    while True:
        print_maze()
        print_inventory()
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            move_player(move)
        else:
            print("Invalid move. Please enter 'w', 'a', 's', or 'd'.")

game_loop()
