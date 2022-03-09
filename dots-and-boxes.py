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

