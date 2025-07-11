from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def test_expression(expression):
    print(f"\n=== Testing: {expression} ===")
    
    # Lexical Analysis
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    print(f"Tokens: {tokens}")
    
    # Parsing
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST: {ast}")
    
    # Interpretation
    interpreter = Interpreter()
    result = interpreter.interpret(ast)
    print(f"Result: {result}")

if __name__ == "__main__":
    # Test cases
    test_expressions = [
        "3 + 4",
        "10 - 5",
        "6 * 7",
        "15 / 3",
        "2 + 3 * 4",  # Should be 14 (multiplication first)
        "(2 + 3) * 4",  # Should be 20 (parentheses first)
        "-5 + 3",
        "3.5 + 2.5",
        "10 / 2 + 3 * 4"
    ]
    
    for expr in test_expressions:
        try:
            test_expression(expr)
        except Exception as e:
            print(f"Error: {e}") 