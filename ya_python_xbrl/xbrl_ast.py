
class XbrlAst:

    def __init__(self):
        self.ast_left = None
        self.ast_right = None
        self.ast_value = None

    @property 
    def left(self):
        return self.ast_left

    @property 
    def right(self):
        return self.ast_right
    
    @property 
    def value(self):
        return self.ast_value

    @left.setter
    def left(self, val):
        self.ast_left = val

    @right.setter
    def right(self, val):
        self.ast_right = val

    @value.setter
    def value(self, val):
        self.ast_value = val
    
