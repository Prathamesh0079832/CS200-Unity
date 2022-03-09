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
