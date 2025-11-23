import random
'''
iterator: An object that returns elements one at a time from a sequence(data stream) 
and also remembers its position between every calls.

A Python object is termed as iterator if it has:
__iter__(): Returns the iterator object itself
__next__(): Returns the nxt item in the sequence and 
            raises StopIteration exception when no more item left.
'''

class Dice:
    def __init__(self,rolls):
        self.rolls = rolls
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.count < self.rolls):
            self.count+=1
            return random.randint(1,6)
        else:
            raise StopIteration
        

dice = Dice(4)
#dice object is iterable: We can run for loop over it.
for die in dice:
    print(die)

#Short-Way of above
dice = [die for die in Dice(4)]
print(dice)

#Behind the scene below stuff happened: 
# dice = Dice(4)
# iterator = iter(dice)#dice.__iter__()
# while True:
#     try:
#         roll = next(iterator)#iterator.__next__()
#         print(roll)
#     except StopIteration:
#         break
