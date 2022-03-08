#tic-tac-toe#

from tkinter import *

import numpy as np


size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2



#create-class#

class Tic_Tac_Toe():

       
       def __init__(self):
           
           self.window = Tk()
           self.window.title('Tic-Tac-Toe')
           self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board) 
           self.canvas.pack() 
           
           self.window.bind('<Button-1>', self.click) # A form of input taken from user as click
          
       def mainloop(self):
           self.window.mainloop() 
     
      
       def initialize_board(self):
           for i in range(2):
              self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)
            









             
           
         
            


          




     
           
         



