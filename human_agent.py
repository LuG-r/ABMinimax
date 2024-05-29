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
                print("What's your next move? In format row,col e.g. 0,1")
                move_input = input(">")
                row, col = map(int, move_input.split(','))

                if not (0 <= row <= 3 and 0 <= col <= 3):
                    raise ValueError("Row and Column indices must be between 0 and 2.")

                if not state.valid_move(row, col):
                    raise ValueError("The selected space is not empty.")

                return row, col
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
