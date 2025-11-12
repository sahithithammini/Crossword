from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pygame
import sys
from PIL import Image, ImageTk
'''code for displaying the image'''
'''code for displaying the image'''
import pygame

import sys
from PIL import Image, ImageTk
 
# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width, screen_height = 800,600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'C:\\Users\\shivathmikavadla\\Pictures\\cross.jpg'  # Replace with the actual path to your image
img = pygame.image.load(image_path)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Blit the image onto the screen at position (x, y) - (0, 0) in this example
    screen.blit(img, (0, 0))

    # Update the display
    pygame.display.flip()



def Start():
    pygame.quit()
    start.destroy()
start=Tk()
start.title("start the game")
start.geometry("100x100")

button=Button(start,text="start",bg="violet",fg="white",command=Start)
button.pack()
start.mainloop()


# Quit Pygame
#pygame.quit()


def set_background(window, image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Create a label with the image and add it to the window
    background_label = Label(window, image=photo)
    background_label.image = photo  # To prevent the image from being garbage collected
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

'''code for game'''


root=Tk()
root.title("Level 1")
root.geometry("500x500")
background_image_path = "C:\\Users\\shivathmikavadla\\Downloads\\pxfuel.jpg"  # Replace with the path to your image file
set_background(root, background_image_path)




#def color(event):

    #E1.config(fg="green")

def show_info_message2():
    messagebox.showinfo("Time's Up")

'''turtle for displaying the text START'''
def game_logic():
    window = Tk()
    window.title("Time's up")
    window.geometry('100x100')
    #timer=Label(window,text="Time's up",width=50,height=50,bg="red",fg="white")
    #timer.pack()
    #background_image_path = "C:\\Users\\shivathmikavadla\\Pictures\\cross2.jpg"  # Replace with the path to your image file
    #set_background(window, background_image_path)
    
    pygame .mixer.init()
    pygame.mixer.music.load("C:\\Users\\shivathmikavadla\\Downloads\\Blockbusters Time Up.mp3")
    pygame.mixer.music.play()
    show_info_message2()
    root.destroy()

#button1 = Button(window, text = "play song" , font=("Helvetica",32),command = play)
#button1.pack(pady = 50)

    window.mainloop()

#button1 = Button(window, text = "play song" , font=("Helvetica",32),command = play)
#button1.pack(pady = 50)

    window.mainloop()
    #rl.pack()   
def set_timer():
    #set the timer delay in milliseconds 1sec=1000milliseconds
    time_delay=120000 #4x60x1000
    root.after(time_delay,game_logic)
   

def click():
    pygame.init()

# Load the sound file
    sound_file = "C:\\Users\\shivathmikavadla\\Downloads\\Mouse-Click-00-c-FesliyanStudios.com.mp3"
    sound = pygame.mixer.Sound(sound_file)

# Play the sound
    sound.play()

# Keep the program running to hear the sound
    pygame.time.wait(int(sound.get_length() * 1000))  # Wait for the sound to finish
    pygame.quit()


def click1(event):
    click()
    root1=Tk()
    root1.title("hint")
    root1.geometry("200x200")
    l=Label(root1,text="DOWN:mate who's close by day",width=50,height=50,bg="orange",fg="white")
    l.pack()
def click2(event):
    root2=Tk()
    root2.title("hint")
    root2.geometry("200x200")
    l=Label(root2,text="DOWN:cultivation location",width=50,height=50,bg="purple",fg="white")
    l.pack()
def click3(event):
    root3=Tk()
    root3.title("hint")
    root3.geometry("200x200")
    l=Label(root3,text="DOWN:December's season",width=50,height=50,bg="green",fg="white")
    l.pack()
def click4(event):
    root4=Tk()
    root4.title("hint")
    root4.geometry("200x200")
    l=Label(root4,text="DOWN:It's for reading",width=50,height=50,bg="maroon",fg="white")
    l.pack()
def click5(event):
    root5=Tk()
    root5.title("hint")
    root5.geometry("200x200")
    l=Label(root5,text="ACROSS:path for car's",width=50,height=50,bg="lime green",fg="white")
    l.pack()
def click6(event):
    root6=Tk()
    root6.title("hint")
    root6.geometry("200x200")
    l=Label(root6,text="ACROSS:aryabhata's creator",width=50,height=50,bg="pink",fg="white")
    l.pack()
def click7(event):
    root7=Tk()
    root7.title("hint")
    root7.geometry("200x200")
    l=Label(root7,text="ACROSS:Finish",width=50,height=50,bg="blue",fg="white")
    l.pack()
def click8(event):
    root8=Tk()
    root8.title("hint")
    root8.geometry("200x200")
    l=Label(root8,text="ACROSS:A performer who moves rythmatically to music",width=50,height=50,bg="red",fg="white")
    l.pack()





def on_entry_keypress(event):
    # Check if the length of the input is greater than 1
    entry=event.widget
   
    if len(entry.get()) >= 1:
        # Block any additional characters by setting the input to the first character
        entry.delete(0, END)
        entry.insert(0, event.char)
        
        return 'break'  # Prevents further handling of the keypress event
def on_entry_keypress1(event):
    # Check if the length of the input is greater than 1
    entry=event.widget
    
    if len(entry.get()) >= 1:
        # Block any additional characters by setting the input to the first character
        entry.delete(1, END)
        entry.insert(1, event.char)
        
        return 'break'  # Prevents further handling of the keypress event




entry_var1=StringVar()
entry_var2=StringVar()
entry_var3=StringVar()
entry_var4=StringVar()
entry_var5=StringVar()
entry_var6=StringVar()
entry_var7=StringVar()
entry_var8=StringVar()
entry_var9=StringVar()
entry_var10=StringVar()
entry_var11=StringVar()
entry_var12=StringVar()
entry_var13=StringVar()
entry_var14=StringVar()
entry_var15=StringVar()
entry_var16=StringVar()
entry_var17=StringVar()
entry_var18=StringVar()
entry_var19=StringVar()
entry_var20=StringVar()
entry_var21=StringVar()
entry_var22=StringVar()
entry_var23=StringVar()
entry_var24=StringVar()
entry_var25=StringVar()
entry_var26=StringVar()
entry_var27=StringVar()
entry_var28=StringVar()
entry_var29=StringVar()
entry_var30=StringVar()
entry_var31=StringVar()

set_timer()
def button_click():
    root.destroy()

button = Button(root,text="score",bg="pink",fg="black",command=button_click)

# Pack the button widget into the window with anchor set to "se"
button.grid(row=10,column=10)
row,column=0,0    
    
for i in range(6):
         
         for j in range(7):
            #white square-numberings
            if i==0 and j==0:
                E1=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var1)
                E1.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E1.insert(0,"1")
                E1.bind("<1>",click1)
                E1.bind("<KeyPress>", on_entry_keypress1)
                #E1.bind("<FocusIn>",save_entry_value)

            elif i==0 and j==1:
                #black squares label
                L1=Label(root,width=5,bg="black",justify="center")
                L1.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                

               
            elif i==0 and j==2:
                e2=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var2)
                e2.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e2.insert(0,"2")
                e2.bind("<1>",click2)
                e2.bind("<KeyPress>", on_entry_keypress1)
                
            elif i==0 and j==3:
                L2=Label(root,width=5,bg="black",justify="center")
                L2.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)


            elif i==0 and j==4:
                L3=Label(root,width=5,bg="black",justify="center")
                L3.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)

            elif i==0 and j==5:
                e5=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var3)
                e5.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e5.insert(0,"3")
                e5.bind("<1>",click3)
                e5.bind("<KeyPress>", on_entry_keypress1)
            elif i==0 and j==6:
                E2=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var4)
                E2.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E2.insert(0,"4")
                E2.bind("<1>",click4)
                E2.bind("<KeyPress>", on_entry_keypress1)
            elif i==0 and j==7:
                l3=Label(root,width=5,bg="black",justify="center")
                l3.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)

            elif i==1 and j==0:
                e6=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var5)
                e6.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e6.insert(0,"5")
                e6.bind("<1>",click5)
                e6.bind("<KeyPress>", on_entry_keypress1)
            elif i==1 and j==1:
                #white squares
                e7=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var6)
                e7.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                
                e7.bind("<KeyPress>", on_entry_keypress)
            elif i==1 and j==2:
                e8=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var7)
                e8.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e8.bind("<KeyPress>", on_entry_keypress)
            elif i==1 and j==3:
                E3=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var8)
                E3.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E3.bind("<KeyPress>", on_entry_keypress)
            elif i==1 and j==4:
                L4=Label(root,width=5,bg="black",justify="center")
                L4.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==1 and j==5:
                e10=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var9)
                e10.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                #e10.insert(0,"6")
                #e10.bind("<1>",click)
                e10.bind("<KeyPress>", on_entry_keypress)
            elif i==1 and j==6:
                e11=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var10)
                e11.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e11.bind("<KeyPress>", on_entry_keypress)
            
            elif i==2 and j==0:
                E4=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var11)
                E4.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E4.insert(0,"6")
                E4.bind("<1>",click6)
                E4.bind("<KeyPress>", on_entry_keypress1)
            elif i==2 and j==1:
                E5=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var12)
                E5.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E5.bind("<KeyPress>", on_entry_keypress)
            elif i==2 and j==2:
                e13=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var13)
                e13.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e13.bind("<KeyPress>", on_entry_keypress)
            elif i==2 and j==3:
                e14=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var14)
                e14.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e13.bind("<KeyPress>", on_entry_keypress)
            elif i==2 and j==4:
                L5=Label(root,width=5,bg="black",justify="center")
                L5.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==2 and j==5:
                E6=Entry(root,width=5,bg="white",justify="center",validate="key",textvariable=entry_var15)
                E6.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E6.bind("<KeyPress>", on_entry_keypress)
            elif i==2 and j==6:
                e16=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var16)
                e16.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e16.bind("<KeyPress>", on_entry_keypress)
            
            elif i==3 and j==0:
                E7=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var17)
                E7.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E7.insert(0,"7")
                E7.bind("<1>",click7)
                E7.bind("<KeyPress>", on_entry_keypress1)
            elif i==3 and j==1:
                e18=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var18)
                e18.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e18.bind("<KeyPress>", on_entry_keypress)
            elif i==3 and j==2:
                e19=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var19)
                e19.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e19.bind("<KeyPress>", on_entry_keypress)
            elif i==3 and j==3:
                l9=Label(root,width=5,bg="black",justify="center")
                l9.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==3 and j==4:
                l10=Label(root,width=5,bg="black",justify="center")
                l10.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==3 and j==5:
                e20=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var20)
                e20.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e20.bind("<KeyPress>", on_entry_keypress)
                #e20.insert(0,"8")
                #e20.bind("<1>",click)
            elif i==3 and j==6:
                e21=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var21)
                e21.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e21.bind("<KeyPress>", on_entry_keypress)
            
            elif i==4 and j==0:
                e23=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var22)
                e23.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e23.bind("<KeyPress>", on_entry_keypress)
            elif i==4 and j==1:
                L6=Label(root,width=5,bg="black",justify="center")
                L6.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==4 and j==2:
                e25=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var23)
                e25.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e25.bind("<KeyPress>", on_entry_keypress)
            elif i==4 and j==3:
                l11=Label(root,width=5,bg="black",justify="center")
                l11.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==4 and j==4:
                l12=Label(root,width=5,bg="black",justify="center")
                l12.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
            elif i==4 and j==5:
                E8=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var24)
                E8.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                E8.bind("<KeyPress>", on_entry_keypress)
            elif i==4 and j==6:
                L7=Label(root,width=5,bg="black",justify="center")
                L7.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
           
            elif i==5 and j==0:
                e29=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var25)
                e29.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e29.insert(0,"8")
                e29.bind("<1>",click8)
                e29.bind("<KeyPress>", on_entry_keypress1)
            elif i==5 and j==1:
                e30=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var26)
                e30.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e30.bind("<KeyPress>", on_entry_keypress)
            elif i==5 and j==2:
                e31=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var27)
                e31.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e31.bind("<KeyPress>", on_entry_keypress)
            elif i==5 and j==3:
                e32=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var28)
                e32.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e32.bind("<KeyPress>", on_entry_keypress)
                
            elif i==5 and j==4:
                e33=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var29)
                e33.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e33.bind("<KeyPress>", on_entry_keypress)
            elif i==5 and j==5:
                e34=Entry(root,width=6,bg="white",justify="center",validate="key",textvariable=entry_var30)
                e34.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
                e34.bind("<KeyPress>", on_entry_keypress)
            elif i==5 and j==6:
                L8=Label(root,width=5,bg="black",justify="center")
                L8.grid(row=row+i+1,column=column+j,sticky="nsew",padx=10,pady=10,ipady=10)
           


root.mainloop()

value1=entry_var1.get()
value2=entry_var2.get()
value3=entry_var3.get()
value4=entry_var4.get()
value5=entry_var5.get()
value6=entry_var6.get()
value7=entry_var7.get()
value8=entry_var8.get()
value9=entry_var9.get()
value10=entry_var10.get()
value11=entry_var11.get()
value12=entry_var12.get()
value13=entry_var13.get()
value14=entry_var14.get()
value15=entry_var15.get()
value16=entry_var16.get()
value17=entry_var17.get()
value18=entry_var18.get()
value19=entry_var19.get()
value20=entry_var20.get()
value21=entry_var21.get()
value22=entry_var22.get()
value23=entry_var23.get()
value24=entry_var24.get()
value25=entry_var25.get()
value26=entry_var26.get()
value27=entry_var27.get()
value28=entry_var28.get()
value29=entry_var29.get()
value30=entry_var30.get()
value31=entry_var31.get()
#print("value entered at row=0 and column=1 is:",value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15,value16,value17,value18,value19,value20,value21,value22,value23,value24,value25,value26,value27,value28,value29,value30,value31)


v1=value1.lower()
v2=value2.lower()
v3=value3.lower()
v4=value4.lower()
v5=value5.lower()
v6=value6.lower()
v7=value7.lower()
v8=value8.lower()
v9=value9.lower()
v10=value10.lower()
v11=value11.lower()
v12=value12.lower()
v13=value13.lower()
v14=value14.lower()
v15=value15.lower()
v16=value16.lower()
v17=value17.lower()
v18=value18.lower()
v19=value19.lower()
v20=value20.lower()
v21=value21.lower()
v22=value22.lower()
v23=value23.lower()
v24=value24.lower()
v25=value25.lower()
v26=value26.lower()
v27=value27.lower()
v28=value28.lower()
v29=value29.lower()
v30=value30.lower()
v31=value31.lower()


#print("value entered at row=0 and column=1 is:",v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31)


def show_info_message():
    messagebox.showinfo( "congractulations", "you won the game")
    

    
#creating the list which contains the strings like row wise
#score=0
list1=['friend','garden','winter','book','road','isro','end','dancer']
#print(v1,v5,v11,v17,v22,v25)
  
s1=v1[1]+v5[1]+v11[1]+v17[1]+v22+v25[1]
s2=v2[1]+v7+v13+v19+v23+v27
s3=v3[1]+v9+v15+v20+v24+v30
s4=v4[1]+v10+v16+v21
s5=v5[1]+v6+v7+v8
s6=v11[1]+v12+v13+v14
s7=v17[1]+v18+v19
s8=v25[1]+v26+v27+v28+v29+v30+v31
score=0

if s1==list1[0]:
    score+=1
if s2==list1[1]:
    score+=1
if s3==list1[2]:
    score+=1
if s4==list1[3]:
    score+=1
if s5==list1[4]:
    score+=1
if s6==list1[5]:
    score+=1
if s7==list1[6]:
    score+=1
if s8==list1[7]:
        score+=1
print("your score is:",score)

def show_info_message1():
    messagebox.showinfo("your score:",score)



if score==8:

    Score=tk.Tk()
    Score.geometry("1000x500")
    Score.title("score")
    labell1=Label(Score,text="congractulations",width=100,fg="purple",font=("Helvetica", 50))
    labell1.pack()
    show_info_message()
    Score.mainloop()
else:
    Score=tk.Tk()
    Score.geometry("500x500")
    Score.title("score")
    labell=Label(Score,text="Game over",width=100,fg="orange",font=("Helvetica", 50))
    labell.pack()
    show_info_message1()
    Score.mainloop()
#view the score button create the window destoy calculation wi