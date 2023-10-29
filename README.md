# IITB_IE619_Project

# Cardisco Game

## About the Project

This project was developed as a course project for IE619 Combinatorial Game Theory at the Indian Institute of Technology Bombay (IIT Bombay) under the guidance of Professor Urban Larrson from the Industrial Engineering and Operational Research (IEOR) department.

## About the Game

### Impartial Games
In combinatorial game theory, "impartial games" are games where the players share the same set of available moves, and the choices made by one player affect the options available to both players. In impartial games, players alternate making moves, and each move changes the state of the game for both players. In impartial games, the players alternate making moves, and each move changes the state of the game for both players. The concept of Nim is a classic example of an impartial game. Other examples include Subtraction Game and Hackenbush. **Cardisco** in our own self created Impartial Game.


### Cardisco Game
Cardisco is an impartial card game implemented using Python and the Pygame library. The game is played with a set of 13 cards numbered from 1 to 13. Players take alternating turns selecting cards based on specific rules, aiming to strategically outmaneuver their opponent.

## Installation

To play Cardisco, you need to have Python and the Pygame library installed on your system. Follow these steps to set up your environment:

1. **Install Python:**
   If you don't have Python installed, you can download it from the official website: [Python Download](https://www.python.org/downloads/).

2. **Install Pygame:**
   Open your terminal or command prompt and run the following command to install Pygame:
   
   ```shell
   pip install pygame

## Rules to Play the Game

### Setup
1. Arrange the 13 cards on a table in ascending order.

### Gameplay
2. Two players take alternating turns selecting cards.
3. Each turn, a player must choose one card based on the card pickup rules.

### Card Pickup Rules
4. The player who begins must select the card numbered 7 as their first move.
5. In subsequent turns, players can only pick cards that meet these conditions:
   - The card is adjacent to the last picked card.
   - The card's number is double the number of the last picked card.
   - The card's number is half the number of the last picked card (except for odd-numbered last picked cards).

### Objective
6. Players aim to strategically select cards to create a position that prevents their opponent from making any legal moves.

### Winning Condition
7. The player wins when their opponent cannot pick up any more cards.
8. In simpler terms, the player who places their opponent in a situation where they can't make a move emerges victorious.

Enjoy playing Cardisco!

## For Any Queries

For any questions or inquiries, please contact [Ishan Grover](22b1528@iitb.ac.in) and [Hardik Gupta](22b1540@iitb.ac.in).

