# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import Canvas
from tkinter import Tk, Button, Label
from random import randint

#defining Tk from Tkinter
root=Tk()
root.title("Catch the ball")
root.resizeable(False, False)

#defining the Canvas
canvas=Canvas(root, width=600, height=600)
canvas.pack()

#variable for vertical distance travelled by ball
limit=0

#variable for horizontal distance of bar from x-axis
dist=5

#variable for score
score=0

#Class for creating and moving the ball
class Ball:
    #for creation of ball on canvas
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.canvas=canvas
        
        #for creation of ball object
        self.ball=canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red", tags="dot1")
        
    #for moving the ball
    def move_ball(self):
        #defining offset
        offset=10
        global limit
        
        #checking if ball lands on ground or bar
        if limit>=510:
            global dist, score, next
            
            #checking that ball falls on the bar
            if (dist-offset<=self.x1 and dist+40+offset>=self.x2):
                #increment the score
                score+=10
                #make the ball disappear
                canvas.delete('dot1')
                #call object again for creation of ball
                ball_set()
            else:
                #disappear the ball and display the score
                canvas.delete('dot1')
                bar.delete_bar(self)
                score_board()
            return
        #increment distance travelled by ball
        limit+=1
        #moving ball in the canvas
        self.canvas.move(self.ball, 0, 1)
        #moving ball continuously
        self.canvas.after(10, self.move_ball)
        
 #class for creating and moving bar
class bar:
    #method for creating bar
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.canvas=canvas
        #creating the bar
        self.rod=canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='yellow', tags='dot2')
        
    #methof for moving the ball
    def move_bar(self, num):
        global dist
        #checking the forward or backward button
        if(num==1):
            #moving bar forward
            self.canvas.move(self.rod, 20, 0)
            dist+=20
        #else move bar backward
        else:
            self.canvas.move(self.rod, -20, 0)
            dist-=20
            
    def delete_bar(self):
        canvas.delete('dot2')
        
#function to define dimesions of  the ball
def ball_set():
    global limit
    limit=0
    #for random x distance from where ball begins to fall
    value=randint(0,570)
    #defining dimensions of the ball
    ball1=Ball(canvas, value, 20, value+30, 50)
    #for moving the ball
    ball1.move_ball()

#displaying scoreboard after game is over
def score_board():
    root2=Tk()
    root2.title('Catch the ball')
    root2.resizeable(False, False)
    canvas2=Canvas(root2, wifth=300, height=300)
    canvas2.pack()
    w=Label(canvas2, text="\nOOPS.. Game is over \n\n  Your Score is " + str(score)+"\n\n")
    w.pack()
    button3=Button(canvas2, text='Play Again?', bg='green', command=lambda:play_again(root2))
    button3.pack()
    button4=Button(canvas2, text='Exit', bg='green', command=lambda:exit_handler(root2))
    button4.pack()
    
#for handling play again request
def play_again(root2):
    root2.destroy()
    main()
    
#for handling exit request
def exit_handler(root2):
    root2.destroy()
    root.destroy()
    
#main function
def main():
    global score, dist
    score=0
    dist=0
    #defining dimensions of the bar
    bar1=bar(canvas, 5, 560, 45, 575)
    #defining buttons
    button=Button(canvas, text="==>", bg="green", command=lambda:bar1.move_bar(1))
    #place the buttons
    button.place(x=300, y=580)
    button2=Button(canvas, text="<==", bg="green", command=lambda:bar1.move_bar(0))
    button2.place(x=260, y=580)
    #calling the function
    ball_set()
    root.mainloop()
    
    #driver code
if(__name__=="__main__"):
    main()
    
        
        