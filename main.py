import pygame
import random
 
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

# missil
missil = pygame.image.load('images/missile.png').convert_alpha()
missil = pygame.transform.scale(missil,(25,25)) # conversão do tamanho da nave
missil = pygame.transform.rotate(missil, -45)

# Posição dos players
pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

# pontos
pontos = 3

# Missil
triggered = False

# Indicates pygame is running
rodando = True

# Font
font = pygame.font.SysFont('fonts/PixelGameFont.ttf',50)

# Colisões
player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

# Funções
# Respawn do alien
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x,respawn_missil_y,triggered,vel_missil_x]

def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False

# Infinite loop
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

    # Teclas
    tecla = pygame.key.get_pressed()
    if (tecla[pygame.K_UP] or tecla[pygame.K_w] ) and pos_player_y > 1:
        pos_player_y -= 1
        if not triggered:
            pos_missil_y -= 1
    
    if (tecla[pygame.K_DOWN] or tecla[pygame.K_s]) and pos_player_y < 665:
        pos_player_y += 1
        if not triggered:
            pos_missil_y += 1
    
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 2

    # Game Over
    if pontos == -1:
        rodando = False

    # Respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()
    
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    # posição do rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x

    alien_rect.y = pos_alien_y
    alien_rect.x = pos_alien_x

    # Movimento
    x-=2
    pos_alien_x -=1
    pos_missil_x += vel_missil_x

    # Mostra colisões
    pygame.draw.rect(screen,(255,0,0),player_rect,4)
    pygame.draw.rect(screen,(255,0,0),missil_rect,4)
    pygame.draw.rect(screen,(255,0,0),alien_rect,4)

    # Score na tela
    score = font.render(f' Pontos: {int(pontos)} ', True, (0,0,0))
    screen.blit(score,(50,50))

    # Cria imagens Players em tela
    screen.blit(alien,(pos_alien_x, pos_alien_y))
    screen.blit(missil,(pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    # Update frame
    pygame.display.update()

'''
git add --all
git commit -m "carrega a página de jogos"
git push -u origin main
'''