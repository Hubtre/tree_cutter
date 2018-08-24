from tkinter import *
from PIL import Image, ImageTk
import random

from subpack1 import money_sys

root = Tk()

#Globals
tree_pressed = False
chosen_tree = 0

class gui:

    def __init__(self):
        frame1 = Canvas(width=1280,height=720,bg="green")
        frame1.pack()
        
        stat_frame = Canvas(root, height=720/7,width=1280/7, bg="grey")
        stat_frame.place(relx=1.0, rely=1.0, x=0, y=0,anchor="se")
        
class tree:
    
    def __init__(self):
        self.num_trees = 30
        self.trees = {}
        self.tree_btn_display = {}
        
    #Generate some sweet trees
    def gen_tree(self,name):
        self.trees[name] = 5
        
        def callback():
            global tree_pressed
            tree_pressed = True
            
            global chosen_tree
            chosen_tree = name 
            
            root.quit()
            
        tree = Image.open("tree_normal1.png").convert("RGBA")
        render_tree = ImageTk.PhotoImage(tree)
        self.tree_btn_display[name] = Button(root, image=render_tree, command= callback)
        self.tree_btn_display[name].image = render_tree
        
        x_coord = random.randint(0,1020)
        y_coord = random.randint(0,620)
        
        self.tree_btn_display[name].place(x=x_coord,y=y_coord)
        
        
    def cut_down(self,which):
        self.num_trees -= 1
        self.tree_btn_display[which].destroy()
        
    def lose_hp(self,which_tree):
        self.trees[which_tree] -= 1

        


#Game setup
char_balance = money_sys.money()

GUI = gui()
Tree = tree()

#Tree generation
i=0
while(i<Tree.num_trees):
    Tree.gen_tree(i)
    i+=1
    

#Game beginning    
LOOP_ACTIVE = TRUE
while LOOP_ACTIVE:
    root.mainloop()
    #generate a tree if one's cut down
    if Tree.num_trees < 30:
        for key in Tree.trees:
            print(key)

    #Get ... when tree is tapped
    if tree_pressed == True:
        print("Tree clicked")
        
        Tree.lose_hp(chosen_tree)
        
        tree_pressed = False
        
    if Tree.trees[chosen_tree] <= 0:
        print("Tree %s cut down"%(chosen_tree))
        Tree.cut_down(chosen_tree)
        

    root.wm_attributes("-alpha", True) #Doesn't work yet


