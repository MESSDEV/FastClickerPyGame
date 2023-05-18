409119import pygame
import time
pygame.init()
'''creating the program window'''
back = (200, 255, 255) #background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
clock = pygame.time.Clock()
'''rectangle class'''
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height) #rectangle
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def outline(self, frame_color, thickness): #outline of an existing rectangle
      pygame.draw.rect(mw, frame_color, self.rect, thickness)  
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
'''class label'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
cards = []
num_cards = 4
x = 70
for i in range(num_cards):
  new_card = Label(x, 170, 70, 100, YELLOW)
  new_card.outline(BLUE, 10)
  new_card.set_text('CLICK', 26)
  cards.append(new_card)
  x = x + 100
 
wait = 0
from random import randint
while True:
  if wait == 0:
      #transferring the label:
       wait = 20 #for how many ticks the label will be in one place
       click = randint(1, num_cards)
       for i in range(num_cards):
          cards[i].color((255,255,0))
          if (i + 1) == click:
              cards[i].draw(10, 40)
          else:
              cards[i].fill()
  else:
      wait -= 1
 
  pygame.display.update()
  clock.tick(40)
