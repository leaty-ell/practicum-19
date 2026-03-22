class TrafficLight:
    """
    A class representing a traffic light.
    
    Class Attributes:
        permissible_values (list): List of possible traffic light signals.
    
    Attributes:
        current_signal (str): The current signal of the traffic light.
        index (int): Current position index in the signal cycle.
    """
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']
    
    def __init__(self):
        """Initialize a new TrafficLight object."""
        self.current_signal = self.permissible_values[0]
        self.index = 0
    
    def next_signal(self):
        """Change the traffic light to the next signal."""
        self.index = (self.index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.index]
    
    def __str__(self):
        """
        Return a string representation of the traffic light.
      
        Returns:
            str: The current signal of the traffic light.
        """
        return self.current_signal

def main():
    """The main function of the program."""
    seven_roads = TrafficLight()
    print(seven_roads.current_signal)
    
    for _ in range(5):
        seven_roads.next_signal()
    
    print(seven_roads.current_signal)


if __name__ == "__main__":
    main()
