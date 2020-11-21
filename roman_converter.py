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
            if i < limit-1:
                next_key = roman_number[i+1]
            if next_key != None and self.components[key]['value'] < self.components[next_key]['value']:
                result -= self.components[key]['value']
            else:
                result += self.components[key]['value']
            print(key,next_key)
            
        return result