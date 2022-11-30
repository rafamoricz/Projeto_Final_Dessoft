# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pega Fruta')

# ----- Inicia assets
largura_fruta = 32
altura_fruta = 32
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/starfield.png').convert()


assets = ['assets/img/bananapixel.png','assets/img/limaopixel.png','assets/img/macapixel.png','assets/img/melanciapixel.png','assets/img/perapixel.png','assets/img/pessegopixel.png'] 
# incluir caminhos das imagens das frutas
# ----- Inicia estruturas de dados
# Definindo os novos tipos


class Sorteio(pygame.sprite.Sprite):
    def __init__(self,caminhos):
        # Sorteia qual fruta sera mostrada na tela
        pygame.sprite.Sprite.__init__(self)
        fruta = caminhos[random.randint(0,len(assets)-1)]
        fruta_img = pygame.image.load(fruta).convert_alpha()
        fruta_img = pygame.transform.scale(fruta_img, (largura_fruta, altura_fruta))
        self.image = fruta_img
        self.rect = self.image.get_rect()

        

class Frutas(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura_fruta)
        self.rect.y = random.randint(-100, -altura_fruta)
        self.speedx = 0
        self.speedy = random.randint(4, 6) # velocidade de queda

    def update(self):
        # Atualizando a posição da fruta
        self.rect.y += self.speedy
        # Se a fruta passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura_fruta)
            self.rect.y = random.randint(-100, -altura_fruta)
            self.speedx = 0
            self.speedy = random.randint(4, 6) # velocidade de queda)

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de frutas
all_frutas = pygame.sprite.Group()
# Criando as frutas
for i in range(8):
    fruta = Frutas(Sorteio(assets))
    all_frutas.add(fruta)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição das frutas
    all_frutas.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando frutas
    all_frutas.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

