from tkinter import *
from PIL import Image, ImageTk
import random

from subpack1 import money_sys

root = Tk()

#Globals
tree_pressed = False
chosen_tree = 0
tree_last_down = None

class gui:

    def __init__(self):
        frame1 = Canvas(width=1280,height=720,bg="green")
        frame1.pack()
        
        stat_frame = Canvas(root, height=720/7,width=1280, bg="grey")
        stat_frame.place(relx=1.0, rely=1.0, x=0, y=0,anchor="se")
        
        cash_label = Label(root, text="Cash balance: 0", anchor=SE, justify=RIGHT)
        cash_label.pack()
        
class tree:
    
    def __init__(self):
        self.num_trees = 0
        self.trees = {}
        self.tree_btn_display = {}
        
    #Generate some sweet trees
    def gen_tree(self,name):
        self.trees[name] = 5
        self.num_trees += 1
        
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
        
        x_coord = random.randint(0,1280)
        y_coord = random.randint(0,520)
        
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
while(i<60):
    Tree.gen_tree(i)
    i+=1
    

#Game beginning    
LOOP_ACTIVE = TRUE
while LOOP_ACTIVE:
    root.mainloop()
    #generate a tree if one's cut down
    if Tree.num_trees < 60:
        for key in Tree.trees:
            if key != tree_last_down:
                continue
            else:
                Tree.gen_tree(tree_last_down)

    #Get ... when tree is tapped
    if tree_pressed == True:
        print("Tree clicked")
        
        Tree.lose_hp(chosen_tree)
        
        char_balance.add(1)
        
        tree_pressed = False
        
    if Tree.trees[chosen_tree] <= 0:
        print("Tree %s cut down"%(chosen_tree))
        Tree.cut_down(chosen_tree)
        tree_last_down = chosen_tree
        
    
        

    root.wm_attributes("-alpha", True) #Doesn't work yet


