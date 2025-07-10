from enum import Enum

#ERROR:
class Error: 
  def __init__(self,pos_start, pos_end, error_name, details):
    self.pos_start = pos_start
    self.pos_end = pos_end
    self.error_name = error_name
    self.details = details

  def as_string(self):
    result = f'{self.error_name}: {self.details}'
    result += f'\nFile {self.pos_start.fileName}, line {self.pos_start.ln + 1}'
    return result
  
class IllegalCharError(Error):
  def __init__(self, pos_start, pos_end, details):
    super().__init__(pos_start, pos_end, "Illegal Character", details)

#POSITION
# class Position:
#   def __init__(self, idx, ln, col, fileName, fileTxt) -> None:
#     self.idx = idx
#     self.ln = ln
#     self.col = col
#     self.fileName = fileName 
#     self.fileTxt = fileTxt
#   def advance(self, current_char) -> int:
#     self.idx += 1
#     self.col += 1
#     if current_char == "\n":
#       self.ln += 1
#       self.col = 0 #reset the column to 0
#     return self.idx
#   def copy(self):
#     return Position(self.idx, self.ln, self.col, self.fileName, self.fileTxt)

class TokenType(Enum):
  INT  = 'INT'
  FLOAT = 'FLOAT'
  PLUS    = 'PLUS'
  MINUS   = 'MINUS'
  DIVIDE = 'DIVIDE'
  STAR    = 'STAR'
  MULTIPLY = 'MULTIPLY'
  GREATERTHAN = 'GREATERTHAN'
  LESSTHAN = 'LESSTHAN'
  RARROW = 'RARROW' #The arrows are for the -> and <- 
  # LARROW = 'LARROW' 
  LPAREN  = 'LPAREN'
  RPAREN  = 'RPAREN'
  IDENT   = 'IDENT' #identifier
  KEYWORD = 'KEYWORD'
  DOLLAR  = 'DOLLAR'
  NEWLINE = 'NEWLINE'
  EOF     = 'EOF'
  EQUAL   = 'EQUAL'
  BANG    = 'BANG'

keywords = ['if','function', 'equal', 'when', 'until', 'each', 'in', 'print']

class Token:
  def __init__(self, type_, value=None):
    self.type = type_
    self.value = value
  
  def __repr__(self):
    # so if you have something like type = INT and value = 42 thats chill but type=PLUS and value=None then just print type
    if self.value: 
      #enum has a property named name
      return f'{self.type.name}:{self.value}'
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
        if (self.pos + 1 < len(self.txt)) and self.txt[self.pos+1] == '>':
          tokens.append(Token(TokenType.RARROW))
          self.advance() # do it twice so for - and >
          self.advance()
        else:
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
      elif self.currChar == '!':
        tokens.append(Token(TokenType.BANG))
        self.advance()
      elif self.currChar == '\n':
        tokens.append(Token(TokenType.NEWLINE))
        self.advance()
      elif self.currChar.isdigit():
        tokens.append(self.makeDigit())
      elif self.currChar.isalpha() or self.currChar == '_': 
        tokens.append(self.makeIdentifier())
      elif self.currChar == '$':
        tokens.append(Token(TokenType.DOLLAR))
        self.advance()
      elif self.currChar == '>':
        tokens.append(Token(TokenType.GREATERTHAN))
        self.advance()
      elif self.currChar == '<':
        if (self.pos + 1 < len(self.txt)) and self.txt[self.pos+1] == '-':
          tokens.append(Token(TokenType.EQUAL)) # Left arrow is equal
          self.advance() # do it twice so for - and >
          self.advance()
        else:
          tokens.append(Token(TokenType.LESSTHAN))
          self.advance()
      else:
        print(f"Warning: Skipping unknown character: {self.currChar}")
        self.advance()
    tokens.append(Token(TokenType.EOF, None))
    return tokens

  def makeDigit(self):
    numOfDot = 0
    numberStr = ''
    while (self.currChar != None) and (self.currChar.isdigit() or self.currChar == '.'):
      if (self.currChar != '.') and (self.currChar.isdigit() == False):
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
    while (self.currChar is not None) and (self.currChar.isdigit() or self.currChar.isalpha() or self.currChar == '_'):
      res += self.currChar
      self.advance()
    if res in keywords:
      return Token(TokenType.KEYWORD, res)
    return Token(TokenType.IDENT, res)

if __name__ == "__main__":
  #test lexer:
  test_input = "3+4 * (2-1)"
  lexer = Lexer(test_input)
  tokens = lexer.tokenize()
  print("Input: ", test_input)
  print("Tokens:", tokens)



  
  
      


  


    


