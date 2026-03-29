# Battleship Game Simulation

## Game Rules

Battleship is a strategic guessing game typically played by two players. In this simplified Python implementation:

### Game Objective
The goal is to sink all of your opponent's ships by guessing their locations on a 10x10 grid.

### Gameplay Mechanics
- Each player has a 10x10 grid representing their game board
- Players take turns attacking coordinates on the opponent's grid
- Ships are represented by '1' on the grid
- Attacks can result in:
  - Hit: When an attack strikes a ship (coordinates with '1')
  - Miss: When an attack strikes an empty grid cell (coordinates with '0')

### Current Implementation Limitations
- This version supports basic ship placement and attacking
- Only single-cell ship placement is currently supported
- No win condition or turn-based gameplay is implemented

## How to Use the Code

### Prerequisites
- Python 3.x
- NumPy library

### Running the Game
1. Ensure you have NumPy installed (`pip install numpy`)
2. Run the script: `python src/battleship.py`

### Example Gameplay
The current `main()` function demonstrates:
- Creating two player grids
- Placing ships on specific coordinates
- Attacking opponent's grid coordinates
- Displaying grid states after attacks

### Future Improvements
- Implement multiple ship types
- Add ship orientation (horizontal/vertical)
- Create turn-based gameplay
- Add win/lose conditions
- Implement AI opponent

### Contributing
Feel free to fork and expand the game's functionality!