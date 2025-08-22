import pygame
import time
import random
import view
import model

# Set up the Pygame window with a resolution of 1024x600 pixels.
pygame.init()

# Get the screen dimensions
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1024, 600), 0, 32)
pygame.display.set_caption('thermometer')

screen_delay = 30
viewt = time.time() + screen_delay
currv = 0
tempt = time.time() + 0.5

#
last_email = 0

# Variables for Pacman animation.
pacman = 0
a = 0 
# Variable for Star Wars animation.
z = 600


# Starting temperature value.
temp = 70.55

# Main loop to update the display.
while True:
    time.sleep(0.5)
    # Check if it's time to switch the display view.
    if time.time() > viewt:
        viewt = time.time() + screen_delay
        currv = random.randint(0,13)
        #currv = 13

        # Reset screen background.
        background = (0, 0, 0) 
        screen.fill(background)
        
        z = 600
    try: 
        temp, email = model.get_temp_API(last_email)
        if email == True:
            last_email = time.time()
    except OSError:
        temp = 70.55
    if temp == None:
        temp = 70.55

    
        
    temp = round(temp, 1)
    
    #Display temperature using the selected view.
    if currv == 0:
        view.classic_display(temp, screen)
    elif currv == 1:
        view.comic_display(temp, screen)
    elif currv == 2:
        view.console_display(temp, screen)
    elif currv == 3:
        view.digital_display(temp, screen)
    elif currv == 4:
        view.galaga_display(temp, screen)
    elif currv == 5:
        view.lovelace_display(temp, screen)
    elif currv == 6:
        view.medieval_display(temp, screen)
    elif currv == 7:
        view.oregon_display(temp, screen)
    elif currv == 8:
        a = a + 10
        if a > 1024:
            a = 0
        pacman = pacman + 1
        if pacman > 4:
            pacman = 1
        time.sleep(0.5)
        view.pacman_display(temp, pacman, a, screen)
    elif currv == 9:
        view.seventies_display(temp, screen)
    elif currv == 10:
        z -= 20
        view.starwars_display(temp, z, screen)
        time.sleep(0.5)
    elif currv == 11:
        view.tetris_display(temp, screen)   
    elif currv == 12:
        view.pokemon_display(temp, screen) 
    elif currv == 13:
        view.minecraft_display(temp, screen) 

    # Handle Pygame events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update the display.
    pygame.display.update()
