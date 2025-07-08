from enum import Enum

# class TokenType(Enum):
#   # pattern                     # token name
#   NUMBER  = r'\d+(\.\d+)?'      # integers and decimals
#   PLUS    = r'\+'               # literal “+”
#   MINUS   = r'-'                # literal “-”
#   STAR    = r'\*'               # literal “*”
#   SLASH   = r'/'                # literal “/”
#   LPAREN  = r'\('               # literal “(”
#   RPAREN  = r'\)'               # literal “)”
#   IDENT   = r'[A-Za-z_]\w*'      # names (and reactive markers later)
#   DOLLAR  = r'\$'               # “$”
#   NEWLINE = r'\n'               # newline
#   WS      = r'[ \t]+'           # whitespace (we’ll skip these)
#   EOF     = ''                  # special case

class TokenType(Enum):
  INT  = 'INT'
  FLOAT = 'FLOAT'
  PLUS    = 'PLUS'
  MINUS   = 'MINUS'
  DIVIDE = 'DIVIDE'
  STAR    = 'STAR'
  MULTIPLY = 'MULTIPLY'
  LPAREN  = 'LPAREN'
  RPAREN  = 'RPAREN'
  IDENT   = 'IDENT' #identifier
  KEYWORD = 'KEYWORD'
  DOLLAR  = 'DOLLAR'
  NEWLINE = 'NEWLINE'
  EOF     = 'EOF'
  EQUAL   = 'EQUAL'
  BANG    = 'BANG'

keywords = ['function', 'equal', 'when', 'until', 'each', 'in', 'print']

class Token:
  def __init__(self, type_, value):
    self.type = type_
    self.value = value
  
  def __repr__(self):
    # so if you have something like type = INT and value = 42 thats chill but type=PLUS and value=None then just print type
    if self.value: 
      return f'{self.type}:{self.value}'
    return f'{self.type}'

class Lexer:
  def __init__(self, text):
    self.txt = text
    self.pos = -1 # why do we start with -1? 
    self.currChar = None
    self.advance()
  
  def advance(self):
    self.pos += 1
    self.currChar = self.txt[self.pos] if self.pos < len(self.txt) else None
  
  def tokenize(self):
    tokens = []
    while self.currChar != None:
      if self.currChar in ' \t': # this checks if it is a space or a tab
        self.advance()
      elif self.currChar == '+':
        tokens.append(Token(TokenType.PLUS))
        self.advance()
      elif self.currChar == '-':
        tokens.append(Token(TokenType.MINUS))
        self.advance()
      elif self.currChar == '*':
        tokens.append(Token(TokenType.MULTIPLY))
        self.advance()
      elif self.currChar == '/':
        tokens.append(Token(TokenType.DIVIDE))
        self.advance()
      elif self.currChar == '(':
        tokens.append(Token(TokenType.LPAREN))
        self.advance()
      elif self.currChar == ')':
        tokens.append(Token(TokenType.RPAREN))
        self.advance()
      elif self.currChar == '=':
        tokens.append(Token(TokenType.EQUAL))
        self.advance()
      elif self.currChar == '!':
        tokens.append(Token(TokenType.BANG))
        self.advance()
      elif self.currChar == '\n':
        tokens.append(Token(TokenType.NEWLINE))
        self.advance()
      elif self.currChar.isDigit():
        tokens.append(self.makeDigit())
      elif self.currChar.isalpa(): 
        tokens.append(self.makeIdentifier)
      elif self.currChar == '$':
        tokens.append(Token(TokenType.DOLLAR))
    tokens.append(Token(TokenType.EOF), None)
      # handle eof, handle numbers, identifiers and unknown characters
    return tokens
  
  def makeDigit(self):
    numOfDot = 0
    numberStr = ''
    while (self.currChar not None) and (self.currChar.isdigit() or self.currChar == '.'):
      if (self.currChar not '.') and (self.currChar.isdigit() == False):
        break # we reached end of number
      if self.currChar == '.':
        numOfDot += 1
        if numOfDot>1:
          raise ValueError("Incorrect int of float")

      numberStr += self.currChar
      self.advance()
    
    #edge case ex) 3.
    if numberStr[-1] == '.':
      raise ValueError("Incorrect int of float")
    return Token(TokenType.INT, int(numberStr)) if numOfDot == 0 else Token(TokenType.FLOAT, float(numberStr))
  
  def makeIdentifier(self):
    res = ''
    while (self.currChar not None) and (self.currChar.isdigit() or self.currChar.isalpha() or self.currChar == '_'):
      res += self.currChar
      self.advance()
    
    return 




  
  
      


  


    


