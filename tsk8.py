from typing import List, Dict, Set

class MorseMsg:
    """
    A class representing a message in Morse code.
  
    Class Attributes:
        MORSE_TO_ENG (dict): Mapping from Morse code to English letters.
        MORSE_TO_RU (dict): Mapping from Morse code to Russian letters.
        VOWELS_ENG (set): Set of English vowels.
        VOWELS_RU (set): Set of Russian vowels.
        CONSONANTS_ENG (set): Set of English consonants.
        CONSONANTS_RU (set): Set of Russian consonants.
    
    Attributes:
        morse_string (str): The original Morse code string.
        morse_letters (list): List of individual Morse code letters.
    """
    MORSE_TO_ENG = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }
   
    MORSE_TO_RU = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '.-.-': 'Э',
        '..--': 'Ю', '.-.-.': 'Я'
    }
    
    VOWELS_ENG = {'A', 'E', 'I', 'O', 'U', 'Y'}
    VOWELS_RU = {'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'}
    CONSONANTS_ENG = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                      'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'}
    CONSONANTS_RU = {'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М',
                     'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
                     'Щ', 'Ъ', 'Ь'}
    
    def __init__(self, morse_string) -> None:
        """Initialize a new MorseMsg object."""
        self.morse_string = morse_string
        self.morse_letters = morse_string.split()
    
    def eng_decode(self) -> str:
        """
        Decode the Morse code message to English letters.
  
        Returns:
            str: The decoded message in English uppercase letters.
        """
        result = ''
        
        for morse_letter in self.morse_letters:
            result += self.MORSE_TO_ENG[morse_letter]
        
        return result
    
    def ru_decode(self) -> str:
        """
        Decode the Morse code message to Russian letters.

        Returns:
            str: The decoded message in Russian uppercase letters.
        """
        result = ''
        
        for morse_letter in self.morse_letters:
          
            result += self.MORSE_TO_RU[morse_letter]
        
        return result
    
    def get_vowels(self, lang) -> List[str]:
        """
        Extract vowels from the decoded message.
       
        Returns:
            list: List of vowels from the message in order of appearance.
        """
        vowels = []
        
        if lang == 'eng':
            decoded = self.eng_decode()
            for letter in decoded:
                if letter in self.VOWELS_ENG:
                    vowels.append(letter)
        elif lang == 'ru':
            decoded = self.ru_decode()
            for letter in decoded:
                if letter in self.VOWELS_RU:
                    vowels.append(letter)
        
        return vowels
    
    def get_consonants(self, lang) -> List[str]:
        """
        Extract consonants from the decoded message.
   
        Args:
            lang (str): Language for consonant extraction. Can be 'eng' or 'ru'.
        
        Returns:
            list: List of consonants from the message in order of appearance.
        """
        consonants = []
        
        if lang == 'eng':
            decoded = self.eng_decode()
            for letter in decoded:
                if letter in self.CONSONANTS_ENG:
                    consonants.append(letter)
        elif lang == 'ru':
            decoded = self.ru_decode()
            for letter in decoded:
                if letter in self.CONSONANTS_RU:
                    consonants.append(letter)
        
        return consonants
    
    def __str__(self) -> str:
        """
        Return the decoded English message as string representation.
    
        Returns:
            str: The decoded message in English uppercase letters.
        """
        return self.eng_decode()


def main() -> None:
    """The main function of the program."""
    msgs = []
    
    msgs.append(MorseMsg('... ... ... ... ... ... ... ...'))
    msgs.append(MorseMsg('... ... ... ... ... ... ... ...'))
    
    for msg in msgs:
        print(msg)
    
    print(msgs[0].eng_decode())
    print(msgs[0].get_vowels('eng'))
    print(msgs[0].get_consonants('eng'))
    print(msgs[1].get_vowels('ru'))
    print(msgs[1].get_consonants('ru'))


if __name__ == "__main__":
    main()
