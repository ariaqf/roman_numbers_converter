import roman_components

class Converter:
    def __init__(self):
        self.components = roman_components.components
    
    def convert(self, roman_number):
        limit = len(roman_number)
        result = 0
        for i in range(limit):
            key = roman_number[i]
            next_key = None
            result += self.components[key].value
            if i < limit:
                next_key = roman_number[i+1]
            if self.components[key].value < self.components[next_key].value:
                result -= self.components[next_key].value
                i += 1
            
        return result