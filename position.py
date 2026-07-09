class Position:
    def __init__(self):
        # having initially defined the bitboards and position metadata
        # without self, I realised I'd be essentially updating the "blueprint"
        # rather than the specific instance - self is necessary here. 

        # Bitboards
        self.white_pawns = 0
        self.white_knights = 0
        self.white_bishops = 0
        self.white_rooks = 0
        self.white_queens = 0
        self.white_king = 0

        self.black_pawns = 0
        self.black_knights = 0
        self.black_bishops = 0
        self.black_rooks = 0
        self.black_queens = 0
        self.black_king = 0

        # Position metadata
        self.active_colour = "w"
        self.castling_rights = ""
        self.en_passant = None
        self.halfmove_clock = 0
        self.fullmove_number = 1
        
        # aggregate masks - this really reminds me of discrete maths. 
        
        position.white_pieces = (
            position.white_pawns |
            position.white_knights |
            position.white_bishops |
            position.white_rooks |
            position.white_queens |
            position.white_king
    )

    position.black_pieces = (
            position.black_pawns |
            position.black_knights |
            position.black_bishops |
            position.black_rooks |
            position.black_queens |
            position.black_king
    )

    position.occupied = (
            position.white_pieces |
            position.black_pieces
    )
        
    def place_piece_on_square(self, square_number, char):
        
        # this is my first introduction to bitwise operators tbh
        
        # as i understand it, each line is basically saying:
        # "update the existing bitboard with whatever the parser told you, but don't overwrite"
            
        match char:
            case "b":
                self.black_bishops |= 1 << square_number
            case "n":
                self.black_knights |= 1 << square_number
            case "r":
                self.black_rooks |= 1 << square_number
            case "k":
                self.black_king |= 1 << square_number
            case "q":
                self.black_queens |= 1 << square_number
            case "p":
                self.black_pawns |= 1 << square_number

            case "B":
                self.white_bishops |= 1 << square_number
            case "N":
                self.white_knights |= 1 << square_number
            case "R":
                self.white_rooks |= 1 << square_number
            case "K":
                self.white_king |= 1 << square_number
            case "Q":
                self.white_queens |= 1 << square_number
            case "P":
                self.white_pawns |= 1 << square_number
                
    def capture_active_colour(self, side):
        self.active_colour = side
        
    def capture_castling_rights(self, castling):
        self.castling_rights = castling
        
    def capture_en_passant_info(self, en_passant):
        self.en_passant = en_passant
        
    def capture_halfmove_clock_value(self, halfmove_clock):
        self.halfmove_clock = halfmove_clock
        
    def capture_fullmove_clock_value(self, fullmove):
        self.fullmove_number = fullmove