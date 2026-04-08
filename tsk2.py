class NotSleeping:
    """
    A class representing a person who cannot sleep and counts sheep.
    
    Attributes:
        name (str): The name of the person.
        count_sheeps (int): The number of sheep counted.
    """
    
    def __init__(self, name, count_sheeps = 0) -> None:
        """Initialize a new NotSleeping object."""
        self.name = name
        self.count_sheeps = count_sheeps
    
    def add_sheep(self) -> None:
        """Add one sheep to the count."""
        self.count_sheeps += 1


def main() -> None:
    """
    Main function to demonstrate the NotSleeping class functionality.
    """
    human = NotSleeping('Мистер Смит')
    human.add_sheep() 
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep()  
    human.add_sheep() 
    
    mr_bean = NotSleeping('Мистер Бин', 9)
    mr_bean.add_sheep() 
    mr_bean.add_sheep()  
    mr_bean.add_sheep()  
    
    print(human.name, 'насчитал', human.count_sheeps, 'овец')
    print(mr_bean.name, 'насчитал', mr_bean.count_sheeps, 'овец')


if __name__ == "__main__":
    main()
