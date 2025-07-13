#########################
# NODE CLASSES
#########################
class NumberNode:
  def __init__(self, tok):
    self.tok = tok
  def __repr__(self):
    return f'{self.tok}'

class BinOpNode:
  def __init__(self, left_tok, op_tok ,right_tok):
    self.left_tok = left_tok
    self.op_tok = op_tok
    self.right_tok = right_tok
  def __repr__(self):
    return f'{self.left_tok}, {self.op_tok}, {self.right_tok}'

class UnOpNode: # for stuff like (-5) 
  def __init__(self, op_tok, tok):
    self.op_tok = op_tok
    self.tok = tok
  def __repr__(self):
    return f'{self.op_tok}, {self.tok}'

#ParenNode is for  partenthesized expressesions like (2+3)
class ParenNode:
  def __init__(self, node):
    self.node = node
  def __repr__(self):
    return f'{self.node}'
  


