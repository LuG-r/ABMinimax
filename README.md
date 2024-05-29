# Noughts and Crosses Game

![Noughts and Crosses](noughts_and_crosses.jpg)

This project implements a simple game of Noughts and Crosses (also known as Tic-Tac-Toe) in Python. It includes a command-line interface for playing against another human or against a computer opponent that uses the Alpha-beta pruning minimax algorithm.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)

## Introduction
Noughts and Crosses is a classic paper-and-pencil game where two players take turns marking spaces in a 3x3 grid with their respective symbols (either 'O' for Noughts or 'X' for Crosses). The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

This project provides a Python implementation of the game, allowing players to compete against each other or against a computer opponent.

## Features
- Play against another human player.
- Play against a computer opponent that uses the [Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) minimax algorithm.
- Interactive command-line interface.
- Detailed error handling and input validation.

## Installation
To install and run the game, follow these steps:

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/your-username/noughts-and-crosses.git
   ```

2. Navigate to the project directory:
   ```
   cd noughts-and-crosses
   ```

3. Run the game:
   ```
   python noughts_and_crosses.py
   ```

## Usage
Follow the on-screen instructions to play the game. You can choose to play against another human player or against the computer. The computer opponent uses the Alpha-beta pruning minimax algorithm to make intelligent moves.

## Game Rules
1. The game is played on a 3x3 grid.
2. Players take turns marking empty spaces with their respective symbols ('O' or 'X').
3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
4. If all spaces are filled and no player has achieved a winning combination, the game is declared a draw.
