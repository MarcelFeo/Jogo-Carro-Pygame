# Importando o Pygame e Random
import pygame
from random import randint

pygame.init()

# Posição inicial do carro
x = 305
y = 100

# Posição do inimigo
x_enemy1 = 200
y_enemy1 = 800
x_enemy2 = 400
y_enemy2 = 1000
x_enemy3 = 305
y_enemy3 = 2200

# Cronometro
timer = 0
time_score = 0 

# "Velocidade" do objeto
velocity = 15

# "Velocidade" do inimigo
velocity_enemy = 22

# Define o background e os carros
background =  pygame.image.load('img/Road.png')
car = pygame.image.load('img/Car.png')
enemy1 = pygame.image.load('img/enemy.png')
enemy2 = pygame.image.load('img/enemy2.png')
enemy3 = pygame.image.load('img/enemy3.png')

# Fonte do texto
font = pygame.font.SysFont('arial black', 50)
font2 = pygame.font.SysFont('arial black', 150)

# O que vai ser escrito
text = font.render('Tempo: ', True, (255, 255, 255), (0, 0, 0))
game_over = font2.render('GAME OVER', True, (0, 0, 0), (255, 255, 255))

# Posição do texto na tela
pos_text = text.get_rect()
pos_text.center = (65, 300)
pos_game_over = game_over.get_rect()
pos_game_over.center = (400, 300)

# Define a window do jogo
window = pygame.display.set_mode((800, 600))

# Define o nome da window
pygame.display.set_caption("Game")

# Deixa a window aberta até que o usuário feche o jogo
window_open = True
while window_open:

  pygame.time.delay(50)

  for event in pygame.event.get():
    # Evento para fechar o jogo (QUIT)
    if event.type == pygame.QUIT:
      window_open = False

  # Pega os comandos dos botões pressionados
  commands = pygame.key.get_pressed()

  # Controles
  if commands[pygame.K_RIGHT] and x <= 430:
    x += velocity
  if commands[pygame.K_LEFT] and x >= 160:
    x -= velocity

  # Colisão
  if ((x + 60 > x_enemy2 and y + 170 > y_enemy2)): # Direita
    y = 1200
    y_enemy2 = 2200
  if ((x - 60 < x_enemy1 and y + 170 > y_enemy1)): # Esquerda
    y = 1200
    y_enemy1 = 2200
  if ((x + 60 > x_enemy3 and y + 170 > y_enemy3) and (x - 60 < x_enemy3 and y + 170 > y_enemy3)): # Centro
    y = 1200
    y_enemy3 = 2200

  # Faz com que o carro inimigo fique dando voltas na tela
  if (y_enemy1 <= -80):
    y_enemy1 = randint(800, 1000)
  if (y_enemy2 <= -80):
    y_enemy2 = randint(1200, 2000)
  if (y_enemy3 <= -80):
    y_enemy3 = randint(2200, 3000)

  # Movimento dos inimigos
  y_enemy1 -= velocity_enemy
  y_enemy2 -= velocity_enemy + 10
  y_enemy3 -= velocity_enemy + 20

  # Faz com que o cronometro funcione
  if (timer < 20):
    timer += 1
  else:
    time_score += 1
    text = font.render('Tempo: ' + str(time_score), True, (255, 255, 255), (0, 0, 0))
    timer = 0


  # Coloca o background
  window.blit(background, (0, 0))

  # Coloca o carro
  window.blit(car, (x, y))

  # Coloca os carros inimigos
  window.blit(enemy1, (x_enemy1, y_enemy1))
  window.blit(enemy2, (x_enemy2, y_enemy2))
  window.blit(enemy3, (x_enemy3, y_enemy3))

  # Coloca o texto na tela
  window.blit(text, pos_text)

  # GAME OVER
  if y == 1200:
    window.blit(game_over, pos_game_over)

  # Atualiza a tela
  pygame.display.update()

pygame.quit()
