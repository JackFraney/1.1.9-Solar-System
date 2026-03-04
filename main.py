import turtle as trtl
# Configure Variables
wn = trtl.Screen()

play = trtl.Turtle()
play.speed(0)
player_shape = "square"
player_color = "red"

draw = trtl.Turtle()
draw_speed = 0
draw.pensize(5)
draw.hideturtle()

# Make a list of blue dots
dot_shape = "circle"
dot_color = "blue"
dot_num = 4
dot_size = 1

dot_list = []

for index in range (dot_num):
  dot = trtl.Turtle()
  dot.shape(dot_shape)
  dot.color(dot_color)
  dot.shapesize(dot_size)
  dot.speed(0)
  dot_list.append(dot)


# Funciton Definitions
def wall (start_x, start_y, angle, length):
  draw.speed(draw_speed)
  draw.pu()
  draw.goto(start_x,start_y)
  draw.pd()
  draw.setheading(angle)
  draw.forward(length)

  
    # Move turtle up, down, left, and right
moveUp = True
moveDown = True
moveLeft = True
moveRight = True

def move_up():
  global moveUp
  moveUp = True
  wn.onkey(stop_up,"w")

  while moveUp == True:
    play.sety(play.ycor()+1)
    for index in range(dot_num):
      dot = dot_list[index]
      dot.circle(25,10)
      if (abs(play.xcor()-dot_list[index].xcor()) < 15 and abs(play.ycor()-dot_list[index].ycor()) < 15):
        play.goto(-250,0)

def stop_up():
  global moveUp
  moveUp = False

def move_down():
  global moveDown
  moveDown = True
  wn.onkey(stop_down,"s")

  while moveDown == True:
    play.sety(play.ycor()-1)
    for index in range(dot_num):
      dot = dot_list[index]
      dot.circle(25,10)
      if (abs(play.xcor()-dot_list[index].xcor()) < 15 and abs(play.ycor()-dot_list[index].ycor()) < 15):
        play.goto(-250,0)

def stop_down():
  global moveDown
  moveDown = False

def move_left():
  global moveLeft
  moveLeft = True
  wn.onkey(stop_left,"a")

  while moveLeft == True:
    play.setx(play.xcor()-1)
    for index in range(dot_num):
      dot = dot_list[index]
      dot.circle(25,10)
      if (abs(play.xcor()-dot_list[index].xcor()) < 15 and abs(play.ycor()-dot_list[index].ycor()) < 15):
        play.goto(-250,0)

def stop_left():
  global moveLeft
  moveLeft = False

def move_right():
  global moveRight
  moveRight = True
  wn.onkey(stop_right,"d")

  while moveRight == True:
    play.setx(play.xcor()+1)
    for index in range(dot_num):
      dot = dot_list[index]
      dot.circle(25,10)
      if (abs(play.xcor()-dot_list[index].xcor()) < 15 and abs(play.ycor()-dot_list[index].ycor()) < 15):
        play.goto(-250,0)

    

def stop_right():
  global moveRight
  moveRight = False


# Events
wn.bgcolor("lightblue")
play.pu()
play.goto(-250, 0)

draw.fillcolor("white")
draw.begin_fill()
wall(-300,-200,0,600)
wall(-300,200,0,600)
wall(-300,-200,90,400)
wall(300,-200,90,400)
draw.end_fill()

# make end zones
draw.fillcolor("green")
draw.begin_fill()
wall(-300,-200,0,100)
wall(-200,-200,90,400)
wall(-200,200,180,100)
wall(-300,200,-90,400)
draw.end_fill()


draw.fillcolor("green")
draw.begin_fill()
wall(200,-200,0,100)
wall(300,-200,90,400)
wall(300,200,180,100)
wall(200,200,-90,400)
draw.end_fill()


play.color(player_color)
play.shape(player_shape)

  # move dot back and forth

dot_x = -150
dot_y = 100

for index in range (dot_num):
  dot = dot_list[index]
  dot.pu()
  dot.goto(dot_x,dot_y)
  dot_x += 100
  if dot_y < 0:
    dot_y = 100
  else:
    dot_y = -100
 

 
 
wn.listen()

wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")  
# bind the functions to the arrow keys


while (True):
  for index in range(dot_num):
    dot = dot_list[index]
    dot.circle(25,10)
    if (abs(play.xcor()-dot_list[index].xcor()) < 15 and abs(play.ycor()-dot_list[index].ycor()) < 15):
      play.goto(-250,0)
    if play.xcor() > 250:
      print("Level Complete")


