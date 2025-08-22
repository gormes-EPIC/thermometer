import pygame # type: ignore
from datetime import date
import cv2


def car_display(temp, screen):
    disp_font = pygame.font.Font('freesansbold.ttf', 60)
    temp_font = pygame.font.Font('freesansbold.ttf', 250)