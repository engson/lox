from src.token_type import TokenType


class Token:
    type: TokenType
    lexeme: str
    literal: object
    line: int

    def __init__(self, type: TokenType, lexeme: str, literal: object, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal} {self.line}";

    
    def __repr__(self):
        return (
            f"Token("
            f"type={self.type!r}, "
            f"lexeme={self.lexeme!r}, "
            f"literal={self.literal!r}, "
            f"line={self.line!r}) "
            f"at {hex(id(self))}"
        )
 
if __name__ == "__main__":
    t = Token(TokenType.VAR, "variabel", {}, 2)
    import pdb; pdb.set_trace()
    
