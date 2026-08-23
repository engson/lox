from src.token import Token
from src.token_type import TokenType


class Scanner:
    
    source: str
    tokens: list[Token]
    start: int = 0
    current: int = 0
    line: int = 1

    keywords:dict[str,TokenType] = {
        "and": TokenType.AND,
        "class": TokenType.CLASS
    }
    
    
    
    def __init__(self):
        self.source: str
