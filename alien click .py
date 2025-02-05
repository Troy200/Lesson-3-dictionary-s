import pgzrun
import random


WIDTH=500
HEIGHT=500

Alien= Actor("alien")
Alien.x=(250)
Alien.y=(250)
msg=""
x="light blue"
score=0
faults=0
def draw():
    screen.fill(x)
    Alien.draw()
    
    screen.draw.text("Shoot the Alien",(200,10))
    screen.draw.text(msg,(10,480),fontsize=30,color="black")
    screen.draw.text("Score "+str(score),(10,460))
    screen.draw.text("Faults "+str(faults),(10,440))
        

def on_mouse_down(pos):
    global msg,x,score,faults
    if Alien.collidepoint(pos):
        Alien.x=random.randint(50,450)
        Alien.y=random.randint(50,450)
        msg="good shot"
        x="green"
        score=score+1

       
    else:
        msg="you missed"
        x="red"
        faults=faults+1
       





pgzrun.go()