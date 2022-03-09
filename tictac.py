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
            
           for i in range(2):
              self.canvas.create_line(0,(i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)
       
       def play_again(self):
            self.initialize_board()
            self.player_X_starts = not self.player_X_starts
            self.player_X_turns = self.player_X_starts
            self.board_status = np.zeros(shape=(3, 3))


 
       def draw_O(self, logical_position):
            logical_position = np.array(logical_position)
            grid_position = self.convert_logical_to_grid_position(logical_position)
            self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    outline=symbol_O_color)


       def draw_X(self, logical_position):


























         







             
           
         
            


          




     
           
         



