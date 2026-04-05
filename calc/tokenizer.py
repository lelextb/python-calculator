import re
from typing import List, NamedTuple

class Token(NamedTuple):
    type: str   # 'NUMBER', 'OPERATOR', 'LPAREN', 'RPAREN'
    value: any  # float for NUMBER, str for others

class Tokenizer:
    """Convert an expression string into a list of tokens."""
    
    def __init__(self, expression: str):
        self.expression = expression.strip()
        self.pos = 0
    
    def tokenize(self) -> List[Token]:
        tokens = []
        # Regex: numbers (including decimals and negatives?), operators, parentheses
        # We'll handle unary minus later in parser; for now simple pattern
        pattern = re.compile(r'(\d+(?:\.\d+)?)|([+\-*/%^()])')
        
        for match in pattern.finditer(self.expression):
            num, op = match.groups()
            if num:
                tokens.append(Token('NUMBER', float(num)))
            elif op:
                if op == '^':
                    op = '**'   # power operator
                tokens.append(Token('OPERATOR', op))
            else:
                raise SyntaxError(f"Unexpected character: {match.group()}")
        
        return tokens