#IDEA for later: add a sentiment funtion for the language that will return the if a string has positive sentiment of negative and ask chatgpt for more ideas

#Constants
DIGITS = '0123456789'
ALPHA = 'abcdefghijklmnopqrstuvwxyz'
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
class Position:
  def __init__(self, idx, ln, col, fileName, fileTxt) -> None:
    self.idx = idx
    self.ln = ln
    self.col = col
    self.fileName = fileName 
    self.fileTxt = fileTxt
  def advance(self, current_char) -> int:
    self.idx += 1
    self.col += 1
    if current_char == "\n":
      self.ln += 1
      self.col = 0 #reset the column to 0
    return self.idx
  def copy(self):
    return Position(self.idx, self.ln, self.col, self.fileName, self.fileTxt)

   
   
#Tokens
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

class Token: 
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    def __repr__(self) -> str:
        if self.value: 
            return f'{self.type}:{self.value}'
        else: return f'{self.type}'
    

#LEXER

class Lexer: 
    def __init__(self, fileName, text):
        self.fileName = fileName
        self.text = text
        self.pos = Position(-1,0,-1, fileName, text)
        self.current_char = None
        self.advance()
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx<len(self.text) else None
    
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t': #skips spaces and tabs
              self.advance()
            elif self.current_char in DIGITS:
              tokens.append(self.make_number())
            elif self.current_char == '+':
              tokens.append(Token(TT_PLUS)) # TT stands for token type
              self.advance()
            elif self.current_char == '-':
              tokens.append(Token(TT_MINUS))
              self.advance()
            elif self.current_char == '/':
              tokens.append(Token(TT_DIV))
              self.advance()
            elif self.current_char == '*':
              tokens.append(Token(TT_MUL))
              self.advance()
            elif self.current_char == '(':
              tokens.append(Token(TT_LPAREN))
              self.advance()
            elif self.current_char == ')':
              tokens.append(Token(TT_RPAREN))
              self.advance()
            else: 
              # return some sort of error 
              pos_start = self.pos.copy()
              char = self.current_char
              self.advance()
              return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
        return tokens, None
        

    def make_number(self):
        num_str = ''
        count_dots = 0 # to see if it is a float

        while self.current_char != None and self.current_char in DIGITS + '.':
          if self.current_char == '.':
            if count_dots == 1: break # cuz can't have more than one dot in num
            dot_count += 1
            num_str += '.'
          else:
            num_str += self.current_char
          self.advance()
        
        if count_dots == 0:
          return Token(TT_INT, int(num_str))
        else: 
          return Token(TT_FLOAT, float(num_str))
    
    #def make_letters(self):
       

#ADDITION: 

#SUBSTRACTION:

#PRINT: 

        
#RUN
def run(fileName, text):
  lexer = Lexer(fileName, text)
  tokens, error = lexer.make_tokens()

  return tokens, error

