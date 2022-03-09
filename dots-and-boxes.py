from tkinter import *
import numpy as np

size_of_board=600
number_of_dots=6
symbol_size=(size_of_board/3-size_of_board/8)/2
symbol_thickness=50
dot_colour='#5eab20'
player1_colour='#158abd'
player1_colour_light='#7fbad4'
player2_colour='#ed271a'
player2_colour_light='#c96b65'
Green_colour='#5eab20'
dot_width=0.25*size_of_board/number_of_dots
edge_width=0.1*size_of_board/number_of_dots
distance_between_dots=size_of_board/(number_of_dots)

class Dots_and_Boxes():
    def __init__(self):
        self.window = Tk()
        self.window.title('Dots_and_Boxes')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.player1_starts = True
        self.refresh_board()
        self.play_again()

    def play_again(self):
        self.refresh_board()
        self.board_status = np.zeros(shape=(number_of_dots - 1, number_of_dots - 1))
        self.row_status = np.zeros(shape=(number_of_dots, number_of_dots - 1))
        self.col_status = np.zeros(shape=(number_of_dots - 1, number_of_dots))

        self.player1_starts = not self.player1_starts
        self.player1_turn = not self.player1_starts
        self.reset_board = False
        self.turntext_handle = []
        self.already_marked_boxes = []
        self.display_turn_text()

    def mainloop(self):
        self.window.mainloop()
    
    def is_grid_occupied(self, logical_position, type):
        r = logical_position[0]
        c = logical_position[1]
        occupied = True

        if type == 'row' and self.row_status[c][r] == 0:
            occupied = False
        if type == 'col' and self.col_status[c][r] == 0:
            occupied = False

        return occupied

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        position = (grid_position-distance_between_dots/4)//(distance_between_dots/2)

        type = False
        logical_position = []
        if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
            r = int((position[0]-1)//2)
            c = int(position[1]//2)
            logical_position = [r, c]
            type = 'row'
            # self.row_status[c][r]=1
        elif position[0] % 2 == 0 and (position[1] - 1) % 2 == 0:
            c = int((position[1] - 1) // 2)
            r = int(position[0] // 2)
            logical_position = [r, c]
            type = 'col'

        return logical_position, type

