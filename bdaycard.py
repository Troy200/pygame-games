import pygame
import sys
pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("light blue")

cake=pygame.image.load("pro game devloper/games/images/bday_cake_for_pgzero-removebg-preview.png")
#cake1=pygame.transform.scale(cake,(400,400))
slinger=pygame.image.load("pro game devloper/games/images/party_slinger_for_pgzero-removebg-preview.png")
font1=pygame.font.SysFont("Arial",70)
text1=font1.render("Happy Birthday",True,"white")

run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()




    screen.blit(cake,(40,80))
    screen.blit(text1,(30,10))
    pygame.display.update()
    pygame.time.wait(3000)
    screen.fill("light blue")
    pygame.display.update()
    

    screen.blit(slinger,(0,0))
    pygame.time.wait(3000)
    screen.fill("light blue")






            
    pygame.display.update()

