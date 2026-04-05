from typing import List, Union
from .tokenizer import Token

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value: float):
        self.value = value

class BinaryOpNode(ASTNode):
    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right

class Parser:
    """Convert token list to AST using precedence climbing / shunting‑yard."""
    
    # Operator precedence and associativity
    PRECEDENCE = {
        '+': 1, '-': 1,
        '*': 2, '/': 2, '%': 2,
        '**': 3
    }
    ASSOC = {
        '+': 'L', '-': 'L',
        '*': 'L', '/': 'L', '%': 'L',
        '**': 'R'
    }
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self) -> ASTNode:
        if not self.tokens:
            raise SyntaxError("Empty expression")
        return self._parse_expression(0)
    
    def _parse_expression(self, min_prec: int) -> ASTNode:
        # Parse left atom (number or parenthesized expression)
        left = self._parse_atom()
        
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token.type != 'OPERATOR':
                break
            op = token.value
            prec = self.PRECEDENCE.get(op, -1)
            if prec < min_prec:
                break
            self.pos += 1
            
            # Right associative: next precedence is same, else prec+1
            next_prec = prec if self.ASSOC.get(op) == 'R' else prec + 1
            right = self._parse_expression(next_prec)
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def _parse_atom(self) -> ASTNode:
        if self.pos >= len(self.tokens):
            raise SyntaxError("Unexpected end of expression")
        token = self.tokens[self.pos]
        if token.type == 'NUMBER':
            self.pos += 1
            return NumberNode(token.value)
        elif token.type == 'OPERATOR' and token.value == '(':
            self.pos += 1
            expr = self._parse_expression(0)
            if self.pos >= len(self.tokens) or self.tokens[self.pos].value != ')':
                raise SyntaxError("Missing closing parenthesis")
            self.pos += 1
            return expr
        else:
            raise SyntaxError(f"Unexpected token: {token}")