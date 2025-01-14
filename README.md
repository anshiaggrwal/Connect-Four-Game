🤔 About the Game
The objective is simple: align four discs of your color (🕢 or 🔴) either horizontally, vertically, or diagonally on a 6x7 board before your opponent does. Players alternate turns, with the user making the first move, followed by the computer.
This project demonstrates:
Interactive gameplay mechanics.
A dynamic console-based user interface.
A focus on Python fundamentals such as loops, conditionals, and recursion.

✨ Features
User vs. Computer Gameplay: Challenge the computer in this turn-based game.
Dynamic Board Display: The game board updates in real-time after each move.
Win/Tie Detection: Automatically detects wins or ties and announces results.
Input Validation: Ensures valid moves and handles errors gracefully.
Opponent: The computer's moves are randomly generated but always valid.

🎮 How to Play
The game begins with the user selecting a column (A-G) and a row (0-5) to drop their disc. Input format: column_row (e.g., A0).
The computer then takes its turn, placing a disc at a valid random position.
Continue alternating turns until:
A player wins by aligning four discs in a row.
The game ends in a tie if no more valid moves are possible.
Invalid inputs or moves prompt the user to re-enter their selection.

🔧 Game Logic Overview
Board Representation: The game board is a 6x7 grid represented as a 2D list.
Win Conditions: The program checks for horizontal, vertical, and diagonal alignments.
Space Validation: Ensures moves are only placed in valid and available positions.
Computer input: The computer's moves are randomly generated while adhering to the game's rules.
