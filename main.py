import pygame
import random

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))

clock = pygame.time.Clock()
running = True

# Cores
PRETO = (0,0,0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Tamanho comida e da cobra
TAMANHO = 50

# Cobra
velocidade = 10
combimento_cobra = 1
posicao_cobra = [largura // 2, altura // 2,]
corpo_cobra = []
cabeca_cobra = []

# Comida
posicao_comida = [random.randint(2, (largura - TAMANHO) // TAMANHO) * TAMANHO, 
                  random.randint(2, (altura - TAMANHO) // TAMANHO) * TAMANHO]


# Deslocamento
deslocamento_x = 0
deslocamento_y = 0

# Desenhar bloco cobra
def desenhar_cobra(corpo):
    for bloco in corpo:
        pygame.draw.rect(screen, VERDE, [bloco[0], bloco[1], TAMANHO, TAMANHO])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                deslocamento_x = 0
                deslocamento_y = -TAMANHO
            elif event.key == pygame.K_DOWN:
                deslocamento_x = 0
                deslocamento_y = TAMANHO
            elif event.key == pygame.K_LEFT:
                deslocamento_x = -TAMANHO
                deslocamento_y = 0
            elif event.key == pygame.K_RIGHT:
                deslocamento_x = TAMANHO
                deslocamento_y = 0
                
    screen.fill("black")
    
    desenhar_cobra(corpo_cobra)
    pygame.draw.rect(screen, VERMELHO, [posicao_comida[0], posicao_comida[1], TAMANHO, TAMANHO])
    
    posicao_cobra[0] += deslocamento_x
    posicao_cobra[1] += deslocamento_y
    cabeca_cobra = [posicao_cobra[0], posicao_cobra[1]]   
    corpo_cobra.append(cabeca_cobra)

    if len(corpo_cobra) > combimento_cobra:
        del corpo_cobra[0]

    for bloco in corpo_cobra[:-1]:
        if(cabeca_cobra == bloco):
            running = False
            
    if cabeca_cobra[0] < 0 or cabeca_cobra[0] > largura or cabeca_cobra[1] > altura or cabeca_cobra[1] < 0:
        running = False
        
    if cabeca_cobra == posicao_comida:
        combimento_cobra += 1
        posicao_comida = [random.randint(0, largura // TAMANHO) * TAMANHO, 
                        random.randint(0, altura // TAMANHO) * TAMANHO]    
        
    pygame.display.flip()
    
    # FPS
    clock.tick(velocidade) 
    
pygame.quit()