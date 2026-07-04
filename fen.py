#!/usr/bin/env python3

from position import Position

def parse_fen():
    print("provide FEN string: ")
    # example fen:
    # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    fen = input()
    fields = fen.split()
    board, side, castling, en_passant, halfmove, fullmove = fields

    parse_piece_placement(board)

    return board, side, castling, en_passant, halfmove, fullmove

    

def parse_piece_placement(board):

    # FEN goes file by file. Numbers mean skip a file for the amount 
    # specified. so 3p2 on a file means, skip three, then there's a pawn,
    # then skip two. 

    # read line by line (separated by / forward slash)
        # there's always 8 lines (ranks). 
    # interpret the content on each rank
        # specifically, extrapolate positional information about each piece 
    # pass that information to relevant bitboard 
    
    # i'll go slow from letter, to rank + file, to square number, to bitboard. 

    
    ranks = board.split("/")
    
    for rank in ranks:
        file_number = 1
        for char in rank:                        
            if char.isalpha():
                
                print("found a piece on this square")
                file_number += 1
                
            elif char.isdigit():

                print("found some empty squares")
                
                empty_squares = int(char)
                
                file_number += empty_squares
                 

parse_fen()
