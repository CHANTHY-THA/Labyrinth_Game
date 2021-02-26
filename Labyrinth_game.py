from tkinter import *
import winsound
root = Tk()

root.title("Wellcome to my game!")
img = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\hell.png")
coint = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\gold.png")
van = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\van.png")
box = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\ban.png")
star = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\life.png")
enamy = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\ee.png")
w = 1320
h = 750
my_canvas = Canvas(root, width=w, height=h, bg ="black")
my_canvas.pack()

# # student move
x = 45
y = 42
my_cicle = my_canvas.create_image(x,y, image=img)

# star 
size = 20
xstar = 30
ystar = 720
my_canvas.create_image(30,720, image=star)



# function

def right(event):
     global x,y 
    
     x = 30
     y = 0
     my_canvas.move(my_cicle, x,y)
def down(event):
     global x,y 
    
     x = 0
     y = 30
     my_canvas.move(my_cicle, x,y)
def up(event):
     global x,y 
     x = 0
     y = -30
     my_canvas.move(my_cicle, x,y)
     print(x,y)


size= 30 
array2D =[
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,4,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,2,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,2,0,0,0,0,0,0,0,0,1],
     [1,0,0,2,0,2,0,2,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1],
     [1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,2,0,0,0,0,0,0,1],
     [1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1],
     [1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,2,0,0,0,0,1],
     [1,2,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],
     [1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,2,0,0,1],
     [1,2,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
     [1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
     [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [1,0,0,0,0,0,0,0,5,0,5,0,5,0,5,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,2,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

def graphic() :
     global gold
     for num in range(len(array2D)):
          for i in range(len(array2D[num])):
               if array2D[num][i] == 1 :
                    my_canvas.create_image(15+(30*i),15+(30*num), image=box)

               elif array2D[num][i] ==2:
                    my_canvas.create_image(15+(30*i),15+(30*num), image=coint)

               elif array2D[num][i] == 4:
                    my_canvas.create_image(15+(30*i),15+(30*num), image=van)
             
                    
def enamymove():
     for num in range(len(array2D)):
          for i in range(len(array2D[num])):
               if array2D[num][i] == 5:
                    oval=my_canvas.create_image(15+(30*i),8+(30*num), image=enamy)
#                canvas.moveto(oval,2,0)
#     canvas.after(50, lambda: enamymove())
def left(event):
     global x,y 
     x = -30
     y = 0
                   
     my_canvas.move(my_cicle, x,y)
enamymove()
graphic()
#key
root.bind("<a>",left)
root.bind("<d>",right)
root.bind("<w>",up)
root.bind("<s>",down)

winsound.PlaySound("sound\\vanda.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
# mainloop
root.mainloop()