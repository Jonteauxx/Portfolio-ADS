import numpy as np
from PIL.Image import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import random

container_dest = ["1", "2", "3"]
RIGHT_MOVE = 5
BEST_MOVE = 10
WRONG_MOVE = -5

ACTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

class dock:
    def __init__(self):
        self.dock = np.zeros((3,3), dtype=str)
        self.dock[:,;] = 'n' #fill the dock with 'n' for empty spaces
        self.set_container_on_dock(self.dock)
    

 
    def print_area(self):
        print('---------------------------------')
        for i in range(dock.shape[0]):
            for j in range(dock.shape[1]):
                if dock[i,j] == 'n':
                    print('n', end="\t") #empty space
                elif dock[i,j] != 'n':
                    print('X', end="\t") #occupied space
                print("\n")
        print('---------------------------------')

class container:
    def __init__(self):
        self.curr_container = random.choice(list(container_dest))
        self.next_container = random.choice(list(container_dest))
        self.give_reward(self.curr_container_choice)

    
    def __str__(self):
        return f"{self.choice}"
    
    def action(self, choice):
        if choice == 0:
            self.move(x=0, y=-1)
        elif choice == 1:
            self.move(x=0, y=1)
        elif choice == 2:
            self.move(x=-1, y=0)
        elif choice == 3:
            self.move(x=1, y=0)

    def set_container_on_dock(self, state):
        #the first random container should be placed on position ([0,0] or [0,2])
        self.dock[0,0] = self.curr_container
        
        #check if placing container on that position is allowed by calling is_allowed_move()
        if self.curr_container == self.next_container:
            self.is_allowed_move(self.next_container, dock)
        elif self.curr_container != self.next_container:
            self.is_allowed_move(self.next_container, dock) 
        
        #place the next container on dock, but check ifAllowed first
        for i in range(dock.shape[0]):
            for j in range(dock.shape[1]):
                if dock[i,j] != 'n' & dock[i,j] == (type(self.curr_container) == str):
                    #update dock with an 'A,B or C' to represent occupied space                     
                    print(self.curr_container, end="\t") #occupied space
                elif dock[i,j] == 'n':
                    print('n', end="\t")
        
       

    def is_allowed_move(self, next_container, action):
        # check allowed move from a given state
        x, y = divmod(0, len(dock))
        if x - 1 & y - 0 != 'n': #up
            next_container
        y += ACTIONS[action][0]
        x += ACTIONS[action][1]
        if x < 0 or y < 0 or x > 3 or y > 3:
            # if robot will move off the board
            return False

        if self.dock[y, x] == 0 or self.dock[y, x] == 2:
            return True
        else:
            return False

    def construct_allowed_states(self):
        # create a dictionary of allowed states from any position
        # using the isAllowedMove() function
        # this is so that you don't have to call the function every time
        allowed_states = {}
        for y, row in enumerate(self.dock):
            for x, col in enumerate(row):
                # iterate through all spaces
                if self.dock[(y,x)] != 1:
                    # if the space is not occupied, add it to the allowed states dictionary
                    allowed_states[(y,x)] = []
                    for action in ACTIONS:
                        if self.is_allowed_move((y,x), action) & (action != 0):
                            allowed_states[(y,x)].append(action)
        self.allowed_states = allowed_states

    def get_pos_and_give_reward(self):
        return self.position, self.give_reward()
        
    def give_reward(self, value):  

        #de waarde die hij ontvangt geeft aan hoeveel rewards hij krijgt door switch cases te gebruiken
