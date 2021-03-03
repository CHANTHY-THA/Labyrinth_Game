from tkinter import *
import winsound
root = Tk()
# file of image 
root.title("Wellcome to my game!")
img = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\hell.png")
coint = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\gold.png")
van = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\van.png")
box = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\ban.png")
enamy = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\ee.png")
fire = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\red.png")
school = PhotoImage(file="C:\\Users\\student\\Desktop\\LABYRINTH_GAME\\picture\\school.png")
w = 1320
h = 685
my_canvas = Canvas(root, width=w, height=h)
my_canvas.pack(side=BOTTOM)

# array2D of graphic
array2D =[
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,10,0,0,1,2,0,2,0,2,0,2,0,2,0,1,0,1,0,2,2,2,2,2,2,2,2,2,1,0,2,0,2,0,2,0,2,0,2,0,2,0,2,1],
     [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,2,1,1,1,1,1,1,1,2,1,0,6,1,1,1,1,1,1,1,1,1,1,1,0,1],
     [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,1,0,0,0,0,0,1,2,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,2,1,0,2,1,0,4,7,0,0,1,2,1,0,1,1,2,1,0,1,0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,6,1,0,0,0,0,0,1,2,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,1,1,1,1,1,1,0,6,0,0,0,1,2,1,0,1,2,2,2,2,2,2,2,2,1,0,1,0,0,1,2,0,0,0,6,0,0,1,0,1],
     [1,0,0,2,0,2,0,2,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1],
     [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,2,1,0,0,0,0,0,0,0,0,5,0,0,0,1,0,1,0,0,1,2,0,0,0,0,1,0,1],
     [1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,2,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,2,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,2,0,0,1,0,1],
     [1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,2,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1],
     [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,2,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,2,0,0,1],
     [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,2,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1],
     [1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,2,1,0,1,0,1,0,0,0,5,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,2,1],
     [1,0,1,0,0,0,0,0,0,0,0,5,0,0,0,0,0,1,5,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1],
     [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1],
     [1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,1,0,0,0,6,0,0,0,0,0,6,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
     [1,0,0,0,0,0,1,2,0,2,0,2,1,0,0,0,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
# Display graphic of game
isFound = True
def graphic() :
     global gold ,isFound
     for num in range(len(array2D)):
          for i in range(len(array2D[num])):
               if array2D[num][i] == 1 :
                    my_canvas.create_image(15+(30*i),15+(30*num), image=box)

               elif array2D[num][i] ==2:
                    my_canvas.create_image(15+(30*i),15+(30*num), image=coint)

               elif array2D[num][i] == 4:
                    my_canvas.create_image(15+(30*i),15+(30*num), image=van)
             
               elif array2D[num][i] == 6:
                    my_canvas.create_image(15+(30*i),25+(30*num), image=fire)
               elif array2D[num][i] == 10:
                    my_canvas.create_image(15+(30*i),15+(30*num), image=img)
               elif array2D[num][i] == 5:
                    my_canvas.create_image(15+(30*i),10+(30*num), image=enamy)
     
               elif array2D[num][i] == 7:
                    my_canvas.create_image(15+(30*i),10+(30*num), image=school)
          
# Move position of player

def PosirionPacman(array2D):
     for i in range(len(array2D)):
          for n in range(len(array2D[i])):
               if array2D[i][n] ==10:
                    postion=[i,n]
     return postion
def moveRight(event):
     position=PosirionPacman(array2D)
     row=position[0]
     column=position[1]
     if array2D[row][column+1] != 5 and array2D[row][column+1] != 6:
          if array2D[row][column+1] == 2:
               array2D[row][column]= 0
               array2D[row][column+1]=10
               coin()
          elif array2D[row][column+1] == 7:
               my_canvas.delete("all")
               youwin()
               array2D[row][column]=0
               array2D[row][column+1]=10
          elif array2D[row][column+1]!= 1:
               array2D[row][column]= 0
               array2D[row][column+1]=10
          my_canvas.delete("all")
     if array2D[row][column+1] == 5 :
          my_canvas.delete("all")
          array2D[row][column]= 0
          array2D[row][column+1]=10
          youLost()
  
     graphic()

def moveLeft(event):
     position=PosirionPacman(array2D)
     row=position[0]
     column=position[1]
     if array2D[row][column-1] != 5 and array2D[row][column-1] != 6:
          if array2D[row][column-1] == 2:
               array2D[row][column]= 0
               array2D[row][column-1]=10
               coin()
          elif array2D[row][column-1] == 7:
               my_canvas.delete("all")
               youwin()
               array2D[row][column]=0
               array2D[row][column]=10
          elif array2D[row][column-1]!= 1:
               array2D[row][column]=0
               array2D[row][column-1]=10
          my_canvas.delete("all")
     if array2D[row][column-1] == 5 :
          my_canvas.delete("all")
          array2D[row][column]= 0
          array2D[row][column-1]=10
          youLost()
     graphic()
def moveUp(event):
     position=PosirionPacman(array2D)
     row=position[0]
     column=position[1]
     if array2D[row-1][column] != 5 and array2D[row-1][column] != 6:
          if array2D[row-1][column] == 2:
               array2D[row][column]= 0
               array2D[row-1][column]=10
               coin()
          elif array2D[row-1][column] == 7:
               my_canvas.delete("all")
               youwin()
               array2D[row][column]=0
               array2D[row-1][column]=10
          elif array2D[row-1][column]!= 1:
               array2D[row][column]=0
               array2D[row-1][column]=10
          my_canvas.delete("all")
     if array2D[row-1][column] == 5 :
          my_canvas.delete("all")
          array2D[row][column]= 0
          array2D[row-1][column]=10
          youLost()
     graphic()
def moveDown( event):
     position=PosirionPacman(array2D)
     row=position[0]
     column=position[1]
     if array2D[row+1][column] != 5 and array2D[row+1][column] != 6:
          if array2D[row+1][column] == 2:
               array2D[row][column]= 0
               array2D[row+1][column]=10
               coin()
          elif array2D[row+1][column] == 7:
               my_canvas.delete("all")
               youwin()
               array2D[row][column]=0
               array2D[row+1][column]=10
          elif array2D[row+1][column]!= 1:
               array2D[row][column]=0
               array2D[row+1][column]=10
          my_canvas.delete("all")
     if array2D[row+1][column] == 5 :
          my_canvas.delete("all")
          array2D[row][column]= 0
          array2D[row+1][column]=10
          youLost()
     graphic()



# count coin of player 
count = 0 
def coin() :
     global count,Label
     winsound.PlaySound("sound\\whenkak.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
     count += 1
    
# Result of game win or lost 
def youwin() :
     global my_canvas,w,h
     my_canvas.create_text(w/2, 20+(h/2) ,font=("Purisa",25),text= "YOU WON !!!")
     winsound.PlaySound("sound\\coin1.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
     my_canvas = Canvas(root, width=w, height=h) 
     label = Label(root,text=("coin:",count))
     labe =label.config(font=("Monospace",20))
     label.place(x=620, y=400)
def youLost() :
     global my_canvas,w,h
     winsound.PlaySound("sound\\gameover.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
     my_canvas.create_text(w/2, 20+(h/2) ,font=("Purisa",25),text= "YOU LOST!")
     my_canvas = Canvas(root, width=w, height=h) 
# move position of player 
root.bind("<a>",moveLeft)
root.bind("<d>",moveRight)
root.bind("<w>",moveUp)
root.bind("<s>",moveDown)
graphic()
# sound game 
winsound.PlaySound("sound\\sound.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
# mainloop
root.mainloop()