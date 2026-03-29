import numpy as np

class Battleship:
    def __init__(self):
        self.grid = np.zeros((10, 10), dtype=int)

    def place_ship(self, x, y):
        if self.grid[x][y] == 0:
            self.grid[x][y] = 1
            return True
        return False

    def attack(self, x, y):
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0
            return True  # Hit
        return False  # Miss

    def display_grid(self):
        print(self.grid)

def main():
    player1 = Battleship()
    player2 = Battleship()

    # Example of placing ships
    player1.place_ship(0, 0)
    player2.place_ship(1, 1)

    # Example of attacking
    if player1.attack(1, 1):
        print("Player 1 hit!")
    else:
        print("Player 1 miss!")

    if player2.attack(0, 0):
        print("Player 2 hit!")
    else:
        print("Player 2 miss!")

    # Display grids
    print("Player 1's grid:")
    player1.display_grid()
    print("Player 2's grid:")
    player2.display_grid()

    # Print "Hello World" 5 times
    for _ in range(5):
        print("Hello World")

if __name__ == "__main__":
    main()