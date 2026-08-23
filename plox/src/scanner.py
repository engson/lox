from frozendict import frozendict

from src import lox
from src.token import Token
from src.token_type import TokenType


class Scanner:
    
    source: str
    tokens: list[Token]
    start: int = 0
    current: int = 0
    line: int = 1

    keywords:frozendict[str,TokenType] = frozendict({
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE        
    })
    
    
    def __init__(self):
        self.source: str


    def scanTokens(self) -> list[Token]: 
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))            
        return self.tokens

    def isAtEnd(self) -> bool:
        return self.current >= len(self.source)

    def advance(self) -> str:
        return self.source[self.current+1]

    def addToken(self, type: TokenType, literal: object | None = None):
        text: str = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))
    
    def match(self, expected: str) -> bool:
        if self.isAtEnd(): return False
        if self.source[self.current] != expected: return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.isAtEnd(): return '\0'
        return self.source[self.current]

    def peekNext(self) -> str:
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]

    def string(self):
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == '\n': self.line += 1
            self.advance()
        if self.isAtEnd():
            lox.error(self.line, "Unterminated string.")
            return
        # the closing "
        self.advance()

        value: str = self.source[self.start + 1:self.current - 1]
        self.addToken(TokenType.STRING, value)

    def number(self):
        while self.peek().isdigit(): self.advance()
        # Look for a fractional part.
        if self.peek() == '.' and self.peekNext().isdigit():
            # consum the "."
            self.advance()

            while self.peek().isdigit(): self.advance()

    def isAlpha(self, c: str) -> bool:
        return c.isalpha() or c == '_'

    def isAlphaNumeric(self, c:str) -> bool:
        return c.isalnum()

    def identifier(self):
        while self.isAlphaNumeric(self.peek()): self.advance()
        text: str = self.source[self.start:self.current]
        type: TokenType = self.keywords.get(text, TokenType.IDENTIFIER)
        self.addToken(type)
        

    def scanToken(self):
        c:str = self.advance()
        assert len(c) == 1
        match c:
            case '(': self.addToken(TokenType.LEFT_PAREN)
            case ')': self.addToken(TokenType.RIGHT_PAREN)
            case '{': self.addToken(TokenType.LEFT_BRACE)
            case '}': self.addToken(TokenType.RIGHT_BRACE)
            case ',': self.addToken(TokenType.COMMA)
            case '.': self.addToken(TokenType.DOT)
            case '-': self.addToken(TokenType.MINUS)
            case '+': self.addToken(TokenType.PLUS)
            case ';': self.addToken(TokenType.SEMICOLON)
            case '*': self.addToken(TokenType.STAR)
            case '!':
                self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=':
                self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '/':
                if self.match('/'):
                    while (self.peek() != '\n' and not self.isAtEnd()): self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            case ' ' | '\r' | '\t': pass
            case '\n':
                self.line += 1
            case '"': self.string()
            case _:
                if c.isdigit():
                    self.number()
                elif self.isAlpha(c):
                    self.identifier()
                else:
                    lox.error(self.line, "Unexpected character.")
            
