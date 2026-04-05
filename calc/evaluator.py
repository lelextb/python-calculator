from .parser import ASTNode, NumberNode, BinaryOpNode

class Evaluator:
    """Evaluate the AST and return a number."""
    
    def evaluate(self, node: ASTNode) -> float:
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, BinaryOpNode):
            left_val = self.evaluate(node.left)
            right_val = self.evaluate(node.right)
            op = node.op
            
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                if right_val == 0:
                    raise ZeroDivisionError("Division by zero")
                return left_val / right_val
            elif op == '%':
                return left_val % right_val
            elif op == '**':
                return left_val ** right_val
            else:
                raise ValueError(f"Unknown operator: {op}")
        else:
            raise TypeError(f"Unknown node type: {type(node)}")