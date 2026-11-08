from itertools import product

def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    dict = []
    
    for i in range(1, 6):
        for prod in product(vowels, repeat=i):
            dict.append(''.join(prod))
    
    dict.sort()
    answer = dict.index(word) + 1
    
    
    return answer