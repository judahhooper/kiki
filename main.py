#!/usr/bin/env python3

from position import Position
from fen import parser
from generate_moves import generate_moves

def main():
    print("Do you want to provide a FEN?")
    answer=input() 
    
    if answer == "Yes":
        print("provide fen")
        # i know i should validate this and i will someday
        fen=input()
        position = Position()
        parser(fen, position)
        generate_moves(position)
    else:
        position = Position()
        generate_moves(position)
        
main()