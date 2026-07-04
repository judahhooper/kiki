#!/usr/bin/env python3

import Position

def parse_fen():
    print("provide FEN string: ")
    # example fen:
    # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    fen = input()
    fields = fen.split()
    board, side, castling, en_passant, halfmove, fullmove = fields

    def parse_board(board):

        # FEN goes file by file. Numbers mean skip a file for the amount 
        # specified. so 3p2 on a file means, skip three, then there's a pawn
        # then skip two. 

parse_fen()