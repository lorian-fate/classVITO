
class Human:
    counter = 0
    def __init__(self, specie):
        self.specie = specie
        self.counter += 1
    
    @classmethod
    def set_att(cls, a, b):
        cls.a = a
        cls.b = b
        return cls.a, cls.b

homo_corpus_perfectum = Human("homo corpus perfectum")
a = homo_corpus_perfectum.counter
#print(homo_corpus_perfectum.set_att('vic', 'def'))

#print(type(a))

from itertools import combinations
import itertools
lis = ['a', 'b', 'c']
l = [i for i in itertools.permutations(lis,  4)]
print(len(l))
print(l)
#print(dir(itertools))