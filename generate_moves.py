#!/usr/bin/env python3

# this common thinking for this problem is:
# one function generates all moves for all pieces on the board, then compiles it into a list
# another function checks the legality of the move (is another piece on the same square, does that move leave
# my king in check)


def generate_moves(position):
    
    
    # the key insight into generating moves is that each piece type has a number, or more accurately a set (mask)
    # of numbers that can be applied to it's bitboard that represent which moves it can make. 
    # pl in the function name stands for pseudolegal 
    
    def generate_pl_pawn_moves():
        position.black_pawns << 8
        position.white_pawns << 8 