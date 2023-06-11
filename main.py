import pygame as py
import sys
from content import stringOfContents

#Enter the expression here
expression = 'A + B * ~C = Q'

inputs, contents = stringOfContents(expression)

py.init()
py.display.set_caption('Truth Table')

fps = 60
fpsClock = py.time.Clock()
width, height = 1000,800
screen = py.display.set_mode((width,height))
textFont = py.font.SysFont('Arial',40)
textBoxColour = (0,100,0)

class TextBox:
    def __init__(self, x, y, w, h, text=''):
        self.textSurface = textFont.render(text,True,(0,0,0))
        self.rect = py.Rect(x, y, w, h)
        
    def draw(self,screen):
        py.draw.rect(screen,textBoxColour,self.rect,2)
        screen.blit(self.textSurface,self.rect)
        
screen.fill((255,255,255))

[[]
 ]


textboxes = []
columns = inputs + 1
rows = 2 ** inputs + 1

hspacing = (width-20)/(columns)
vspacing = (height-40)/(rows)

print(contents)
for r in range(rows):
    for c in range(columns):
        TextBox(10+hspacing*c,20+vspacing*r,hspacing,vspacing,contents[c+r*columns]).draw(screen)

py.display.flip()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            
