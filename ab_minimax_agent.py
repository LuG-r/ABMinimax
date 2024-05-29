"""
ABMinimaxAgent for Noughts and Crosses.

This module defines an ABMinimaxAgent class that implements the Alpha-beta
pruning minimax algorithm to determine the best move in a game of Noughts and
Crosses. The agent evaluates the board state recursively and chooses the
optimal move to maximise it's chance of winning.

Author: Lucas Gracia
Date: 13th May 2024
"""
import math

class ABMinimaxAgent:
    """
    An agent that uses the Alpha-beta pruning minimax algorithm to play
    Noughts and Crosses.

    Attributes:
        verbose (bool): Whether to print the value of each action evaluated.
    """
    def __init__(self, verbose=False):
        """
        Initialises the ABMinimaxAgent.

        Args:
            verbose (bool): Whether the value of each evaluated action should
                            be printed.
        """
        self.verbose = verbose

    def next_move(self, state):
        """
        Determines the best next move for the current player using the 
        minimax algorithm with Alpha-beta pruning.

        Args:
            state (NoughtsAndCrosses): The current game state.

        Returns:
            tuple: The row and column indices of the best move.
        """
        player = state.next_player

        best_action = None
        best_value = -math.inf
        for action in state.actions():
            new_state = state.move(action[0], action[1])
            action_value = self.get_value(new_state, player, get_min=True)
            if self.verbose:
                print(action_value, end=" ")
            if action_value > best_value:
                best_action = action
                best_value = action_value
        if self.verbose:
            print()
        return best_action

    def get_value(self, state, player, get_min, alpha=-math.inf, beta=math.inf):
        """
        Recursively evaluate the game state to determine the best move using
        the minimax algorithm with Alpha-beta pruning.

        Args:
            state (NoughtsAndCrosses): The current game state.
            player (str): The player for whom the value is being calculated.
            get_min (bool): If true, calculate the minimum value, otherwise
                            calculate the maximum value.
            alpha (float): The alpha value for Alpha-beta pruning. Default is 
                           -infinity.
            beta (float): The beta value for Alpha-beta pruning. Default is 
                          +infinity.

        Returns:
            int: The value of the game state.
        """
        other_player = state.flip_player[player]

        winner = state.winner()
        if winner == player:
            return 1
        if winner == other_player:
            return -1
        if winner == state.draw:
            return 0

        best_value = math.inf
        if not get_min:
            best_value *= -1

        for action in state.actions():
            new_state = state.move(action[0], action[1])
            action_value = self.get_value(new_state, player,
                                          get_min= not get_min,
                                          alpha=alpha, beta=beta)

            if not get_min:
                alpha = max(alpha, action_value)
                if action_value >= beta:
                    return action_value
            else:
                beta = min(beta, action_value)
                if action_value <= alpha:
                    return action_value

            if not get_min and action_value > best_value \
                   or get_min and action_value < best_value:
                best_value = action_value

        return best_value
