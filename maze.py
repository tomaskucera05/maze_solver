import pygame
import time
pygame.init()
pygame.display.set_caption("Maze Solver")
screen = pygame.display.set_mode((640, 640))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 200, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)   

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#", "#"],
    ["#", " ", "#", "#", " ", "#", " ", "#", "#", " ", "#", " ", "#", " ", " ", "#"],
    ["#", " ", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", " ", " ", " ", "#", " ", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", "#", "#", " ", "#", " ", "#", "#", " ", " ", " ", " ", "#"],
    ["#", "#", " ", " ", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#"],
    ["#", "#", "#", " ", "#", "#", " ", " ", "#", "#", "#", "#", " ", " ", "#", "#"],
    ["#", "G", " ", " ", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#"],
    ["#", "#", "#", "#", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#", "#", "#"],
    ["#", "#", "#", " ", "#", " ", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#"],
    ["#", "#", "#", " ", "#", "#", " ", "#", " ", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", " ", " ", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", " ", "#"],
    ["#", "#", "#", "#", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]
robot_row = 1
robot_col = 1
move_stage = 0
ROWS = len(maze)
COLS = len(maze[0])
TILE_SIZE = 640//16

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * TILE_SIZE
            y = row * TILE_SIZE

            tile = maze[row][col]
            color = WHITE 

            if tile == "#":
                color = BLACK
            elif tile == "S":
                color = GREEN
            elif tile == "G":
                color = RED

            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (200, 200, 200), (x, y, TILE_SIZE, TILE_SIZE), 1) 
    robot_x = robot_col * TILE_SIZE
    robot_y = robot_row * TILE_SIZE
    pygame.draw.rect(screen, BLUE, (robot_x, robot_y, TILE_SIZE, TILE_SIZE))

visited = set()
visited.add((robot_row, robot_col))

def move():
    global robot_col, robot_row, move_stage, visited
    directions = [(-1,0), (0,1), (0,-1), (1,0)]

    for i in range(4):
        dr, dc = directions[move_stage]
        new_row = robot_row + dr
        new_col = robot_col + dc

        if maze[new_row][new_col] != "#" and (new_row, new_col) not in visited:
            robot_row = new_row
            robot_col = new_col
            visited.add((robot_row, robot_col))
            time.sleep(0.3)
            return True
        else:
            move_stage = (move_stage + 1) % 4

    return False


visited_stuck = set()
move_stuck = 0

def stuck():
    global move_stuck, visited_stuck, robot_row, robot_col

    visited_stuck.add((robot_row, robot_col))
    directions = [(-1,0), (0,1), (0,-1), (1,0)]
    dr, dc = directions[move_stuck]
    new_row = robot_row + dr
    new_col = robot_col + dc

    if maze[new_row][new_col] != "#" and ((new_row, new_col)) not in visited_stuck:
        visited_stuck.add((robot_row, robot_col))
        robot_row = new_row
        robot_col = new_col
        time.sleep(0.3)
    else:
        move_stuck = (move_stuck + 1) % 4

running = True
while running:
    screen.fill(WHITE)
    draw_maze()
    if maze[robot_row][robot_col] != "G":
        if not move():
            stuck()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

