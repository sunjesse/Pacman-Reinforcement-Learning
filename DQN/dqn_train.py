import pacman
import pygame
import random
import numpy as np
import constants
import shelve
import moving_average as ma
import replay_buffer as rb

''' ---- Training ---- '''
replay_buffer_size = 999 #1000 effectively.
epislon = 1
sample_epsilon = 0.8
gamma = 0.99
gameOver = False
training = True
beta = 0.95

constants.target_network.apply_softmax = True
constants.q_network.apply_softmax = True

while(training):
    try:
        if len(constants.scores) >= 10:
            temp = 150/(sum(constants.scores[-10:])/10) #moving average
        else:
            temp = 15
        print("Temp is: " + str(temp))
        constants.target_network.temp = temp
        constants.q_network.temp = temp
        pacman.game(gameOver, constants.target_network, gamma, sample_epsilon, replay_buffer_size) #calculate TD error and put in a parallel deque.
        gameOver = False
        pacman.reset()
    except KeyboardInterrupt:
        shelf = shelve.open("objects", writeback = True)
        print("Saving training data...")

        try:
            shelf["q_network"] = constants.q_network
            shelf["target_network"] = constants.target_network
            shelf["replay_buffer"] = rb.replay_buffer
            shelf["replay_buffer_two"] = rb.replay_buffer_two
            shelf["count"] = rb.count
            shelf["count_two"] = rb.count_two
            shelf["scores"] = constants.scores
            print("Sucessfully saved objects and lists in objects.db.")
            if shelf["first_time"]:
                shelf["first_time"] = False

        finally:
            shelf.close()
        training = False

pygame.quit()
quit()
