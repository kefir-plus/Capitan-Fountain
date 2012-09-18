# -*- coding: utf-8 -*-
import sys,random,pygame
from collections import deque

pygame.init()		#инициальзация

textcolor = 0,0,0		#цвет текста
size = width, height = 800, 600		#размер окна
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Капитан-фонтан")		#заголовок окна

class tree:
	'Doc: Class Tree represents the Physical Tree/Zombie and properties'
	def __init__(self):
		self.img = pygame.image.load("res/enemy.png")
		self.rect = self.img.get_rect()
		ty = random.random()
		ty = ty * 500
		self.rect = self.rect.move(730,ty)
		spawn = self.rect
	def get_rectangle(self):
		return self.rect
	def left(self): 
		return self.rect.left
	def right(self):
		return self.rect.right
	def top(self):
		return self.rect.top
	def bottom(self):
		return self.rect.bottom
	def render(self):
		screen.blit(self.img,self.rect)
	def move(self,x,y):
		self.rect = self.rect.move(x,y)

bg = pygame.image.load("res/fonr.jpg")
bgrect = bg.get_rect()
screen.blit(bg,bgrect)

#play again? :)
def re_play():
	gover = pygame.image.load("res/gover.png")
	grect = gover.get_rect()

	#Play again please :D
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.blit(bg,bgrect)
		screen.blit(gover,grect)
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_SPACE]: break
		pygame.display.flip()
	begin()

#oops gameover condition
def gameover(x,y):
	tempscreen = pygame.image.load("res/gameover.jpeg")
	trect = tempscreen.get_rect()
	boom = pygame.image.load("res/boom.png")
	brect = boom.get_rect()
	brect = brect.move(x,y)
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		screen.blit(tempscreen,trect)
		screen.blit(boom,brect)
		
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_RETURN]:break
		pygame.display.flip()

	re_play()


def begin():

	#Мой код
	########
	font = pygame.font.Font("res/font.ttf",18)
	########

	#init some important vars and load some images
	score = 0
	timer = 32
	trees = deque()
	trees.append(tree())

	meme = pygame.image.load("res/fonman.png")
	mrect = meme.get_rect()
	mrect = mrect.move(200,230)


	#end of init-ing some important vars and loading some images

	#Мой код
	########
	building = pygame.image.load("res/b.png")
	bx = 200
	by = 264
	########

	while 1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT: sys.exit()
		screen.blit(bg,bgrect)
		
		#Мой код
		########
		bx = bx - 5
		if bx <= - 400: bx = 800
		screen.blit(building, (bx, by))
		########

		#render the scoreboard
		if pygame.time.get_ticks()%200: score = score + 1
		scoreline = "DISTANCE: "+str(score)
		scoreboard = font.render(scoreline,1,textcolor)
		
		screen.blit(scoreboard,scoreboard.get_rect())
		
		#render trees at random intervals of time
		if pygame.time.get_ticks() % (100*random.randint(1,3)) == 0:
			tree_o = tree()
			trees.append(tree_o)
		for Tree in trees:
			Tree.move(-4,0)
			Tree.render()
	
		if trees:
			if trees[0].right() < 0 : trees.popleft()
 	
		pressed = pygame.key.get_pressed()
		moved = 0
		
		#jump for sometime if up key is pressed
		if pressed[pygame.K_UP]:
			mrect = mrect.move(0,-5)
			screen.blit(meme,mrect)
			moved = 0
		if pressed[pygame.K_DOWN]:
			mrect = mrect.move(0,5)
			screen.blit(meme,mrect)
			moved = 0
		else:
			screen.blit(meme,mrect)

		
		#death condition 
		for Tree in trees:
			if Tree.left() <=274 and Tree.left() >= 258:
				if mrect.bottom == 395: 
					pygame.image.save(screen,"res/gameover.jpeg")
					x = Tree.get_rectangle()
					gameover(x[0],x[1])
		
			if Tree.left() <= 168 and Tree.left() >= 154:
				if mrect.bottom == 395: 
					pygame.image.save(screen,"res/gameover.jpeg")
					x = Tree.get_rectangle()
					gameover(x[0],x[1])
	
		if moved == 1:
			mrect = mrect.move(-31,90)
			timer = timer + 1

		if timer <= 25: timer = timer + 1
		pygame.display.flip()	


def main():
	
	#draw the welcome screen
	welcome = pygame.image.load("res/welcome.png")
	wrect = welcome.get_rect()

	#wait till the user presses "enter" key
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
	
 		screen.blit(welcome,wrect)
		pressed = pygame.key.get_pressed()
		
		if pressed[pygame.K_RETURN]: break
	
		pygame.display.flip()
	
	#BEGIN THE GAME :D
	begin()

if __name__ == "__main__":
	main()