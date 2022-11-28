# Importing the pygame module
import pygame
from pygame.locals import *
 
# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()



# tamanho da janela
x = 1280
y = 720
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em Python')

# fundo da tela
bg = pygame.image.load('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg,(x,y))


# Indicates pygame is running
rodando = True

# infinite loop
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    pygame.display.update()



'''
git remote add origin https://github.com/joeyrfs/jogo_nave_01.git
git add --all
git commit -m "carrega a página de jogos"
git push -u origin main
'''