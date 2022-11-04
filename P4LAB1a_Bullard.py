# Brief Description: This program work on two shapes for to be display turtle! I also got little fancy with this?!
# I put in a prompt, so you can pick from 1-2 to get one of the shapes or even both by putting in anything higher than 2(gives you both shapes)!
# For more on this, please refer to the note below! You will see what I mean when you run this one!?

# CTI-110

# P4LAB1a - Shapes

# Kelly Bullard

# November 3, 2022

#

# Note: All of the shapes in this program does draw them in 2 different sizes and colors! Each one does starts with given So again, you will see what I mean when you run this one!?
import turtle        
win = turtle.Screen()  
t = turtle.Turtle()   # The t = is for all them(opt = shapes)

# Added some display options to make this special for opt's while loop
opt = int(input('Choose either 1-2(or enter a higher number than two for both) for a shape: '))
t.shape("turtle")   # For pen's icon shape
t.fillcolor('green') # This fills in the turtle!
# Added some display stuff to make this opt to give you 2 squares like in the note
while(opt == 1):
    t.pensize(3)            # Pen's size 
    t.pencolor("green")       # pen's color
    side_length = 100;
    t.forward(side_length)          
    t.left(90)            
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    
    t.pencolor("blue")     # Pen's color for this one
    side_length = 50;
    t.forward(side_length)          
    t.left(90)            
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    # The end commands
    win.mainloop()             # Waits for the user to close window
    

# Added some display stuff to make this opt to give you 2 triangles like in the note
# The triangle(s), sides are 360 / 3 = 120 degrees
while(opt == 2):
    t.pensize(3)           # Pen's size 
    t.pencolor("purple")     # Pen's color
    t.forward(100)          
    t.left(120)            
    t.forward(100)
    t.left(120)
    t.forward(100)
    
    t.pencolor("pink")       # Pen's color for this one
    t.forward(60)          
    t.left(120)            
    t.forward(60)
    t.left(120)
    t.forward(60)
    # The end commands
    win.mainloop()             # Waits for the user to close window
   
# Added some display stuff but nothing new but just having both shapes(2 of each shape) like in the note
else:
    t.pensize(3)            # Pen's size for both shapes
    t.pencolor("green")       # pen's color for the square
    side_length = 100;
    t.forward(side_length)          
    t.left(90)            
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    
    t.pencolor("blue")     # Pen's color for this one
    side_length = 50;
    t.forward(side_length)          
    t.left(90)            
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    
    t.pencolor("purple")     # Pen's color for the triangle
    t.forward(100)          
    t.left(120)            
    t.forward(100)
    t.left(120)
    t.forward(100)
    
    t.pencolor("pink")       # Pen's color for this one
    t.forward(60)          
    t.left(120)            
    t.forward(60)
    t.left(120)
    t.forward(60)
   
# The end commands
win.mainloop()             # Waits for the user to close window
