import pygame as pg

pg.init()

win = pg.display.set_mode((500,500))
pg.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pg.time.delay(100)
    for event in pg.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pg.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

    pg.draw.rect(win, (255, 0, 0), (x, y, width, height))  # This takes: window/surface, color, rect
    pg.display.update()  # This updates the screen so we can see our rectangle

pg.quit()  # If we exit the loop this will execute and close our game
