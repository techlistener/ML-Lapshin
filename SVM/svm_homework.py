import pygame
import sklearn.svm as svm
import numpy as np
from enum import Enum


class Button(Enum):
    Left = 1
    Right = 3


class Type(Enum):
    First = 1
    Second = 2


def draw_circle(coordinates_array, classification_array, current_event, current_class):
    color = redAsRgb if current_class == 1 else greenAsRgb
    pygame.draw.circle(window, color, current_event.pos, radius)
    coordinates_array.append(current_event.pos)
    classification_array.append(current_class)


redAsRgb = (255, 0, 0)
greenAsRgb = (0, 255, 0)
whiteAsRgb = (255, 255, 255)
radius = 5
line_width = 2
window_width = 1280
window_height = 720

pygame.init()

window = pygame.display.set_mode((window_width, window_height))
window.fill(whiteAsRgb)
pygame.display.update()

coordinates = []
classification = []

canPlay = True
while canPlay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            canPlay = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == Button.Left.value:
                draw_circle(coordinates, classification, event, Type.First.value)
            elif event.button == Button.Right.value:
                draw_circle(coordinates, classification, event, Type.Second.value)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            clf = svm.SVC(kernel='linear', C=1.0)
            clf.fit(coordinates, classification)

            a = clf.coef_[0][0]
            b = clf.coef_[0][1]
            c = clf.intercept_

            x = np.linspace(0, window_width, 2)
            y = (-1 * c - a * x) / b

            pygame.draw.line(window, (0, 0, 0), [x[0], y[0]], [x[1], y[1]], line_width)

        pygame.display.update()

pygame.quit()