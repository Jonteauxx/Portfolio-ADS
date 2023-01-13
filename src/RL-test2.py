import numpy as np
from PIL.Image import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import random

style.use("ggplot")

SIZE = 3

HM_EPISODES = 25000
RIGHT_MOVE = 5
WRONG_MOVE = -5
BEST_MOVE = 10
FINAL_POS_REWARD = 25
epsilon = 0.9
EPS_DECAY = 0.9998  # Every episode will be epsilon*EPS_DECAY
SHOW_EVERY = 3000  # how often to play through env visually.

start_q_table = None # None or Filename

LEARNING_RATE = 0.1
DISCOUNT = 0.95

CONTAINER_N = 1  # CONTAINER key in dict
FINAL_POS_N = 2  # FINAL_POS key in dict

container_type = {1: (0,0,0), 2: (100,100,100), 3: (255,255,255)}
ACTIONS = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}


class area(object):
    def __init__(self):
        self.area = np.zeros((SIZE, SIZE))

    def print_area(self):
        print('---------------------------------')
        for row in self.area:
            for col in row:
                if col == 0:
                    print('', end="\t") # empty space
                elif col == 1:
                    print('X', end="\t") # occupied space
            print("\n")
        print('---------------------------------')

    

class Container:
    # initialize first container in area
    def __init__(self):
        self.x = random.choice(list(container_type.values()))
        self.y = self.x

    def __str__(self):
        return f"{self.x}, {self.y}"

    # Gives us 4 total movement options. (0,1,2,3)
    def action(self, choice):
        if choice == 0:
            self.move(x=0, y=-1)
        elif choice == 1:
            self.move(x=0, y=1)
        elif choice == 2:
            self.move(x=-1, y=0)
        elif choice == 3:
            self.move(x=1, y=0)

    def move(self, x=False, y=False):

        # If no value for x, move randomly
        if not x:
            self.x += np.random.randint(-1, 2)
        else:
            self.x += x

        # If no value for y, move randomly
        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y


        # If we are out of bounds, fix!
        if self.x < 0:
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1
    
    def is_allowed_move(self, state, action):
        # check allowed move from a given state
        x += ACTIONS[action][0]
        y += ACTIONS[action][1]
        if y < 0 or x < 0 or y > 5 or x > 5:
            # if robot will move off the board
            return False

        if self.area[y, x] == 0 or self.area[y, x] == 2:
            # if robot moves into empty space or its original start position
            return True
        else:
            return False

    def get_state(self):
        return self.x, self.y

    # def give_reward(self):
    #     if self.get_state :

if start_q_table is None:
    # initialize the q-table#
    q_table = {}
    for i in range(-SIZE+1, SIZE):
        for ii in range(-SIZE+1, SIZE):
            for iii in range(-SIZE+1, SIZE):
                    for iiii in range(-SIZE+1, SIZE):
                        q_table[((i, ii), (iii, iiii))] = [np.random.uniform(-5, 0) for i in range(4)]

else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)



episode_rewards = []

for episode in range(HM_EPISODES):
    curr_container = Container()
    next_container = Container()

    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True
    else:
        show = False

    episode_reward = 0
    for i in range(200):
        obs = (curr_container-next_container)
        #print(obs)
        if np.random.random() > epsilon:
            # GET THE ACTION
            action = np.argmax(q_table[obs])
        else:
            action = np.random.randint(0, 4)
        # Take the action!
        next_container.action(action)

        if next_container.x == curr_container.x and next_container.y == curr_container.y:
            reward = WRONG_MOVE
        elif curr_container.x != next_container.x and curr_container.y != next_container.y:
            reward = RIGHT_MOVE
        else:
            reward = BEST_MOVE
        ## NOW WE KNOW THE REWARD, LET'S CALC YO
        # first we need to obs immediately after the move.
        new_obs = (curr_container-next_container)
        max_future_q = np.max(q_table[new_obs])
        current_q = q_table[obs][action]

        if reward == FINAL_POS_REWARD:
            new_q = FINAL_POS_REWARD
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[obs][action] = new_q

        if show:
            env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)  # starts an rbg of our size
            env[next_container.x][next_container.y] = container_type[FINAL_POS_N]  # sets the FINAL_POS location tile to green color
            env[curr_container.x][curr_container.y] = container_type[CONTAINER_N]  # sets the CONTAINER tile to blue
            img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
            img = img.resize((300, 300))  # resizing so we can see our agent in all its glory.
            cv2.imshow("image", np.array(img))  # show it!
            if reward == FINAL_POS_REWARD or reward == WRONG_MOVE:  # crummy code to hang at the end if we reach abrupt end for good reasons or not.
                if cv2.waitKey(500) & 0xFF == ord('q'):
                    break
            else:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        episode_reward += reward
        if reward == FINAL_POS_REWARD or reward == WRONG_MOVE:
            break

    #print(episode_reward)
    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
    
plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"Reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()