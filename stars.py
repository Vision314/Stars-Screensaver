import pygame, random
pygame.init()

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Stars")


run = True
while run:
    pygame.time.delay(50)

    pygame.mouse.set_visible(False)


    for event in pygame.event.get():
        if pygame.mouse.get_rel() > (0, 0):
            run = False

    x = random.randint(1, 1920)
    y = random.randint(1, 1080)
    width = 1
    height = 1




    # if you wanted just black and white:
    starColor = random.randint(1, 255)
    pygame.draw.rect(win, (starColor, starColor, starColor), (x, y, width, height))

    # making different color stars (I like this one better ¯\_(ツ)_/¯)

    # starColorR = random.randint(1, 255)
    # starColorG = random.randint(1, 255)
    # starColorB = random.randint(1, 255)
    # pygame.draw.rect(win, (starColorR, starColorG, starColorB), (x, y, width, height))

    pygame.display.update()



pygame.quit()
