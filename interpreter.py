from parser import ASTNode, NumberNode, BinaryOpNode, UnaryOpNode

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
    
    def visit_NumberNode(self, node):
        return node.value
    
    def visit_BinaryOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if node.op == 'PLUS':
            return left + right
        elif node.op == 'MINUS':
            return left - right
        elif node.op == 'MULTIPLY':
            return left * right
        elif node.op == 'DIVIDE':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        else:
            raise Exception(f'Unknown operator: {node.op}')
    
    def visit_UnaryOpNode(self, node):
        value = self.visit(node.node)
        
        if node.op == 'PLUS':
            return value
        elif node.op == 'MINUS':
            return -value
        else:
            raise Exception(f'Unknown unary operator: {node.op}')
    
    def interpret(self, ast):
        return self.visit(ast) 