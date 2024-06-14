import board
import adafruit_dht
import pygame
import time
from datetime import date
import random

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)
dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

# Set up pygame window
pygame.init()
screen = pygame.display.set_mode((1024, 600), 0, 32)
pygame.display.set_caption('thermometer')

# Initializations for display swaps
screen_delay = 15
viewt = time.time() + screen_delay
currv = 0

# Starting temp
temp = 70.5

# Pacman vars
pacman = 0
a = 0 

# Star Wars vars
z = 600


def classic_display(temp):

    disp_font = pygame.font.Font('freesansbold.ttf', 60)
    temp_font = pygame.font.Font('freesansbold.ttf', 250)

    if temp < 50:
        background = (65, 105, 225) # royal blue
    elif temp < 55:
        background = (135, 206, 250) # light sky blue
    elif temp < 60:
        background = (224, 255, 255) # light cyan
    elif temp < 65:
        background = (240, 255, 240) # honeydew
    elif temp < 70:
        background = (154, 205, 50) # yellow green
    elif temp < 75:
        background = (255, 215, 0) # yellow
    elif temp < 80:
        background = (250, 128, 114) # gold
    else: 
        background = (250, 128, 114) # salmon
    screen.fill(background)

    message_text = disp_font.render("° Fahrenheit", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 440)
    screen.blit(message_text, message_rect)

    message_text = temp_font.render(str(temp), True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 300)
    screen.blit(message_text, message_rect)


def comic_display(temp):

    temp_font = pygame.font.SysFont('comicsans', 300)
    disp_font = pygame.font.SysFont('comicsans', 90)

    background = (255, 255, 255) 
    screen.fill(background)

    message_text = temp_font.render(str(temp), True, (0,255,0))
    message_rect = message_text.get_rect()
    message_rect.center = (500, 300)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("degrees", True, (0,0,255))
    message_rect = message_text.get_rect()
    message_rect.center = (880, 380)
    screen.blit(message_text, message_rect)
   

def console_display(temp):

    font = pygame.font.SysFont('consolas', 60)

    background = (0, 0, 0) 
    screen.fill(background)
   
    message_text = font.render(str(date.today()), True, (0,255,0))
    message_rect = message_text.get_rect()
    message_rect.center = (740, 480)
    screen.blit(message_text, message_rect)

    message_text = font.render(str(temp) + "° Fahrenheit", True, (0,255,0))
    message_rect = message_text.get_rect()
    message_rect.center = (740, 550)
    screen.blit(message_text, message_rect)


def digital_display(temp):

    temp_font = pygame.font.SysFont('ibm3270semicondensed', 480)
    disp_font = pygame.font.SysFont('ibm3270semicondensed', 60)

    background = (0, 0, 0) 
    screen.fill(background)
   
    message_text = temp_font.render(str(temp), True, (173,9,33))
    message_rect = message_text.get_rect()
    message_rect.center = (500, 375)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("DEGREES FAHRENHEIT", True, (173,9,33))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 80)
    screen.blit(message_text, message_rect)

def lovelace_display(temp):
    img = pygame.image.load('ada.png')
    screen.blit(img, (0,0))

    disp_font = pygame.font.SysFont('arial', 50, bold=True)

    message_text = disp_font.render("The server", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (265, 265)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("room is " + str(temp), True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (285, 315)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("degrees", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (235, 365)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("Fahrenheit.", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (275, 415)
    screen.blit(message_text, message_rect)

def medieval_display(temp):

    temp_font = pygame.font.SysFont('ebgaramondsc', 480)
    disp_font = pygame.font.SysFont('ebgaramondsc', 60)

    background = (214, 197, 159) 
    screen.fill(background)


    message_text = disp_font.render("Hear Ye! Hear Ye! It is", True, (35,35,35))
    message_rect = message_text.get_rect()
    message_rect.center = (330, 100)
    screen.blit(message_text, message_rect)
    
    message_text = temp_font.render(str(temp), True, (35,35,35))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 280)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("degrees Fahrenheit.", True, (35,35,35))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 550)
    screen.blit(message_text, message_rect)

def oregon_display(temp):
    img = pygame.image.load('oregontrail.png')
    screen.blit(img, (125,100))

    pygame.draw.rect(screen, (0,255,0), pygame.Rect(100, 400, 824, 100))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(106, 406, 812, 88))

    disp_font = pygame.font.SysFont('tlwgtypist', 40, bold=True)
    message_text = disp_font.render("It is " + str(temp) + " degrees Fahrenheit.", True, (0,255,00))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 450)
    screen.blit(message_text, message_rect)


def pacman_display(temp, num, a):

    temp_font = pygame.font.SysFont('amiga', 400)
    disp_font = pygame.font.SysFont('amiga', 80)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 525, 1024, 75))

    b = a + 5
    while b < 1024:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(b, 565, 5, 5))
        b = b + 25
    pygame.display.flip()

    if num == 1:
        img = pygame.image.load('pacman1.png')
    elif num == 3:
        img = pygame.image.load('pacman3.png')
    else:
        img = pygame.image.load('pacman2.png')
    screen.blit(img, (a,550))

    message_text = temp_font.render(str(temp), True, (0, 0, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 270)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("degrees", True, (0, 0, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 490)
    screen.blit(message_text, message_rect)
    

def seventies_display(temp):

    temp_font = pygame.font.SysFont('sawasdee', 480)
    disp_font = pygame.font.SysFont('sawasdee', 60)

    background = (35, 35, 35) 
    screen.fill(background)

    message_text = temp_font.render(str(temp), True, (37, 155, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 250)
    screen.blit(message_text, message_rect)

    message_text = temp_font.render(str(temp), True, (37, 219, 86))
    message_rect = message_text.get_rect()
    message_rect.center = (522, 250)
    screen.blit(message_text, message_rect)

    message_text = temp_font.render(str(temp), True, (219, 180, 37))
    message_rect = message_text.get_rect()
    message_rect.center = (532, 250)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("degrees fahrenheit", True, (37, 155, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 530)
    screen.blit(message_text, message_rect)


def starwars_display(temp, z):

    title_font = pygame.font.SysFont('ubuntucondensed', round(0.088*z))
    title_font2 = pygame.font.SysFont('ubuntucondensed', round(0.1333*(z + 0.1333*z)))
    disp_font = pygame.font.SysFont('roboto', round(0.08333*z), bold=True)
    disp_font2 = pygame.font.SysFont('roboto', round(0.08333*(z + 0.2*z)), bold=True)
    disp_font3 = pygame.font.SysFont('roboto', round(0.08333*(z + 0.3*z)), bold=True)
    disp_font4 = pygame.font.SysFont('roboto', round(0.08333*(z + 0.4*z)), bold=True)

    background = (0, 0, 0) 
    screen.fill(background)

    message_text = title_font.render("EPISODE IV:", True, (255, 242, 0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, z)
    screen.blit(message_text, message_rect)

    message_text = title_font2.render("A NEW HOPE", True, (255, 242, 0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, z + 0.1333*z)
    screen.blit(message_text, message_rect)

    message_text =  disp_font.render("It was a period of civil war.", True, (255, 242, 0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, z + 0.4*z)
    screen.blit(message_text, message_rect)

    message_text =  disp_font2.render("And it was " + str(temp) + " degrees" , True, (255, 242, 0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, z + 0.5*z)
    screen.blit(message_text, message_rect)

    message_text =  disp_font3.render("Fahrenheit in the server" , True, (255, 242, 0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, z + 0.6*z)
    screen.blit(message_text, message_rect)

    message_text =  disp_font4.render("room.                                 " , True, (255, 242, 0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, z + 0.7*z)
    screen.blit(message_text, message_rect)


while True:
    if time.time() > viewt:
        viewt = time.time() + screen_delay
        currv = random.randint(0,9)

        background = (0, 0, 0) 
        screen.fill(background)
        
        z = 600
    
    try:
        temperature_c = dhtDevice.temperature
        temp = temperature_c * (9 / 5) + 32
    except RuntimeError as error:
        time.sleep(0.5)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(0.5)
    temp = round(temp, 1)
  

    if currv == 0:
        classic_display(temp)
    elif currv == 1:
        console_display(temp)
    elif currv == 2:
        comic_display(temp)
    elif currv == 3:
        digital_display(temp)
    elif currv == 4:
        lovelace_display(temp)
    elif currv == 5:
        medieval_display(temp)
    elif currv == 6:
        oregon_display(temp)
    elif currv == 7:
        a = a + 10
        if a > 1024:
            a = 0
        pacman = pacman + 1
        if pacman > 4:
            pacman = 1
        pacman_display(temp, pacman, a)
    elif currv == 8:
        seventies_display(temp)
    elif currv == 9:
        z -= 20
        starwars_display(temp, z)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()


    