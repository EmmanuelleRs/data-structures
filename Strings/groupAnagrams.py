# Given a list of Anagrams, create a list o anagrams groups 

# Example input ['abc', 'bca', 'aab', 'baa', 'aba']
# Example output [['abc', 'bca'], ['aab', 'baa', 'aba']]

def grupByAnagrams(words):
    anagrams = {}
    
    for word in words:
        sorted_word = ''.join(sorted(word)) # sorted split the string and return a new sorted array

        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        
        anagrams[sorted_word].append(word)
        
    return list(anagrams.values())




