# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pega Fruta')

# ----- Inicia assets
largura_fruta = 32
altura_fruta = 32
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/fundofinal.jpg').convert()
pygame.mixer.music.load('assets/snd/91476_Glorious_morning.mp3')
pygame.mixer.music.set_volume(0.4)

cesta_WIDTH = 64
cesta_HEIGHT = 64
assets = ['assets/img/bananapixel.png','assets/img/limaopixel.png','assets/img/macapixel.png','assets/img/melanciapixel.png','assets/img/perapixel.png','assets/img/pessegopixel.png'] 
# incluir caminhos das imagens das frutas
# ----- Inicia estruturas de dados
# Definindo os novos tipos
cesta_img = pygame.image.load('assets/img/cesta.png').convert_alpha()
cesta_img = pygame.transform.scale(cesta_img, (cesta_WIDTH, cesta_HEIGHT))
font = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

starttime = time.time()


class Cesta(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Frutas(pygame.sprite.Sprite):
    def __init__(self, caminhos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        fruta = caminhos[random.randint(0,len(assets)-1)]
        fruta_img = pygame.image.load(fruta).convert_alpha()
        fruta_img = pygame.transform.scale(fruta_img, (largura_fruta, altura_fruta))
        self.image = fruta_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura_fruta)
        self.rect.y = random.randint(-500, -altura_fruta)
        self.speedx = 0
        self.speedy = 4 # velocidade de queda

    def update(self):
        # Atualizando a posição da fruta
        self.rect.y += self.speedy
        # Se a fruta passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            fruta = assets[random.randint(0,len(assets)-1)]
            fruta_img = pygame.image.load(fruta).convert_alpha()
            fruta_img = pygame.transform.scale(fruta_img, (largura_fruta, altura_fruta))
            self.image = fruta_img
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH-largura_fruta)
            self.rect.y = random.randint(-500, -altura_fruta)
            self.speedx = 0
            self.speedy = 4 # velocidade de queda)

class Pedras(pygame.sprite.Sprite):
    def __init__(self):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        pedra_img = pygame.image.load('assets/img/pedrapixel.png').convert_alpha()
        pedra_img = pygame.transform.scale(pedra_img, (largura_fruta, altura_fruta))
        self.image = pedra_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura_fruta)
        self.rect.y = random.randint(-300, -altura_fruta)
        self.speedx = 0
        self.speedy = 3 # velocidade de queda

    def update(self):
        # Atualizando a posição da fruta
        self.rect.y += self.speedy
        # Se a fruta passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            pedra_img = pygame.image.load('assets/img/pedrapixel.png').convert_alpha()
            pedra_img = pygame.transform.scale(pedra_img, (largura_fruta, altura_fruta))
            self.image = pedra_img
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH-largura_fruta)
            self.rect.y = random.randint(-300, -altura_fruta)
            self.speedx = 0
            self.speedy = 3 # velocidade de queda)

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de frutas
all_sprites = pygame.sprite.Group()
all_frutas = pygame.sprite.Group()
all_pedras = pygame.sprite.Group()
player = Cesta(cesta_img)
all_sprites.add(player)
# Criando as frutas
for i in range(8):
    fruta = Frutas(assets)
    all_sprites.add(fruta)
    all_frutas.add(fruta)

for i in range(2):
    pedra = Pedras()
    all_sprites.add(pedra)
    all_pedras.add(pedra)


score = 0

pygame.mixer.music.play(loops=-1)
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    now = time.time()
    if now > starttime + 60:
        print('Your score was: {}'.format(score))
        break

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 12
            if event.key == pygame.K_RIGHT:
                player.speedx += 12
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 12
            if event.key == pygame.K_RIGHT:
                player.speedx -= 12

    # ----- Atualiza estado do jogo
    # Atualizando a posição das frutas
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, all_frutas, True, pygame.sprite.collide_mask)
    if len(hits) != 0:
        for i in hits:
            all_frutas.remove(i)
            all_sprites.remove(i)
            fruta = Frutas(assets)
            all_sprites.add(fruta)
            all_frutas.add(fruta)
            score += 10
    hitspedra = pygame.sprite.spritecollide(player, all_pedras, True, pygame.sprite.collide_mask)
    if len(hitspedra) != 0:
        for i in hitspedra:
            all_pedras.remove(i)
            all_sprites.remove(i)
            pedra= Pedras()
            all_sprites.add(pedra)
            all_pedras.add(pedra)
            score -= 15
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando frutas
    all_sprites.draw(window)

    text_surface = font.render("{:05d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    text_surfacetempo = font.render("{:03d}".format(int(now - starttime+1)), True, (255, 255, 0))
    text_recttempo = text_surfacetempo.get_rect()
    text_recttempo.midtop = (WIDTH - 40,  10)
    window.blit(text_surfacetempo, text_recttempo)
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

