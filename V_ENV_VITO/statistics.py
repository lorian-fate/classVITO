#from tia_COVID_19 import Process_DATA


class My_Statistics:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def constant(self):
        return len(self.x)

    @property
    def average_X(self):
        return sum(self.x) / self.constant
    
    @property
    def average_Y(self):
        return sum(self.y) / self.constant
    
    @property
    def sum_XY(self):
        return sum([x*y for x, y in zip(self.x, self.y)])
    
    @property
    def sum_X(self):
        return sum([x**2 for x in self.x])
    
    @property
    def sum_Y(self):
        return sum([y**2 for y in self.y])
    
    @property
    def sum_X_sum_Y(self):
        return sum([((x**2)*(y**2)) for x, y in zip(self.x, self.y)])

    @property
    def variance_X(self):
        return sum([(x-self.average_X)**2 for x in self.x]) / self.constant
    
    @property
    def variance_Y(self):
        return sum([(y-self.average_Y)**2 for y in self.y]) / self.constant
    
    @property
    def b(self):
        return ((self.constant*self.sum_XY) - (sum(self.x)*sum(self.y))) \
        / ((self.constant*self.sum_X) - (sum(self.x)**2))
    
    @property
    def b_0(self):
        return self.average_Y - self.b*self.average_X
    
    #@property
    def pred(self, value_K):
        return self.b*value_K + self.b_0
    

    def covariace(self):
        return (self.sum_XY / self.constant) - self.average_X*self.average_Y





"""obj = Statistics([2, 3, 5, 8, 9, 11, 14, 15],  [12, 6, 7, 3, 15, 10, 18, 5])
print(obj.variance_Y)
print(obj.sum_XY)
print(obj.sum_X_sum_Y)
print(obj.b)"""

"""ob = Process_DATA()
print(ob.date_tia)"""
