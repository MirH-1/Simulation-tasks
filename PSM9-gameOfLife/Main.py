import pygame
import sys
from random import randrange
from tkinter import Tk, Label, Entry, Button, StringVar, Frame

class Grid:
    def __init__(self, resolution, screen_width, screen_height):
        self.resolution = resolution
        self.columns = screen_width // resolution
        self.rows = screen_height // resolution
        self.cells = [[randrange(2) for _ in range(self.columns)] for _ in range(self.rows)]
        self.default_rules()

    def default_rules(self):
        self.lower_bound = 2
        self.upper_bound = 3
        self.rebirth = 3

    def count_neighbors(self, x, y):
        directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]
        return sum(self.cells[(x + dx) % self.columns][(y + dy) % self.rows] for dx, dy in directions)

    def update_grid(self):
        new_grid = [[0] * self.columns for _ in range(self.rows)]
        for x in range(self.columns):
            for y in range(self.rows):
                neighbors = self.count_neighbors(x, y)
                if self.cells[x][y] == 1 and (neighbors < self.lower_bound or neighbors > self.upper_bound):
                    new_grid[x][y] = 0
                elif self.cells[x][y] == 0 and neighbors == self.rebirth:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = self.cells[x][y]
        self.cells = new_grid

    def draw(self, surface):
        for x in range(self.columns):
            for y in range(self.rows):
                color = (255, 255, 255) if self.cells[x][y] == 1 else (0, 0, 0)
                pygame.draw.rect(surface, color, [x * self.resolution, y * self.resolution, self.resolution, self.resolution])

def setup_tkinter(grid):
    root = Tk()
    root.title("Control Panel for Game of Life")
    frame = Frame(root)
    frame.pack()

    lower_bound_var = StringVar(value='2')
    upper_bound_var = StringVar(value='3')
    rebirth_var = StringVar(value='3')

    Label(frame, text="Lower Bound:").pack(side='left')
    Entry(frame, textvariable=lower_bound_var, width=5).pack(side='left')
    Label(frame, text="Upper Bound:").pack(side='left')
    Entry(frame, textvariable=upper_bound_var, width=5).pack(side='left')
    Label(frame, text="Rebirth:").pack(side='left')
    Entry(frame, textvariable=rebirth_var, width=5).pack(side='left')

    def update_rules():
        try:
            lower = int(lower_bound_var.get())
            upper = int(upper_bound_var.get())
            rebirth = int(rebirth_var.get())
            grid.lower_bound = lower
            grid.upper_bound = upper
            grid.rebirth = rebirth
        except ValueError as e:
            print(e)

    Button(root, text="Update Rules", command=update_rules).pack()
    return root

def main():
    pygame.init()
    screen_width, screen_height, resolution = 1000, 1000, 20
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    grid = Grid(resolution, screen_width, screen_height)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    root = setup_tkinter(grid)
    root.update()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        grid.update_grid()
        grid.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        clock.tick(5)  # Update speed
        root.update()

    pygame.quit()
    root.destroy()
    sys.exit()

if __name__ == "__main__":
    main()
