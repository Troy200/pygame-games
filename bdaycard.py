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
slinger1=pygame.transform.scale(slinger,(600,600))
partypop=pygame.image.load("pro game devloper/games/images/party-popper-_for_pgzero-removebg-preview.png")
font1=pygame.font.SysFont("Arial",70)
font2=pygame.font.SysFont("Arial",30)
text1=font1.render("Happy Birthday",True,"white")
text2=font2.render("Have a great time at your birthday party.",True,"white")
text3=font2.render("Wishing you a  wonderful year ahead. ",True,"white")
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
    
    

    screen.blit(slinger1,(0,0))
    screen.blit(text2,(30,270))
    pygame.display.update()
    pygame.time.wait(3000)
    screen.fill("light blue")

    screen.blit(partypop,(0,200))
    screen.blit(text3,(30,10))
    pygame.display.update()
    pygame.time.wait(3000)
    screen.fill("light blue")





            
    pygame.display.update()

