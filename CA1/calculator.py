import math

class Calculator(object):
 
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
 
    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError

    def multi(self, x,y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x*y
        else:
            raise ValueError

    def div(self, x,y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x/y
        else:
            raise ValueError            

    def expo(self, x,y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x**y
        else:
            raise ValueError            

    def sqr(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return x**2
        else:
            raise ValueError            

    def cbe(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return x**3
        else:
            raise ValueError

            
    def tan(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.tan(x)
        else:
            raise ValueError            

    def sin(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.sin(x)
        else:
            raise ValueError            
                        
    def cos_calc(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.cos(x)
        else:
            raise ValueError                       
            
