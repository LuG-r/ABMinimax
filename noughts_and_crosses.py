"""
Noughts and Crosses Game Module.

This module contains an implementation of the NoughtsAndCrosses class,
which represents a game of Noughts and Crosses (also called Tic-Tac-Toe).
It provides functionality for playing the game, including methods for checking
the board or a winner or a draw, making moves and determining available
actions.

Author: Lucas Gracia
Date: 13th May 2024
"""
import copy
import numpy as np
from human_agent import HumanAgent
from ab_minimax_agent import ABMinimaxAgent

class NoughtsAndCrosses:
    """
    Represents a game of Noughts and Crosses.

    This class provides the functionality for playing Noughts and Crosses,
    including methods for checking the board for a winner or a draw, making
    moves and determining available actions.

    Attributes:
        empty (str): The symbol representing an empty cell on the board.
        nought (str): The symbol representing player O (Nought).
        cross (str): The symbol representing player X (Cross).
        draw (str): The symbol representing a draw outcome.
        next_player (str): The symbol of the player who will move next.
        flip_player (dict): A dictionary mapping opposing player symbols.
        board (numpy.ndarray): A 3x3 numpy array representing the game board.

    Methods:
        winner(): Checks the board for a winner or a draw.
        actions(): Returns a list of actions (empty cells) on the board.
        valid_move(row, col): Checks if the given move is valid.
        move(row, col): Returns a copy of the board state with a move applied.
    """
    def __init__(self):
        self.empty = ' '
        self.nought = 'O'
        self.cross = 'X'
        self.draw = 'draw'

        self.next_player = self.cross
        self.flip_player = {
          self.cross: self.nought,
          self.nought: self.cross
        }

        self.board = np.array([[self.empty for _ in range(3)] for _ in range(3)])

    def valid_move(self, row, col):
        """
        Checks if the move at the given position is valid.

        Returns:
            bool: True if the cell at (row, col) is empty, False otherwise.
        """
        return self.board[row, col] == self.empty

    def move(self, row, col):
        """
        Returns a copy of the board state with the move applied.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            NoughtsAndCrosses: A new instance of the game with a move applied.

        Raises:
            ValueError: If the specified position is not empty.
        """
        if not self.valid_move(row, col):
            raise ValueError("Position not empty")
        state = copy.deepcopy(self)
        state.board[row, col] = state.next_player
        state.next_player = state.flip_player[state.next_player]
        return state

    def winner(self):
        """
        Checks the Noughts and Crosses board for a winner or a draw.

        Returns:
            int or str or bool: The winning symbol, "draw" or False if the game is ongoing.
        """
        lines = [
            self.board[0, :],   # First row
            self.board[1, :],   # Second row
            self.board[2, :],   # Third row
            self.board[:, 0],   # First column
            self.board[:, 1],   # Second column
            self.board[:, 2],   # Third column
            self.board.diagonal(),  # Main diagonal
            np.fliplr(self.board).diagonal()  # Anti diagonal
        ]

        for line in lines:
            if np.all(line == line[0]) and line[0] != self.empty:
                return line[0]

        if np.all(self.board != self.empty):
            return self.draw

        return False


    def actions(self):
        """
        Returns a list of available actions (empty spaces) on the board.

        Returns:
            List[Tuple[Int, Int]]: List of (row, col) tuples for empty cells.
        """
        row, col = np.nonzero(self.board == self.empty)
        return list(zip(row, col))


if __name__ == '__main__':
    player1 = HumanAgent()
    player2 = ABMinimaxAgent()
    game = NoughtsAndCrosses()
    print(game.board)
    while not game.winner():
        move = player1.next_move(game)
        game = game.move(move[0], move[1])
        print(game.board)
        if game.winner() == game.cross:
            print("Player one wins!")
            break
        if game.winner() == game.draw:
            print("It's a draw.")
            break

        move = player2.next_move(game)
        game = game.move(move[0], move[1])
        print(game.board)
        if game.winner() == game.nought:
            print("Player 2 wins!")
            break
        if game.winner() == game.draw:
            print("It's a draw.")
            break
