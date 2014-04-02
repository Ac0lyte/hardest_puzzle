# puzzle_piece.py
# Author: Tim Schaller <timschaller@gmail.com>
# GPLv3, etc..etc..
#
# This defines a basic puzzle piece for a type of puzzle where
# every piece is square and each side has one of a predefined
# edge. In the case of the puzzle I am solving for there are 
# four types "heart, spade, diamond, and club" and each side
# may be either male or female.
#

class puzzle_side:
    "A single side of a puzzle piece. Has gender and shape"

    def __init__(self, value):
        if isinstance(value, puzzle_side):
            self.shape = value.shape
            self.gender = value.gender
        else:
            v = list(value)
            self.shape  = v[0]
            self.gender = v[1]

    def fit(self,other):
        if( (self.shape == '?') or (other.shape == '?') ):
            return True
        return (self.shape == other.shape) and (self.gender != other.gender)

    def __eq__(self,other):
        return (self.shape == other.shape) and (self.gender == other.gender)

    def flip_gender(self):
        if self.gender == '?':
            return

        if self.gender == '+':
            self.gender = '-'
        else:
            self.gender = '+'

    def out(self):
        return self.shape + self.gender

class puzzle_piece:
    "A 4 sided puzzle piece."

    #side = []
    ## rotation = 0

    def __init__(self, north, east, south, west):
        self.rotation = 0
        self.side = []
        self.side.append(puzzle_side(north))
        self.side.append(puzzle_side(east))
        self.side.append(puzzle_side(south))
        self.side.append(puzzle_side(west))

    def __eq__(self, other):
        #print self.north.printable(), " ", self.east.printable(), " ", self.south.printable(), " ", self.west.printable(), "\n"
        #print other.north.printable(), " ", other.east.printable(), " ", other.south.printable(), " ", other.west.printable(), "\n"
        return (( self.north().fit(other.north()) ) and
                ( self.east().fit(other.east()  )) and
                ( self.south().fit(other.south()) ) and
                ( self.west().fit(other.west())  ))

    def __ne__(self,other):
        return not self == other

    
    # compares self against the other with self
    # rotated to all four possible positions. On a
    # match it returns the rotation that matches.
    #
    # Otherwise a False is returned.
    # Please note that this will leave self in the
    # same rotation as it started.

    def rotcmp(self,other):
        # Store rotation state
        old_rotation = self.rotation

        # Assume false unless found otherwise. 
        match = -1

        for rot in range(0,4):
            self.rotation = rot
            if self == other:
                match = rot
                break

        # restore rotation state
        self.rotation = old_rotation
        return match

    # Compares one side of self to all sides of other
    def side_cmp( self, side, other):
        old_rotation = other.rotation
        match = False

        for rot in range(0,4):
            other.rotation = rot
            if self.fit(self.side[side], other.side[rot]):
                match = rot
                break

        other.rotation = old_rotation
        return match

    def flip_gender(self):
        for idx in range(0,4):
            self.side[idx].flip_gender()

    def north(self):
        return self.side[(0 + self.rotation) % 4]
    
    def east(self):
        return self.side[(1 + self.rotation) % 4]
    
    def south(self):
        return self.side[(2 + self.rotation) % 4]
    
    def west(self):
        return self.side[(3 + self.rotation) % 4]
   
    def rotate(self):
        self.rotation = (self.rotation + 1 ) % 4 
        return self.rotation


