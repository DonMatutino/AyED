import pygame

def set_score(score):
    score [0] = 0

    if score [4] > 5:
        score [4] = 0
        score [3] += 1
max_score = 99999
score = [0, 0, 0, 0, 0]
print("Puntaje: ", score[0])
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sistema de Score")
pygame.init()
[21:59]
pip install pygame