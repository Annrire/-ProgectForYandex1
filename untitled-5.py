import pygame
import os
pygame.init()
 
sc = pygame.display.set_mode((400, 300))
sc.fill((255, 255, 255))
x = 80
y = 100
fullname = os.path.join('data', 'creature.png')
dog_surf = pygame.image.load(fullname)
dog_rect = dog_surf.get_rect(bottomright=(x, y))
sc.blit(dog_surf, dog_rect)
pygame.display.update()
running = True
start = False
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10            
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
            start = True
    if start:
        pygame.draw.circle(sc, (255, 255, 255), (x, y), 300)        
        start = False
        dog_rect = dog_surf.get_rect(bottomright=(x, y))
        sc.blit(dog_surf, dog_rect)  
    pygame.display.update()    
pygame.quit()