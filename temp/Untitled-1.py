from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('PIN&PON')
ck=time.Clock()
fps=144
a=transform.scale(image.load('63e88ac100f1091469bedb8f4da81058.jpg'), (700,500))
class gmsprite(sprite.Sprite):
    def __init__ (self, img, x, y, speed,weight,height):
        sprite.Sprite.__init__(self)
        self.image= transform.scale(image.load(img), (weight,height))
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class cort(gmsprite):
    def move(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y <= 395:
            self.rect.y+=self.speed
cort1=cort("file.jpg",12,250,3,10,100)
cort2=cort("file.jpg",688,250,3,10,100)
game=True
while game:
    for k in event.get():
        if k.type == QUIT:
            game=False
    window.blit(a,(0,0))
    cort1.reset()
    cort1.move()
    cort2.reset()
    cort2.move()
    display.update()
    ck.tick(fps)