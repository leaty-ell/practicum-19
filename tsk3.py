class NotSleeping:
    """
     A class representing a person who cannot sleep and counts sheep.
    This class keeps track of a person's name and the number of sheep they have counted
    while trying to fall asleep. The person can lose count and start over.
    
    Attributes:
        name (str): The name of the person.
        count_sheeps (int): The number of sheep counted.
    """
    
    def __init__(self, name, count_sheeps=0) -> None:
        """Initialize a new NotSleeping object."""
        self.name = name
        self.count_sheeps = count_sheeps
    
    def add_sheep(self) -> None:
        """Add one sheep to the count."""
        self.count_sheeps += 1
    
    def lost(self) -> None:
        """Reset the sheep counter."""
        self.count_sheeps = 0
    
    def get_count_sheeps(self) -> int:
        """Return the current number of counted sheep."""
        return self.count_sheeps


def main() -> None:
    """The main function of the program."""
    human = NotSleeping('Мистер Смит')
    
    human.add_sheep()  
    human.add_sheep() 
    human.add_sheep()  
    human.add_sheep() 
    human.add_sheep()  
    
    print(human.name, 'насчитал', human.count_sheeps, 'овец')
    
    human.lost()
   
    human.add_sheep()  
    human.add_sheep() 
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep() 
    
    print(human.name, 'насчитал', human.get_count_sheeps(), 'овец')


if __name__ == "__main__":
    main()
