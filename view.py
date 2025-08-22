import pygame
from datetime import date
import cv2

def classic_display(temp, screen):
    """
    Function to display temperature in classic style.
    """
    disp_font = pygame.font.Font('freesansbold.ttf', 60)
    temp_font = pygame.font.Font('freesansbold.ttf', 250)

    # Set background color based on temperature.
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

    # Display "° Fahrenheit" text.
    message_text = disp_font.render("° Fahrenheit", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 440)
    screen.blit(message_text, message_rect)

    # Display temperature value.
    message_text = temp_font.render(str(temp), True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 300)
    screen.blit(message_text, message_rect)


def comic_display(temp, screen):
    """
    Function to display temperature with Comic Sans
    """
    temp_font = pygame.font.Font('fonts/comicsans.ttf', 300)
    disp_font = pygame.font.Font('fonts/comicsans.ttf', 90)

    # Set background color.
    background = (255, 255, 255) 
    screen.fill(background)

    # Display temperature value.
    message_text = temp_font.render(str(temp), True, (0,255,0))
    message_rect = message_text.get_rect()
    message_rect.center = (500, 300)
    screen.blit(message_text, message_rect)

    # Display "degrees" text.
    message_text = disp_font.render("degrees", True, (0,0,255))
    message_rect = message_text.get_rect()
    message_rect.center = (880, 380)
    screen.blit(message_text, message_rect)


def console_display(temp, screen):
    """
    Function to display temperature in console style.
    """
    font = pygame.font.SysFont('dejavusansmono', 60)

    # Set background color.
    background = (0, 0, 0) 
    screen.fill(background)
   
    # Display current date.
    message_text = font.render(str(date.today()), True, (0,255,0))
    message_rect = message_text.get_rect()
    message_rect.center = (720, 480)
    screen.blit(message_text, message_rect)

    # Display temperature value and unit.
    message_text = font.render(str(temp) + "° Fahrenheit", True, (0,255,0))
    message_rect = message_text.get_rect()
    message_rect.center = (720, 550)
    screen.blit(message_text, message_rect)


def digital_display(temp, screen):
    """
    Function to display temperature in digital style.
    """
    temp_font = pygame.font.Font('fonts/ibm3270semicondensed.ttf', 480)
    disp_font = pygame.font.Font('fonts/ibm3270semicondensed.ttf', 60)

    # Set background color.
    background = (0, 0, 0) 
    screen.fill(background)
   
    # Display temperature value.
    message_text = temp_font.render(str(temp), True, (173,9,33))
    message_rect = message_text.get_rect()
    message_rect.center = (500, 375)
    screen.blit(message_text, message_rect)

    # Display "DEGREES FAHRENHEIT" text.
    message_text = disp_font.render("DEGREES FAHRENHEIT", True, (173,9,33))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 80)
    screen.blit(message_text, message_rect)



cap = cv2.VideoCapture('assets/galaga_79sec_480p.mp4')
success, img = cap.read()
shape = img.shape[1::-1]
clock = pygame.time.Clock()
def galaga_display(temp, screen):
    """
    Function to display temperature with a Galaga theme.
    E.Y. 2024
    """
    disp_font = pygame.font.Font('fonts/topaz.ttf', 50)
    message_text = disp_font.render(str(temp) + " degrees Fahrenheit", True, (255, 255, 255))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 550)
    screen.blit(message_text, message_rect)
    
    success, img = cap.read()
    if success:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "RGB"), (100, 30))
    
def lovelace_display(temp, screen):
    """
    Function to display temperature with an Ada Lovelace theme.
    """
    img = pygame.image.load('assets/ada.png')
    screen.blit(img, (0,0))


    disp_font = pygame.font.SysFont('arial', 50, bold=True)

    # Display thematic text.
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


def medieval_display(temp, screen):
    """
    Function to display temperature with a medieval style.
    """
    temp_font = pygame.font.SysFont('z003', 480)
    disp_font = pygame.font.SysFont('z003', 60)

    # Set background color.
    background = (214, 197, 159) 
    screen.fill(background)

    # Display thematic text.
    message_text = disp_font.render("Hear Ye! Hear Ye! It is", True, (35,35,35))
    message_rect = message_text.get_rect()
    message_rect.center = (330, 100)
    screen.blit(message_text, message_rect)
    
    # Display temperature value.
    message_text = temp_font.render(str(temp), True, (35,35,35))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 380)
    screen.blit(message_text, message_rect)

    # Display "degrees Fahrenheit." text.
    message_text = disp_font.render("degrees Fahrenheit.", True, (35,35,35))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 550)
    screen.blit(message_text, message_rect)

def oregon_display(temp, screen):
    """
    Function to display temperature with an Oregon Trail theme.
    """
    img = pygame.image.load('assets/oregontrail.png')
    screen.blit(img, (125,100))

    # Draw a green rectangle for text background.
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(100, 400, 824, 100))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(106, 406, 812, 88))

    disp_font = pygame.font.Font('fonts/courierprime.ttf', 40)
    message_text = disp_font.render("It is " + str(temp) + " degrees Fahrenheit.", True, (0,255,00))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 450)
    screen.blit(message_text, message_rect)


def pacman_display(temp, num, a, screen):

    """
    Function to display temperature with a Pacman theme.
    """
    # Fill background
    background = (0, 0, 0) 
    screen.fill(background)

    temp_font = pygame.font.Font('fonts/topaz.ttf', 400)
    disp_font = pygame.font.Font('fonts/topaz.ttf', 80)

    # Draw a black rectangle for Pacman animation.
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 525, 1024, 75))

    # Draw Pacman trail.
    b = a + 5
    while b < 1024:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(b, 565, 5, 5))
        b = b + 25
    pygame.display.flip()

    # Load Pacman image based on animation frame.
    if num == 1:
        img = pygame.image.load('assets/pacman1.png')
    elif num == 3:
        img = pygame.image.load('assets/pacman3.png')
    else:
        img = pygame.image.load('assets/pacman2.png')
    screen.blit(img, (a,550))

    # Display temperature value.
    message_text = temp_font.render(str(temp), True, (0, 0, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 270)
    screen.blit(message_text, message_rect)

    # Display "degrees" text.
    message_text = disp_font.render("degrees", True, (0, 0, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 490)
    screen.blit(message_text, message_rect)

def pokemon_display(temp, screen):
    """
    Function to display temperature with a Pokemon theme.
    """
    # Fill background
    background = (255, 255, 255) 
    screen.fill(background)

    # Load image
    img = pygame.image.load('assets/pokemon.jpg')
    screen.blit(img, (212,0))

    disp_font = pygame.font.SysFont('liberationmono', 30, bold=True)

    # Display thematic text.
    message_text = disp_font.render("A wild "+ str(temp) + " degree server" , True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (475, 445)
    screen.blit(message_text, message_rect)

    message_text = disp_font.render("room appeared!", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (375, 480)
    screen.blit(message_text, message_rect)


def seventies_display(temp, screen):
    """
    Function to display temperature in 70's font.
    """
    temp_font = pygame.font.SysFont('nimbussansnarrow', 480)
    disp_font = pygame.font.SysFont('nimbussansnarrow', 60)

    # Set background color.
    background = (35, 35, 35) 
    screen.fill(background)

    # Display temperature value with a shadow effect.
    message_text = temp_font.render(str(temp), True, (37, 155, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 350)
    screen.blit(message_text, message_rect)

    message_text = temp_font.render(str(temp), True, (37, 219, 86))
    message_rect = message_text.get_rect()
    message_rect.center = (522, 350)
    screen.blit(message_text, message_rect)

    message_text = temp_font.render(str(temp), True, (219, 180, 37))
    message_rect = message_text.get_rect()
    message_rect.center = (532, 350)
    screen.blit(message_text, message_rect)

    # Display "degrees fahrenheit" text.
    message_text = disp_font.render("degrees fahrenheit", True, (37, 155, 219))
    message_rect = message_text.get_rect()
    message_rect.center = (512, 530)
    screen.blit(message_text, message_rect)




def starwars_display(temp, z, screen):
    """
    Function to display temperature with a Star Wars theme.
    """
    title_font = pygame.font.Font('fonts/ubuntucondensed.ttf', round(0.088*z))
    title_font2 = pygame.font.Font('fonts/ubuntucondensed.ttf', round(0.1333*(z + 0.1333*z)))
    disp_font = pygame.font.SysFont('piboto', round(0.08333*z), bold=True)
    disp_font2 = pygame.font.SysFont('piboto', round(0.08333*(z + 0.2*z)), bold=True)
    disp_font3 = pygame.font.SysFont('piboto', round(0.08333*(z + 0.3*z)), bold=True)
    disp_font4 = pygame.font.SysFont('piboto', round(0.08333*(z + 0.4*z)), bold=True)

    # Set background color.
    background = (0, 0, 0) 
    screen.fill(background)

    # Display Star Wars style text crawl.
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



# Function to display temperature with a Tetris theme.
# - J.P. 2024
ColorPatters = [
[(66, 66, 255),(99, 173, 255)],
[(16, 148, 0),(140, 214, 0)],
[(156, 24, 206),(239, 107, 255)],
[(0, 88, 248),(91, 219, 87)],
[(231, 0, 91),(88, 248, 152)],
[(88, 248, 152),(107, 136, 255)],
[(248, 56, 0),(127, 127, 127)],
[(107, 71, 255),(171, 0, 35)],
[(0, 88, 248),(248, 56, 0)],
[(248, 56, 0),(255, 163, 71)],
]
NumberLayout = {
    "0":[[1,0],[2,0], [0,1],[0,2],[0,3], [3,1],[3,2],[3,3], [1,4],[2,4]],
    "1":[[0,4],[1,4],[2,4],[3,4], [1,3],[2,3],[1,2],[2,2],[0,1],[1,1],[2,1],[1,0],[2,0]],
    "2":[[0,4],[1,4],[2,4],[3,4], [0,0],[1,0],[2,0], [3,1],[2,2],[1,3]],
    "3":[[0,0],[1,0],[2,0], [1,2],[2,2], [0,4],[1,4],[2,4], [3,1],[3,3]],
    "4":[[2,4],[2,3],[2,2],[2,1],[2,0], [3,2],[1,2],[0,2], [1,1]],
    "5":[[0,0],[1,0],[2,0],[3,0],[0,0], [0,4],[1,4],[2,4], [3,3],[2,2],[2,2],[1,1], [0,1]],
    "6":[[3,0],[2,0], [1,1],[2,1],[0,2],[0,3],[3,2],[3,3],[1,4],[2,4]],
    "7":[[0,0],[1,0],[2,0],[3,0],[2,1],[1,2],[1,3],[1,4]],
    "8":[[1,0],[2,0],[0,1],[3,1], [1,2],[2,2],[0,3],[3,3],[1,4],[2,4]],
    "9":[[1,0],[2,0],[0,1],[3,1],[1,2],[2,2], [3,2],[2,3],[1,4]],
    ".":[[1,4],[2,4],[1,3],[2,3]],
    "°":[[1,0],[2,0],[1,1],[2,1]],
}
def Spawn_tet_tile(x,y,screen,size = 32,pattern = ColorPatters[0],num = 0):
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x, y, size,size))
    img = pygame.transform.scale(pygame.image.load(f"{'assets/Tetris_'+(num%2 == 0 and 'outline' or 'whole')}.png"), (size,size))
    img.fill(pattern[num%2], None, pygame.BLEND_RGBA_MULT)
    screen.blit(img, (x,y))

def tetris_display(temp, screen):
    screen.fill((0, 0, 0))

    # Background Rendering
    ogw, h = pygame.display.get_surface().get_size()
    h = 600
    w = 1024
    img = pygame.transform.scale(pygame.image.load('assets/Tetris_bg.png'), (w, h))
    screen.blit(img, ((ogw/2)-(w/2),0))

    # Pattern to Temp range
    if temp <= -6:
        pattern = ColorPatters[0]
    elif temp <= 8:
        pattern = ColorPatters[1]
    elif temp <= 22:
        pattern = ColorPatters[2]
    elif temp <= 36:
        pattern = ColorPatters[3]
    elif temp <= 50:
        pattern = ColorPatters[4]
    elif temp <= 64:
        pattern = ColorPatters[5]
    elif temp <= 78:
        pattern = ColorPatters[6]
    elif temp <= 92:
        pattern = ColorPatters[7]
    elif temp <= 106:
        pattern = ColorPatters[8]
    else:
        pattern = ColorPatters[9]

    count = 0
    size = 20
    left = (ogw/2)-((len([*str(temp),"°"])*size*3.75)/2)
    for l in [*str(temp),"°"]:
        for p in NumberLayout.get(l):
            Spawn_tet_tile(left+(p[0]*size)+(count*size*4.25),(h/2)+(p[1]*size)-size*2,screen, size,pattern,count)
        count += 1

def nightsky_display(temp):
    img = pygame.image.load('nightsky.jpeg')
    screen.blit(img, (0,0))

    temp_font = pygame.font.Font(None, 500)
    f_font = pygame.font.Font(None, 300)
    time_font = pygame.font.SysFont("Arial", 100)

    # Display Fahrenheit text.
    message_text = f_font.render(str("°F"), True, (173,216,230))
    message_rect = message_text.get_rect()
    message_rect.center = (860, 300)
    screen.blit(message_text, message_rect)

    # Display temperature value.
    message_text = temp_font.render(str(temp), True, (225,225,225))
    message_rect = message_text.get_rect()
    message_rect.center = (400, 250)
    screen.blit(message_text, message_rect)

    # Display time.
    time = date.today()
    message_text = time_font.render(str(time), True, (173,216,230))
    message_rect = message_text.get_rect()
    message_rect.center = (500, 500)
    screen.blit(message_text, message_rect)
