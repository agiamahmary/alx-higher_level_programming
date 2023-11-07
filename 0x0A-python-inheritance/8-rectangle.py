 #!/usr/bin/python3
''' Contains Rectangle class
that Inherits from BaseGeometry
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """ Inherits BaseGeometry Class """
    
    def __init__(self, width, height):
        if not self.integer_validator('width', width):
            if  not self.integer_validator("height", height):
                self.__height = height
                self.__width = width
