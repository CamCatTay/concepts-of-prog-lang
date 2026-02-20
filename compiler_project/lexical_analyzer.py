from enum import Enum, auto # so I don't have to manually assign token id's

class Token(Enum):

    # character classes
    EOF = -1
    UNKNOWN = 99
    LETTER = auto()
    DIGIT = auto()

    # literals
    INTEGER_LITERAL = auto()
    FLOAT_LITERAL = auto()
    STRING_LITERAL = auto()
    CHARACTER_LITERAL = auto()

    # identifiers
    IDENTIFIER = auto() # names (variable, function, class, ect...)

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
    KEYWORD_FUNCTION = auto() # def


#example: if there is public token return it otherwise return IDENTIFIER
#lexeme = "public"
#token_type = KEYWORDS.get(lexeme, TokenType.IDENTIFIER)
KEYWORDS = {
    "public": Token.KEYWORD_PUBLIC
    "class": Token.KEYWORD_CLASS
    "static": Token.KEYWORD_STATIC
    "void": Token.KEYWORD_VOID
    "system": Token.KEYWORD_SYSTEM
    "out": Token.KEYWORD_OUT
    "def": Token.KEYWORD_FUNCTION
}

# open input file and read through each character
def main():

