class Word:
    def __init__(self, word):
        self.word = word
    
    def __str__(self):
        return self.word.capitalize()
    def __repr__(self):
        return f"Word('{self.word}')"
    
    def __eq__(self, other): #==
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented
    def __ne__(self, other): #!=
        if isinstance(other, Word):
            return len(self.word) != len(other.word)
        return NotImplemented
    def __lt__(self, other): #<
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
    def __gt__(self, other): #>
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented
    def __le__(self, other): #<=
        if isinstance(other, Word):
            return len(self.word) <= len(other.word)
        return NotImplemented
    def __ge__(self, other): #>=
        if isinstance(other, Word):
            return len(self.word) >= len(other.word)
        return NotImplemented

w1 = Word("hello")
w2 = Word("bye")
print(w1)    
print(w2)         

print(repr(w1)) 

print(w1 > w2)    
print(w1 == w2)   
print(Word("hello").__eq__(10))