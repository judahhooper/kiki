#!/usr/bin/env python3

# this common thinking for this problem is:
# one function generates all moves for all pieces on the board, then compiles it into a list
# another function checks the legality of the move (is another piece on the same square, does that move leave
# my king in check)


def generate_moves(position):
    
    # the key insight into generating moves is that each piece type has a number, or more accurately a set (mask)
    # of numbers that can be applied to it's bitboard that represent which moves it can make. 
    # pl in the function name stands for pseudolegal 
    # so you get this function to generate legal moves, and then compare that against the position's record of occupied squares for legality. Knights can hop over pieces so 
    # that needs to be taken into account, too. 
    
    def generate_pl_pawn_moves():
        
        # pawn moves that would result in two pieces occupying the same square should never be generated!
        white_pushes = (position.white_pawns << 8) & ~position.occupied
        black_pushes = (position.black_pawns << 8) & ~position.occupied
        
        # diagonal moves.. either one square to the left (9) or one to the right (7)
        # "keep only the destinations that contain a black piece" ergo captures 
        
        white_left_captures = (position.white_pawns << 7) & position.black_pieces
        white_right_captures = (position.white_pawns << 9) & position.white_pieces
        black_left_captures = (position.black_pawns << 7) & position.black_pieces
        black_right_captures = (position.black_pawns << 9) & position.white_pieces
        
        