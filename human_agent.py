"""
Simple Human Agent for playing noughts and crosses.

Author: Lucas Gracia
Date: 13th May 2024
"""

class HumanAgent:
    """
    Represents a human player agent.

    This class allows a human player to input their move in the format
    "row, col", validates the input and returns the move if it's valid.

    Methods:
        next_move(state): Prompts the user for their next move and returns it.
    """
    def next_move(self, state):
        """
        Prompts the user for their next move and returns it.

        Args:
            state (NoughtsAndCrosses): The current state of the game.

        Returns:
            tuple: The row and column indices of the player's move.
        """
        while True:
            try:
                print("What's your next move? In format row,col")
                move = input(">")
                move = move.split(',')
                move = int(move[0]), int(move[1])
                if not state.valid_move(move[0], move[1]):
                    print("Space must be empty.")
                else:
                    return move
            except ValueError:
                print("Please enter a space as row,col between 0,0 and 2,2")
