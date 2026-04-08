class User:
    """
    A class representing a website user.
 
    Attributes:
        id (int): Unique user identifier.
        nick_name (str): User's nickname (login).
        first_name (str): User's first name.
        last_name (str): User's last name (optional).
        middle_name (str): User's middle name (optional).
        gender (str): User's gender (optional).
    """
    
    def __init__(self, id, nick_name, first_name, last_name='', middle_name='', gender='') -> None:
        """Initialize a new User object."""
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
    
    def update(self, id=None, nick_name=None, first_name=None, last_name=None, middle_name=None, gender=None) -> None:
        """Update user attributes."""
        if id is not None:
            self.id = id
        if nick_name is not None:
            self.nick_name = nick_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if gender is not None:
            self.gender = gender
    
    def __str__(self) -> str:
        """Return a string representation of the User object."""
        name_parts = []
        
        if self.last_name:
            name_parts.append(self.last_name)
        
        name_parts.append(self.first_name)
        
        if self.middle_name:
            name_parts.append(self.middle_name)
        
        name_string = ' '.join(name_parts)
        
        result = f"ID: {self.id} LOGIN: {self.nick_name} NAME: {name_string}"
        
        if self.gender:
            result += f" GENDER: {self.gender}"
        
        return result
    
    def __repr__(self) -> str:
        """Return a string representation for debugging and collections."""
        return self.nick_name


def main():
    """Main function to demonstrate the User class functionality."""
    user_1 = User(12, 'alex', 'Алексей')
    print(user_1)
    
    user_2 = User(44, 'andru', 'Андрей', 'Петров')
    print(user_2)
    
    user_3 = User(25, 'nik', 'Николай', 'Иванов', 'Федорович')
    print(user_3)
    
    user_4 = User(61, 'ivan', 'Денис', 'Сидоров', 'Алексеевич', 'М')
    print(user_4)
    
    user_5 = User(47, 'ann', 'Анна', gender='F')
    print(user_5)
    

    user_4.update(0, None, 'Ваня')  
    print(user_4)
    
    user_3.update(15, None, 'Никита', None, 'Петрович')  
    print(user_3)
    
    users = []
    users.append(user_2)
    users.append(user_4)
    users.append(user_5)
    users.append(user_1)
    users.append(user_3)
    print(users)


if __name__ == "__main__":
    main()
