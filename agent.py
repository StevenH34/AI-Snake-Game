import torch
import random
import numpy as np

from collections import deque
from snake_game import SnakeGameAI, Direction, Point

"""
Agent:
    - Game
    - model

Training:
    - state = get_state(game)
    - action = get_move(state):
        model.predict()
    - reward, game_over, score = game.play_step(action)
    - new_state = get_state(game)
    - remember
    - model.train()
"""

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001


class Agent:

    def __init__(self):
        pass

    def get_state(self, game):
        pass
    

    

