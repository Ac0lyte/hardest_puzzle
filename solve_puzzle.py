from puzzlepiece import PuzzlePiece


north = 0
east  = 1
south = 2
west  = 3

# Define what the pieces look like.
pieces = ( PuzzlePiece('S+', 'D+', 'H-', 'D-' ),
           PuzzlePiece('H+', 'D+', 'C-', 'C-' ),
           PuzzlePiece('H+', 'S+', 'S-', 'C-' ),
           PuzzlePiece('H+', 'D+', 'D-', 'H-' ),
           PuzzlePiece('D+', 'C+', 'C-', 'D-' ),
           PuzzlePiece('S+', 'S+', 'H-', 'C-' ),
           PuzzlePiece('C+', 'H+', 'S-', 'H-' ),
           PuzzlePiece('C+', 'H+', 'D-', 'C-' ),
           PuzzlePiece('S+', 'D+', 'S-', 'H-' ))

# Possible places to put the pieces
# Positions have piece index and rotation
board = [[ PuzzlePiece('??', '??', '??', '??'),
           PuzzlePiece('??', '??', '??', '??'),
           PuzzlePiece('??', '??', '??', '??')],
         [ PuzzlePiece('??', '??', '??', '??'),
           PuzzlePiece('??', '??', '??', '??'),
           PuzzlePiece('??', '??', '??', '??')],
         [ PuzzlePiece('??', '??', '??', '??'),
           PuzzlePiece('??', '??', '??', '??'),
           PuzzlePiece('??', '??', '??', '??')]]

# Path to follow when placing pieces on the board
path = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]


def debug(*message):
    debug = False

    if debug:
        output = []
        for item in message:
            output.append(str(item))

        print ''.join(output)


# Yes I know, I should be using loops to print out the board
# so that it can be an arbitrary size.
def print_board(board):
    print "==========================="
    print '  ', board[0][0].north(), '      ', board[0][1].north(), '      ', board[0][2].north(), '  '
    print board[0][0].west(), '**', board[0][0].east(), '', \
          board[0][1].west(), '**', board[0][1].east(), '', \
          board[0][2].west(), '**', board[0][2].east(), ''
    print '  ', board[0][0].south(), '      ', board[0][1].south(), '      ', board[0][2].south(), '  '
    print

    print '  ', board[1][0].north(), '      ', board[1][1].north(), '      ', board[1][2].north(), '  '
    print board[1][0].west(), '**', board[1][0].east(), '', \
          board[1][1].west(), '**', board[1][1].east(), '', \
          board[1][2].west(), '**', board[1][2].east(), ''
    print '  ', board[1][0].south(), '      ', board[1][1].south(), '      ', board[1][2].south(), '  '
    print

    print '  ', board[2][0].north(), '      ', board[2][1].north(), '      ', board[2][2].north(), '  '
    print board[2][0].west(), '**', board[2][0].east(), '', \
          board[2][1].west(), '**', board[2][1].east(), '', \
          board[2][2].west(), '**', board[2][2].east(), ''
    print '  ', board[2][0].south(), '      ', board[2][1].south(), '      ', board[2][2].south(), '  '
    print "==========================="
    print


# Try to place a piece on the board
# Pass in the path index to try,
# and the current board status.
# The list of pieces and a list of used pieces

def place_piece(path, board, path_idx, pieces, used):

    unknown = PuzzlePiece('??', '??', '??', '??')

    debug("Entering place_piece at depth ", path_idx)
    debug("    current path:", used)

    # No pieces left to try... return
    if path_idx >= len(path):
        print "I win?!?!\n\n"

        print_board(board)

        exit(0)

    # path(path_idx) will tell us where on the board we want to place a piece.
    (pos_x, pos_y) = path[path_idx]

    # Find the shape of the piece we need.
    # Yes I know using constants is bad and will
    # keep this from working on board sizes other then 3x3

    if (pos_x -1) != -1:
        north = board[pos_x -1][pos_y].south()
    else:
        north = unknown.south()

    if (pos_x +1) != 3:
        south = board[pos_x +1][pos_y].north()
    else:
        south = unknown.north()

    if (pos_y -1) != -1:
        west = board[pos_x][pos_y -1].east()
    else:
        west = unknown.east()

    if (pos_y +1) != 3:
        east = board[pos_x][pos_y +1].west()
    else:
        east = unknown.west()

    # This creates a piece with all the proper shapes, but not the proper genders.
    spot = PuzzlePiece( north, east, south, west)
    #spot.flip_gender()

    for idx in range(0,9):
        debug("    testing piece ",idx," at depth ", path_idx)
        if idx in used:
            debug("        piece ", idx, "has been used. NEXT!")
            next
        else:
            rotation = pieces[idx].rotcmp(spot)
            debug("      rotation = "), rotation

            if rotation != -1:
                debug("placing piece[",idx,"] at ",pos_x,",",pos_y," with rotation ", rotation,".\n")
                temp_piece = board[pos_x][pos_y]
                board[pos_x][pos_y] = pieces[idx]
                board[pos_x][pos_y].rotation = rotation
                #print_board(board)
                used.append(idx)

                place_piece(path, board, path_idx + 1, pieces, used)

                debug("removing piece[",idx,"] at ",pos_x,",",pos_y,".\n")
                board[pos_x][pos_y] = temp_piece
                #print_board(board)
                used.pop()

    # If we got here we couldn't find a match for that spot on the board
    # That lead to board compleation. Return to try the next one.
    debug("Exiting place_piece from depth ",path_idx)
    return

used = []
place_piece(path, board, 0, pieces, used)

print "huh?\n"
