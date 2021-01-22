from enum import Enum, unique, auto 

@unique 
class Fruit(Enum): 
    APPLE = 1 
    BANANA = 2 
    ORANGE = 3 
    TOMATO = 4 
    PEAR = auto()
    
def main(): 
    print(Fruit.APPLE) #Fruit.APPLE
    print(type(Fruit.APPLE)) # <enum 'Fruit'>
    print(repr(Fruit.APPLE)) # <Fruit.APPLE: 1>
    print(Fruit.PEAR.value) #5 
    
    # hashable and can be used as keys
    myFruits = {} 
    myFruits[Fruit.BANANA] = "Come see me"
    print(myFruits[Fruit.BANANA]) 
 
main()