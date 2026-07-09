#!/usr/bin/env python3

from position import Position
from fen import parser

def main():
    print("Do you want to provide a FEN?")
    answer=input() 
    
    if answer == "Yes":
        print("provide fen")
        fen=input()
        position = Position()
        parser(fen, position)
        generate_moves(position)
    else:
        position = Position()
        generate_moves(position)