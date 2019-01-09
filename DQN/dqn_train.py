import pacman
import random
import numpy as np
import constants

'''
TO DO:
1. TD Error in Sampling
2. Add backprop after every forward pass into pacman.game() in pacman.py
3. Try and except inside this file -> if game is closed via cmd+c or whatever, then save current progress.
4. Create a file that stores data during training: q-values, loss, etc..
5. Seperate file that saves the current networks, current replay buffer, etc.
6. Matplotlib // Maybe run a process displaying the data concurrently during training? Maybe idk.
'''

''' ---- Training ---- '''
replay_buffer_size = 1000
epislon = 1
sample_epsilon = 0.8
gamma = 0.9
gameOver = False
training = True
outer_time_step = 0

while(training):
    pacman.game(gameOver, constants.target_network, gamma, sample_epsilon, replay_buffer_size) #calculate TD error and put in a parallel deque.
    gameOver = False
    pacman.reset()

pygame.quit()
quit()
