import pgzrun
import random


WIDTH=500
HEIGHT=500

Alien= Actor("alien")
Alien.x=(250)
Alien.y=(250)
msg=""
def draw():
    screen.fill("light blue")
    Alien.draw()
    
    screen.draw.text("Shoot the Alien",(200,10))
    screen.draw.text(msg,(10,480),fontsize=50,color="black")


def on_mouse_down(pos):
    global msg
    if Alien.collidepoint(pos):
        Alien.x=random.randint(50,450)
        Alien.y=random.randint(50,450)
        msg="good shot"
         #screen.fill("green")
    else:
        msg="you missed"
pgzrun.go()