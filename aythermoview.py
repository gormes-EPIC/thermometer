import pygame
import random
def BouncingTemp(temp, screen):
    colors = [
        (255, 0, 0),     # Red
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
        (255, 255, 0),   # Yellow
        (0, 255, 255),   # Cyan
        (255, 0, 255),   # Magenta
        (255, 165, 0),   # Orange
        (128, 0, 128),   # Purple
        (255, 255, 255), # White
        (255, 105, 180)  # Pink
    ]

    usedcolor = random.choice(colors)
    black = (0, 0, 0)
    dvdxspeed = 2
    dvdyspeed = 2
    Temp = temp
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1024, 600))
    pygame.display.set_caption("Hello World!")
    pygame.font.init()
    dvd = pygame.Rect(512, 300, 100, 25)
    font = pygame.font.SysFont('Impact', 48)
    temp_surface = font.render(f"{Temp} F°", True, usedcolor)
    text_rect = temp_surface.get_rect(center = dvd.center)


    running = True
    while running:
        screen.fill(black)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if dvd.x <= 925 and dvd.x >= 0:
            dvd.x += dvdxspeed
        else:
            dvdxspeed = -(dvdxspeed)
            usedcolor = random.choice(colors)
            dvd.x += dvdxspeed
        if dvd.y <= 570 and dvd.y >= 50:
            dvd.y += dvdyspeed
        else:
            dvdyspeed = -(dvdyspeed)
            usedcolor = random.choice(colors)
            dvd.y += dvdyspeed

    

        pygame.draw.ellipse(screen, usedcolor, dvd)

        temp_surface = font.render(f"{Temp} F°", True, usedcolor)
        temp_rect = temp_surface.get_rect()
        temp_rect.center = (dvd.centerx, dvd.centery-40)
        screen.blit(temp_surface, temp_rect)


        pygame.display.update()
        clock.tick(60)
    pygame.quit()
        # screen.fill(white)
        # pygame.display.update()

        # time.sleep(3)
        # screen.fill(blue)
        # pygame.display.update()
        # time.sleep(3)

        # Update the display.
    