#!/usr/bin/env python3

import bitboards
import position
# this common thinking for this problem is:
# one function generates all moves for all pieces on the board, then compiles it into a list
# another function checks the legality of the move (is another piece on the same square, does that move leave
# my king in check)


def generate_moves(position):
    
    # the key insight into generating moves is that each piece type has a number, or more accurately a set (mask)
    # of numbers that can be applied to it's bitboard that represent which moves it can make. 
    # so you get this function to generate legal moves, and then compare that against the position's record of occupied squares for legality. 
    
    def generate_pawn_moves():
        
        # when pawns are on their starting squares, they can move two squares forward - black starts on RANK_7!
        # a sublety - it's not enough to check that the DESTINATION square is empty, as double pawn pushes are not available when an intermediate square is occupied. This hit me in the face, lol
        # better to start by generating all single pushes, then checking if the square in front is empty, if the pawn landed on rank 3/6 meaning it came from rank 2/7 then 
        # pawn moves that would result in two pieces occupying the same square should never be generated!
        
        white__single_pushes = (position.white_pawns << 8) & ~position.occupied
        black_single_pushes = (position.black_pawns >> 8) & ~position.occupied
        
        white_double_pushes = ((white__single_pushes & bitboards.RANK-_3) << 8) & ~position.occupied
        black_double_pushes = ((black_single_pushes & bitboards.RANK_6) >> 8) & ~position.occupied
        
        # diagonal moves.. either one square to the left (9) or one to the right (7)
        # "keep only the destinations that contain a black piece" ergo captures 
        # also need to consider what happens at the edge of the board? Presumably captures that are generated with out of bounds values will "wrap" onto the wrong squares..
  
        white_left_captures = ((position.white_pawns & bitboards.NOT_FILE_A) << 7) & position.black_pieces 
        white_right_captures = ((position.white_pawns & bitboards.NOT_FILE_H) << 9) & position.black_pieces
        black_left_captures = ((position.black_pawns & bitboards.NOT_FILE_H) >> 7) & position.white_pieces
        black_right_captures = ((position.black_pawns & bitboards.NOT_FILE_A) >> 9) & position.white_pieces
        
     
    def generate_knight_moves():
        # building the knight attack table is best. saves on CPU time which is a minor efficiency but they accumulate quickly!
        print(nothing)