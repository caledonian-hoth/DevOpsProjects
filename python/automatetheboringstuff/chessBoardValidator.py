#! /usr/bin/python
chessBoard = {'1h': 'bking', '8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
import pprint

def isValidChessBoard(board):
    """
    In this function, I will validate wether the chess pieces are valid.
    A valid board will have exactly one black king and exactly one white king. 
    Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
    The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
    This function should detect when a bug has resulted in an improper chess board.
    """
    # I am building a dictionary of how many times each chess piece (chessBoard value) appears on the board (chessBoard dictionary)
    countPiece = {} # Start with an empty dictionary.
    wPieces = 0 # Sum of white pieces 
    bPieces = 0 # Sum of black pieces
    x = '' # x axis containing letters
    y = 0  # y axis containing single digits

    for k,v in board.items():  # Running through the dictionary.
        countPiece.setdefault(v, 0) 
        """ setdefault checks if the key exists in the dictionary, if not, it adds is with a default value of 0. If it finds one, it returns it's existing value.
        This builds the initial dictionary with all the pieces encountered on board.
        """
        countPiece[v] += 1 # Increase the number of pieces encountered by 1.
        if str(v[0]) == 'w':
            wPieces += 1 # Increase the sum of white pieces.
        else:
            bPieces += 1 # Increase the sum of black pieces.
        # Here we check if the position on the board is out of bounds, if it's more than 2 characters long
        if len(k) > 2:
            return False    
        if int(k[0]) > y:
            y = int(k[0]) # We're getting the highest value on the y axis and compare it with the imposed limit
        if str(k[1]) > x:
            x = str(k[1]) # We're getting the highest value on the x axis and compare it with the imposed limit

    # Here we check if there are more or less than 1 of each kings.
    if countPiece['bking'] != 1 or countPiece['wking'] != 1:
        return False
    # Here we check if we have more than 8 pawns of any color. We can have 0.
    elif countPiece.get('wpawn', 0) > 8 or countPiece.get('bpawn', 0) > 8:
        return False
    # Here we check if either of the players have more than 16 pieces
    elif wPieces > 16 or bPieces > 16:
        return False    
    elif x > 'h' or y > 8:
        return False
    else:
        return True

print(isValidChessBoard(chessBoard))