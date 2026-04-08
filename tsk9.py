from typing import List

class StrandsDNA:
    """
    A class representing DNA strands.
 
    Attributes:
        all_strands (list): List containing all DNA strands.
    """
    
    def __init__(self) -> None:
        """Initialize a new StrandsDNA object."""
        self.all_strands = []
    
    def add_strands(self, strands) -> None:
        """
        Add DNA strands to the collection.
        
        Args:
            strands (str): String containing DNA strands separated by spaces.
        """
        new_strands = strands.split()
      
        for strand in new_strands:
            self.all_strands.append(strand)
    
    def get_max_strands(self) -> str:
        """
        Get the longest unique DNA strands in alphabetical order.
        
        Returns:
            str: Space-separated string of longest unique strands in alphabetical order.
        """
        if not self.all_strands:
            return ''
          
        max_length = 0
        for strand in self.all_strands:
            if len(strand) > max_length:
                max_length = len(strand)
        
        longest_strands = []
        for strand in self.all_strands:
            if len(strand) == max_length:
                longest_strands.append(strand)
        
        unique_strands = sorted(set(longest_strands))
        result = ' '.join(unique_strands)
        
        return result
    
    def __str__(self) -> str:
        """
        Return a string representation of all DNA strands.
        
        Returns:
            str: Space-separated string of all DNA strands.
        """
        return ' '.join(self.all_strands)
  

def main() -> None:
    """The main function of the program."""
    covid_19 = StrandsDNA()
    
    covid_19.add_strands('GAAT ACCGTT TTGC TGGGAC')
    print(covid_19)  
  
    covid_19.add_strands('ACCT AGGCT TGGGAC')
    covid_19.add_strands('CATTTT TAATTC')
    print(covid_19) 
    
    print(covid_19.get_max_strands())


if __name__ == "__main__":
    main()
