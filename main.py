# Importing the pygame module
import pygame
import random
 
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

# alien
alien = pygame.image.load('images/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien,(50,50))

# player
playerImg = pygame.image.load('images/space.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg,(50,50)) # conversão do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, -90)

# posição dos players
pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300


# Indicates pygame is running
rodando = True

# funções

# respawn do alien
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

# infinite loop
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    screen.blit(bg,(0,0))

    # Carrosel da imagem de fundo
    rel_x = x % bg.get_rect().width
    screen.blit(bg,(rel_x - bg.get_rect().width,0)) # cria background
    if rel_x < 1280:
        screen.blit(bg,(rel_x,0))

    # teclas
    tecla = pygame.key.get_pressed()
    if (tecla[pygame.K_UP] or tecla[pygame.K_w] ) and pos_player_y > 1:
        pos_player_y -= 1
    if (tecla[pygame.K_DOWN] or tecla[pygame.K_s]) and pos_player_y < 665:
        pos_player_y += 1

    # respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    # movimento
    x-=2
    pos_alien_x -=1

    # players em tela
    screen.blit(alien,(pos_alien_x, pos_alien_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    # update frame
    pygame.display.update()



'''
git add --all
git commit -m "carrega a página de jogos"
git push -u origin main
'''