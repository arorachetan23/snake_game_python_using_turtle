
import turtle
import time


canvas=turtle.Screen()
canvas.title("Sanke Game")
canvas.setup(width=700,height=700)
canvas.bgcolor("#00bfff")
canvas.tracer(0) #turn off all animation

def go_up():
	head.direction="up"


def go_down():
	head.direction="down"


def go_left():
	head.direction="left"


def go_right():
	head.direction="right"			

def move_snake():
	y=head.ycor()
	x=head.xcor()

	if head.direction=="up":
		head.sety(y+20)

	if head.direction=="down":
		head.sety(y-20)

	if head.direction=="right":
		head.setx(x+20)

	if head.direction=="left":
		head.setx(x-20)		

#head of the snake

head=turtle.Turtle()
head.speed(0)
#ToDo: change the shape to triangle and then move accordingly
head.shape("square")
head.color("gray")
head.penup() #so that it doesn't draw anything
head.goto(0,0)
head.direction="stop"

delay=0.1

#keyboard setup
canvas.listen()
canvas.onkeypress(go_up,"w")
canvas.onkeypress(go_down,"s")
canvas.onkeypress(go_right,"d")
canvas.onkeypress(go_left,"a")

while True:
	canvas.update()
	move_snake()
	time.sleep(delay)




canvas.mainloop()  # startover