from enum import Enum, auto

class Token(Enum):

    # offset token id's to separate them from char class id's
    #def _generate_next_value_(name, start, count, last_values):
    #    return count + 100

    # char classes
    EOF = -1
    UNKNOWN = 0
    LETTER = 1
    DIGIT = 2
    TAB = 3

    # literals
    INT_LITERAL = auto()
    FLOAT_LITERAL = auto()
    STRING_LITERAL = auto()
    CHAR_LITERAL = auto()

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
    #INDENTATION = auto() # 4 spaces = indentation (for python)

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
    "public": Token.KEYWORD_PUBLIC,
    "class": Token.KEYWORD_CLASS,
    "static": Token.KEYWORD_STATIC,
    "void": Token.KEYWORD_VOID,
    "system": Token.KEYWORD_SYSTEM,
    "out": Token.KEYWORD_OUT,
    "def": Token.KEYWORD_FUNCTION,
}

# using globals was annoying and passing vars was making
# code hard to read so I opted to use a class instead
class Lexer:
    def __init__(self):
        self.char_class = None
        self.next_char = None
        self.lexeme = None
        self.lex_length = None
        self.token = None
        self.next_token = None

    def get_char(self, char):

        self.next_char = char

        if not char:
            self.char_class = Token.EOF
            self.next_token = Token.EOF
        elif char.isalpha():
            self.char_class = Token.LETTER
        elif char.isdigit():
            self.char_class = Token.DIGIT
        elif char == "\t":
            self.char_class = Token.TAB
        else:
            self.char_class = Token.UNKNOWN

# file to parse
file_path = "test_files/python_add_numbers.py"

# functions

# when there is a space this is called to find indentation
def is_indentation(file):
    return

def add_char():
    return

# get_char - gets next character in file and sets character class based on result


def get_non_blank():

    return

def lex():
    global lex_length

    match(char_class):

        case Token.EOF:
            return

        case Token.LETTER:
            return

        case Token.DIGIT:
            return

        case Token.TAB:
            return

        case Token.UNKNOWN:
            return



def lookup(char):
    match(char):
        case "(":
            add_char()
            next_token = Token.LEFT_PARENTHESIS

        case ")":
            add_char()
            next_token = Token.RIGHT_PARENTHESIS

        case "+":
            add_char()
            next_token = Token.ADDITION_OPERATOR

        case "-":
            add_char()
            next_token = Token.SUBTRACTION_OPERATOR

        case "*":
            add_char()
            next_token = Token.MULTIPLICATION_OPERATOR

        case "/":
            add_char()
            next_token = Token.DIVISION_OPERATOR

        case _:
            add_char()
            next_token = Token.EOF



# open input file and read through each char
def main():
    try:
        with open(file_path, "r") as file:

            lexer = Lexer

            while lexer.next_token != Token.EOF:
                char = file.read(1)
                get_char(char)
                lex()

    except FileNotFoundError:
        print(f"Error: '{file_path}' not found")

# initialize
main()
