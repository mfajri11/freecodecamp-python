class Rectangle:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"{Rectangle.__name__}(width={self.width}, height={self.height})"
    
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = ''
        for h in range(self.height):
            pic += '*'*self.width + '\n'
        return pic
    
    def get_amount_inside(self, sq):
        return int((self.height / sq.height)*(self.width/sq.width))
    
    
    
    
class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
      return f"{Square.__name__}(side={self.width})"

    def set_side(self, new_side):
        self.set_width(new_side)
        self.set_height(new_side)

    