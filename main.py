#!/usr/bin/env python3
"""
Modular arithmetic calculator.
Supports +, -, *, /, %, **, and parentheses.
Example: (3 + 5) * 2 - 4 / 2   ->   14.0
"""

from calc.tokenizer import Tokenizer
from calc.parser import Parser
from calc.evaluator import Evaluator

def evaluate_expression(expr: str) -> float:
    """Parse and evaluate a mathematical expression."""
    tokens = Tokenizer(expr).tokenize()
    ast = Parser(tokens).parse()
    result = Evaluator().evaluate(ast)
    return result

def main():
    print("=== Advanced Calculator ===")
    print("Supported operators: +, -, *, /, %, **, ( )")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            expr = input(">>> ").strip()
            if expr.lower() in ('quit', 'exit', 'q'):
                break
            if not expr:
                continue
            
            result = evaluate_expression(expr)
            print(f"{expr} = {result}\n")
        
        except (SyntaxError, ZeroDivisionError, ValueError, TypeError) as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

if __name__ == "__main__":
    main()