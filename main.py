import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("movements")
x=250
y=250
sprite= pygame.image.load("ufo.png")
sprite_rect= sprite.get_rect(center=(x,y))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    key=pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        x=x-5
    
    if key[pygame.K_RIGHT]:
        x=x+5

    
    if key[pygame.K_DOWN]:
        y=y+5
    
    if key[pygame.K_UP]:
        y=y-5
    sprite_rect.center=(x,y)
    
    screen.blit(sprite,sprite_rect)
    pygame.display.flip()