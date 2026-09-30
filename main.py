import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
SIZE = 20
grid = []
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONWAYS GAME OF LIFE")
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 200, 100)

for i in range(int(WIDTH/SIZE)):
    grid.append([])
    for j in range(int(HEIGHT/SIZE)):
        grid[i].append(0)


playing = False
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    playing = False
                else: 
                    playing = True 

            if event.key == pygame.K_r:
                grid = []
                for i in range(int(WIDTH/SIZE)):
                    grid.append([])
                    for j in range(int(HEIGHT/SIZE)):
                        grid[i].append(0)


        if not playing and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = int(event.pos[0]/SIZE)
                y = int(event.pos[1]/SIZE)
                if grid[x][y] == 1:
                    grid[x][y] = 0
                else:
                    grid[x][y] = 1
    screen.fill(BLACK)

    if playing:
        grid_copy = [row[:] for row in grid]
        for i in range(int(WIDTH/SIZE)):
            for j in range(int(HEIGHT/SIZE)):
                neighbors = 0
                for move_x in [-1, 0, 1]:
                    for move_y in [-1, 0, 1]:
                        if move_x == 0 and move_y == 0:
                            continue
                        neighbor_x = (i+move_x)%int(WIDTH/SIZE)
                        neighbor_y = (j+move_y)%int(HEIGHT/SIZE)
                        neighbors += grid_copy[neighbor_x][neighbor_y]

                # conways rules
                if grid_copy[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        grid[i][j] = 0
                else:
                    if neighbors == 3:
                        grid[i][j] = 1
                
    # make grid
    for i in range(int(WIDTH/SIZE)):
        pygame.draw.line(screen, GREY, (i*SIZE, 0), (i*SIZE, HEIGHT))
    for i in range(int(HEIGHT/SIZE)):
        pygame.draw.line(screen, GREY, (0, i*SIZE), (WIDTH, i*SIZE))

    for i in range(int(WIDTH/SIZE)):
        for j in range(int(HEIGHT/SIZE)):
            sqr = grid[i][j]
            if sqr == 1:
                pygame.draw.rect(screen, GREEN, (i*SIZE, j*SIZE, SIZE, SIZE))

    pygame.display.flip()

pygame.quit()