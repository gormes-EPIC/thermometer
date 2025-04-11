import pygame
import time
import random
import views
# import board
# import adafruit_dht

# Initialize the DHT device for temperature and humidity reading.
# DHT11 sensor on pin D4 and DHT22 sensor on pin D18.
# dhtDevice = adafruit_dht.DHT11(board.D4)

# Set up the Pygame window with a resolution of 1024x600 pixels.
pygame.init()
screen = pygame.display.set_mode((1024, 600), 0, 32)
pygame.display.set_caption('thermometer')

# Initialize variables for screen display timing and current view.
screen_delay = 30
viewt = time.time() + screen_delay
currv = 0
tempt = time.time() + 0.5

# Variables for Pacman animation.
pacman = 0
a = 0 
# Variable for Star Wars animation.
z = 600


# Starting temperature value.
temp = 70.5

# def get_temp():
#     try:
#         temperature_c = dhtDevice.temperature
#         temp = temperature_c * (9 / 5) + 32
#         return temp
#     except RuntimeError as error:
#         time.sleep(0.5)
#     except Exception as error:
#         dhtDevice.exit()
#         raise error

# Main loop to update the display.
while True:
    # Check if it's time to switch the display view.
    if time.time() > viewt:
        viewt = time.time() + screen_delay
        currv += 1
        if currv > 11:
            currv = 0

        # Reset screen background.
        background = (0, 0, 0) 
        screen.fill(background)
        
        z = 600

    #temp = get_temp()
    temp = 70.5

    # Update temperature reading every 0.5 seconds.
    if time.time() > tempt:
        tempt = time.time() + 1
        temp = round(temp, 1)
    
    #Display temperature using the selected view.
    if currv == 0:
        views.classic_display(temp, screen)
    elif currv == 1:
        views.comic_display(temp, screen)
    elif currv == 2:
        views.console_display(temp, screen)
    elif currv == 3:
        views.digital_display(temp, screen)
    elif currv == 4:
        views.galaga_display(temp, screen)
    elif currv == 5:
        views.lovelace_display(temp, screen)
    elif currv == 6:
        views.medieval_display(temp, screen)
    elif currv == 7:
        views.oregon_display(temp, screen)
    elif currv == 8:
        a = a + 10
        if a > 1024:
            a = 0
        pacman = pacman + 1
        if pacman > 4:
            pacman = 1
        time.sleep(0.5)
        views.pacman_display(temp, pacman, a, screen)
    elif currv == 9:
        views.seventies_display(temp, screen)
    elif currv == 10:
        z -= 20
        views.starwars_display(temp, z, screen)
        time.sleep(0.5)
    elif currv == 11:
        views.tetris_display(temp, screen)
    

    # Handle Pygame events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update the display.
    pygame.display.update()