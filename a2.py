# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol,  row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def __str__(self):
        res = "{0} at {1} ate {2} sprouts.".format( self.symbol, (self.row,self.col) , self.num_sprouts_eaten ) 
        return res

    def set_location(self, row, col):
        self.row = row
        self.col = col

    def get_location(self):
        return (self.row, self.col)

    def eat_sprout(self):
        self.num_sprouts_eaten += 1
    
class Maze:
    """ A 2D maze. """

    def __init__(self, maze_str, rat_1, rat_2 ):
        self.maze = maze_str
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        sprouts = 0
        for line in maze_str:
            for elem in line:
                if elem == SPROUT:
                    sprouts += 1
        self.num_sprouts_left = sprouts

    def __str__(self):
        res = ""
        rows = len(self.maze)
        cols = len(self.maze[0])
        for i in range(rows):
            for j in range(cols):
                char = self.get_character( i, j )
                res += char
            res += "\n"
        res += str(self.rat_1)
        res += "\n"
        res += str(self.rat_2)
        return res
                
    def is_wall(self, row, col):
        elem = self.maze[row][col]
        return ( elem == WALL )

    def get_character(self, row, col ):
        elem = self.maze[row][col]
        if self.rat_1.get_location() == ( row, col ):
            elem = self.rat_1.symbol
        if self.rat_2.get_location() == ( row, col ):
            elem = self.rat_2.symbol
        return elem

    def set_character(self, row, col, new_char ):
        self.maze[row][col] = new_char

    def move(self, Rat, vert_change, hor_change ):
        new_location = ( Rat.row + vert_change, Rat.col + hor_change )
        elem = self.get_character( new_location[0], new_location[1] )
        if elem == WALL:
            return False
        else:
            Rat.set_location(new_location[0], new_location[1] )
            if elem == SPROUT:
                Rat.eat_sprout()
                self.set_character( new_location[0], new_location[1], HALL)
                self.num_sprouts_left -= 1
            return True
            
    
if __name__ == "__main__":

    Jen = Rat(RAT_1_CHAR,1,4)
    print(Jen)
    
    Jen.set_location(2,5)
    Jen.eat_sprout()
    print(Jen)

    Paul = Rat(RAT_2_CHAR, 3, 5 )

    Doom = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Jen,
      Paul)

    print(Doom)
    

    
