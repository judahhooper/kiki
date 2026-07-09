#!/usr/bin/env python3

from position import Position

def parse_fen(fen):
    fields = fen.split()
    board, side, castling, en_passant, halfmove, fullmove = fields
    p = Position()
    parse_piece_placement(board, p) 
    p.capture_active_colour(side)
    p.capture_castling_rights(castling)
    p.capture_en_passant_info(en_passant)
    p.capture_halfmove_clock_value(halfmove)
    p.capture_fullmove_clock_value(fullmove)
    return p

def parse_piece_placement(board, p):

    # FEN goes file by file. Numbers mean skip a file for the amount 
    # specified. so 3p2 on a file means, skip three, then there's a pawn,
    # then skip two. 

    # read line by line (separated by / forward slash)
        # there's always 8 lines (ranks). 
    # interpret the content on each rank
        # specifically, extrapolate positional information about each piece 
    # pass that information to relevant bitboard 
    
    # i'll go slow from letter, to rank + file, to square number, to bitboard. 

    # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
     #8/8/8/3p4/8/8/8/8 w KQkq - 0 1
    ranks = board.split("/")
    
    # count backwards because that's how chess works, apparently 
    rank_number = 9
    
    # recall for square -> co-ordinate mapping; rank = index / 8 & file = index modulo 8
    # for co-ordinate -> square mapping;  square = (rank - 1) * 8 + (file - 1)
    # this is a bit of a fork in the road -  either a1 = 0 or a8 = 0. 
    # I've chosen to go with a1 = 0, as it looks to be what other engines use
    # and it's also how i'd count a chessboard if prompted on any given day, anyway.  
    
    for rank in ranks:
        file_number = 1
        rank_number -= 1
        for char in rank:      
            if char.isalpha():
                square_number = ((rank_number - 1)*8)+(file_number-1)
                p.place_piece_on_square(square_number, char)
                file_number += 1   
            
            elif char.isdigit():
                square_number= ((rank_number - 1)*8)+(file_number-1)
                empty_squares = int(char)
                p.place_piece_on_square(square_number, char) 
                file_number += empty_squares
                