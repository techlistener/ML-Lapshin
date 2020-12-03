import numpy as np
import random
import pygame
import tensorflow as tf
from keras.models import load_model
from enum import Enum
from PIL import Image
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
dbname = 'mnist.keras'


class Button(Enum):
    Left = 1
    Right = 3


try:
    f = open(dbname)
    f.close()
    print('reading db from file')
    model = load_model(dbname)
except IOError:
    print('creating db')
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = Sequential()
    model.add(Flatten())

    model.add(Dense(256, activation=tf.nn.relu))
    model.add(Dense(256, activation=tf.nn.relu))
    model.add(Dense(10, activation=tf.nn.softmax))

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    model.fit(x=x_train, y=y_train, epochs=16, batch_size=32)

    model.save(dbname)

print(model.summary())


def save_picture_and_predict(screen):
    path = 'digit.png'
    pygame.image.save(screen, path)
    img = Image.open(path)
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0
    prediction = model.predict([img])[0]
    res = prediction.argsort()[::-1]
    print(res)


screen = pygame.display.set_mode((280, 280))
line_start = None

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == Button.Right.value:
                save_picture_and_predict(screen)
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            screen.fill(BLACK)
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pygame.draw.circle(screen, WHITE,
                           (pos[0] + random.randrange(2), pos[1] + random.randrange(2)), random.randrange(1, 5))
    pygame.display.update()