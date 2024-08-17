# Sudoku Game with Solver Integration

## How to Use
1. **Install requeriments.txt**: Open your terminal and run `pip install -r requeriments.txt`
2. **Start the Game**: Run the script `main.py` to launch the Sudoku game window.
3. **Solve the Puzzle**: Click the "SOLVE" button to let the solver fill in the correct numbers.
4. **Reset the Board**: Click the "RESET" button to start a new game with a fresh puzzle.

## Overview

This project is a Sudoku game implemented with Python's Pygame library for the graphical user interface (GUI) and custom algorithms for Sudoku puzzle generation and solving. The application allows users to interact with the game board. The main focus of this project is to demonstrate the functionality of the Sudoku solver and provide a visual representation of this operation.

## Components

### 1. Sudoku Solver

The `solver` module contains functions to solve the Sudoku puzzle using a backtracking algorithm. It includes:

- **`SudokuSolver()`**: This function attempts to solve the Sudoku puzzle. It finds the next empty cell and tries placing numbers from 1 to 9. If placing a number leads to a solution, it recursively continues; otherwise, it backtracks by resetting the cell to 0.

- **`findEmptyCell()`**: This function searches for the next empty cell (a cell with a value of 0) in the grid. If no empty cells are found, it returns `None`, indicating that the puzzle is solved.

- **`isValid()`**: This function checks whether placing a specific number in a given cell is valid. It ensures that the number does not already exist in the same row, column, or 3x3 sub-grid.

### 2. Sudoku Board Generation

The `generate` module is responsible for creating a Sudoku board. It generates a complete, valid Sudoku board and then randomly removes some numbers while ensuring that the puzzle remains solvable with a unique solution. The key steps are:

- **Generating a Full Board**: Start with a complete Sudoku board, filled with valid numbers.
- **Removing Numbers**: Randomly remove numbers from the board while checking that the board retains a unique solution.

### 3. Graphical User Interface (GUI)

The GUI is implemented using Pygame. It provides an interactive environment for users to play Sudoku and includes the following features:

- **Drawing the Board**: The `draw_board` function draws the grid and lines of the Sudoku board on the screen.

- **Drawing Numbers**: The `draw_numbers` function displays the numbers on the board. Editable numbers are shown in green, while static numbers are shown in blue.

- **Drawing Buttons**: The `draw_buttons` function displays buttons for resetting the board and solving the puzzle. The "CHECK" button and its associated functionality were removed, leaving the remaining buttons for resetting and solving.

- **Resetting the Board**: The `reset_board` function generates a new puzzle and resets the editable state.

- **Solving the Puzzle**: The `solve_board` function uses the solver to fill in the correct numbers for the puzzle.

### 4. Main Loop

The `main` function controls the game loop, handling user interactions and updating the display. It processes events such as mouse clicks and keyboard inputs, updates the board, and refreshes the screen.

## Purpose

The primary purpose of this project is to provide a visual representation of the Sudoku solver's functionality. By interacting with the GUI, users can observe how the solver fills in the correct numbers for a given puzzle and validate the solver's effectiveness.

## Conclusion

This project demonstrates a functional Sudoku game with interactive GUI components and an integrated solver. The focus is on showcasing the solver's capabilities and providing a visual representation of its operation, making it a comprehensive Sudoku application.