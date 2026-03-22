class Game:
    """
    A class representing a basketball game.
    
    Attributes:
        teams (dict): Dictionary containing team names with keys 'command1' and 'command2'.
        score1 (int): Score of the first team.
        score2 (int): Score of the second team.
    """
    
    def __init__(self, teams):
        """Initialize a new Game object."""
        self.teams = teams
        self.score1 = 0  
        self.score2 = 0  
    
    def ball_thrown(self, command, points):
        """Add points to the specified team."""
        if command == 1:
            self.score1 += points
        elif command == 2:
            self.score2 += points
    
    def get_score(self):
        """
        Return the current score of the game. 
        This method returns a tuple containing the scores of both teams.
        """
        return (self.score1, self.score2)
    
    def get_winner(self):
        """Determine the winner of the game."""
        if self.score1 > self.score2:
            return self.teams['command1']
        elif self.score2 > self.score1:
            return self.teams['command2']
        else:
            return 'Ничья'


def main():
    """The main function of the program."""
    game_one = Game({'command1': 'Юта Джаз', 'command2': 'Майами Хит'})
    
    game_one.ball_thrown(1, 2) 
    game_one.ball_thrown(1, 3) 
    game_one.ball_thrown(2, 2)  
    game_one.ball_thrown(1, 1)  
    
    print(game_one.get_score()) 

    game_one.ball_thrown(2, 3)  
    game_one.ball_thrown(2, 2)  
    game_one.ball_thrown(1, 2)  
    
    print(game_one.get_score())  
    print(game_one.get_winner())  

if __name__ == "__main__":
    main()
