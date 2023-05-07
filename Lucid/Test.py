import collections
import functools
from functools import cmp_to_key


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + " Age: " + str(self.age)

"""
Part 1:
   Sort a list of people by age ascending.  For person's with
   the same age, sort ascending alphabetically by name

   For example:
	 Person("Bob", 28)
	 Person("Jill", 31)
	 Person("Andy", 32)
	 Person("Sam", 32)
"""

def comparator(p1, p2):
    #TODO: Fill in this function
    if p1.age < p2.age:
        return -1
    elif p1.age > p2.age:
        return 1
    else:
        if p1.name < p2.name:
            return -1
        elif p1.name > p2.name:
            return 1
    return 0

def sortedData(data):
    return sorted(data, key=cmp_to_key(comparator))

if __name__ == '__main__':
    print('Part 1:')
    people = [
        Person("Matt", 50),
        Person("Lulu", 5),
        Person("Laura", 49),
        Person("Abby", 50),
        Person("Chris", 1),
        Person("Jen", 35),
        Person("Flavia", 12),
        Person("Alicia", 21),
        Person("Greg", 78),
        Person("Boris", 9),
    ]
    for p in sortedData(people):
        print(p)
    print()

"""
Part 2:
    Given a string with a comma separated list of sock colors, determine how
	many pairs of each color sock can be made, output the number of pairs you
	can make that match
    for example:
        `red,blue,red,green,green,red`
    would yield the following in the output:
		Sock Pairs: 2
"""

def numSockPairs(socksStr):
    #TODO your implementation goes here. This should return the total number of pairs.
    hashMap = dict()
    socks = socksStr.split(',')
    for sock in socks:
        if sock not in hashMap:
            hashMap[sock] = 1
        else:
            hashMap[sock] += 1
    numPairs = 0
    for key in hashMap:
        numPairs += (hashMap[key] // 2)
    return numPairs

if __name__ == '__main__':
    print('Part 2:')
    pairs = numSockPairs("red,blue,purple,red,green,green,purple,red,yellow,red,red,yellow,red,purple")
    print('Sock Pairs: ' + str(pairs))
    print()

"""
Part 3: Implement the board game Othello/Reversi on the following board.
            
    Othello is a game played on an 8x8 board between two players. There are sixty-four identical game pieces 
	called disks, which are light on one side and dark on the other. Players take turns placing disks on the 
	board with their assigned color facing up. During a play, any disks of the opponent's color that are in a 
	straight line and bounded by the disk just placed and another disk of the current player's color are turned 
	over to the current player's color. The object of the game is to have the majority of disks turned to display
	your color when the last playable empty square is filled.

	The game begins with four disks placed in a square in the middle of the grid, two facing white-side-up, two
	dark-side-up, so that the same-colored disks are on a diagonal

	  a b c d e f g h
	1 
	2 
	3       
	4       W B
	5       B W
	6 
	7 
	8
				
	Dark must place a piece (dark-side-up) on the board and so that there exists at least one straight 
	(horizontal, vertical, or diagonal) occupied line between the new piece and another dark piece, with one or
	more contiguous light pieces between them. For move one, dark has four options shown by Xs below:

	  a b c d e f g h
	1
	2 
	3       X
	4     X W B
	5       B W X
	6         X	 
	7 
	8
		
	Play always alternates. After placing a dark disk, dark turns over (flips to dark, captures) the single disk
	(or chain of light disks) on the line between the new piece and an anchoring dark piece. A valid move is one
	where at least one piece is reversed (flipped over).

	If dark decided to put a piece in the topmost location, one piece gets turned over, so that the board appears thus:

	  a b c d e f g h
	1 
	2
	3       B
	4       B B
	5       B W          
	6 
	7 
	8

	Now light plays. This player operates under the same rules, with the roles reversed: light lays down a light
	piece, causing a dark piece to flip. Possibilities at this time appear thus (indicated by Ys):
		
	  a b c d e f g h
	1 
	2
	3     Y B Y
	4       B B
	5     Y B W         
	6 
	7 
	8 

	Light takes the bottom left option and reverses one piece:

	  a b c d e f g h
	1 
	2
	3       B 
	4       B B
	5     W W W          
	6 
	7 
	8 
				
	Pieces may be captured in more than one direction. For example, if light places a piece at e3, the dark 
	pieces at d4 and e4 are both captured: 

	  a b c d e f g h               a b c d e f g h
	1                             1
	2                             2          
	3       B               ==>   3       B W
	4       B B                   4       W W
	5     W W W                   5     W W W
	6                             6
	7                             7
	8                             8
							
	Players take alternate turns. If one player can not make a valid move, play passes back to the other player.
	When neither player can move, the game ends. This occurs when the grid has filled up or when neither player
	can legally place a piece in any of the remaining squares. This means the game may end before the grid is 
	completely filled.             

	Game rules: 
		https://en.wikipedia.org/wiki/Reversi#Rules
	Online game with valid move highlighting: 
		https://www.topster.net/reversi/zweispieler.html

	Extra credit: Have one human play against a computer that always makes a legal move.
	Extra extra credit: Have the computer make at least somewhat strategic moves rather than just some legal
	move.
"""

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

class Othello:
    WHITE = 'W'
    BLACK = 'B'

    def __init__(self):
        self.spaces = [[None] * 8 for x in range(8)]
        self.spaces[3][3] = Othello.BLACK
        self.spaces[3][4] = Othello.WHITE
        self.spaces[4][3] = Othello.WHITE
        self.spaces[4][4] = Othello.BLACK

    def render(self):
        print(' ', *(chr(ord('a') + x) for x in range(8)))
        for y in range(8):
            print(y + 1, *(self.spaces[x][y] or ' ' for x in range(8)))

    def getMoveInput(self):
        while True:
            try:
                row, col = input()
                x = max(0, min(7, ord(row) - ord('a')))
                y = max(0, min(7, ord(col) - ord('1')))
            except ValueError as e:
                print(e)
            else:
                return Coordinate(x, y)

	# TODO: Implement this function.
	# A fully-working solution must do the following:
	#   1. Alternate turns between WHITE and BLACK.
	#   2. Reverse pieces correctly
	#   3. Only allow valid moves (on empty square and reverses 1+ enemy pieces)
	#   4. Check for no valid moves for game end and declare the winner
    def tryFlip(self, coordinate, turn):
        return self.tryFlipHorizontal(coordinate, turn) or self.tryFlipVertical(coordinate, turn)
    #horizontally check
    def tryFlipHorizontal(self, coordinate, turn):
        selfColor = turn
        #check right
        # WWB
        rightCount = 0
        
        for i in range(coordinate.x + 1, 8):
            if self.spaces[coordinate.x][i] is None:
                rightCount = 0
                break
            elif self.spaces[i][coordinate.y] == selfColor:
                destination = Coordinate(i, coordinate.y)
                break
            else:
                rightCount += 1
        #flip right
        if rightCount > 0:
            for i in range(coordinate.x + 1, destination.x):
                self.spaces[i][coordinate.y] = selfColor

        #check left
        destination = Coordinate(-1, -1)
        leftCount = 0
        for i in range(coordinate.x - 1, -1, -1):
            if self.spaces[i][coordinate.y] is None:
                leftCount = 0
                break
            elif self.spaces[i][coordinate.y] == selfColor:
                destination = Coordinate(i, coordinate.y)
                break
            else:
                leftCount += 1
        #flip left
        if leftCount > 0 and destination.x != -1:
            for i in range(coordinate.x - 1, destination.x):
                self.spaces[i][coordinate.y] = selfColor
        return rightCount > 0 or leftCount > 0
    #horizontally check
    def tryFlipVertical(self, coordinate, turn):
        selfColor = turn
        #check right
        rightCount = 0
        for i in range(coordinate.y + 1, 8):
            if self.spaces[coordinate.x][i] is None:
                rightCount = 0
                break
            elif self.spaces[coordinate.x][i] == selfColor:
                destination = Coordinate(coordinate.x, i)
                break
            else:
                rightCount += 1
        #flip right
        if rightCount > 0:
            for i in range(coordinate.y + 1, destination.y):
                self.spaces[coordinate.x][i] = selfColor

        #check left
        leftCount = 0
        for i in range(coordinate.y - 1, -1, -1):
            if self.spaces[coordinate.x][i] is None:
                leftCount = 0
                break
            elif self.spaces[coordinate.x][i] == selfColor:
                destination = Coordinate(coordinate.x, i)
                break
            else:
                leftCount += 1
        #flip left
        if leftCount > 0:
            for i in range(coordinate.y - 1, destination.y):
                self.spaces[coordinate.x][i] = selfColor
        return rightCount > 0 or leftCount > 0
    def play(self):
        turn = Othello.WHITE
        while True:
            self.render()

            #read move input until valid
            while True:
                coordinate = self.getMoveInput()
                #check validity of move
                if self.tryFlip(coordinate, turn):
                    self.spaces[coordinate.x][coordinate.y] = turn
                    break
                

            #switch turn
            if turn == Othello.WHITE:
                turn = Othello.BLACK
            else:
                turn = Othello.WHITE

if __name__ == '__main__':
    print('Part 3:')
    othello = Othello()
    othello.play()
    print()
