"""Code taken from https://github.com/devsisters/DQN-tensorflow/blob/master/dqn/history.py"""

import numpy as np

from agent.utils.constants import *
from agent.utils.strings import *

class History:
    '''Experiance buffer of the behaniour policy of the agent'''

    def __init__(self, logger, config):
        self.logger = logger

        batch_size, history_length, self.num_channels = \
            config[BATCH_SIZE], config[HISTORY_LENGTH], config[NUM_CHANNELS]

        self._history = np.zeros(
            [history_length, self.num_channels], dtype=np.float32)

    def add(self, screen):
        if screen.shape != (self.num_channels, ):
            self.logger.error(INVALID_TIMESTEP)
            
        self._history[:-1] = self._history[1:]
        self._history[-1] = screen
    
    def set_history(self, state):
        for screen in state:
            self.add(screen)

    @property
    def history(self):
        return self._history
