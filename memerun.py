import sys,random,pygame
from collections import deque

pygame.init()

textcolor = 255,205,125
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("memeRun by Suhas")

class tree:
	'Doc: Class Tree represents the Physical Tree and properties'
	def __init__(self):
		self.img = pygame.image.load("tree.png")
		self.rect = self.img.get_rect()
		self.rect = self.rect.move(730,305)
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

bg = pygame.image.load("memebg.png")
bgrect = bg.get_rect()
screen.blit(bg,bgrect)

def gameover():
	gover = pygame.image.load("gover.png")
	grect = gover.get_rect()
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.blit(bg,bgrect)
		screen.blit(gover,grect)
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_RETURN]: break
		pygame.display.flip()
	begin()
		
		
def begin():
	score = 0
	timer = 0
	trees = deque()
	trees.append(tree())

	meme = pygame.image.load("meme.png")
	mrect = meme.get_rect()
	mrect = mrect.move(200,330)

	leg3 = pygame.image.load("leg3.png")
	legs = pygame.image.load("legs.png")
	lr3 = leg3.get_rect()
	lrect = legs.get_rect()
	lr3 = lr3.move(200,350)
	lrect = lrect.move(160,350)

	myfont = pygame.font.Font("Kelvinized.ttf",18)
	while 1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT: sys.exit()
		screen.blit(bg,bgrect)
		
		if pygame.time.get_ticks()%200: score = score + 1
		scoreline = "DISTANCE: "+str(score)
		scoreboard = myfont.render(scoreline,1,textcolor)
		
		screen.blit(scoreboard,scoreboard.get_rect())
		
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

		if pressed[pygame.K_UP]:
			if timer <  20:
				mrect = mrect.move(30,-90)
				lr3 = lr3.move(30,-90)
				screen.blit(meme,mrect)
				screen.blit(leg3,lr3)
				moved = 1
				#timer = timer + 1
			else:
				screen.blit(meme,mrect)
				screen.blit(legs,lrect)
			
		else:
			screen.blit(meme,mrect)
			screen.blit(legs,lrect)
		
		for Tree in trees:
			if Tree.left() <=274 and Tree.left() >= 258:
				if mrect.bottom == 395: gameover()
			

		if moved == 1:
			mrect = mrect.move(-30,90)
			lr3 = lr3.move(-30,90)
			
		if timer > 40 : timer = 0
		pygame.display.flip()	


def main():
	
	welcome = pygame.image.load("welcome.png")
	wrect = welcome.get_rect()
	wrect = wrect.move(40,40)

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
	
 		screen.blit(welcome,wrect)
		pressed = pygame.key.get_pressed()
		
		if pressed[pygame.K_RETURN]: break
	
		pygame.display.flip()

	begin()

if __name__ == "__main__":
	main()
