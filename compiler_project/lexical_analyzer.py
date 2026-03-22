from enum import Enum, auto


class Token(Enum):

    # char classes
    EOF = -1
    UNKNOWN = 0
    LETTER = 1
    DIGIT = 2
    TAB = 3

    # literals
    INT_LITERAL = auto()
    FLOAT_LITERAL = auto()
    STRING_LITERAL = auto()   # double-quoted  "..."
    CHAR_LITERAL = auto()     # single-quoted  '...'

    # identifiers
    IDENTIFIER = auto()

    # operators
    ASSIGN_OPERATOR = auto()
    ADDITION_OPERATOR = auto()
    SUBTRACTION_OPERATOR = auto()
    MULTIPLICATION_OPERATOR = auto()
    DIVISION_OPERATOR = auto()

    # grouping
    LEFT_PARENTHESIS = auto()
    RIGHT_PARENTHESIS = auto()
    LEFT_SQUARE_BRACKET = auto()
    RIGHT_SQUARE_BRACKET = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()

    # separators
    DOT = auto()
    COMMA = auto()
    APOSTROPHE = auto()
    QUOTATION = auto()
    SEMICOLON = auto()
    COLON = auto()

    # modifier keywords
    KEYWORD_PUBLIC = auto()
    KEYWORD_CLASS = auto()
    KEYWORD_STATIC = auto()
    KEYWORD_VOID = auto()
    KEYWORD_SYSTEM = auto()
    KEYWORD_OUT = auto()
    KEYWORD_FUNCTION = auto()  # def

    # extra keywords needed for the Java file
    KEYWORD_INT = auto()
    KEYWORD_STRING = auto()
    KEYWORD_PRINTLN = auto()
    KEYWORD_MAIN = auto()


KEYWORDS = {
    "public":   Token.KEYWORD_PUBLIC,
    "class":    Token.KEYWORD_CLASS,
    "static":   Token.KEYWORD_STATIC,
    "void":     Token.KEYWORD_VOID,
    "System":   Token.KEYWORD_SYSTEM,
    "out":      Token.KEYWORD_OUT,
    "def":      Token.KEYWORD_FUNCTION,
    "int":      Token.KEYWORD_INT,
    "String":   Token.KEYWORD_STRING,
    "println":  Token.KEYWORD_PRINTLN,
    "main":     Token.KEYWORD_MAIN,
}


class Lexer:
    def __init__(self, source: str):
        self.source = source          # full source text
        self.pos = 0                  # current read position
        self.next_char = ""
        self.char_class = None
        self.lexeme = ""
        self.next_token = None
        self.tokens: list[tuple[Token, str]] = []

        self._advance()

    # helpers

    def _advance(self):
        """Read the next character from source and classify it."""
        if self.pos < len(self.source):
            self.next_char = self.source[self.pos]
            self.pos += 1
        else:
            self.next_char = ""

        self.get_char(self.next_char)

    def get_char(self, char: str):
        """Set char_class based on the character."""
        if not char:
            self.char_class = Token.EOF
            self.next_token = Token.EOF
        elif char.isalpha() or char == "_":
            self.char_class = Token.LETTER
        elif char.isdigit():
            self.char_class = Token.DIGIT
        elif char == "\t":
            self.char_class = Token.TAB
        else:
            self.char_class = Token.UNKNOWN

    def add_char(self):
        """Append the current character to the lexeme."""
        self.lexeme += self.next_char

    def get_non_blank(self):
        """Skip whitespace (spaces, tabs, newlines)."""
        while self.next_char in (" ", "\t", "\n", "\r"):
            self._advance()

    def lookup(self, char: str) -> Token:
        """Return the token for a single-character symbol."""
        self.add_char()
        mapping = {
            "(": Token.LEFT_PARENTHESIS,
            ")": Token.RIGHT_PARENTHESIS,
            "[": Token.LEFT_SQUARE_BRACKET,
            "]": Token.RIGHT_SQUARE_BRACKET,
            "{": Token.LEFT_BRACKET,
            "}": Token.RIGHT_BRACKET,
            "+": Token.ADDITION_OPERATOR,
            "-": Token.SUBTRACTION_OPERATOR,
            "*": Token.MULTIPLICATION_OPERATOR,
            "/": Token.DIVISION_OPERATOR,
            "=": Token.ASSIGN_OPERATOR,
            ".": Token.DOT,
            ",": Token.COMMA,
            ";": Token.SEMICOLON,
            ":": Token.COLON,
        }
        return mapping.get(char, Token.UNKNOWN)

    # string / char literal helpers

    def _read_string_literal(self, quote_char: str) -> Token:
        """Read everything up to the closing quote_char.
        The opening quote is already in self.lexeme before this is called."""
        while self.next_char and self.next_char != quote_char:
            self.add_char()
            self._advance()
        # read closing quote
        self.add_char()   # add the closing quote
        self._advance()   # move past it
        return Token.STRING_LITERAL if quote_char == '"' else Token.CHAR_LITERAL

    # core lex method returns one (Token, lexeme) pair

    def lex(self) -> tuple[Token, str] | None:
        """Scan and return the next token, or None at EOF."""
        self.get_non_blank()
        self.lexeme = ""

        match self.char_class:

            case Token.EOF:
                self.next_token = Token.EOF
                return None

            # identifiers & keywords
            case Token.LETTER:
                self.add_char()
                self._advance()
                while self.char_class in (Token.LETTER, Token.DIGIT):
                    self.add_char()
                    self._advance()
                self.next_token = KEYWORDS.get(self.lexeme, Token.IDENTIFIER)

            # integer (or float) literals
            case Token.DIGIT:
                self.add_char()
                self._advance()
                while self.char_class == Token.DIGIT:
                    self.add_char()
                    self._advance()
                if self.next_char == ".":
                    self.add_char()
                    self._advance()
                    while self.char_class == Token.DIGIT:
                        self.add_char()
                        self._advance()
                    self.next_token = Token.FLOAT_LITERAL
                else:
                    self.next_token = Token.INT_LITERAL

            # unknown / symbols
            case Token.UNKNOWN:
                char = self.next_char

                # double-quoted string  "..."
                if char == '"':
                    self.add_char()   # include opening "
                    self._advance()   # move past it
                    self.next_token = self._read_string_literal('"')

                # single-quoted string/char  '...'
                elif char == "'":
                    self.add_char()   # include opening '
                    self._advance()   # move past it
                    self.next_token = self._read_string_literal("'")

                # skip comments:  # ... (Python)  or  // ... (Java)
                elif char == "#":
                    while self.next_char and self.next_char != "\n":
                        self._advance()
                    return self.lex()   # recurse to get next real token

                elif char == "/" and self.pos < len(self.source) and self.source[self.pos] == "/":
                    while self.next_char and self.next_char != "\n":
                        self._advance()
                    return self.lex()

                else:
                    self.next_token = self.lookup(char)
                    self._advance()

            case Token.TAB:
                # treat tab as whitespace and move on
                # test file does not use indent / dedent in any meaningful way
                # so tabs can be ignored (behavior will need to change if test files become more complex)
                self._advance()
                return self.lex()

            case _:
                self.next_token = Token.UNKNOWN
                self._advance()

        return (self.next_token, self.lexeme)

    # tokenize the entire source

    def tokenize(self) -> list[tuple[Token, str]]:
        """Walk the source and collect every token."""
        self.tokens = []
        while True:
            result = self.lex()
            if result is None or result[0] == Token.EOF:
                break
            self.tokens.append(result)
        return self.tokens


# tokenize file and print results
def tokenize_file(path: str):
    print(f"\n{'='*60}")
    print(f"  FILE: {path}")
    print(f"{'='*60}")
    try:
        with open(path, "r") as f:
            source = f.read()
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        for token, lexeme in tokens:
            print(f"  {token.name:<30} |  {repr(lexeme)}")
        print(f"\n  Total tokens: {len(tokens)}")
    except FileNotFoundError:
        print(f"  Error: '{path}' not found.")

# tokenizes both files if this program is ran directly
if __name__ == "__main__":
    tokenize_file("test_files/python_add_numbers.py")
    tokenize_file("test_files/java_add_numbers.java")