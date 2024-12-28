'''
SNAKE GAME (turtle module)
'''
import os
import turtle 
import time 
import random

delay = 0.1

# score
score = 0
high_score = 0

# setting up screen
window = turtle.Screen()
window.title("Snake game by @usaid")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  #turns off animation on the screen

# snake head
head = turtle.Turtle()
head.speed(0)  # not movement speed but animation speed
head.shape("circle")
head.color("dark green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Score: {score}  High Score: {high_score}",align="center", font=("Courier", 24, "normal"))


# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)   
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20) 
        
# keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# window.onkeypress(go_up, "w")
# window.onkeypress(go_down, "s")
# window.onkeypress(go_left, "a")
# window.onkeypress(go_right, "d")

# main gameloop
try:
    while True:
        window.update()
        
        # check for collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                
                # hide the segments
                for segment in segments:
                    segment.goto(1000,1000)
                
                # clear segments list
                segments.clear() 
                
                # reset the score
                score = 0
                
                # reset the delay
                delay = 0.1
                
                pen.clear()    
                pen.write(f"Score: {score}  High Score: {high_score}",align="center", font=("Courier", 24, "normal"))            
        
        
        # check for a collision with border
        if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            # clear segments list
            segments.clear()
            
            # reset the score
            score = 0    
            
            # reset the delay
            delay = 0.1        
            
            pen.clear()    
            pen.write(f"Score: {score}  High Score: {high_score}",align="center", font=("Courier", 24, "normal"))        
        
        
        
        # check for a collision with the food
        if head.distance(food) < 20:  # each basic turtle shape is 20 pixel wide and 20 pixel tall
            # move food to random spot on screen
            x = random.randint(-280,280)  #our screen is 600 x 600 so it would be from -300 to 300
            y = random.randint(-280,280)
            food.goto(x,y)
            
            # add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)
            
            # increase the score
            score += 10
            
            # shorten the delay
            delay -= 0.005
            
            if score > high_score:
                high_score = score
            
            pen.clear()    
            pen.write(f"Score: {score}  High Score: {high_score}",align="center", font=("Courier", 24, "normal"))
            
            
        # move the end segments firstin reverse order
        for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)
            
        # move segments zero to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
            
        move()
        
        time.sleep(delay)
except turtle.Terminator:
    print("Turtle graphics window closed. Exiting program.")


window.mainloop()  #keep window open 


