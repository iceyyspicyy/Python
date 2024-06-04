import random
from collections import Counter

someWords = '''chair table bag tiger'''
someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Lets play hangman :p ')

    for i in word:
        print('_' , end=' ') #the end makes sure that the words appear in the same line, otherwise it is addedd with newline /n
    print('')

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    history = ''

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            try:
                guess = str(input("Enter a letter!"))
                history += guess
                print(history)
            except ValueError:
                print('Only a letter')
                continue
            
            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('Enter one at a time')
                continue
            elif guess in letterGuessed:
                print('Already guessed')
                continue
            
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)!= Counter(word)):
                    print(char, end=' ')
                    correct += 1
                
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end =' ')
                    print(word)
                    flag = 1
                    print('Congratulations, you won')
                    break
                    break
                else:
                    print('_', end= ' ')

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')        
        exit()          

                
            