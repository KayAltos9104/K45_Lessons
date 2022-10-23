import pygame
import cellular_automata
from cellular_automata import *  

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
SCALE = 5


def render_field(field):    
    for y in range(0, len(field), 1):
        for x in range(0, len(field[y]), 1):
            if field[y][x] == 1:
                print('\u25a0', end='')
            elif field[y][x] == 0:
                print(' ', end='')
        print()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Cellular Automata')
    clock = pygame.time.Clock()
    CA = CellularAutomata(160)    
    iterations = 120
    while iterations >=0:
        CA.update_field()        
        iterations -= 1

    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(WHITE)
        for y in range(0, len(CA.field), 1):
            for x in range(0, len(CA.field[y]), 1):
                if CA.field[y][x] == 1:
                    pygame.draw.rect(screen, BLACK,(x*SCALE, y*SCALE, SCALE, SCALE))
              
            
        #pygame.draw.rect(screen, BLACK, (50,50, 100, 100))
        pygame.display.flip()
        clock.tick(FPS)
    
    
    #render_field(CA.field)
       

main()
    
    

        


           

     
